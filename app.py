"""
app.py  —  PitWall Analytics Dashboard  (Group Edition)
Run with:   streamlit run app.py
"""
from __future__ import annotations
import sys
from pathlib import Path

ROOT = Path(__file__).parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st

st.set_page_config(
    page_title="PitWall Analytics",
    page_icon="🏎",
    layout="wide",
    initial_sidebar_state="collapsed",
)

from theme          import F1_CSS
from data_generator import load_data
import tab1_descriptive
import tab2_diagnostic
import tab3_predictive
import tab4_prescriptive
import tab5_regression

st.markdown(F1_CSS, unsafe_allow_html=True)

@st.cache_data(show_spinner=False)
def _load():
    return load_data()

with st.spinner("Loading race data…"):
    subs, sess, mrr = _load()

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="
    background: #FFFFFF;
    border-bottom: 1px solid #E8E8EC;
    border-top: 3px solid #E8002D;
    padding: 24px 32px 18px 32px;
    margin: -0.5rem -2rem 1.5rem -2rem;
    box-shadow: 0 1px 6px rgba(0,0,0,0.05);
">
    <div style="display:flex; align-items:center; gap:10px; margin-bottom:4px;">
        <span style="
            background:#E8002D; color:#fff; font-size:8px; font-weight:700;
            letter-spacing:2.5px; text-transform:uppercase;
            padding:3px 8px; border-radius:3px;
            font-family:'Inter',sans-serif;
        ">F1 ANALYTICS</span>
        <span style="
            font-size:9px; color:#9CA3AF; font-weight:600;
            letter-spacing:2px; text-transform:uppercase;
            font-family:'Inter',sans-serif;
        ">SUBSCRIBER RETENTION INTELLIGENCE · GROUP EDITION</span>
    </div>
    <div style="
        font-family:'Inter',sans-serif; font-size:26px; font-weight:800;
        color:#1A1A1A; letter-spacing:-0.5px; margin-bottom:4px;
    ">🏎 PitWall Analytics</div>
    <div style="
        font-family:'Inter',sans-serif; font-size:12px; color:#9CA3AF;
        letter-spacing:0.2px;
    ">
        800 Subscribers &nbsp;·&nbsp; 29,240 Sessions &nbsp;·&nbsp;
        3 Plan Tiers &nbsp;·&nbsp; Seasons 2023 – 2024
    </div>
</div>
""", unsafe_allow_html=True)

# ── Tabs ──────────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📋  Descriptive",
    "🔍  Diagnostic",
    "🔮  Predictive",
    "🎯  Prescriptive",
    "📈  Regression",
])

with tab1: tab1_descriptive.render(subs, sess, mrr)
with tab2: tab2_diagnostic.render(subs, sess, mrr)
with tab3: tab3_predictive.render(subs, sess, mrr)
with tab4: tab4_prescriptive.render(subs, sess, mrr)
with tab5: tab5_regression.render(subs, sess, mrr)
