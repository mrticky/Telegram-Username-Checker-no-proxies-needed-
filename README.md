🔍 Features

High-speed multithreaded scanning
Checks large username lists with up to 20 concurrent workers.

Accurate availability detection
Parses Telegram profile pages and handles:

Available usernames

Taken usernames

Invalid or reserved usernames

Discord Webhook Notifications
Instantly notifies you when a username becomes available.

Beep Alerts (Windows compatible)
Optional audio alert when an available username is found.

Customizable UI
Menu-driven system with ASCII art, colorized output, and live status logs.

Automatic Hit Saving
All available usernames are written to hits.txt.

📁 Files

usernames.txt — Put your list of usernames here

hits.txt — Automatically stores available usernames

config.json — Stores webhook + beep settings

🛠 How It Works

The script checks usernames by requesting their Telegram profile page and analyzing the <title> tag to determine:

Available

Unavailable

Invalid

Runs continuously and refreshes every 10 seconds.

▶️ Usage

Add usernames to usernames.txt

Run the script

Select Start Username Checker

Optionally configure webhook + beep alerts

⚠️ Disclaimer

This tool is for educational and personal use only.
It does not bypass Telegram rules, rate limits, or reserved username policies.
