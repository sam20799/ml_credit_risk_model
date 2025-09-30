import streamlit as st
from prediction_helper import predict  # Ensure this is correctly linked to your prediction_helper.py
from datetime import datetime

# Set the page configuration and title
st.set_page_config(
    page_title="Sam Finance: Credit Risk Modelling",
    page_icon="🏦",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    /* Global Styles */
    .stApp {
        font-family: 'Inter', sans-serif;
    }

    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    .main-header h1 {
        margin: 0;
        font-size: 2.5rem;
        font-weight: 700;
    }

    .main-header p {
        margin: 0.5rem 0 0 0;
        font-size: 1.1rem;
        opacity: 0.9;
    }

    .input-section {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        margin-bottom: 0.8rem;
        border-left: 4px solid #667eea;
    }

    .section-title {
        color: #667eea;
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 0.8rem;
        display: flex;
        align-items: center;
    }

    .section-title::before {
        content: "📋";
        margin-right: 0.5rem;
    }

    .loan-ratio-display {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
        margin: 0.5rem 0;
    }

    .loan-ratio-display .ratio-label {
        font-size: 0.9rem;
        opacity: 0.9;
        margin-bottom: 0.3rem;
    }

    .loan-ratio-display .ratio-value {
        font-size: 1.8rem;
        font-weight: bold;
    }

    .results-section {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-top: 2rem;
        text-align: center;
    }

    .result-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 0.5rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        flex: 1;
    }

    .result-value {
        font-size: 2rem;
        font-weight: bold;
        color: #667eea;
    }

    .result-label {
        font-size: 1rem;
        color: #666;
        margin-top: 0.5rem;
    }

    .insights-section {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-top: 2rem;
    }

    .insight-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }

    .insight-title {
        color: #667eea;
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }

    .insight-text {
        color: #333;
        font-size: 1rem;
        line-height: 1.6;
        margin: 0.5rem 0;
    }

    .insight-highlight {
        color: #f5576c;
        font-weight: 600;
    }

    /* Fix for Number Input Styling */
    .stNumberInput > div > div > input {
        background-color: #f8f9fa !important;
        border: 1px solid #ddd !important;
        border-radius: 8px !important;
        color: #333 !important;
        padding: 0.5rem !important;
    }

    .stNumberInput label {
        color: #e2e8f0 !important;
        font-weight: 600 !important;
        font-size: 15px !important;
        margin-bottom: 8px !important;
        text-shadow: 0 1px 2px rgba(0,0,0,0.1) !important;
    }

    /* Complete Fix for Selectbox Styling */
    .stSelectbox label {
        color: #e2e8f0 !important;
        font-weight: 600 !important;
        font-size: 15px !important;
        margin-bottom: 8px !important;
        text-shadow: 0 1px 2px rgba(0,0,0,0.1) !important;
    }

    /* Selectbox container */
    .stSelectbox > div > div {
        background-color: #f8f9fa !important;
        border: 1px solid #ddd !important;
        border-radius: 8px !important;
    }

    /* Selected value display */
    .stSelectbox div[data-baseweb="select"] {
        background-color: #f8f9fa !important;
        border: 1px solid #ddd !important;
        border-radius: 8px !important;
    }

    .stSelectbox div[data-baseweb="select"] > div {
        color: #333 !important;
        background-color: transparent !important;
        font-weight: 500 !important;
    }

    /* Dropdown arrow */
    .stSelectbox div[data-baseweb="select"] svg {
        color: #333 !important;
    }

    /* Dropdown menu */
    .stSelectbox div[role="listbox"] {
        background-color: white !important;
        border: 1px solid #ddd !important;
        border-radius: 8px !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15) !important;
    }

    /* Dropdown options */
    .stSelectbox div[role="option"] {
        color: #333 !important;
        background-color: white !important;
        padding: 8px 12px !important;
        font-weight: 500 !important;
    }

    .stSelectbox div[role="option"]:hover {
        background-color: #f0f2f6 !important;
        color: #333 !important;
    }

    .stSelectbox div[role="option"][aria-selected="true"] {
        background-color: #667eea !important;
        color: white !important;
    }

    /* Button Styling */
    .stButton button {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%) !important;
        color: white !important;
        border: none !important;
        padding: 1rem 2rem !important;
        border-radius: 25px !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        transition: transform 0.2s !important;
        width: 100% !important;
    }

    .stButton button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 12px rgba(79, 172, 254, 0.4) !important;
    }

    /* Help text styling */
    .stTooltipIcon {
        color: #667eea !important;
    }
</style>
""", unsafe_allow_html=True)

# Main header
st.markdown("""
<div class="main-header">
    <h1>🏦 Sam Finance</h1>
    <p>Advanced Credit Risk Assessment & Modelling Platform</p>
</div>
""", unsafe_allow_html=True)

# Add Model Insights Section at the top
with st.expander("📊 View Model Insights & Feature Importance", expanded=False):
    st.markdown("""
    <div class="insight-card">
        <div class="insight-title">🎯 Understanding Our Credit Risk Model</div>
        <div class="insight-text">
            Our machine learning model analyzes <span class="insight-highlight">13 key features</span> to predict loan default probability. 
            Below is the feature importance chart showing how each factor influences credit risk assessment.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Display the feature importance image
    try:
        st.image("feature_importance.png", caption="Feature Importance in Logistic Regression Model",
                 use_container_width=True)
    except:
        st.warning("⚠️ Feature importance chart not found. Please ensure 'assets/feature_importance.png' exists.")

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("### 🔴 Top Risk Factors (Highest Impact)")
        st.markdown("""
        1. **Loan-to-Income Ratio (~17.5)** - The strongest predictor of default risk
        2. **Credit Utilization Ratio (~16.0)** - High credit usage signals financial stress
        3. **Delinquency Ratio (~13.5)** - Past payment behavior predicts future defaults
        """)

        st.markdown("### 🟡 Moderate Risk Factors")
        st.markdown("""
        - Average DPD per Delinquency (~2.0) - Severity of payment delays
        - Rented Residence (~1.8) - Less stability than homeowners
        - Number of Open Accounts (~1.0) - More accounts = higher risk
        - Unsecured Loans (~0.8) - No collateral increases risk
        """)

    with col2:
        st.markdown("### 🟢 Protective Factors (Lower Risk)")
        st.markdown("""
        - **Home Loans (-2.5)** - Lowest default rates
        - **Owned Residence (-0.2)** - More financial stability
        """)

        st.markdown("### 💡 What This Means")
        st.markdown("""
        - Keep Loan-to-Income ratio **below 2.0**
        - Maintain Credit Utilization **under 30%**
        - Avoid payment delays
        - Home loans significantly improve creditworthiness
        """)

    st.markdown("""
    <div class="insight-card">
        <div class="insight-title">💡 What This Means for You</div>
        <div class="insight-text">
            • Keep your <span class="insight-highlight">Loan-to-Income ratio below 2.0</span> for better approval chances<br>
            • Maintain <span class="insight-highlight">Credit Utilization under 30%</span> of your total limit<br>
            • Avoid payment delays - <span class="insight-highlight">delinquency history heavily impacts your score</span><br>
            • Home loans and owned residences significantly improve creditworthiness<br>
            • The model weighs recent payment behavior more than demographic factors
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Personal Information Section
st.markdown("""
<div class="input-section">
    <div class="section-title">Personal & Financial Information</div>
</div>
""", unsafe_allow_html=True)

row1 = st.columns(3)
with row1[0]:
    age = st.number_input('🧑 Age', min_value=18, step=1, max_value=100, value=28, help="Applicant's age in years")
with row1[1]:
    income = st.number_input('💰 Annual Income', min_value=0, value=1200000, help="Annual income in your local currency")
with row1[2]:
    loan_amount = st.number_input('🏠 Loan Amount', min_value=0, value=2560000, help="Requested loan amount")

# Calculate Loan to Income Ratio and display it beautifully
loan_to_income_ratio = loan_amount / income if income > 0 else 0

# Loan Details Section
st.markdown("""
<div class="input-section">
    <div class="section-title">Loan Details & History</div>
</div>
""", unsafe_allow_html=True)

row2 = st.columns(3)
with row2[0]:
    st.markdown(f"""
    <div class="loan-ratio-display">
        <div class="ratio-label">📊 Loan to Income Ratio</div>
        <div class="ratio-value">{loan_to_income_ratio:.2f}</div>
    </div>
    """, unsafe_allow_html=True)

with row2[1]:
    loan_tenure_months = st.number_input('📅 Loan Tenure (months)', min_value=0, step=1, value=36,
                                         help="Loan duration in months")
with row2[2]:
    avg_dpd_per_delinquency = st.number_input('⏰ Avg DPD', min_value=0, value=20,
                                              help="Average Days Past Due per delinquency")

# Credit Profile Section
st.markdown("""
<div class="input-section">
    <div class="section-title">Credit Profile & Risk Factors</div>
</div>
""", unsafe_allow_html=True)

row3 = st.columns(3)
with row3[0]:
    delinquency_ratio = st.number_input('⚠️ Delinquency Ratio (%)', min_value=0, max_value=100, step=1, value=30,
                                        help="Percentage of delinquent months")
with row3[1]:
    credit_utilization_ratio = st.number_input('💳 Credit Utilization Ratio (%)', min_value=0, max_value=100, step=1,
                                               value=30, help="Percentage of credit limit used")
with row3[2]:
    num_open_accounts = st.number_input('📋 Open Loan Accounts', min_value=1, max_value=4, step=1, value=2,
                                        help="Number of currently open loan accounts")

# Additional Information Section
st.markdown("""
<div class="input-section">
    <div class="section-title">Additional Information</div>
</div>
""", unsafe_allow_html=True)

row4 = st.columns(3)
with row4[0]:
    residence_type = st.selectbox('🏠 Residence Type', ['Owned', 'Rented', 'Mortgage'],
                                  help="Current residence ownership status")
with row4[1]:
    loan_purpose = st.selectbox('🎯 Loan Purpose', ['Education', 'Home', 'Auto', 'Personal'],
                                help="Primary purpose of the loan")
with row4[2]:
    loan_type = st.selectbox('🔐 Loan Type', ['Unsecured', 'Secured'], help="Type of loan security")

# Center the button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    calculate_risk = st.button('🚀 Calculate Credit Risk', use_container_width=True, type="primary")

# Button to calculate risk
if calculate_risk:
    with st.spinner('🔄 Analyzing credit risk... Please wait'):
        # Call the predict function from the helper module
        probability, credit_score, rating = predict(age, income, loan_amount, loan_tenure_months,
                                                    avg_dpd_per_delinquency,
                                                    delinquency_ratio, credit_utilization_ratio, num_open_accounts,
                                                    residence_type, loan_purpose, loan_type)

    # Display the results in an attractive format
    st.markdown("""
    <div class="results-section">
        <h2 style="color: #667eea; margin-bottom: 2rem;">📊 Credit Risk Assessment Results</h2>
    </div>
    """, unsafe_allow_html=True)

    result_col1, result_col2, result_col3 = st.columns(3)

    with result_col1:
        st.markdown(f"""
        <div class="result-card">
            <div class="result-value" style="color: #f5576c;">⚠️ {probability:.2%}</div>
            <div class="result-label">Default Probability</div>
        </div>
        """, unsafe_allow_html=True)

    with result_col2:
        # Color coding for credit score
        score_color = "#4facfe" if credit_score > 700 else "#f093fb" if credit_score > 600 else "#f5576c"
        st.markdown(f"""
        <div class="result-card">
            <div class="result-value" style="color: {score_color};">📈 {credit_score}</div>
            <div class="result-label">Credit Score</div>
        </div>
        """, unsafe_allow_html=True)

    with result_col3:
        # Color coding for rating
        rating_colors = {
            'Poor': '#f5576c',
            'Average': '#f093fb',
            'Good': '#667eea',
            'Excellent': '#4facfe'
        }
        rating_color = rating_colors.get(rating, '#667eea')
        st.markdown(f"""
        <div class="result-card">
            <div class="result-value" style="color: {rating_color};">⭐ {rating}</div>
            <div class="result-label">Credit Rating</div>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; padding: 1.5rem; color: #666;">
    <p>🎯 <strong>Sam Finance</strong> - Empowering Financial Decisions with AI</p>
    <p style="font-size: 0.9rem; opacity: 0.8;">Advanced Machine Learning Models for Precise Credit Risk Assessment</p>
    <p style="font-size: 0.8rem; margin-top: 1rem; opacity: 0.6;">
        © {datetime.now().year} SHUBHAM KR. All rights reserved. | Developed using Streamlit
    </p>
</div>
""", unsafe_allow_html=True)