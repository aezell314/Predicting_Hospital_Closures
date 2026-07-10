import streamlit as st
import joblib
import pandas as pd
import utils
import numpy as np
import shap
import matplotlib.pyplot as plt
 
st.set_page_config(
    page_title="Rural Hospital Risk Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
)
 
# -----------------------------
# Helpers
# -----------------------------
@st.cache_resource
def load_artifacts():
    model = joblib.load("./data/hospital_closure_model.pkl")
    preprocessor = joblib.load("./data/preprocessor.pkl")
    train_unscaled = utils.train_unscaled  # raw, unprocessed training data
    train_scaled = utils.train_scaled  # preprocessed training data
    test_data = utils.test  # preprocessed test data with predicted risk scores appended
    return model, preprocessor, train_unscaled, train_scaled, test_data
 
 
@st.cache_data
def build_baseline_features(train_unscaled: pd.DataFrame) -> dict:
    med = lambda col: train_unscaled[col].median()
    mode = lambda col: train_unscaled[col].mode()[0]
 
    return {
        "Medicaid charges": med("Medicaid charges"),
        "STATEMENT OF REVENUES AND EXPENSES: Net Income (G3_C1_29)": med(
            "STATEMENT OF REVENUES AND EXPENSES: Net Income (G3_C1_29)"
        ),
        "ADJUSTED SALARIES, Subtotal Salaries": med(
            "ADJUSTED SALARIES, Subtotal Salaries"
        ),
        "BALANCE SHEET: Prepaid expenses (G_C1THRU4_8)": med(
            "BALANCE SHEET: Prepaid expenses (G_C1THRU4_8)"
        ),
        "BED DAYS: Total Hospital": med("BED DAYS: Total Hospital"),
        "Number of Interns & Residents": med("Number of Interns & Residents"),
        "BALANCE SHEET: Cash on Hand and in Banks (G_C1THRU4_1)": med(
            "BALANCE SHEET: Cash on Hand and in Banks (G_C1THRU4_1)"
        ),
        "Cost To Charge Ratio": med("Cost To Charge Ratio"),
        "Total discharges": med("Total discharges"),
        "Cost of Uncompensated Care": med("Cost of Uncompensated Care"),
        "BALANCE SHEET: Accounts Receivable (G_C1THRU4_4)": med(
            "BALANCE SHEET: Accounts Receivable (G_C1THRU4_4)"
        ),
        "Total Salaries": med("Total Salaries"),
        "BALANCE SHEET: Total Assets (G_C1THRU4_36)": med(
            "BALANCE SHEET: Total Assets (G_C1THRU4_36)"
        ),
        "BALANCE SHEET: Total Current Assets (G_C1THRU4_11)": med(
            "BALANCE SHEET: Total Current Assets (G_C1THRU4_11)"
        ),
        "REIMBURSEMENT SETTLEMENT: Interim payments": med(
            "REIMBURSEMENT SETTLEMENT: Interim payments"
        ),
        "Total Bad Debt expense": med("Total Bad Debt expense"),
        "NUMBER OF BEDS: Adults & Pediatrics": med(
            "NUMBER OF BEDS: Adults & Pediatrics"
        ),
        "NUMBER OF BEDS: Total Hospital": med("NUMBER OF BEDS: Total Hospital"),
        "Total Inpatient Days": med("Total Inpatient Days"),
        "Total Days Title XVIII": med("Total Days Title XVIII"),
        "Total cost of charity care": med("Total cost of charity care"),
        "Total Costs": med("Total Costs"),
        "NUMBER OF BEDS: ICU": med("NUMBER OF BEDS: ICU"),
        "Total Charges": med("Total Charges"),
        "Net Revenue from Medicaid": med("Net Revenue from Medicaid"),
        "Total Liabilities": med("Total Liabilities"),
        "HVBP payment adjustment amount": med("HVBP payment adjustment amount"),
        "REIMBURSEMENT SETTLEMENT: Subtotal": med(
            "REIMBURSEMENT SETTLEMENT: Subtotal"
        ),
        "IPPS Interim payment": med("IPPS Interim payment"),
        "IPPS Payment amount (unadjusted)": med(
            "IPPS Payment amount (unadjusted)"
        ),
        "RECONCILIATION OF CAPITAL COST CENTERS: Depreciation, Total (A7_3_C9_3)": med(
            "RECONCILIATION OF CAPITAL COST CENTERS: Depreciation, Total (A7_3_C9_3)"
        ),
        "BALANCE SHEET: Total Current Liabilities (G_C1THRU4_45)": med(
            "BALANCE SHEET: Total Current Liabilities (G_C1THRU4_45)"
        ),
        "BALANCE SHEET: Inventory (G_C1THRU4_7)": med(
            "BALANCE SHEET: Inventory (G_C1THRU4_7)"
        ),
        "STATEMENT OF REVENUES AND EXPENSES: Net Patient Revenue (G3_C1_3)": med(
            "STATEMENT OF REVENUES AND EXPENSES: Net Patient Revenue (G3_C1_3)"
        ),
        "Financial Indicators: Total Net Assets": med(
            "Financial Indicators: Total Net Assets"
        ),
        "S-10 DATA: Medicaid Costs": med("S-10 DATA: Medicaid Costs"),
        "Financial Indicators: Cash Reserves": med(
            "Financial Indicators: Cash Reserves"
        ),
        "Financial Indicators: Net Profit Margin": med(
            "Financial Indicators: Net Profit Margin"
        ),
        "Financial Indicators: Operating Profit": med(
            "Financial Indicators: Operating Profit"
        ),
        "Financial Indicators: Operating Profit Margin": med(
            "Financial Indicators: Operating Profit Margin"
        ),
        "Financial Indicators: LIQUIDITY current ratio": med(
            "Financial Indicators: LIQUIDITY current ratio"
        ),
        "Financial Indicators: LIQUIDITY acid-test ratio": med(
            "Financial Indicators: LIQUIDITY acid-test ratio"
        ),
        "Financial Indicators: LIQUIDITY acid-test ratio (variation)": med(
            "Financial Indicators: LIQUIDITY acid-test ratio (variation)"
        ),
        "Financial Indicators: LIQUIDITY cash ratio": med(
            "Financial Indicators: LIQUIDITY cash ratio"
        ),
        "Financial Indicators: SOLVENCY Debt-to-Equity Ratio": med(
            "Financial Indicators: SOLVENCY Debt-to-Equity Ratio"
        ),
        "Financial Indicators: SOLVENCY Debt Ratio": med(
            "Financial Indicators: SOLVENCY Debt Ratio"
        ),
        "Financial Indicators: SOLVENCY Equity Ratio": med(
            "Financial Indicators: SOLVENCY Equity Ratio"
        ),
        "Financial Indicators: SOLVENCY total assets less total liabilities": med(
            "Financial Indicators: SOLVENCY total assets less total liabilities"
        ),
        "Financial Indicators: EFFICIENCY asset turnover ratio": med(
            "Financial Indicators: EFFICIENCY asset turnover ratio"
        ),
        "Financial Indicators: EFFICIENCY Accounts Receivable Turnover Ratio": med(
            "Financial Indicators: EFFICIENCY Accounts Receivable Turnover Ratio"
        ),
        "Emergency Services": mode("Emergency Services"),
        "RUCA": mode("RUCA"),
        "Metro_Status": mode("Metro_Status"),
        "Status": mode("Status"),
        "Hospital Type": mode("Hospital Type"),
        "nsurveys": med("nsurveys"),
        "rrate": med("rrate"),
        "clean_score": med("clean_score"),
        "commdoc_score": med("commdoc_score"),
        "commnurse_score": med("commnurse_score"),
        "explain_score": med("explain_score"),
        "help_score": med("help_score"),
        "info_score": med("info_score"),
        "overall_score": med("overall_score"),
        "pain_score": med("pain_score"),
        "quiet_score": med("quiet_score"),
        "recommend_score": med("recommend_score"),
        "understood_score": med("understood_score"),
        "% <65 without Health Insurance": med("% <65 without Health Insurance"),
        "Dist Hosp By 00 - 39% Util Rate Short Term General Hospitals": med(
            "Dist Hosp By 00 - 39% Util Rate Short Term General Hospitals"
        ),
        "Dist Hosp By 40 - 59% Util Rate Short Term General Hospitals": med(
            "Dist Hosp By 40 - 59% Util Rate Short Term General Hospitals"
        ),
        "Dist Hosp By 60 - 79% Util Rate Short Term General Hospitals": med(
            "Dist Hosp By 60 - 79% Util Rate Short Term General Hospitals"
        ),
        "Dist Hosp By 80+% Util Rate Short Term General Hospitals": med(
            "Dist Hosp By 80+% Util Rate Short Term General Hospitals"
        ),
        "Median Household Income": med("Median Household Income"),
        "Per Capita # Short Term General Hosps": med(
            "Per Capita # Short Term General Hosps"
        ),
        "Per Capita Hospital Admissions": med(
            "Per Capita Hospital Admissions"
        ),
        "Per Capita Hospital Beds": med("Per Capita Hospital Beds"),
        "Per Capita Inpatient Days in ST Gen Hosp": med(
            "Per Capita Inpatient Days in ST Gen Hosp"
        ),
        "Per Capita Personal Income": med("Per Capita Personal Income"),
        "Per Capita Phys,Primary Care, Patient Care Non-Fed": med(
            "Per Capita Phys,Primary Care, Patient Care Non-Fed"
        ),
        "Per Capita Short Term Gen Hosp Admissions": med(
            "Per Capita Short Term Gen Hosp Admissions"
        ),
        "Per Capita Short Term General Hosp Beds": med(
            "Per Capita Short Term General Hosp Beds"
        ),
        "Per Capita Total Active D.O.s Non-Federal": med(
            "Per Capita Total Active D.O.s Non-Federal"
        ),
        "Per Capita Total Active M.D.s Non-Federal": med(
            "Per Capita Total Active M.D.s Non-Federal"
        ),
        "Per Capita Total Medicare Inpatient Days Short Term General Hospitals": med(
            "Per Capita Total Medicare Inpatient Days Short Term General Hospitals"
        ),
        "Per Capita Total Number Hospitals": med(
            "Per Capita Total Number Hospitals"
        ),
        "Percent Persons in Poverty": med("Percent Persons in Poverty"),
        "Population Estimate": med("Population Estimate"),
        "Unemployment Rate, 16+": med("Unemployment Rate, 16+"),
    }
 
 
def build_features(baseline_features: dict, inputs: dict) -> dict:
    features = dict(baseline_features)
    features["Financial Indicators: SOLVENCY Debt Ratio"] = inputs["debt_ratio"]
    features["Financial Indicators: SOLVENCY Equity Ratio"] = inputs["equity_ratio"]
    features["Per Capita Total Medicare Inpatient Days Short Term General Hospitals"] = inputs[
        "medicare_inpatient_days"
    ]
    features["Per Capita Short Term Gen Hosp Admissions"] = inputs[
        "gen_hosp_admissions"
    ]
    features["Hospital Type"] = inputs["hospital_type"]
    return features
 
 
# -----------------------------
# Load data and artifacts
# -----------------------------
model, preprocessor, train_unscaled, train_scaled, test_data = load_artifacts()
baseline_features = build_baseline_features(train_unscaled)
 
 
# -----------------------------
# Defaults / reset support
# -----------------------------
defaults = {
    "debt_ratio": float(baseline_features["Financial Indicators: SOLVENCY Debt Ratio"]),
    "equity_ratio": float(baseline_features["Financial Indicators: SOLVENCY Equity Ratio"]),
    "medicare_inpatient_days": float(
        baseline_features[
            "Per Capita Total Medicare Inpatient Days Short Term General Hospitals"
        ]
    ),
    "gen_hosp_admissions": float(
        baseline_features["Per Capita Short Term Gen Hosp Admissions"]
    ),
    "hospital_type": "Non-Profit",
}
 
for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value
 
 
def reset_inputs():
    for key, value in defaults.items():
        if key in st.session_state:
            del st.session_state[key]  # Clear existing widget state
        st.session_state[key] = value

 
 
# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.markdown("## About")
    st.write(
        "This dashboard estimates rural hospital closure risk using financial, operational, and county-level indicators."
    )
 
    st.markdown("## How to use")
    st.write(
        """
        1. Adjust the highlighted inputs.
        2. Review the hospital type and ownership.
        3. Click **Evaluate Hospital**.
        """
    )
 
    st.markdown("## Model note")
    st.caption("Meant for decision support, not a diagnosis or final forecast.")
 
st.header("Rural Hospital Risk Dashboard")
st.caption(
    "Decision-support interface to help assess closure risk using features most important to the Cox model."
)
 
# -----------------------------
# Input area
# -----------------------------
left, right = st.columns([1.1, 1])
 
with left:
    with st.container(border=True):
        st.subheader("Financial Indicators")
        debt_ratio = st.slider(
            "Debt Ratio",
            float(train_unscaled["Financial Indicators: SOLVENCY Debt Ratio"].min()),
            float(train_unscaled["Financial Indicators: SOLVENCY Debt Ratio"].max()),
            key="debt_ratio",
            help="Total Liabilities / Total Assets",
       )
        equity_ratio = st.slider(
            "Equity Ratio",
            float(train_unscaled["Financial Indicators: SOLVENCY Equity Ratio"].min()),
            float(train_unscaled["Financial Indicators: SOLVENCY Equity Ratio"].max()),
            key="equity_ratio",
            help="Total Net Assets or Equity / Total Assets",
        )
 
    with st.container(border=True):
        st.subheader("Area Health Resource Indicators")
        medicare_inpatient_days = st.slider(
            "Per Capita Medicare Inpatient Days",
            float(
                train_unscaled[
                    "Per Capita Total Medicare Inpatient Days Short Term General Hospitals"
                ].min()
            ),
            float(
                train_unscaled[
                    "Per Capita Total Medicare Inpatient Days Short Term General Hospitals"
                ].max()
            ),
            key="medicare_inpatient_days",
            help="County-level utilization for Medicare inpatient days at Short Term General Hospitals (a facility that provides localized public medical, surgical, and emergency care where the average patient stay is less than 30 days)",
        )
        gen_hosp_admissions = st.slider(
            "Per Capita Short Term General Hospital Admissions",
            float(train_unscaled["Per Capita Short Term Gen Hosp Admissions"].min()),
            float(train_unscaled["Per Capita Short Term Gen Hosp Admissions"].max()),
            key="gen_hosp_admissions",
            help="County-level utilization for total hospital admissions at short term general hospitals (a facility that provides localized public medical, surgical, and emergency care where the average patient stay is less than 30 days)",
        )
 
    with st.container(border=True):
        st.subheader("Hospital Information")
        hospital_type = st.radio(
            "Hospital Type",
            options=["Non-Profit", "For-Profit", "Government"],
            horizontal=True,
            key="hospital_type",
        )
 
with right:
    with st.container(border=True):
        st.subheader("What changed from baseline?")
        st.write(
            "These inputs are compared against the training-set median to help explain the result."
        )
 
        changed_inputs = {
            "Debt Ratio": (debt_ratio, baseline_features["Financial Indicators: SOLVENCY Debt Ratio"]),
            "Equity Ratio": (equity_ratio, baseline_features["Financial Indicators: SOLVENCY Equity Ratio"]),
            "Per Capita Medicare Inpatient Days": (
                medicare_inpatient_days,
                baseline_features[
                    "Per Capita Total Medicare Inpatient Days Short Term General Hospitals"
                ],
            ),
            "Per Capita Hospital Admissions": (
                gen_hosp_admissions,
                baseline_features["Per Capita Short Term Gen Hosp Admissions"],
            ),
        }
 
        for label, (current, baseline) in changed_inputs.items():
            delta = current - baseline
            st.metric(label, f"{current:.3f}", delta=f"{delta:+.3f}")
 
    with st.container(border=True):
        st.subheader("Make Prediction")
        st.write("Click the button to evaluate the current configuration.")
        btn_left, btn_right = st.columns(2)
        with btn_left:
            evaluate = st.button("Evaluate Hospital", use_container_width=True, type="primary")
        with btn_right:
            reset = st.button("Reset to Defaults", use_container_width=True)
            if reset:
                reset_inputs()
                st.rerun()
 
# -----------------------------
# Prediction
# -----------------------------
if evaluate:
    inputs = {
        "debt_ratio": debt_ratio,
        "equity_ratio": equity_ratio,
        "medicare_inpatient_days": medicare_inpatient_days,
        "gen_hosp_admissions": gen_hosp_admissions,
        "hospital_type": hospital_type,
    }
 
    features = build_features(baseline_features, inputs)
    features_df = pd.DataFrame([features])
    features_df = preprocessor.transform(features_df)
 
    prediction = model.predict(features_df)
    risk_score = float(prediction[0])
 
    low_cutoff = round(test_data['Pred_Closure'].quantile(0.5), 2)
    high_cutoff = round(test_data['Pred_Closure'].quantile(0.9), 2)
    if risk_score >= high_cutoff:
        score_class = "HIGH"
        risk_class = "risk-high"
        status_text = "High Risk"
        status_color = "red"
    elif risk_score <= low_cutoff:
        score_class = "LOW"
        risk_class = "risk-low"
        status_text = "Low Risk"
        status_color = "yellow"
    else:
        score_class = "MODERATE"
        risk_class = "risk-moderate"
        status_text = "Moderate Risk"
        status_color = "green"
 
    st.markdown("---")
    score_left, score_right = st.columns([1.15, 1])
 
    with score_left:
        st.subheader(f":{status_color}-background[{status_text}]")
        st.caption("Estimated closure risk score:")
        st.metric(label="Risk Score", value=f"{risk_score:.2f}")
        st.caption(
            f"Threshold bands: Low ≤ {low_cutoff}, Moderate {low_cutoff}–{high_cutoff}, High ≥ {high_cutoff}"
        )
 
    with score_right:
        with st.container(border=True):
            st.subheader("Summary")
            st.write(f"This hospital has a **{score_class}** chance of closing.")
 
            max_score = round(test_data['Pred_Closure'].max(), 2)
            min_score = round(test_data['Pred_Closure'].min(), 2)
 
            if risk_score <= min_score:
                st.progress(0)
            elif risk_score >= max_score:
                st.progress(1)
            else:
                st.progress((risk_score - min_score) / (max_score - min_score))
            st.caption("Progress bar is a visual aid, not a probability.")
 
    st.subheader("SHAP Plot")
    st.write("The prediction is driven primarily by the following features:")
 
    feature_cols = [col for col in train_scaled.columns if col not in ['CCN', 'Status', 'Time', 'Year']]
    X_train = train_scaled[feature_cols]
    X_train_summary = shap.sample(X_train.to_numpy(), nsamples=100)
 
    explainer = shap.KernelExplainer(model.predict, X_train_summary)
    shap_values = explainer.shap_values(features_df)
    exp = shap.Explanation(
        values=shap_values,
        base_values=explainer.expected_value,
        data=features_df,
        feature_names=feature_cols,
    )
 
    fig, ax = plt.subplots(figsize=(10, 6))
    shap.plots.waterfall(exp[0])
    plt.tight_layout()
    st.pyplot(fig)