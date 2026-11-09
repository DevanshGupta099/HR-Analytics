# 👥 Regular Lab Exercise-6 (Q8): Streamlit HR Workforce Analytics Dashboard
**Course:** 2MCA-B PYTHON Programming (MCA411-2)  
**Date:** 09-11-2026 (Monday 09:45 AM - 11:45 AM)  
**Student Name:** Devansh Gupta  
**Register No:** 2647218  
**Department:** Department of Computer Science, CHRIST (Deemed to be University)

---

## 📌 Problem Statement (Q8)
> **Design a web application to explore the different graphs using layouts (Streamlit Application for Analysis)**  
> Develop an interactive web-based data analytics application using Python Streamlit to explore, analyse and visualize patterns in a domain-specific dataset (Human Resources Management workforce dataset, maintaining domain consistency with Lab 1 & Lab 2). Design a visually appealing, user-friendly, and interactive dashboard that enables users to explore the dataset, identify meaningful patterns, interpret analytical results, and support data-driven decision-making.

---

## 📂 Lab 6 Directory Contents

| File Name | Purpose | Description |
| :--- | :--- | :--- |
| **`app.py`** | Main Application | Full interactive Streamlit HR dashboard (standard cloud entrypoint) |
| **`2647218_P8.py`** | Submission Script | Official script with registration header for Google Classroom submission |
| **`hr_workforce_data.csv`** | Domain Dataset | 250 curated employee records with 14 attributes matching Lab 1 & Lab 2 schema |
| **`requirements.txt`** | Dependencies | Package specifications (`streamlit`, `pandas`, `numpy`, `plotly`) |
| **`2647218_P6_Lab_Report.docx`** | Submission Report | Complete official Word document with embedded screenshots, analysis & rubrics |
| **`screenshots/`** | Visual Artifacts | High-resolution PNGs of dashboard layout, salary bar chart, hiring line trend, and scatter plot |

---

## 🚀 How to Run the Application Locally

1. Open PowerShell or Command Prompt in this folder:
   ```bash
   cd "C:\Users\Devansh\OneDrive\Desktop\Devansh\MCA\Python\Lab 6"
   ```

2. Run the application:
   ```bash
   python -m streamlit run app.py
   ```
   *(Or if streamlit is directly in your PATH:)*
   ```bash
   streamlit run app.py
   ```

3. Your browser will automatically open:
   👉 **`http://localhost:8501`**

---

## 📊 Application Layout & Features

### 1. Interactive Filters (Sidebar)
- **Joining Date Range Picker (`st.date_input`)**: Filter employee tenure and cohort cohorts.
- **Department Multiselect (`st.multiselect`)**: Engineering, Data Science, HR, Sales, Marketing, Finance, Operations.
- **Attrition Status (`st.selectbox`)**: Filter by All, Active employees, or Resigned/Attrition cases.
- **Overtime Status (`st.selectbox`)**: Filter by Yes / No overtime engagement.
- **Salary Range Slider (`st.slider`)**: Custom minimum and maximum monthly compensation filters.
- **Performance Rating Range Slider (`st.slider`)**: Filter appraisal scores between 1.0 and 5.0 ⭐.
- **Reset Filters (`st.button`)**: Clear all active filters with one click.

### 2. Executive KPI Metric Cards (`st.columns`)
- **Total Headcount**: Count of employee records matching active filters.
- **Active Staff**: Count of currently employed staff.
- **Attrition Rate**: Percentage of workforce that left (`(Attrition / Total) * 100`).
- **Average Monthly Salary**: Mean compensation in INR (₹).
- **Average Performance Score**: Mean composite score (`Rating * 12 + Attendance * 0.40`).

### 3. Visualizations (`st.tabs` & Plotly)
- **Bar Chart**: Average Monthly Salary and Total Payroll expenditure across Departments.
- **Line Chart**: Cumulative Headcount Growth & Hiring Trajectory over time.
- **Scatter Plot**: Monthly Salary vs. Composite Performance Score (bubble size = Experience, color = Attrition).
- **Donut Chart**: Departmental Headcount Proportion & Distribution.

### 4. Layout Organization
- `st.sidebar`: Collapsible filter controls.
- `st.columns`: Side-by-side metric scorecards and comparative charts.
- `st.container` & `st.expander`: Collapsible dataset inspection, summary statistics (`describe()`), and column dictionary.
- `st.tabs`: 4 clean horizontal views:
  1. 📋 Dataset Overview
  2. 📊 Visualizations
  3. 📑 Departmental Summary
  4. 💡 Strategic HR Insights

---

## 🌐 Public Cloud Deployment Guide (Streamlit Community Cloud)

1. **Push to GitHub**:
   - Create a GitHub repository (e.g., `streamlit-hr-analytics`).
   - Push `app.py`, `hr_workforce_data.csv`, and `requirements.txt`.
   - Push to the `main` branch.

2. **Deploy on Streamlit Community Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io/) and log in with GitHub.
   - Click **"New app"**.
   - Select your repository, branch (`main`), and set Main file path to `app.py`.
   - Click **"Deploy!"**.
   - Streamlit provides your public HTTPS link (e.g., `https://<your-username>-hr-analytics.streamlit.app`).

---

## 🎓 Viva Voce Quick Cheat Sheet (Rubric R4 Defense)

1. **Why does Streamlit rerun the whole script?**
   - Streamlit follows a reactive script-as-app paradigm. When a user interacts with a widget (slider, dropdown), Streamlit re-executes top-to-bottom with updated values, recomputing KPIs and graphs instantly.
2. **What does `@st.cache_data` do in our app?**
   - It caches the `load_data()` function. `hr_workforce_data.csv` is read once and stored in memory. Subsequent reruns read from RAM in <1ms without disk I/O.
3. **How is the composite Performance Score computed?**
   - Matching Lab 2: `Performance_Score = (Appraisal_Rating / 5.0) * 60 + Attendance_Pct * 0.40`, creating a balanced 0–100 index weighted 60% on supervisor rating and 40% on punctuality/attendance.
4. **What business insight does the scatter plot reveal?**
   - Top-tier performers (score > 85) with lower compensation bands (< ₹65,000) show higher flight/attrition risk, indicating that compensation misalignment drives talent churn.
