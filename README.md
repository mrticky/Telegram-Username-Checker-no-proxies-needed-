# Telegram Username Checker

A multithreaded Telegram username checker with Discord webhook alerts, optional beep notifications, and automatic saving of available usernames.

---

## Features

- **High-speed multithreaded username checking**
- **Accurate detection** of available, unavailable, and invalid/reserved usernames
- **Optional beep alert** when a username becomes available
- **Discord webhook notifications**
- **Automatically saves available usernames** to `hits.txt`
- **Menu-driven interface** with colored terminal output
- **Continuous monitoring** — rechecks usernames every 10 seconds

---

## Requirements

- Python **3.8+**

### Install dependencies:

```bash
pip install requests colorama
File Structure
graphql
Copy code
project/
├── checker.py        # Main script
├── usernames.txt     # Add usernames to check
├── hits.txt          # Created automatically when an available username is found
├── config.json       # Stores webhook + beep settings
└── README.md
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourname/telegram-username-checker.git
cd telegram-username-checker
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Add usernames (one per line) to:

Copy code
usernames.txt
Usage
Run the script:

bash
Copy code
python checker.py
You will see a menu:

markdown
Copy code
1. Start username checker
2. Options
Options Menu
Set Discord webhook URL

Toggle beep on/off

Remove webhook

Example Output
markdown
Copy code
Time       | Username            | Status
--------------------------------------------------
12:03:15   | example_name        | unavailable
12:03:16   | rareuser123         | available
            >>> rareuser123 is available! CLAIM NOW! <<<
If a webhook is set:

arduino
Copy code
Telegram username available: rareuser123
How It Works
Requests https://t.me/<username>

Reads the <title> tag and Telegram page text

Determines whether the username is:

Available

Unavailable

Invalid / Reserved

No API keys or authentication required.

Disclaimer
This tool is for educational use only.
Using it to violate Telegram’s Terms of Service is not recommended.
The author is not responsible for misuse.

