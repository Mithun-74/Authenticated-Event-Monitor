# 🚨 Nova Event Sentinel

A real-time authenticated event monitoring system that watches a portal (Laravel Nova API) and sends instant notifications when new eligible events appear on the front page.

This project uses reverse-engineered API requests, session authentication, and automated filtering to notify students about competitions and paper presentations before others.

---

## ✨ Features

* 🔐 Authenticated API monitoring (login session based)
* ⚡ Real-time front-page event tracking
* 🧠 Smart filtering:

  * Competition
  * Paper Presentation
  * ONLINE events
  * Active status only
* 📱 Instant Telegram notifications
* ♻️ Duplicate prevention using `event_code`
* ⏱️ Background polling every 60 seconds
* 🌐 Deployable on Render (24/7 uptime)

---

## 🧱 Tech Stack

* Python
* Requests
* python-dotenv
* Telegram Bot API
* Render (Background Worker)

---

## 📂 Project Structure

```
Event_notifier_bot/
│
├── main.py
├── requirements.txt
├── seen.json       # tracked event IDs
└── README.md
```

---

## ⚙️ Setup (Local Machine)

### 1️⃣ Clone Repo

```
git clone <https://github.com/Mithun-74/Authenticated-Event-Monitor.git>
cd Event_notifier_bot
```

---

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Create `.env` File

```
COOKIE=your_session_cookie
BOT_TOKEN=your_telegram_bot_token
CHAT_ID=your_telegram_chat_id
```

⚠️ Do NOT add quotes around values.

---

### 4️⃣ Run the Bot

```
python main.py
```

Expected output:

```
🔎 Checking events...
Status code: 200
✅ No new matching events.
```

---

## 🤖 Telegram Setup

1. Create a bot using **@BotFather**
2. Copy the API Token
3. Send `/start` to your bot
4. Get chat ID from:

```
https://api.telegram.org/bot<TOKEN>/getUpdates
```

---

## 🌐 Deploy on Render (24/7)

1. Push project to GitHub
2. Go to Render Dashboard
3. Create **Background Worker**
4. Settings:

Build Command:

```
pip install -r requirements.txt
```

Start Command:

```
python main.py
```

Add Environment Variables in Render:

```
COOKIE
BOT_TOKEN
CHAT_ID
```

---

## 🔐 Security Notes

* `.env` must never be committed to GitHub
* Session cookie is stored securely as environment variable
* Script only reads data accessible to your account

---

## 📌 How It Works

```
Login Session → Hidden Nova API → JSON Parsing
        ↓
Smart Filtering Engine
        ↓
Telegram Notification System
```

The bot monitors only the **front page**, ensuring fast detection with minimal server load.

---

## 🧠 Learning Concepts

* Authenticated API Scraping
* Laravel Nova Reverse Engineering
* Session-based Automation
* Real-time Notification Systems

---

## ⚠️ Disclaimer

This tool is intended for personal educational use with authorized access only. Do not abuse API endpoints or violate institutional policies.

---

## ⭐ Future Improvements

* Auto-login session refresh
* Email + Discord notifications
* Web dashboard for events
* Deployment via Docker

---

Built with curiosity ❤️
