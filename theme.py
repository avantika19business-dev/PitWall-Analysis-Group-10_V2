# theme.py  —  PitWall Analytics  ·  F1 Premium Light Design System

# ── Core Palette ──────────────────────────────────────────────────────────────
F1_RED      = "#E8002D"
F1_BLACK    = "#1A1A1A"
F1_WHITE    = "#FFFFFF"
F1_SILVER   = "#6B7280"
F1_GOLD     = "#C9921A"
F1_GREY     = "#F5F5F7"
F1_DGREY    = "#E8E8EC"
CARBON      = "#2C2C2C"

ACCENT_TEAL   = "#0E7490"
ACCENT_GREEN  = "#15803D"
ACCENT_AMBER  = "#B45309"
ACCENT_BLUE   = "#1D4ED8"
ACCENT_PURPLE = "#7C3AED"

PLAN_COLORS = {
    "Pit Lane":     "#6B7280",
    "Podium":       "#E8002D",
    "Paddock Club": "#C9921A",
}
CHANNEL_COLORS = {
    "Paid Ad":      "#E8002D",
    "Organic":      "#15803D",
    "Social Media": "#B45309",
    "Referral":     "#0E7490",
}
NPS_COLORS = {
    "Promoter":  "#15803D",
    "Passive":   "#B45309",
    "Detractor": "#E8002D",
}
CHURN_COLORS = {
    "Active":  "#15803D",
    "Churned": "#E8002D",
}
RISK_COLORS = {
    "Low Risk":    "#15803D",
    "Medium Risk": "#B45309",
    "High Risk":   "#E8002D",
}
SEGMENT_COLORS = {
    "Champions": "#C9921A",
    "Engaged":   "#15803D",
    "At Risk":   "#B45309",
    "Dormant":   "#E8002D",
}
CLASSIFIER_COLORS = {
    "Random Forest":  "#E8002D",
    "Logistic Reg.":  "#0E7490",
    "Decision Tree":  "#C9921A",
    "KNN":            "#15803D",
    "Naive Bayes":    "#7C3AED",
    "SVM":            "#1D4ED8",
}


def hex_to_rgba(hex_color: str, alpha: float = 0.15) -> str:
    h = hex_color.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return f"rgba({r},{g},{b},{alpha})"


def base_layout(title: str = "", height: int = 400) -> dict:
    return dict(
        title=dict(
            text=f"<b>{title}</b>" if title else "",
            font=dict(color="#1A1A1A", size=13, family="Inter, Arial, sans-serif"),
            x=0.0, xanchor="left", pad=dict(b=6),
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#1A1A1A", family="Inter, Arial, sans-serif", size=12),
        height=height,
        margin=dict(l=48, r=32, t=52, b=44),
        legend=dict(
            bgcolor="rgba(255,255,255,0.95)",
            bordercolor="#E8E8EC", borderwidth=1,
            font=dict(color="#1A1A1A", size=11),
        ),
        xaxis=dict(
            gridcolor="#EBEBEF", linecolor="#D1D5DB", zerolinecolor="#D1D5DB",
            tickfont=dict(color="#6B7280", size=11),
            title_font=dict(color="#6B7280", size=11),
        ),
        yaxis=dict(
            gridcolor="#EBEBEF", linecolor="#D1D5DB", zerolinecolor="#D1D5DB",
            tickfont=dict(color="#6B7280", size=11),
            title_font=dict(color="#6B7280", size=11),
        ),
        hoverlabel=dict(
            bgcolor="#FFFFFF", bordercolor="#E8E8EC",
            font=dict(color="#1A1A1A", size=12),
        ),
    )


F1_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    background-color: #F5F5F7 !important;
    color: #1A1A1A !important;
}
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
section.main,
.main .block-container,
[data-testid="stTabsContent"] {
    background-color: #F5F5F7 !important;
}
.main .block-container {
    padding: 0.5rem 2rem 2rem 2rem !important;
    max-width: 1400px !important;
}
[data-testid="stSidebar"] {
    background-color: #FFFFFF !important;
    border-right: 1px solid #E8E8EC !important;
}
[data-testid="stSidebar"] * { color: #1A1A1A !important; }

[data-testid="stTabs"] > div:first-child {
    border-bottom: 1px solid #E8E8EC;
    background: transparent;
}
[data-testid="stTabs"] button {
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    font-size: 12px !important;
    letter-spacing: 0.2px !important;
    color: #9CA3AF !important;
    padding: 10px 18px !important;
    border-bottom: 2px solid transparent !important;
    background: transparent !important;
    border-radius: 0 !important;
}
[data-testid="stTabs"] button:hover { color: #374151 !important; }
[data-testid="stTabs"] button[aria-selected="true"] {
    color: #E8002D !important;
    border-bottom: 2px solid #E8002D !important;
    font-weight: 700 !important;
}
[data-testid="stTabsContent"] { padding-top: 1.5rem; }

[data-testid="metric-container"] {
    background: #FFFFFF !important;
    border: 1px solid #E8E8EC !important;
    border-left: 4px solid #E8002D !important;
    border-radius: 10px !important;
    padding: 18px 20px !important;
    box-shadow: 0 1px 4px rgba(0,0,0,0.06) !important;
}
[data-testid="metric-container"] label {
    color: #9CA3AF !important;
    font-size: 10px !important;
    letter-spacing: 1.5px !important;
    text-transform: uppercase !important;
    font-weight: 600 !important;
}
[data-testid="stMetricValue"] {
    color: #1A1A1A !important;
    font-size: 24px !important;
    font-weight: 800 !important;
    letter-spacing: -0.5px !important;
}
[data-testid="stMetricDelta"] span { font-size: 11px !important; font-weight: 500 !important; }

h1 { color: #1A1A1A !important; font-weight: 800 !important; font-size: 1.5rem !important; letter-spacing: -0.5px !important; }
h2 { color: #1A1A1A !important; font-weight: 700 !important; font-size: 1.2rem !important; letter-spacing: -0.3px !important; margin-bottom: 0.2rem !important; }
h2 em { color: #6B7280 !important; font-weight: 400 !important; font-size: 0.85rem; }
h3 { color: #374151 !important; font-weight: 600 !important; font-size: 0.88rem !important; }
hr { border-color: #E8E8EC !important; margin: 1.2rem 0 !important; }

[data-testid="stPlotlyChart"] {
    background: #FFFFFF;
    border: 1px solid #E8E8EC;
    border-radius: 12px;
    padding: 4px;
    box-shadow: 0 1px 4px rgba(0,0,0,0.05);
}
[data-testid="stDataFrame"] {
    border: 1px solid #E8E8EC !important;
    border-radius: 10px !important;
    overflow: hidden !important;
    box-shadow: 0 1px 4px rgba(0,0,0,0.04) !important;
}

.insight-box {
    background: #FFFFFF;
    border: 1px solid #E8E8EC;
    border-left: 4px solid #E8002D;
    border-radius: 0 10px 10px 0;
    padding: 14px 16px;
    margin: 6px 0 12px 0;
    font-size: 13px;
    line-height: 1.7;
    color: #374151;
    box-shadow: 0 1px 4px rgba(0,0,0,0.04);
}
.insight-box b { color: #E8002D; font-weight: 700; }

.rec-box {
    background: #FFFFFF;
    border: 1px solid #E8E8EC;
    border-left: 4px solid #15803D;
    border-radius: 0 10px 10px 0;
    padding: 14px 16px;
    margin: 6px 0 12px 0;
    font-size: 13px;
    line-height: 1.7;
    color: #374151;
    box-shadow: 0 1px 4px rgba(0,0,0,0.04);
}
.rec-box b { color: #15803D; font-weight: 700; }

.warn-box {
    background: #FFFFFF;
    border: 1px solid #E8E8EC;
    border-left: 4px solid #B45309;
    border-radius: 0 10px 10px 0;
    padding: 14px 16px;
    margin: 6px 0 12px 0;
    font-size: 13px;
    line-height: 1.7;
    color: #374151;
    box-shadow: 0 1px 4px rgba(0,0,0,0.04);
}
.warn-box b { color: #B45309; font-weight: 700; }

.section-label {
    font-size: 10px;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #E8002D;
    font-weight: 700;
    margin-bottom: 8px;
    font-family: 'Inter', sans-serif;
}
.chart-header {
    font-size: 13px;
    font-weight: 600;
    color: #0E7490;
    margin-bottom: 4px;
}

#MainMenu, footer, [data-testid="stToolbar"] { visibility: hidden; }
[data-testid="stHeader"] { background-color: #F5F5F7 !important; }
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: #F5F5F7; }
::-webkit-scrollbar-thumb { background: #D1D5DB; border-radius: 3px; }
</style>
"""


def section_label(text: str) -> str:
    return f'<div class="section-label">{text}</div>'

def chart_header(text: str) -> str:
    return f'<div class="chart-header">{text}</div>'

def insight_box(html: str) -> str:
    return f'<div class="insight-box">{html}</div>'

def rec_box(html: str) -> str:
    return f'<div class="rec-box">{html}</div>'

def warn_box(html: str) -> str:
    return f'<div class="warn-box">{html}</div>'
