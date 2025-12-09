Telegram Username Checker

A fast multithreaded Telegram username scanner with Discord webhook alerts, optional beep notifications, and automatic hit saving.

Features

High-Speed Multithreading — Checks usernames using up to 20 threads

Accurate Detection — Detects available, unavailable, and invalid/reserved usernames

Alerts System

Optional beep sound when a name becomes available

Discord webhook notifications

Automatic Logging — Saves available usernames to hits.txt

Interactive Menu — Options menu, ASCII art banner, colored CLI output

Continuous Monitoring — Re-scans all usernames every 10 seconds

Requirements

Python 3.8+

Install required packages:

pip install requests colorama

File Structure
project/
│── checker.py        # Main script
│── usernames.txt     # Add usernames to scan
│── hits.txt          # Auto-created when a username is available
│── config.json       # Webhook + beep settings
└── README.md

Installation

Clone the repository:

git clone https://github.com/yourname/telegram-username-checker.git
cd telegram-username-checker


Install dependencies:

pip install -r requirements.txt


Add usernames (one per line) to:

usernames.txt

Usage

Run the script:

python checker.py


Main menu:

1. Start username checker
2. Options

Options Menu

Set Discord webhook URL

Enable/disable beep notifications

Remove webhook

Example Output
Time       | Username            | Status
--------------------------------------------------
12:03:15   | example_name        | unavailable
12:03:16   | rareuser123         | available
            >>> rareuser123 is available! CLAIM NOW! <<<


If a webhook is configured, the script also sends:

Telegram username available: rareuser123

How It Works

The script performs an HTTP GET request to:

https://t.me/<username>


It then analyzes the <title> tag and Telegram error messages to determine:

Available

Unavailable

Invalid / Reserved
