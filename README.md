📨 Telegram Username Checker

A fast, multithreaded Telegram username scanner with Discord webhook alerts, beep notifications, and automatic hit saving.

⭐ Features

⚡ High-Speed Multithreading — Checks usernames using up to 20 threads.

🎯 Accurate Detection — Identifies available, unavailable, and invalid/reserved usernames.

🔔 Alerts System

Optional beep sound when a username becomes available

Discord webhook notifications

📁 Automatic Logging — Saves available usernames to hits.txt.

🧩 Interactive Menu — Includes options panel, ASCII art header, and colored CLI output.

🔄 Continuous Monitoring — Re-scans the list every 10 seconds.

📦 Requirements

Your environment should have:

Python 3.8+

The following pip packages:

pip install requests colorama

📂 File Structure
📁 Project/
 ├── checker.py           # Main script
 ├── usernames.txt        # Add usernames to check
 ├── hits.txt             # Automatically created when available names are found
 ├── config.json          # Webhook + beep settings
 └── README.md

🔧 Installation

Clone the repository:

git clone https://github.com/yourname/telegram-username-checker.git
cd telegram-username-checker


Install dependencies:

pip install -r requirements.txt


(or manually install requests + colorama)

Add your username list:
Insert usernames into usernames.txt, one per line.

▶️ Usage

Run the script:

python checker.py


Navigate the menu:

1. Start username checker
2. Options

Options Menu Includes:

Set / remove Discord webhook

Toggle beep notifications

View current settings

🖥️ Output Example
Time       | Username            | Status
--------------------------------------------------
12:03:15   | example_name        | unavailable
12:03:16   | rareuser123         | available
            >>> rareuser123 is available! CLAIM NOW! <<<

🎯 Webhook Notifications

If enabled, the script will send a Discord message when a username becomes available:

Telegram username available: rareuser123

🧠 How It Works

The checker:

Fetches https://t.me/<username>

Reads the <title> tag and specific Telegram response patterns

Determines:

Available

Unavailable

Reserved / invalid
