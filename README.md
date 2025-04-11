# Somnia2

# 🤖 Somnia Multi-Wallet Farming Bot

Automated Somnia Testnet farming bot designed to manage 100+ wallets with human-like randomness and daily task distribution.

---

## 🔧 Features

- ✅ Faucet claim (once daily per wallet)
- 🎯 3–4 random Web3 interactions per wallet per day
- 🤖 Random delays to mimic human behavior
- 📒 Task logging to prevent duplicate actions
- 📂 Modular structure for easy customization
- 🛡️ Wallets are isolated to avoid Sybil detection patterns

---

## 📁 Folder Structure

somnia-bot/ ├── multiwallet_somnia_bot.py # Main runner script ├── wallets.json # List of wallets with private keys ├── modules/ │ ├── faucet.py # Faucet claim logic │ ├── tasks.py # Web3 interactions (mint, transfer, swap) ├── utils/ │ ├── logger.py # Action logger └── logs/ └── action_log.csv # Log of all actions per wallet


---

## 🚀 How to Use

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/Somnia2.git
cd Somnia2
---
