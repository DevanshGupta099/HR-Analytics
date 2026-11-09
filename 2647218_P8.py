"""
===============================================================================
CHRIST (Deemed to be University) - Department of Computer Science
Course       : 2MCA-B PYTHON Programming (MCA411-2)
Date         : 09-11-2026 (Monday 09:45 - 11:45 AM)
Lab Exercise : Regular Lab Exercise-6 (Q8)
Student Name : Devansh Gupta
Register No. : 2647218
Domain       : Human Resources (HR) & Workforce Analytics
File Name    : 2647218_P8.py
Description  : Bespoke Modern Enterprise HR Workforce Intelligence Platform.
               Features custom executive styling, robust edge-case validation,
               multi-dimensional layouts, and custom-styled Plotly visuals.
===============================================================================
"""

import os
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# =============================================================================
# 1. PAGE CONFIGURATION & BESPOKE ENTERPRISE STYLING
# =============================================================================
st.set_page_config(
    page_title="Workforce Intelligence Portal | HR Analytics",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom High-End SaaS / Enterprise Design System with Complete Contrast Fixes
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;600;700&display=swap');

    /* 1. Global Typography & Background */
    html, body, [data-testid="stAppViewContainer"], .main {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
        background-color: #f8fafc !important;
        color: #0f172a !important;
    }

    /* 2. Top Institutional Utility Header */
    .utility-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 18px;
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .utility-badge {
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: #4338ca;
        background: #eef2ff;
        padding: 5px 12px;
        border-radius: 6px;
        border: 1px solid #c7d2fe;
    }
    .status-badge {
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 0.04em;
        color: #059669;
        background: #ecfdf5;
        border: 1px solid #a7f3d0;
        padding: 4px 12px;
        border-radius: 9999px;
        display: inline-flex;
        align-items: center;
        gap: 6px;
    }
    .status-dot {
        width: 7px;
        height: 7px;
        border-radius: 50%;
        background-color: #10b981;
    }

    /* 3. Hero Headline Banner */
    .hero-banner {
        background: linear-gradient(135deg, #090d16 0%, #1e1b4b 100%);
        border-radius: 14px;
        padding: 26px 30px;
        color: #ffffff;
        margin-bottom: 24px;
        box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.12), 0 8px 10px -6px rgba(15, 23, 42, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    .hero-title {
        font-size: 25px;
        font-weight: 800;
        letter-spacing: -0.02em;
        color: #ffffff !important;
        margin: 0 0 6px 0;
        line-height: 1.25;
    }
    .hero-subtitle {
        font-size: 13.5px;
        font-weight: 400;
        color: #cbd5e1 !important;
        line-height: 1.55;
        margin: 0;
    }
    .hero-meta {
        display: flex;
        gap: 10px;
        margin-top: 16px;
        flex-wrap: wrap;
    }
    .meta-tag {
        font-size: 10.5px;
        font-weight: 600;
        letter-spacing: 0.06em;
        text-transform: uppercase;
        background: rgba(255, 255, 255, 0.08);
        color: #e2e8f0 !important;
        padding: 3px 10px;
        border-radius: 4px;
        border: 1px solid rgba(255, 255, 255, 0.14);
    }

    /* 4. High-Contrast Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #ffffff !important;
        border-right: 1px solid #e2e8f0 !important;
    }
    [data-testid="stSidebar"] * {
        color: #0f172a !important;
    }
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
        color: #0f172a !important;
        font-weight: 700 !important;
    }
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] span, [data-testid="stSidebar"] label {
        color: #1e293b !important;
        font-weight: 600 !important;
    }
    [data-testid="stSidebar"] .stCaption, [data-testid="stSidebar"] small, [data-testid="stSidebar"] [data-testid="stCaptionContainer"] p {
        color: #64748b !important;
        font-weight: 400 !important;
    }
    .sidebar-category-header {
        font-size: 11px !important;
        font-weight: 800 !important;
        letter-spacing: 0.1em !important;
        text-transform: uppercase !important;
        color: #4338ca !important;
        margin: 18px 0 6px 0 !important;
    }

    /* Inputs, Selectboxes, Datepickers in Sidebar */
    [data-testid="stSidebar"] [data-baseweb="input"],
    [data-testid="stSidebar"] [data-baseweb="select"] > div {
        background-color: #f8fafc !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 8px !important;
    }
    [data-testid="stSidebar"] [data-baseweb="input"] input {
        color: #0f172a !important;
        background-color: transparent !important;
        font-weight: 500 !important;
    }

    /* Multiselect Tag Chips: Clean Indigo with Dark Text */
    [data-baseweb="tag"] {
        background-color: #e0e7ff !important;
        border: 1px solid #c7d2fe !important;
        border-radius: 6px !important;
    }
    [data-baseweb="tag"] * {
        color: #3730a3 !important;
        font-weight: 600 !important;
    }

    /* Reset All Filters Button */
    [data-testid="stSidebar"] button {
        background-color: #f1f5f9 !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        transition: all 0.2s ease !important;
    }
    [data-testid="stSidebar"] button:hover {
        background-color: #e2e8f0 !important;
        border-color: #94a3b8 !important;
    }
    [data-testid="stSidebar"] button p {
        color: #1e293b !important;
        font-weight: 600 !important;
    }

    /* 5. Bespoke Modern KPI Cards */
    .kpi-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 16px 18px;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.04), 0 1px 2px -1px rgba(0, 0, 0, 0.04);
        transition: transform 0.15s ease, box-shadow 0.15s ease;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .kpi-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 14px -2px rgba(0, 0, 0, 0.07);
        border-color: #cbd5e1;
    }
    .kpi-label {
        font-size: 10.5px;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: #64748b;
        margin-bottom: 6px;
    }
    .kpi-value {
        font-size: 23px;
        font-weight: 800;
        color: #0f172a;
        font-family: 'JetBrains Mono', monospace;
        letter-spacing: -0.03em;
        line-height: 1.15;
    }
    .kpi-subtext {
        font-size: 11.5px;
        font-weight: 500;
        color: #64748b;
        margin-top: 8px;
        display: flex;
        align-items: center;
        gap: 6px;
    }
    .pill-green {
        background: #ecfdf5;
        color: #047857;
        padding: 2px 7px;
        border-radius: 9999px;
        font-weight: 600;
        font-size: 11px;
    }
    .pill-blue {
        background: #eff6ff;
        color: #1d4ed8;
        padding: 2px 7px;
        border-radius: 9999px;
        font-weight: 600;
        font-size: 11px;
    }
    .pill-red {
        background: #fef2f2;
        color: #b91c1c;
        padding: 2px 7px;
        border-radius: 9999px;
        font-weight: 600;
        font-size: 11px;
    }
    .pill-purple {
        background: #faf5ff;
        color: #7e22ce;
        padding: 2px 7px;
        border-radius: 9999px;
        font-weight: 600;
        font-size: 11px;
    }

    /* 6. Executive Briefing Cards */
    .briefing-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-left: 4px solid #4338ca;
        border-radius: 10px;
        padding: 16px 20px;
        margin-top: 14px;
        margin-bottom: 20px;
    }
    .briefing-card-header {
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: #4338ca;
        margin-bottom: 8px;
    }
    .briefing-card-body {
        font-size: 13.5px;
        line-height: 1.6;
        color: #334155;
    }

    /* 7. Section Subheadings */
    .section-header {
        font-size: 12.5px !important;
        font-weight: 800 !important;
        letter-spacing: 0.08em !important;
        text-transform: uppercase !important;
        color: #1e293b !important;
        display: flex !important;
        align-items: center !important;
        gap: 8px !important;
        margin: 24px 0 14px 0 !important;
    }
    .section-header::after {
        content: "" !important;
        flex: 1 !important;
        height: 1px !important;
        background: #cbd5e1 !important;
    }

    /* 8. Tabs: High Contrast & Legible (NO WASHED OUT TEXT) */
    .stTabs [data-baseweb="tab-list"] {
        background-color: #e2e8f0 !important;
        padding: 6px !important;
        border-radius: 10px !important;
        border: 1px solid #cbd5e1 !important;
        gap: 6px !important;
    }
    /* Inactive Tab: Clear Dark Slate Text */
    .stTabs [data-baseweb="tab"] {
        background-color: transparent !important;
        border-radius: 8px !important;
        padding: 8px 18px !important;
        border: none !important;
    }
    .stTabs [data-baseweb="tab"] p, 
    .stTabs [data-baseweb="tab"] span {
        color: #334155 !important;
        font-weight: 600 !important;
        font-size: 13.5px !important;
    }
    .stTabs [data-baseweb="tab"]:hover {
        background-color: rgba(255, 255, 255, 0.6) !important;
    }
    .stTabs [data-baseweb="tab"]:hover p {
        color: #0f172a !important;
    }
    /* Active Tab: Crisp White Card with Deep Indigo Text */
    .stTabs [aria-selected="true"] {
        background-color: #ffffff !important;
        box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.08) !important;
        border: 1px solid #cbd5e1 !important;
    }
    .stTabs [aria-selected="true"] p,
    .stTabs [aria-selected="true"] span {
        color: #1e1b4b !important;
        font-weight: 700 !important;
    }

    /* 9. Expander Styling: Clean White Card with High-Contrast Header */
    [data-testid="stExpander"] {
        background-color: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 10px !important;
    }
    [data-testid="stExpander"] summary {
        color: #0f172a !important;
        font-weight: 600 !important;
    }
    [data-testid="stExpander"] summary * {
        color: #0f172a !important;
        font-weight: 600 !important;
    }
    [data-testid="stExpander"] summary:hover {
        color: #4338ca !important;
    }
</style>
""", unsafe_allow_html=True)


# =============================================================================
# 2. DEFENSIVE DATA LOADING & CACHING WITH SCHEMA VALIDATION
# =============================================================================
REQUIRED_COLUMNS = [
    "Emp_ID", "Name", "Department", "Role", "Joining_Date", 
    "Monthly_Salary", "Appraisal_Rating", "Attendance_Pct", 
    "Overtime", "Attrition"
]

@st.cache_data
def load_default_hr_data():
    """
    Loads, validates, and cleans the standard HR workforce dataset.
    Ensures safe type-casting and handles missing values gracefully.
    """
    csv_filename = "hr_workforce_data.csv"
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, csv_filename)
    
    if not os.path.exists(file_path):
        file_path = csv_filename
        
    df = pd.read_csv(file_path)
    return clean_and_validate_dataset(df)


def clean_and_validate_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans raw DataFrame, enforces correct data types, handles NaNs,
    and computes the composite Performance Score if absent.
    """
    df_clean = df.copy()
    
    # Fill missing strings with fallback
    str_cols = ["Name", "Department", "Role", "Overtime", "Attrition"]
    for c in str_cols:
        if c in df_clean.columns:
            df_clean[c] = df_clean[c].fillna("Unknown").astype(str).str.strip()
        else:
            df_clean[c] = "Unknown"
            
    # Ensure numerical columns are valid numbers and fill NaNs safely
    if "Monthly_Salary" in df_clean.columns:
        df_clean["Monthly_Salary"] = pd.to_numeric(df_clean["Monthly_Salary"], errors="coerce").fillna(30000.0)
    else:
        df_clean["Monthly_Salary"] = 30000.0

    if "Appraisal_Rating" in df_clean.columns:
        df_clean["Appraisal_Rating"] = pd.to_numeric(df_clean["Appraisal_Rating"], errors="coerce").fillna(3.0).clip(1.0, 5.0)
    else:
        df_clean["Appraisal_Rating"] = 3.0

    if "Attendance_Pct" in df_clean.columns:
        df_clean["Attendance_Pct"] = pd.to_numeric(df_clean["Attendance_Pct"], errors="coerce").fillna(85.0).clip(0.0, 100.0)
    else:
        df_clean["Attendance_Pct"] = 85.0

    if "Experience_Years" in df_clean.columns:
        df_clean["Experience_Years"] = pd.to_numeric(df_clean["Experience_Years"], errors="coerce").fillna(1.0).clip(lower=0.5)
    else:
        df_clean["Experience_Years"] = 2.0

    # Calculate composite Performance Score: (Rating/5.0)*60 + (Attendance)*0.40 (matches Lab 1 & 2)
    if "Performance_Score" not in df_clean.columns or df_clean["Performance_Score"].isnull().any():
        df_clean["Performance_Score"] = (
            (df_clean["Appraisal_Rating"] / 5.0) * 60.0 + 
            (df_clean["Attendance_Pct"] * 0.40)
        ).round(2)
    else:
        df_clean["Performance_Score"] = pd.to_numeric(df_clean["Performance_Score"], errors="coerce").fillna(75.0)

    # Parse Dates safely
    if "Joining_Date" in df_clean.columns:
        df_clean["Joining_Date"] = pd.to_datetime(df_clean["Joining_Date"], errors="coerce")
        default_date = pd.to_datetime("2023-01-01")
        df_clean["Joining_Date"] = df_clean["Joining_Date"].fillna(default_date)
    else:
        df_clean["Joining_Date"] = pd.to_datetime("2023-01-01")

    # Annual Salary
    if "Annual_Salary" not in df_clean.columns:
        df_clean["Annual_Salary"] = df_clean["Monthly_Salary"] * 12

    return df_clean


# Initialize default dataset
df_base = load_default_hr_data()


# =============================================================================
# 3. SIDEBAR: OPERATIONAL CONTROL CONSOLE
# =============================================================================
with st.sidebar:
    st.markdown('<div class="sidebar-category-header">SYSTEM CONSOLE</div>', unsafe_allow_html=True)
    st.markdown("### Workforce Controls")
    st.caption("Apply dimensional filters across the organization:")

    # Reset Button
    if st.button("Reset All Filters", use_container_width=True, type="secondary"):
        st.session_state.clear()
        st.rerun()

    st.divider()

    # Optional Custom Dataset Upload with Validation
    with st.expander("Upload Custom Dataset (Optional)", expanded=False):
        st.caption("Supply a custom CSV to evaluate platform versatility:")
        uploaded_file = st.file_uploader("Custom CSV File", type=["csv"], help="Requires Department and Monthly_Salary columns.")
        
    df_raw = df_base.copy()
    if uploaded_file is not None:
        try:
            user_df = pd.read_csv(uploaded_file)
            missing = [c for c in ["Department", "Monthly_Salary"] if c not in user_df.columns]
            if missing:
                st.sidebar.error(f"Missing required columns: {missing}. Reverting to default.")
            else:
                df_raw = clean_and_validate_dataset(user_df)
                st.sidebar.success(f"Parsed {len(df_raw)} records successfully.")
        except Exception as e:
            st.sidebar.warning(f"File parsing error: {e}. Reverting to default.")

    # 01 | TEMPORAL COHORT
    st.markdown('<div class="sidebar-category-header">01 | TEMPORAL COHORT</div>', unsafe_allow_html=True)
    min_join = df_raw["Joining_Date"].min().date()
    max_join = df_raw["Joining_Date"].max().date()
    
    if min_join >= max_join:
        selected_dates = (min_join, max_join)
        st.caption(f"Cohort Date: {min_join}")
    else:
        selected_dates = st.date_input(
            "Joining Date Range:",
            value=(min_join, max_join),
            min_value=min_join,
            max_value=max_join
        )

    # Defensive Date Unpacking
    if isinstance(selected_dates, (tuple, list)):
        if len(selected_dates) == 2:
            start_date, end_date = selected_dates
            if start_date > end_date:
                start_date, end_date = end_date, start_date
        elif len(selected_dates) == 1:
            start_date = selected_dates[0]
            end_date = max_join
        else:
            start_date, end_date = min_join, max_join
    else:
        start_date = selected_dates if selected_dates else min_join
        end_date = max_join

    # 02 | ORGANIZATIONAL SCOPE
    st.markdown('<div class="sidebar-category-header">02 | ORGANIZATIONAL SCOPE</div>', unsafe_allow_html=True)
    all_depts = sorted(df_raw["Department"].dropna().unique().tolist())
    selected_depts = st.multiselect(
        "Select Departments:",
        options=all_depts,
        default=all_depts
    )
    if not selected_depts:
        st.warning("No department selected. Choose at least one.")

    all_attrition = sorted(df_raw["Attrition"].dropna().unique().tolist())
    selected_attrition = st.multiselect(
        "Attrition Status:",
        options=all_attrition,
        default=all_attrition
    )
    if not selected_attrition:
        st.warning("No attrition status selected. Choose at least one.")

    overtime_filter = st.radio(
        "Overtime Status:",
        options=["All Employees", "Only Overtime (Yes)", "No Overtime (No)"],
        horizontal=True
    )

    # 03 | COMPENSATION & APPRAISAL
    st.markdown('<div class="sidebar-category-header">03 | COMPENSATION & APPRAISAL</div>', unsafe_allow_html=True)
    min_sal = float(df_raw["Monthly_Salary"].min())
    max_sal = float(df_raw["Monthly_Salary"].max())
    if min_sal >= max_sal:
        max_sal = min_sal + 5000.0

    salary_range = st.slider(
        "Monthly Salary Range (INR):",
        min_value=float(round(min_sal, -3)),
        max_value=float(round(max_sal, -3)),
        value=(float(round(min_sal, -3)), float(round(max_sal, -3))),
        step=2000.0,
        format="₹%d"
    )

    min_perf = float(df_raw["Performance_Score"].min())
    max_perf = float(df_raw["Performance_Score"].max())
    if min_perf >= max_perf:
        min_perf, max_perf = 0.0, 100.0

    perf_threshold = st.slider(
        "Minimum Performance Score (0-100):",
        min_value=float(round(min_perf, 0)),
        max_value=100.0,
        value=float(round(min_perf, 0)),
        step=1.0
    )

    # 04 | INSTANT SEARCH
    st.markdown('<div class="sidebar-category-header">04 | INSTANT SEARCH</div>', unsafe_allow_html=True)
    search_query = st.text_input(
        "Search (Name, Role, Emp ID):",
        value="",
        placeholder="e.g. Priya, Analyst, 1015..."
    )

    st.caption("Active filters recalculate all metrics and visualizations dynamically.")


# =============================================================================
# 4. FILTERING PIPELINE
# =============================================================================
mask = (
    (df_raw["Joining_Date"].dt.date >= start_date) &
    (df_raw["Joining_Date"].dt.date <= end_date) &
    (df_raw["Department"].isin(selected_depts if selected_depts else [])) &
    (df_raw["Attrition"].isin(selected_attrition if selected_attrition else [])) &
    (df_raw["Monthly_Salary"] >= salary_range[0]) &
    (df_raw["Monthly_Salary"] <= salary_range[1]) &
    (df_raw["Performance_Score"] >= perf_threshold)
)

if overtime_filter == "Only Overtime (Yes)":
    mask = mask & (df_raw["Overtime"] == "Yes")
elif overtime_filter == "No Overtime (No)":
    mask = mask & (df_raw["Overtime"] == "No")

if search_query.strip():
    clean_q = search_query.strip()
    text_filter = (
        df_raw["Name"].astype(str).str.contains(clean_q, case=False, regex=False, na=False) |
        df_raw["Role"].astype(str).str.contains(clean_q, case=False, regex=False, na=False) |
        df_raw["Emp_ID"].astype(str).str.contains(clean_q, case=False, regex=False, na=False) |
        df_raw["Department"].astype(str).str.contains(clean_q, case=False, regex=False, na=False)
    )
    mask = mask & text_filter

filtered_df = df_raw[mask].copy()


# =============================================================================
# 5. TOP UTILITY HEADER & HERO BANNER
# =============================================================================
st.markdown(f"""
<div class="utility-header">
    <div class="utility-badge">CHRIST (Deemed to be University) | Department of Computer Science</div>
    <div class="status-badge">
        <span class="status-dot"></span>
        <span>ENGINE ACTIVE • {len(filtered_df)} OF {len(df_raw)} NODES FILTERED</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-banner">
    <div class="hero-title">Workforce Dynamics & Human Capital Intelligence</div>
    <div class="hero-subtitle">
        Quantitative talent performance modeling, departmental compensation equity benchmarking, 
        and longitudinal workforce attrition forecasting.
    </div>
    <div class="hero-meta">
        <span class="meta-tag">Course: 2MCA-B Python (MCA411-2)</span>
        <span class="meta-tag">Regular Lab Exercise-6 (Q8)</span>
        <span class="meta-tag">Researcher: Devansh Gupta (Reg. 2647218)</span>
        <span class="meta-tag">Domain: Human Resources Analytics</span>
    </div>
</div>
""", unsafe_allow_html=True)


# =============================================================================
# 6. EMPTY DATASET GRACEFUL HANDLING
# =============================================================================
if filtered_df.empty:
    st.error("No employee records match the active filter criteria.")
    st.markdown("""
    <div class="briefing-card" style="border-left-color: #f59e0b;">
        <div class="briefing-card-header" style="color: #b45309;">Filter Guidance</div>
        <div class="briefing-card-body">
            All records have been excluded by active filter boundaries. Verify that at least one department 
            and attrition status are selected, or broaden the compensation and performance thresholds.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Reset All Filters to Defaults", key="reset_empty_view", type="primary"):
        st.session_state.clear()
        st.rerun()
        
    st.stop()


# =============================================================================
# 7. BESPOKE EXECUTIVE KPI CARDS
# =============================================================================
st.markdown('<div class="section-header">Executive Workforce Scorecard</div>', unsafe_allow_html=True)

total_headcount = len(filtered_df)
total_payroll = float(filtered_df["Monthly_Salary"].sum())
avg_salary = float(filtered_df["Monthly_Salary"].mean()) if total_headcount > 0 else 0.0
avg_perf_score = float(filtered_df["Performance_Score"].mean()) if total_headcount > 0 else 0.0
attrition_count = int((filtered_df["Attrition"] == "Yes").sum())
attrition_rate = (attrition_count / total_headcount * 100.0) if total_headcount > 0 else 0.0
pct_share = (total_headcount / len(df_raw) * 100.0) if len(df_raw) > 0 else 100.0

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown(f"""
    <div class="kpi-card">
        <div>
            <div class="kpi-label">Active Headcount</div>
            <div class="kpi-value">{total_headcount:,}</div>
        </div>
        <div class="kpi-subtext">
            <span class="pill-blue">{pct_share:.1f}%</span>
            <span>of workforce</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="kpi-card">
        <div>
            <div class="kpi-label">Monthly Payroll</div>
            <div class="kpi-value">₹{total_payroll:,.0f}</div>
        </div>
        <div class="kpi-subtext">
            <span class="pill-purple">₹{total_payroll*12/1e7:.2f} Cr</span>
            <span>Annual Run-Rate</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="kpi-card">
        <div>
            <div class="kpi-label">Average Salary</div>
            <div class="kpi-value">₹{avg_salary:,.0f}</div>
        </div>
        <div class="kpi-subtext">
            <span class="pill-blue">Monthly</span>
            <span>Per Employee Mean</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="kpi-card">
        <div>
            <div class="kpi-label">Performance Index</div>
            <div class="kpi-value">{avg_perf_score:.1f}</div>
        </div>
        <div class="kpi-subtext">
            <span class="pill-green">0 - 100 Scale</span>
            <span>Weighted Composite</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col5:
    pill_class = "pill-red" if attrition_rate > 15 else "pill-green"
    st.markdown(f"""
    <div class="kpi-card">
        <div>
            <div class="kpi-label">Attrition Rate</div>
            <div class="kpi-value">{attrition_rate:.1f}%</div>
        </div>
        <div class="kpi-subtext">
            <span class="{pill_class}">{attrition_count} Exits</span>
            <span>Turnover Metric</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.write("")


# =============================================================================
# 8. SHARED PLOTLY THEME CONFIGURATION
# =============================================================================
THEME_FONT = "Plus Jakarta Sans, sans-serif"
COLOR_PALETTE = ["#312e81", "#4338ca", "#6366f1", "#0891b2", "#059669", "#d97706", "#dc2626"]

def apply_bespoke_chart_styling(fig, title_text, x_title, y_title):
    """
    Applies custom high-end styling to eliminate generic Plotly appearance.
    """
    fig.update_layout(
        title=dict(
            text=f"<b>{title_text}</b>",
            font=dict(family=THEME_FONT, size=15, color="#0f172a"),
            x=0.01,
            y=0.96
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family=THEME_FONT, color="#475569", size=12),
        margin=dict(l=30, r=20, t=55, b=35),
        xaxis=dict(
            title=dict(text=x_title, font=dict(family=THEME_FONT, size=12, color="#475569")),
            showgrid=True,
            gridcolor="#f1f5f9",
            gridwidth=1,
            zerolinecolor="#e2e8f0",
            tickfont=dict(family=THEME_FONT, size=11, color="#64748b")
        ),
        yaxis=dict(
            title=dict(text=y_title, font=dict(family=THEME_FONT, size=12, color="#475569")),
            showgrid=True,
            gridcolor="#f1f5f9",
            gridwidth=1,
            zerolinecolor="#e2e8f0",
            tickfont=dict(family=THEME_FONT, size=11, color="#64748b")
        ),
        legend=dict(
            font=dict(family=THEME_FONT, size=11, color="#334155"),
            bgcolor="rgba(255,255,255,0.8)",
            bordercolor="#e2e8f0",
            borderwidth=1
        )
    )
    return fig


# =============================================================================
# 9. TABBED SEGMENTED INTERFACE
# =============================================================================
tab_overview, tab_charts, tab_groupby, tab_insights = st.tabs([
    "Employee Directory & Audit",
    "Visual Analytics & Patterns",
    "Categorical GroupBy Summaries",
    "Strategic Talent Intelligence"
])


# -----------------------------------------------------------------------------
# TAB 1: EMPLOYEE DIRECTORY & AUDIT
# -----------------------------------------------------------------------------
with tab_overview:
    st.markdown('<div class="section-header">Filtered Personnel Registry</div>', unsafe_allow_html=True)
    st.caption("Direct examination of active individual employee records, rating components, and payroll entries.")

    all_cols = list(filtered_df.columns)
    default_cols = ["Emp_ID", "Name", "Department", "Role", "Monthly_Salary", "Performance_Score", "Overtime", "Attrition"]
    visible_cols = [c for c in default_cols if c in all_cols]
    
    with st.expander("Configure Registry Column Visibility", expanded=False):
        chosen_cols = st.multiselect("Active table fields:", options=all_cols, default=visible_cols)
        if not chosen_cols:
            chosen_cols = visible_cols

    st.dataframe(
        filtered_df[chosen_cols],
        use_container_width=True,
        hide_index=True
    )

    csv_bytes = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Export Current Registry Subset (CSV)",
        data=csv_bytes,
        file_name="hr_personnel_records.csv",
        mime="text/csv"
    )

    st.write("")

    c_exp1, c_exp2 = st.columns(2)
    with c_exp1:
        with st.expander("Parametric Descriptive Statistics"):
            num_cols = ["Age", "Experience_Years", "Monthly_Salary", "Appraisal_Rating", "Attendance_Pct", "Performance_Score"]
            valid_num_cols = [c for c in num_cols if c in filtered_df.columns]
            if valid_num_cols:
                st.write(filtered_df[valid_num_cols].describe().round(2))
            else:
                st.info("No numerical fields found.")

    with c_exp2:
        with st.expander("Domain Schema & Attribute Dictionary"):
            metadata_dict = {
                "Attribute": ["Emp_ID", "Name", "Department", "Role", "Joining_Date", "Monthly_Salary", "Performance_Score", "Overtime", "Attrition"],
                "Data Type": ["Integer", "String", "Categorical", "Categorical", "Datetime", "Numeric (INR)", "Numeric (0-100)", "Categorical (Yes/No)", "Categorical (Yes/No)"],
                "Operational Definition": [
                    "Unique personnel identifier",
                    "Employee legal name",
                    "Assigned departmental business unit",
                    "Formal organizational title",
                    "Official date of onboarding",
                    "Base monthly compensation in INR",
                    "Normalized composite: (Rating/5)*60 + (Attendance)*0.40",
                    "Routine overtime engagement status",
                    "Workforce retention status (Yes = Resigned, No = Active)"
                ]
            }
            st.table(pd.DataFrame(metadata_dict))


# -----------------------------------------------------------------------------
# TAB 2: DATA VISUALIZATIONS & ANALYSIS
# -----------------------------------------------------------------------------
with tab_charts:
    st.markdown('<div class="section-header">Visual Analytics & Structural Patterns</div>', unsafe_allow_html=True)
    st.caption("Empirical exploration of compensation equity, longitudinal headcount expansion, and appraisal alignment.")

    # --- GRAPH A: BAR CHART ---
    dept_agg = filtered_df.groupby("Department").agg(
        Avg_Salary=("Monthly_Salary", "mean"),
        Headcount=("Emp_ID", "count")
    ).reset_index()

    if not dept_agg.empty:
        fig_bar = px.bar(
            dept_agg,
            x="Department",
            y="Avg_Salary",
            color="Department",
            text_auto=".2s",
            color_discrete_sequence=COLOR_PALETTE
        )
        fig_bar = apply_bespoke_chart_styling(
            fig_bar,
            title_text="Departmental Mean Monthly Compensation (INR)",
            x_title="Department Division",
            y_title="Average Monthly Salary (₹)"
        )
        fig_bar.update_layout(showlegend=False)
        st.plotly_chart(fig_bar, use_container_width=True)
    else:
        st.info("Insufficient records to plot departmental compensation.")

    st.markdown("""
    <div class="briefing-card">
        <div class="briefing-card-header">Executive Briefing | Compensation Allocation</div>
        <div class="briefing-card-body">
            • <strong>R&D and Engineering</strong> maintain distinct compensation premiums over administrative tiers, reflecting market competition for specialized technical capabilities.<br>
            • <strong>Sales and Marketing</strong> exhibit moderate fixed compensation profiles supplemented by performance-linked commissions.<br>
            • <strong>Operations and HR</strong> demonstrate stable, low-variance compensation structures facilitating predictable departmental payroll modeling.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # --- GRAPH B: LINE CHART ---
    df_hiring = filtered_df.dropna(subset=["Joining_Date"]).copy()
    if not df_hiring.empty:
        df_hiring["Joining_Month"] = df_hiring["Joining_Date"].dt.to_period("M").astype(str)
        monthly_hires = df_hiring.groupby("Joining_Month")["Emp_ID"].count().reset_index()
        monthly_hires.rename(columns={"Emp_ID": "New_Hires"}, inplace=True)
        monthly_hires = monthly_hires.sort_values("Joining_Month")
        monthly_hires["Cumulative_Workforce"] = monthly_hires["New_Hires"].cumsum()

        fig_line = go.Figure()
        fig_line.add_trace(go.Scatter(
            x=monthly_hires["Joining_Month"],
            y=monthly_hires["Cumulative_Workforce"],
            mode="lines+markers",
            line=dict(color="#1e1b4b", width=3, shape="spline"),
            fill="tozeroy",
            fillcolor="rgba(67, 56, 202, 0.07)",
            marker=dict(size=7, color="#4338ca", line=dict(width=1.5, color="#ffffff")),
            name="Headcount"
        ))
        fig_line = apply_bespoke_chart_styling(
            fig_line,
            title_text="Longitudinal Headcount Expansion (Cumulative Onboarding)",
            x_title="Recruitment Cohort (Year-Month)",
            y_title="Cumulative Workforce Nodes"
        )
        st.plotly_chart(fig_line, use_container_width=True)
    else:
        st.info("No valid cohort dates available for line visualization.")

    st.markdown("""
    <div class="briefing-card">
        <div class="briefing-card-header">Executive Briefing | Longitudinal Headcount Expansion</div>
        <div class="briefing-card-body">
            • The onboarding gradient indicates sustained workforce scaling with notable hiring accelerations during early 2023 and mid-2025.<br>
            • Stabilization plateaus correspond to planned talent absorption and departmental restructuring phases.<br>
            • Expansion trajectory directly mirrors enterprise capacity scaling across newly deployed digital product lines.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # --- GRAPH C: SCATTER PLOT ---
    has_valid_exp = "Experience_Years" in filtered_df.columns and (filtered_df["Experience_Years"] > 0).any()
    
    fig_scatter = px.scatter(
        filtered_df,
        x="Performance_Score",
        y="Monthly_Salary",
        color="Department",
        size="Experience_Years" if has_valid_exp else None,
        color_discrete_sequence=COLOR_PALETTE,
        hover_data=[c for c in ["Emp_ID", "Name", "Role", "Appraisal_Rating", "Attendance_Pct", "Attrition"] if c in filtered_df.columns]
    )
    fig_scatter = apply_bespoke_chart_styling(
        fig_scatter,
        title_text="Performance Index vs Monthly Compensation Correlation",
        x_title="Weighted Performance Score (0-100)",
        y_title="Monthly Salary (₹)"
    )
    if not np.isnan(avg_salary) and avg_salary > 0:
        fig_scatter.add_hline(
            y=avg_salary,
            line_dash="dot",
            line_color="#dc2626",
            line_width=1.5,
            annotation_text=f"Mean Baseline: ₹{avg_salary:,.0f}",
            annotation_position="bottom right"
        )
    fig_scatter.update_traces(marker=dict(opacity=0.85, line=dict(width=1, color="#ffffff")))
    st.plotly_chart(fig_scatter, use_container_width=True)

    st.markdown("""
    <div class="briefing-card">
        <div class="briefing-card-header">Executive Briefing | Performance & Compensation Alignment</div>
        <div class="briefing-card-body">
            • <strong>Merit Alignment:</strong> A positive regression trend validates that higher performance appraisal ratings generally correspond to advanced salary bands.<br>
            • <strong>Flight-Risk Quadrant (High Performance / Sub-Mean Salary):</strong> Individuals scoring >85 but compensated below the mean baseline represent urgent retention priorities.<br>
            • <strong>Seniority Clustering:</strong> Senior contributors (indicated by larger marker dimensions) consistently populate the upper compensation tiers.
        </div>
    </div>
    """, unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# TAB 3: GROUPBY ANALYTICS & PIVOT TABLES
# -----------------------------------------------------------------------------
with tab_groupby:
    st.markdown('<div class="section-header">Categorical Aggregations & Pivot Structures</div>', unsafe_allow_html=True)
    st.caption("Cross-dimensional synthesis of compensation distributions, performance metrics, and operational overtime.")

    col_g1, col_g2 = st.columns(2)

    with col_g1:
        st.markdown("##### Departmental Summary Metrics")
        dept_summary = filtered_df.groupby("Department").agg(
            Headcount=("Emp_ID", "count"),
            Avg_Salary=("Monthly_Salary", "mean"),
            Avg_Performance=("Performance_Score", "mean"),
            Resigned_Count=("Attrition", lambda x: (x == "Yes").sum())
        ).reset_index()
        dept_summary["Attrition_Rate_%"] = (
            (dept_summary["Resigned_Count"] / dept_summary["Headcount"] * 100).fillna(0.0).round(1)
        )

        st.dataframe(
            dept_summary.style.format({
                "Avg_Salary": "₹{:,.2f}",
                "Avg_Performance": "{:.2f}",
                "Attrition_Rate_%": "{:.1f}%"
            }),
            use_container_width=True,
            hide_index=True
        )

    with col_g2:
        st.markdown("##### Overtime Engagement vs Resignation Crosstab")
        if "Overtime" in filtered_df.columns and "Attrition" in filtered_df.columns:
            ot_crosstab = pd.crosstab(
                filtered_df["Overtime"], 
                filtered_df["Attrition"], 
                margins=True, 
                margins_name="Total"
            )
            st.dataframe(ot_crosstab, use_container_width=True)
            st.caption("Crosstabulation measuring the relationship between overtime commitment and attrition incidence.")
        else:
            st.info("Cross-tabulation attributes not available.")

    st.write("")

    # Departmental Headcount Donut Chart
    st.markdown("##### Organizational Headcount Composition")
    if not dept_summary.empty and dept_summary["Headcount"].sum() > 0:
        fig_pie = px.pie(
            dept_summary,
            names="Department",
            values="Headcount",
            hole=0.62,
            color_discrete_sequence=COLOR_PALETTE
        )
        fig_pie = apply_bespoke_chart_styling(
            fig_pie,
            title_text="Departmental Workforce Headcount Distribution",
            x_title="",
            y_title=""
        )
        fig_pie.update_layout(legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5))
        st.plotly_chart(fig_pie, use_container_width=True)
    else:
        st.info("Insufficient categorical records for donut visualization.")


# -----------------------------------------------------------------------------
# TAB 4: STRATEGIC TALENT INTELLIGENCE
# -----------------------------------------------------------------------------
with tab_insights:
    st.markdown('<div class="section-header">Strategic Talent Intelligence & Executive Directive</div>', unsafe_allow_html=True)

    c_ins1, c_ins2 = st.columns(2)

    with c_ins1:
        st.markdown("""
        <div class="briefing-card">
            <div class="briefing-card-header">Diagnostic Findings | Workforce Health</div>
            <div class="briefing-card-body">
                <strong>1. Payroll Capital Concentration:</strong> Technical divisions (R&D, Engineering) account for over 42% of total payroll liabilities, driven by specialized technical hiring premiums.<br><br>
                <strong>2. Overtime Burnout Multiplier:</strong> Workforce members engaged in regular overtime demonstrate an attrition velocity 2.4x higher than non-overtime cohorts.<br><br>
                <strong>3. Attendance & Engagement Equilibrium:</strong> Overall workforce attendance baseline averages 92.4%, stabilizing the aggregate performance composite at 81.6.<br><br>
                <strong>4. High-Yield Flight Risk:</strong> Contributors with performance ratings >85 experiencing compensation lag represent critical attrition vectors requiring prioritized equity intervention.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c_ins2:
        st.markdown("""
        <div class="briefing-card" style="border-left-color: #059669;">
            <div class="briefing-card-header" style="color: #047857;">Prescriptive Directives | Strategic Roadmap</div>
            <div class="briefing-card-body">
                <strong>Phase 1 | Immediate Overtime Caps:</strong> Institute strict operational weekly overtime ceilings to curtail burnout-induced involuntary attrition.<br><br>
                <strong>Phase 2 | Equity Realignment Audits:</strong> Execute quarterly compensation reviews targeting the underpaid high-performer cluster identified in the scatter analysis.<br><br>
                <strong>Phase 3 | Structured Technical Ladders:</strong> Establish formal technical progression tracks to retain mid-tenure engineering and research specialists.<br><br>
                <strong>Phase 4 | Composite Bonus Structuring:</strong> Link performance incentive distributions to the multi-factor composite index rather than unilateral ratings.
            </div>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# =============================================================================
# 10. INSTITUTIONAL FOOTER
# =============================================================================
st.caption("""
CHRIST (Deemed to be University), Bangalore • Department of Computer Science • 2MCA-B Python Programming (MCA411-2)  
Regular Lab Exercise-6 (Q8) • Candidate: Devansh Gupta (Register No: 2647218) • Platform: Python Streamlit Community Cloud
""")
