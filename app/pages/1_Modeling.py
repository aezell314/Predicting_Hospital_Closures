import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Modeling Closure Risk",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.subheader('How was risk evaluated?')
'''
This project uses a penalized **Cox Proportional Hazards** regression model, which is a method used in survival analysis to model the time it takes for an event (in this case, hospital closure) to occur while accounting for multiple predictor variables. 

Cox Regression models can be used either to test hypotheses about the independent variables or to build a predictive model; in this case, a predictive model was fit to the data.

**Survival analysis** was an appropriate framework to use here since based on recent trends, we expect more rural hospitals to close over the coming years. 
However, these closures are not captured in the dataset, even as certain predictor values might be indicating an imminent closure. 
This is referred to in survival analysis as "right-censoring". 

The model predictions take the form of a risk score which is the exponentiated sum of the regression coefficients; the risk score indicates how much more or less likely a hospital is to close at any given time compared to the baseline chance of closing. 

The *scikit-survival* library was used to implement the model, since its penalized Cox model (*CoxnetSurvivalAnalysis*) supports Ridge and Lasso regularization. 
This coefficient penalization is helpful for the high-dimensional data in this project. 
Many of the features are related to one another (high multicollinearity), which breaks normal Cox regression models, but penalized Cox models can prune features more aggressively to deal with this issue.
'''

st.subheader('Hyperparameter Tuning')
'''
Data between 2022 and 2025 was reserved as our "real-world" test data; this resulted in a 75%/25% train/test split.

The train set was further split into 5 "folds" using scikit-learn's TimeSeriesSplit class. This type of splitting preserves the chronological ordering of the data and prevents leakage of earlier training data into later validation sets.
'''

st.space('small')
img_path = Path(__file__).parent.parent / "images" / "TimeSeriesSplit.png"

if img_path.exists():
    st.image(str(img_path), width=900)
else:
    st.error(f"File not found at: {img_path}")

st.markdown("Visualization of 5-fold cross-validation using a time series split. <a href='#cite-1'>[1]</a>. ", unsafe_allow_html=True)
st.space('small')

'''
For each iteration of the 5-fold cross-validation, data pre-processing steps are applied (scaling numeric featuers, imputing missing value, and encoding categorical features).
Then, a model is fit the training fold and is evaluated via the corresponding validation fold. 

Time series 5-fold cross-validation allowed for the tuning of the l1_ratio and alpha_min_ratio hyperparameters. These control the amount and type of regularization that is applied to the model.
'''

st.subheader('Model Evaluation')
'''
Cox Regression models are often evaluated using their **concordance index** (often called **Harrell's C-index**), which is essentially the survival analysis equivalent to the ROC-AUC metric.
The concordance index calculates every possible pairs of hospitals in the dataset and checks whether the predicted risk score was higher for the hospital that closed earlier. If so, the model's prediction was accurate and the pair is considered "concordant".

Since our data has a high rate of censoring (hospitals not closing within the given time frame), the Concordance Index can be overly optimistic. 
Thus, **Uno's concordance index** was used as the primary evaluation metric, which uses **Inverse Probability of Censoring Weights (IPCW)**, correcting for this over-optimism issue.

The model achieved an Uno's concordance index score of **0.988** on the real-world test data, indicating a very strong association between the model's Hazard Ratio scores and the actual hospital closure outcomes.
'''

st.subheader('Explainability & Interpretability')

st.markdown("#### Model Coefficients")
'''
Since the Cox regression model is a linear model, feature coefficients can be extracted and analyzed to see exactly how much each feature increases or decreases the log-hazard risk. 
A positive coefficient indicates a higher risk of hospital closure, while a negative coefficient indicates a protective effect.
'''
st.space('small')
img_path = Path(__file__).parent.parent / "images" / "neg_coefs.png"

if img_path.exists():
    st.image(str(img_path), width=600)
else:
    st.error(f"File not found at: {img_path}")
st.caption("Model features with negative coefficients")
img_path = Path(__file__).parent.parent / "images" / "pos_coefs.png"

if img_path.exists():
    st.image(str(img_path), width=500)
else:
    st.error(f"File not found at: {img_path}")
st.caption("Model features with positive coefficients")
st.space('small')


st.write(
    "The exponentiated coefficients, also known as hazard ratios, show the effect size of each feature. "
    "For example, having a RUCA score of 1 reduces the risk score by a factor of "
    "$e^{-0.078098}$, or about 92%, indicating a lower chance of hospital closure."
)

st.markdown("#### Permutation Importance Scores")
'''
The salience of each feature can also be evaluated via permutation feature importance scores.
Permutation feature importance will measure how much the model's concordance index score drops when the values of a single feature are randomly shuffled.
A high score indicates the feature is used heavily by the model to make accurate predictions; a low score indicates the model does not heavily rely on the feature's value when making predictions, suggesting the feature might be irrelevant, redundant, or mostly "noise".
'''
st.space('small')
img_path = Path(__file__).parent.parent / "images" / "HighPerm.png"

if img_path.exists():
    st.image(str(img_path), width=550)
else:
    st.error(f"File not found at: {img_path}")
st.caption("Model features with high permutation importance scores")
st.space('small')

st.space('small')
img_path = Path(__file__).parent.parent / "images" / "LowPerm.png"

if img_path.exists():
    st.image(str(img_path), width=350)
else:
    st.error(f"File not found at: {img_path}")
st.caption("Model features with low permutation importance scores")
st.space('small')

st.markdown("#### SHAP Scores")
'''
The impact of each feature can also be captured by SHAP (SHapley Additive exPlanations) scores. 
Each SHAP value represents the amount that a specific feature's value pushed the hospital closure risk score up or down relative to the baseline risk.
'''
img_path = Path(__file__).parent.parent / "images" / "shap_summary_bar_plot.png"

if img_path.exists():
    st.image(str(img_path))
else:
    st.error(f"File not found at: {img_path}")

st.subheader("References")
st.markdown("<span id='cite-1'>[1]</span> En-nasiry, Mouad. *Time Series Splitting Techniques: Ensuring Accurate Model Validation* 2024 June 18. https://medium.com/@mouadenna/time-series-splitting-techniques-ensuring-accurate-model-validation-5a3146db3088", unsafe_allow_html=True)

