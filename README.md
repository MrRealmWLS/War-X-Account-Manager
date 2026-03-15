# War X Account Manager

**War X Account Manager** is a Python-based command-line tool designed to perform bulk management actions on a Discord account using a user token. The tool provides options to leave servers, close direct messages, remove friends, or perform all actions at once through a simple terminal interface with styled output.

> Created by **Realm X Arbaz**

---

## 📌 Project Description

War X Account Manager is a terminal utility that interacts with the Discord API to automate several account management actions. It uses a token-based login system and provides a clean CLI interface with gradient text styling.

The tool collects a user's guilds (servers), friends, and direct message channels, allowing the user to manage them quickly using different menu options.

It is built using Python and uses libraries like **requests**, **colorama**, and **pystyle** to handle API requests and provide a visually styled command-line interface.

---

## ✨ Project Features

* 🔐 **Token Authentication**

  * Logs into a Discord account using a provided token.

* 🧹 **Bulk Server Leaving**

  * Automatically leaves all joined servers.

* 💬 **Bulk DM Closing**

  * Closes all open direct message channels.

* 👥 **Bulk Friend Removal**

  * Removes all friends from the account.

* 💣 **Full Account Clean (Nuke Option)**

  * Removes friends, leaves servers, and closes DMs in one command.

* 🎨 **Styled CLI Interface**

  * Uses gradient colored text and centered formatting.

* ⚡ **Rate Limit Handling**

  * Detects Discord API rate limits and retries after the specified delay.

---

## ⚠️ Use At Your Own Risk

This project interacts directly with the **Discord API using user tokens**. Misuse of this tool may violate Discord's **Terms of Service** and could lead to **account suspension or termination**.

By using this software, you agree that:

* You are responsible for how you use the tool.
* The developer is **not responsible for any account bans, data loss, or misuse**.
* The tool should only be used for **educational or personal account management purposes**.

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/MrRealmWLS/War-X-Account-Manager.git
cd war-x-account-manager
```

### 2. Install Required Dependencies

```bash
pip install requests colorama pystyle
```

### 3. Run the Program

```bash
python main.py
```

---

## 🖥 Requirements

* Python **3.8+**
* Internet connection
* Required Python libraries:

  * `requests`
  * `colorama`
  * `pystyle`

---

## 📂 Project Structure

```
War-X-Account-Manager/
│
├── main.py
└── README.md
```

---

## 📜 Disclaimer

This project is provided **for educational purposes only**. The developer does not encourage or support violating Discord’s Terms of Service.

Use responsibly.

---

## 👤 Author

**Realm X Arbaz**

If you like the project, consider ⭐ starring the repository.
