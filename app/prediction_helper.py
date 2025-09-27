import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import  MinMaxScaler


MODEL_PATH = 'app/artifacts/model_data.joblib'
model_data = joblib.load(MODEL_PATH)
model = model_data['model']
scaler = model_data['scaler']
features = model_data['features']
cols_to_scale = model_data['cols_to_scale']

print(features)

def prepare_df(age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
            delinquency_ratio, credit_utilization_ratio, num_open_accounts,
            residence_type, loan_purpose, loan_type):

    input_data = {
        'age': age,
        'loan_tenure_months': loan_tenure_months,
        'number_of_open_accounts': num_open_accounts,
        'credit_utilization_ratio': credit_utilization_ratio,
        'loan_to_income': loan_amount / income if income > 0 else 0,
        'delinquency_ratio': delinquency_ratio,
        'avg_dpd_per_delinquency': avg_dpd_per_delinquency,
        'residence_type_Owned': 1 if residence_type == 'Owned' else 0,
        'residence_type_Rented': 1 if residence_type == 'Rented' else 0,
        'loan_purpose_Education': 1 if loan_purpose == 'Education' else 0,
        'loan_purpose_Home': 1 if loan_purpose == 'Home' else 0,
        'loan_purpose_Personal': 1 if loan_purpose == 'Personal' else 0,
        'loan_type_Unsecured': 1 if loan_type == 'Unsecured' else 0,
        # additional dummy fields just for scaling purpose
        'number_of_dependants': 1,  # Dummy value
        'years_at_current_address': 1,  # Dummy value
        'zipcode': 1,  # Dummy value
        'sanction_amount': 1,  # Dummy value
        'processing_fee': 1,  # Dummy value
        'gst': 1,  # Dummy value
        'net_disbursement': 1,  # Computed dummy value
        'principal_outstanding': 1,  # Dummy value
        'bank_balance_at_application': 1,  # Dummy value
        'number_of_closed_accounts': 1,  # Dummy value
        'enquiry_count': 1  # Dummy value
    }

    df = pd.DataFrame([input_data])
    df[cols_to_scale] = scaler.transform(df[cols_to_scale])
    df = df[features]
    return df

def predict(age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
            delinquency_ratio, credit_utilization_ratio, num_open_accounts,
            residence_type, loan_purpose, loan_type):


    df_input = prepare_df(age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
            delinquency_ratio, credit_utilization_ratio, num_open_accounts,
            residence_type, loan_purpose, loan_type)

    probability,credit_score,rating =  calculate_credit_score(df_input)

    return probability,credit_score,rating

def calculate_credit_score(df_input,base_score=300,scale_length=600):
    #Logistic function to calculate probability
    y = np.dot(df_input.values,model.coef_.T)+model.intercept_
    default_probability = 1/(1+np.exp(-y))
    non_default_probability = 1-default_probability

    credit_score = base_score+non_default_probability.flatten()*scale_length

    def get_rating(score):
        if 300<=score<500:
            return 'Poor'
        elif 500<=score<650:
            return 'Average'
        elif 650<=score<700:
            return 'Good'
        elif 700<=score<=900:
            return 'Excellent'
        else:
            return 'Undefined'


    rating = get_rating(credit_score[0])

    return default_probability.flatten()[0],int(credit_score),rating


