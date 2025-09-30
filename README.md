# 🏦 Sam Finance - Credit Risk Modelling Platform

An advanced credit risk assessment application built with Streamlit that uses machine learning to predict loan default probability and calculate credit scores.

## 📋 Overview

Sam Finance is a comprehensive credit risk assessment platform that analyzes various financial and personal parameters to provide:
- **Default Probability**: Likelihood of loan default
- **Credit Score**: Numerical score ranging from 300-900
- **Credit Rating**: Qualitative rating (Poor, Average, Good, Excellent)

## ✨ Features

- **Interactive UI**: Modern, gradient-styled interface with real-time calculations
- **Comprehensive Analysis**: Evaluates multiple risk factors including:
  - Personal information (age, income)
  - Loan details (amount, tenure, purpose)
  - Credit history (delinquency ratio, credit utilization)
  - Financial metrics (loan-to-income ratio, DPD)
- **Machine Learning Powered**: Uses trained logistic regression model for predictions
- **Real-time Metrics**: Automatically calculates loan-to-income ratio
- **Color-coded Results**: Visual indicators for risk levels

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/sam20799/ml_credit_risk_model.git
cd sam-finance-credit-risk
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Ensure the model artifacts are in place:
```
app/artifacts/model_data.joblib
```

### Running the Application

Launch the Streamlit app:
```bash
streamlit run app/main.py
```

The application will open in your default web browser at `http://localhost:8501`

## 📁 Project Structure

```
.
├── main.py                      # Main Streamlit application
├── prediction_helper.py         # Prediction logic and model interface
├── requirements.txt             # Python dependencies
├── datasets/
└── app/
    ├── main.py                      # Main Streamlit application
    └── artifacts/
         └── model_data.joblib    # Trained model and preprocessing artifacts
```

## 🔧 Usage

1. **Enter Personal Information**:
   - Age (18-100 years)
   - Annual Income
   - Loan Amount

2. **Provide Loan Details**:
   - Loan Tenure in months
   - Average Days Past Due (DPD)

3. **Input Credit Profile**:
   - Delinquency Ratio (%)
   - Credit Utilization Ratio (%)
   - Number of Open Loan Accounts (1-4)

4. **Additional Information**:
   - Residence Type (Owned/Rented/Mortgage)
   - Loan Purpose (Education/Home/Auto/Personal)
   - Loan Type (Secured/Unsecured)

5. Click **"Calculate Credit Risk"** to get results

## 📊 Model Information

The application uses a logistic regression model that:
- Processes 24 features including categorical variables
- Uses MinMaxScaler for feature normalization
- Calculates credit scores on a 300-900 scale
- Provides probability-based risk assessment

### Credit Score Ranges

| Score Range | Rating |
|-------------|--------|
| 300-499 | Poor |
| 500-649 | Average |
| 650-699 | Good |
| 700-900 | Excellent |

## 🛠️ Technical Stack

- **Frontend**: Streamlit with custom CSS styling
- **ML Framework**: scikit-learn
- **Data Processing**: pandas, numpy
- **Model Persistence**: joblib
- **Additional**: XGBoost (dependency)

## 📦 Dependencies

```
pandas==2.3.1
joblib==1.5.2
streamlit==1.48.1
numpy==2.3.1
scikit-learn==1.7.1
xgboost==3.0.5
```

## 🎨 UI Features

- Gradient-styled headers and sections
- Interactive number inputs with validation
- Real-time loan-to-income ratio calculation
- Color-coded results based on risk levels
- Responsive design with three-column layout
- Custom-styled buttons and dropdowns

## 🔒 Model Artifacts

The `model_data.joblib` file contains:
- Trained logistic regression model
- MinMaxScaler for feature normalization
- Feature list for correct input ordering
- Columns to scale configuration

## 👨‍💻 Author

**SHUBHAM KR**

## 📄 License

© 2025 SHUBHAM KR. All rights reserved.

## 🤝 Contributing

This is a proprietary project. For collaboration opportunities, please contact the author.

## ⚠️ Disclaimer

This application is for educational and demonstration purposes. Credit decisions should not be made solely based on this tool's output. Always consult with financial professionals for actual lending decisions.

## 📞 Support

For issues, questions, or feedback, please open an issue in the repository or contact the development team.

---

**Note**: Ensure you have the trained model file (`model_data.joblib`) in the correct directory before running the application.