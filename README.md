Telegram Username Checker

A multithreaded Telegram username checker with Discord webhook alerts, optional beep notifications, and automatic saving of available usernames.

Features

High-speed multithreaded username checking

Detects available, unavailable, and invalid/reserved usernames

Optional beep sound when a username becomes available

Discord webhook notifications

Saves all available usernames to hits.txt

Menu-driven interface with colored terminal output

Automatically rechecks usernames every 10 seconds

Requirements

Python 3.8+

Install dependencies:

pip install requests colorama

File Structure
project/
│── checker.py        # Main script
│── usernames.txt     # Add usernames to check
│── hits.txt          # Automatically created when an available username is found
│── config.json       # Stores webhook + beep settings
└── README.md

Installation

Clone the repository:

git clone https://github.com/yourname/telegram-username-checker.git
cd telegram-username-checker


Install dependencies:

pip install -r requirements.txt


Add your usernames (one per line) to:

usernames.txt

Usage

Run the script:

python checker.py


You will see a menu:

1. Start username checker
2. Options

Options Menu

Set Discord webhook URL

Toggle beep on/off

Remove currently saved webhook

Example Output
Time       | Username            | Status
--------------------------------------------------
12:03:15   | example_name        | unavailable
12:03:16   | rareuser123         | available
            >>> rareuser123 is available! CLAIM NOW! <<<


If a webhook is configured, you will also receive a message like:

Telegram username available: rareuser123

How It Works

The script performs a GET request to
https://t.me/<username>

It analyzes the page’s <title> and Telegram error text.

Based on this, it determines whether the username is:

Available

Unavailable

Invalid / Reserved

The script does not use Telegram's API.

Disclaimer

This tool is for educational purposes only.
Do not use it to violate Telegram’s Terms of Service.
The author is not responsible for any misuse.
