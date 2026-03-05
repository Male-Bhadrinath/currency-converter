# 💱 Global Currency Converter

> A real-time currency converter web app built with **Python + Streamlit**, supporting **34 world currencies** with live exchange rates.

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red?style=flat&logo=streamlit)
![API](https://img.shields.io/badge/API-ExchangeRate--API-green?style=flat)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat)

---

## 🌍 Overview

**Global Currency Converter** is a beautifully designed, real-time currency conversion tool that helps you instantly convert between 34 world currencies. Whether you're a traveller, student, freelancer, or business owner — this app gives you accurate, live conversion results in seconds.

---

## ✨ Features

- 🔴 **Live Exchange Rates** — Fetches real-time data from ExchangeRate-API
- 🌐 **34 Currencies Supported** — USD, INR, EUR, GBP, JPY, AED, and many more
- ⇄ **Instant Swap** — One-click swap between From & To currencies
- 📊 **Quick Reference Table** — See conversions for 1, 10, 50, 100, 500, 1000, 5000, 10000
- 🌎 **Popular Rates Panel** — View major world currencies at a glance
- 🕐 **Rate Timestamp** — Shows exactly when rates were last updated
- 📖 **Built-in Guide Sidebar** — About, Features, Installation & How-to-Use tabs
- 🎨 **Beautiful Dark UI** — Gradient theme with smooth animations
- ⚡ **Rate Caching** — Avoids repeated API calls, refreshes every 5 minutes

---

## 🖥️ App Preview

```
💰 Enter Amount  →  🔵 From Currency  ⇄  🟡 To Currency  →  🚀 Convert
                         ↓
              🟡 Result with live rate
                         ↓
         📊 Quick table  +  🌐 Popular currencies
```

---

## 🌐 Supported Currencies

| Flag | Code | Country |
|------|------|---------|
| 🇺🇸 | USD | United States |
| 🇮🇳 | INR | India |
| 🇪🇺 | EUR | Eurozone |
| 🇬🇧 | GBP | United Kingdom |
| 🇯🇵 | JPY | Japan |
| 🇦🇺 | AUD | Australia |
| 🇨🇦 | CAD | Canada |
| 🇨🇭 | CHF | Switzerland |
| 🇨🇳 | CNY | China |
| 🇦🇪 | AED | UAE |
| 🇸🇦 | SAR | Saudi Arabia |
| 🇶🇦 | QAR | Qatar |
| 🇰🇼 | KWD | Kuwait |
| 🇸🇬 | SGD | Singapore |
| 🇭🇰 | HKD | Hong Kong |
| 🇰🇷 | KRW | South Korea |
| 🇧🇷 | BRL | Brazil |
| 🇲🇽 | MXN | Mexico |
| 🇿🇦 | ZAR | South Africa |
| 🇹🇷 | TRY | Turkey |
| 🇷🇺 | RUB | Russia |
| 🇹🇭 | THB | Thailand |
| 🇲🇾 | MYR | Malaysia |
| 🇮🇩 | IDR | Indonesia |
| 🇵🇰 | PKR | Pakistan |
| 🇧🇩 | BDT | Bangladesh |
| 🇱🇰 | LKR | Sri Lanka |
| 🇳🇵 | NPR | Nepal |
| 🇳🇿 | NZD | New Zealand |
| 🇦🇷 | ARS | Argentina |
| 🇧🇭 | BHD | Bahrain |
| 🇴🇲 | OMR | Oman |
| 🇪🇬 | EGP | Egypt |
| 🇳🇬 | NGN | Nigeria |

---

## ⚙️ Local Setup

### 1. Make sure Python is installed

Download Python from [python.org](https://python.org)
> ✅ During install, check **"Add Python to PATH"**

Verify installation:
```bash
python --version
```

---

### 2. Download the project files

Save these two files into a folder on your computer:
- `currency_converter_app.py`
- `requirements.txt`

---

### 3. Install dependencies

Open **Command Prompt** (Windows) or **Terminal** (Mac/Linux) inside your project folder:

```bash
pip install streamlit requests
```

Or using the requirements file:

```bash
pip install -r requirements.txt
```

---

### 4. Run the app

```bash
python -m streamlit run currency_converter_app.py
```

---

### 5. Open in browser

The app opens automatically at:

```
http://localhost:8501
```

> 💡 Use `python -m streamlit` on Windows if `streamlit run` alone doesn't work.

---

## 🧭 How to Use

**Step 1 — Enter Amount**
Type the money amount you want to convert in the **"Amount to Convert"** input box.

**Step 2 — Choose From Currency**
Click the **🔵 From Currency** dropdown → select the currency you're converting *from* (e.g. USD 🇺🇸).

**Step 3 — Choose To Currency**
Click the **🟡 To Currency** dropdown → select the currency you want to convert *to* (e.g. INR 🇮🇳).

**Step 4 — Convert**
Click the **🚀 Convert Now** button to see the live result instantly.

**Step 5 — Swap (Optional)**
Hit the **⇄ button** in the middle to instantly flip the From ↔ To currencies.

**Step 6 — Read Results**
- 🟡 Large number = your converted amount
- Rate badge = exact exchange rate (both directions)
- Quick table = handy reference for common amounts
- Bottom section = other popular currency rates

---

## 📁 Project Structure

```
currency-converter/
│
├── currency_converter_app.py   # Main Streamlit app
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## 📦 Requirements

```
streamlit
requests
```

---

## 🚀 Deploy on Streamlit Cloud (Free)

1. Push your files to a **GitHub repository**
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Click **"New app"** → select your repo
5. Set main file: `currency_converter_app.py`
6. Click **"Deploy!"** 🎉

Your app goes live at:
```
https://your-username-currency-converter.streamlit.app
```

---

## 🔗 Data Source

Exchange rates powered by **[ExchangeRate-API](https://exchangerate-api.com)**
- Free tier: 1,500 requests/month
- Rates update frequency: Every 24 hours on free plan
- App caches rates for 5 minutes to reduce API calls

---

## 📄 License

This project is open source under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

- [Streamlit](https://streamlit.io) — for the amazing web framework
- [ExchangeRate-API](https://exchangerate-api.com) — for free live exchange rates
- [Google Fonts](https://fonts.google.com) — Inter font used in UI

---

> Made with ❤️ using Python & Streamlit
