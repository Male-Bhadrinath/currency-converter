import streamlit as st
import requests
import time
from datetime import datetime

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="🌍 Global Currency Converter",
    page_icon="💱",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------------
# CUSTOM CSS - Beautiful Dark Theme
# ---------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        min-height: 100vh;
    }

    .main-title {
        text-align: center;
        font-size: 2.8rem;
        font-weight: 700;
        background: linear-gradient(90deg, #f7971e, #ffd200, #f7971e);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
        animation: shimmer 3s infinite;
    }

    .subtitle {
        text-align: center;
        color: #a0a8c0;
        font-size: 1rem;
        margin-bottom: 2rem;
    }

    .card {
        background: rgba(255,255,255,0.06);
        border: 1px solid rgba(255,255,255,0.12);
        border-radius: 20px;
        padding: 2rem;
        backdrop-filter: blur(10px);
        margin-bottom: 1.5rem;
    }

    .result-box {
        background: linear-gradient(135deg, rgba(247,151,30,0.15), rgba(255,210,0,0.1));
        border: 2px solid rgba(247,151,30,0.4);
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        margin-top: 1.5rem;
        animation: fadeIn 0.5s ease;
    }

    .result-amount {
        font-size: 3rem;
        font-weight: 700;
        color: #ffd200;
        line-height: 1.2;
    }

    .result-label {
        font-size: 1rem;
        color: #a0a8c0;
        margin-top: 0.3rem;
    }

    .rate-badge {
        display: inline-block;
        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(255,255,255,0.15);
        border-radius: 50px;
        padding: 0.4rem 1rem;
        font-size: 0.85rem;
        color: #c0c8e0;
        margin-top: 1rem;
    }

    .currency-label {
        font-size: 0.85rem;
        font-weight: 600;
        color: #a0a8c0;
        margin-bottom: 0.3rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    .stSelectbox > div > div {
        background: rgba(255,255,255,0.07) !important;
        border: 1px solid rgba(255,255,255,0.15) !important;
        border-radius: 12px !important;
        color: white !important;
    }

    .stNumberInput > div > div > input {
        background: rgba(255,255,255,0.07) !important;
        border: 1px solid rgba(255,255,255,0.15) !important;
        border-radius: 12px !important;
        color: white !important;
        font-size: 1.2rem !important;
        padding: 0.6rem 1rem !important;
    }

    .stButton > button {
        background: linear-gradient(135deg, #f7971e, #ffd200) !important;
        color: #1a1a2e !important;
        font-weight: 700 !important;
        font-size: 1.05rem !important;
        border: none !important;
        border-radius: 14px !important;
        padding: 0.75rem 2rem !important;
        width: 100% !important;
        transition: transform 0.2s, box-shadow 0.2s !important;
        letter-spacing: 0.03em;
    }

    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(247,151,30,0.4) !important;
    }

    .swap-btn > button {
        background: rgba(255,255,255,0.08) !important;
        color: white !important;
        border: 1px solid rgba(255,255,255,0.2) !important;
        border-radius: 50% !important;
        width: 48px !important;
        font-size: 1.3rem !important;
        padding: 0.3rem !important;
    }

    .mini-card {
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 14px;
        padding: 1rem;
        text-align: center;
        margin: 0.3rem;
    }

    .mini-flag { font-size: 1.8rem; }
    .mini-rate { font-size: 1.1rem; font-weight: 600; color: #ffd200; }
    .mini-code { font-size: 0.75rem; color: #a0a8c0; margin-top: 0.2rem; }

    .footer {
        text-align: center;
        color: #555a80;
        font-size: 0.78rem;
        margin-top: 2rem;
        padding-top: 1rem;
        border-top: 1px solid rgba(255,255,255,0.05);
    }

    .live-dot {
        display: inline-block;
        width: 8px; height: 8px;
        background: #2ecc71;
        border-radius: 50%;
        margin-right: 6px;
        animation: pulse 1.5s infinite;
    }

    @keyframes pulse {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.5; transform: scale(1.3); }
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    h3 { color: #e0e4f0 !important; }
    .stMarkdown p { color: #c0c8e0; }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# CURRENCY DATA
# ---------------------------------------------------------
CURRENCY_INFO = {
    "USD": {"country": "United States", "symbol": "$", "flag": "🇺🇸"},
    "INR": {"country": "India", "symbol": "₹", "flag": "🇮🇳"},
    "EUR": {"country": "Eurozone", "symbol": "€", "flag": "🇪🇺"},
    "GBP": {"country": "United Kingdom", "symbol": "£", "flag": "🇬🇧"},
    "JPY": {"country": "Japan", "symbol": "¥", "flag": "🇯🇵"},
    "AUD": {"country": "Australia", "symbol": "A$", "flag": "🇦🇺"},
    "CAD": {"country": "Canada", "symbol": "C$", "flag": "🇨🇦"},
    "CHF": {"country": "Switzerland", "symbol": "CHF", "flag": "🇨🇭"},
    "CNY": {"country": "China", "symbol": "¥", "flag": "🇨🇳"},
    "NZD": {"country": "New Zealand", "symbol": "NZ$", "flag": "🇳🇿"},
    "SGD": {"country": "Singapore", "symbol": "S$", "flag": "🇸🇬"},
    "HKD": {"country": "Hong Kong", "symbol": "HK$", "flag": "🇭🇰"},
    "AED": {"country": "UAE", "symbol": "د.إ", "flag": "🇦🇪"},
    "SAR": {"country": "Saudi Arabia", "symbol": "﷼", "flag": "🇸🇦"},
    "QAR": {"country": "Qatar", "symbol": "ر.ق", "flag": "🇶🇦"},
    "KWD": {"country": "Kuwait", "symbol": "KD", "flag": "🇰🇼"},
    "BHD": {"country": "Bahrain", "symbol": "BD", "flag": "🇧🇭"},
    "OMR": {"country": "Oman", "symbol": "﷼", "flag": "🇴🇲"},
    "ZAR": {"country": "South Africa", "symbol": "R", "flag": "🇿🇦"},
    "TRY": {"country": "Turkey", "symbol": "₺", "flag": "🇹🇷"},
    "RUB": {"country": "Russia", "symbol": "₽", "flag": "🇷🇺"},
    "THB": {"country": "Thailand", "symbol": "฿", "flag": "🇹🇭"},
    "MYR": {"country": "Malaysia", "symbol": "RM", "flag": "🇲🇾"},
    "IDR": {"country": "Indonesia", "symbol": "Rp", "flag": "🇮🇩"},
    "PKR": {"country": "Pakistan", "symbol": "₨", "flag": "🇵🇰"},
    "BDT": {"country": "Bangladesh", "symbol": "৳", "flag": "🇧🇩"},
    "LKR": {"country": "Sri Lanka", "symbol": "Rs", "flag": "🇱🇰"},
    "NPR": {"country": "Nepal", "symbol": "₨", "flag": "🇳🇵"},
    "KRW": {"country": "South Korea", "symbol": "₩", "flag": "🇰🇷"},
    "MXN": {"country": "Mexico", "symbol": "$", "flag": "🇲🇽"},
    "BRL": {"country": "Brazil", "symbol": "R$", "flag": "🇧🇷"},
    "ARS": {"country": "Argentina", "symbol": "$", "flag": "🇦🇷"},
    "EGP": {"country": "Egypt", "symbol": "£", "flag": "🇪🇬"},
    "NGN": {"country": "Nigeria", "symbol": "₦", "flag": "🇳🇬"},
}

CURRENCY_OPTIONS = [
    f"{info['flag']} {code} — {info['country']}"
    for code, info in CURRENCY_INFO.items()
]
CODE_FROM_OPTION = {
    f"{info['flag']} {code} — {info['country']}": code
    for code, info in CURRENCY_INFO.items()
}

# ---------------------------------------------------------
# API CALL
# ---------------------------------------------------------
@st.cache_data(ttl=300)
def fetch_rates(base: str):
    try:
        url = f"https://api.exchangerate-api.com/v4/latest/{base}"
        resp = requests.get(url, timeout=8)
        return resp.json()
    except Exception:
        return None

# ---------------------------------------------------------
# SESSION STATE
# ---------------------------------------------------------
if "from_idx" not in st.session_state:
    st.session_state.from_idx = list(CURRENCY_INFO.keys()).index("USD")
if "to_idx" not in st.session_state:
    st.session_state.to_idx = list(CURRENCY_INFO.keys()).index("INR")

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------
st.markdown('<div class="main-title">💱 Global Currency Converter</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle"><span class="live-dot"></span>Live exchange rates · 34 currencies · Real-time data</div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# MAIN CONVERTER CARD
# ---------------------------------------------------------
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)

    # Amount input
    st.markdown('<p class="currency-label">💰 Amount to Convert</p>', unsafe_allow_html=True)
    amount = st.number_input("", min_value=0.01, value=100.0, step=1.0, format="%.2f", label_visibility="collapsed")

    st.markdown("<br>", unsafe_allow_html=True)

    # From / To selectors
    col1, col_swap, col2 = st.columns([5, 1, 5])

    with col1:
        st.markdown('<p class="currency-label">🔵 From Currency</p>', unsafe_allow_html=True)
        from_sel = st.selectbox("from", CURRENCY_OPTIONS,
                                index=st.session_state.from_idx,
                                label_visibility="collapsed", key="from_sel")

    with col_swap:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown('<div class="swap-btn">', unsafe_allow_html=True)
        if st.button("⇄", key="swap"):
            st.session_state.from_idx = st.session_state.to_idx
            st.session_state.to_idx = CURRENCY_OPTIONS.index(from_sel)
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<p class="currency-label">🟡 To Currency</p>', unsafe_allow_html=True)
        to_sel = st.selectbox("to", CURRENCY_OPTIONS,
                              index=st.session_state.to_idx,
                              label_visibility="collapsed", key="to_sel")

    st.markdown("<br>", unsafe_allow_html=True)

    # Convert button
    convert_clicked = st.button("🚀 Convert Now", key="convert")
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# RESULT
# ---------------------------------------------------------
from_code = CODE_FROM_OPTION[from_sel]
to_code   = CODE_FROM_OPTION[to_sel]
from_info = CURRENCY_INFO[from_code]
to_info   = CURRENCY_INFO[to_code]

if convert_clicked or True:   # auto-convert on load too
    with st.spinner("Fetching live rates..."):
        data = fetch_rates(from_code)

    if data and "rates" in data:
        rate = data["rates"].get(to_code)
        if rate:
            converted = amount * rate
            inv_rate  = 1 / rate

            st.markdown(f"""
            <div class="result-box">
                <div style="font-size:1rem; color:#a0a8c0; margin-bottom:0.5rem;">
                    {from_info['flag']} {from_info['symbol']}{amount:,.2f} {from_code} =
                </div>
                <div class="result-amount">{to_info['flag']} {to_info['symbol']}{converted:,.2f}</div>
                <div class="result-label">{to_code} · {to_info['country']}</div>
                <div class="rate-badge">
                    1 {from_code} = {rate:.4f} {to_code} &nbsp;|&nbsp; 1 {to_code} = {inv_rate:.4f} {from_code}
                </div>
                <div style="font-size:0.75rem; color:#555a80; margin-top:0.8rem;">
                    🕐 Rates updated: {datetime.now().strftime('%d %b %Y, %H:%M')}
                </div>
            </div>
            """, unsafe_allow_html=True)

            # ---------------------------------------------------------
            # QUICK REFERENCE TABLE
            # ---------------------------------------------------------
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("### 📊 Quick Amounts")

            quick_amounts = [1, 10, 50, 100, 500, 1000, 5000, 10000]
            cols = st.columns(4)
            for i, qa in enumerate(quick_amounts):
                with cols[i % 4]:
                    qval = qa * rate
                    st.markdown(f"""
                    <div class="mini-card">
                        <div class="mini-code">{from_info['flag']} {qa:,} {from_code}</div>
                        <div class="mini-rate">{to_info['symbol']}{qval:,.2f}</div>
                        <div class="mini-code">{to_code}</div>
                    </div>
                    """, unsafe_allow_html=True)

            # ---------------------------------------------------------
            # POPULAR RATES vs FROM CURRENCY
            # ---------------------------------------------------------
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("### 🌐 Popular Currencies vs 1 " + from_code)

            popular = ["USD", "EUR", "GBP", "INR", "JPY", "AED", "CAD", "AUD"]
            popular = [c for c in popular if c != from_code][:6]

            pcols = st.columns(3)
            for i, pc in enumerate(popular):
                pr = data["rates"].get(pc, 0)
                pinfo = CURRENCY_INFO[pc]
                with pcols[i % 3]:
                    st.markdown(f"""
                    <div class="mini-card">
                        <div class="mini-flag">{pinfo['flag']}</div>
                        <div class="mini-rate">{pinfo['symbol']}{pr:,.4f}</div>
                        <div class="mini-code">{pc} · {pinfo['country']}</div>
                    </div>
                    """, unsafe_allow_html=True)

    else:
        st.error("❌ Could not fetch live exchange rates. Please check your internet connection.")

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.markdown("""
<div class="footer">
    💱 Global Currency Converter · Powered by ExchangeRate-API · Built with Streamlit<br>
    Data refreshes every 5 minutes · For reference only
</div>
""", unsafe_allow_html=True)
