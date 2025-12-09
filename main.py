import sys
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
import re
import requests

def check_telegram_username(username):
	if len(username) < 5:
		return False
	if not re.match(r'^[a-zA-Z][a-zA-Z0-9_]{4,31}$', username):
		return None
	url = f"https://t.me/{username}"
	headers = {
		"User-Agent": "Mozilla/5.0"
	}
	response = requests.get(url, headers=headers, allow_redirects=True)
	if "This username is invalid." in response.text:
		return None
	start = response.text.find('<title>')
	end = response.text.find('</title>')
	title = response.text[start+7:end].strip() if start != -1 and end != -1 else ""
	if title.startswith("Telegram: Contact @") or title.startswith("Telegram: View @"):
		return False
	elif title.startswith("Telegram Messenger"):
		return True
	elif title.startswith("Telegram: Launch @"):
		return False
	else:
		print(f"DEBUG: Unexpected title for {username}: {title}")
		return False

def main():
	with open("usernames.txt", "r") as f:
		usernames = [line.strip() for line in f if line.strip()]
	from threading import Lock
	hits_lock = Lock()

	def process_username(username):
		result = check_telegram_username(username)
		if result is None:
			return f"{username}: invalid"
		elif result:
			with hits_lock:
				with open("hits.txt", "a") as hits_file:
					hits_file.write(username + "\n")
			return f"{username}: available"
		else:
			return f"{username}: unavailable"

	import time
	import os
	import json
	from colorama import init, Fore, Style
	init(autoreset=True)

	def print_ascii_art():
		ascii_art = '''
 _   _      _          
| |_(_) ___| | ___   _ 
| __| |/ __| |/ / | | |
| |_| | (__|   <| |_| |
 \__|_|\___|_|\_\\__, |
                 |___/ 
		'''
		print(Fore.RED + ascii_art + Style.RESET_ALL)

	def load_webhook():
		try:
			with open("config.json", "r") as f:
				data = json.load(f)
				return data.get("webhook"), data.get("beep", True)
		except Exception:
			return None, True

	def save_webhook(url):
		beep = True
		try:
			with open("config.json", "r") as f:
				data = json.load(f)
				beep = data.get("beep", True)
		except Exception:
			pass
		with open("config.json", "w") as f:
			json.dump({"webhook": url, "beep": beep}, f)

	def save_beep_setting(beep):
		webhook = None
		try:
			with open("config.json", "r") as f:
				data = json.load(f)
				webhook = data.get("webhook")
		except Exception:
			pass
		with open("config.json", "w") as f:
			json.dump({"webhook": webhook, "beep": beep}, f)

	def send_discord_webhook(webhook_url, message):
		try:
			import requests
			requests.post(webhook_url, json={"content": message})
		except Exception as e:
			print(f"[!] Failed to send to Discord webhook: {e}")

	def menu():
		while True:
			os.system("cls" if os.name == "nt" else "clear")
			print_ascii_art()
			print("1. start username checker")
			print("2. options")
			choice = input("\nEnter your choice: ").strip()
			if choice == "1":
				start_checker()
			elif choice == "2":
				options_menu()
			else:
				print("Invalid choice. Try again.")
				time.sleep(1)

	def options_menu():
		while True:
			os.system("cls" if os.name == "nt" else "clear")
			print(Fore.RED + "Options" + Style.RESET_ALL)
			print("1. Set Discord webhook URL")
			print("2. Toggle beep (on/off)")
			print("3. Remove Discord webhook")
			print("99. Back to main menu")
			webhook, beep = load_webhook()
			print(f"\nCurrent beep setting: {'ON' if beep else 'OFF'}")
			print(f"Current webhook: {webhook if webhook else 'None'}")
			choice = input("\nEnter your choice: ").strip()
			if choice == "1":
				url = input("Enter Discord webhook URL: ").strip()
				save_webhook(url)
				print("Webhook saved!")
				time.sleep(1)
			elif choice == "2":
				save_beep_setting(not beep)
				print(f"Beep is now {'ON' if not beep else 'OFF'}.")
				time.sleep(1)
			elif choice == "3":
				save_webhook(None)
				print("Discord webhook removed!")
				time.sleep(1)
			elif choice == "99":
				return
			else:
				print("Invalid choice. Try again.")
				time.sleep(1)

	def start_checker():
		usernames = []
		with open("usernames.txt", "r") as f:
			usernames = [line.strip() for line in f if line.strip()]
		webhook_url, beep = load_webhook()
		import datetime

		def process_username(username):
			result = check_telegram_username(username)
			now = datetime.datetime.now().strftime('%H:%M:%S')
			if result is None:
				status = "invalid"
			elif result is True:
				status = "available"
				with hits_lock:
					with open("hits.txt", "a") as hits_file:
						hits_file.write(username + "\n")
				if beep:
					try:
						import winsound
						winsound.Beep(1000, 700)
					except ImportError:
						print("\a")
				if webhook_url:
					print(f"[DEBUG] Sending webhook for available username: {username}")
					send_discord_webhook(webhook_url, f"Telegram username available: {username}")
			else:
				status = "unavailable"
			return now, username, status

		os.system("cls" if os.name == "nt" else "clear")
		print_ascii_art()
		print("\n[Checking usernames... Press Ctrl+C to stop]\n")
		print("="*50)
		print(f"{'Time':<10} | {'Username':<20} | {'Status':<12}")
		print("-"*50)
		while True:
			with ThreadPoolExecutor(max_workers=20) as executor:
				future_to_username = {executor.submit(process_username, username): username for username in usernames}
				for future in as_completed(future_to_username):
					now, username, status = future.result()
					print(f"{now:<10} | {username:<20} | {status:<12}")
					if status == "available":
						print(f"{'':<10} | {'':<20} | >>> {username} is available! CLAIM NOW! <<<")
			print("="*50)
			time.sleep(10)

	hits_lock = threading.Lock()
	menu()

if __name__ == "__main__":
	main()
