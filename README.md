# 🤖 Somnia Multi-Wallet Farming Bot

An advanced automation script to farm the **Somnia testnet** using multiple wallets. This bot claims faucets and performs random token interactions with human-like behavior to avoid Sybil detection.

---

## 🔧 Features

- 🚰 Automatic faucet claim for each wallet (once per day)
- 🎯 3–4 random Web3 interactions per wallet (daily)
- 🕒 Random delays between actions (to simulate human usage)
- 📒 Logs every action to prevent duplication
- 🔒 Wallets operate in isolation for safety & Sybil resistance
- 📦 Modular structure for easy customization

---

## ⚙️ Setup Instructions

### 1. 📥 Clone the Repo
```bash
git clone https://github.com/your-username/Somnia2.git
cd Somnia2
```

### 2. 🧪 Install Required Python Packages
```bash
pip install requests web3
```

> If you plan to use contract calls:
```bash
pip install eth-account
```

### 3. 🔑 Add Your Wallets

Edit `wallets.json` and add your wallets like so:
```json
[
  {
    "address": "0xYourWalletAddress1",
    "private_key": "0xYourPrivateKey1"
  },
  {
    "address": "0xYourWalletAddress2",
    "private_key": "0xYourPrivateKey2"
  }
]
```

### 4. ▶️ Run the Bot
```bash
python multiwallet_somnia_bot.py
```

---

## ✅ How It Works

1. The script loops through all wallets in `wallets.json`.
2. It checks if the faucet was already claimed today. If not, it claims it.
3. Then it performs 3–4 random tasks (like mint, transfer, swap).
4. Actions are logged to avoid duplicates using `action_log.csv`.
5. Random delays between actions are added to mimic real users.

---

## 🧠 Customize Your Tasks

Modify `modules/tasks.py` to plug in your actual contract calls or token logic:

```python
def mint_token(address, private_key):
    # Your mint logic here
    return "mint"
```

Add more custom tasks if needed:
```python
tasks = [mint_token, transfer_token, swap_token, your_custom_task]
```

---

## 📌 Supported

- ✅ Somnia Testnet
- ✅ Any EVM-compatible testnet (with minor changes)

---

## ⚠️ Disclaimer

This software is provided for **testing, educational, and research** purposes only.  
Use responsibly. The author is not responsible for any misuse or financial loss.

---

## 🙌 Credits

Based on and inspired by:
- [Trackko/Somnia2](https://github.com/Trackko/Somnia2)

Made with 💻 by the Web3 farming community.
