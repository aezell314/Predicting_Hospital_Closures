import streamlit as st

st.set_page_config(
    page_title="Project Conclusions",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.subheader('Final Conclusions')
st.markdown(""" ###### Overall Takeaways
Hospital closure risk is primarily driven by external geographical and socioeconomic factors, alongside hospital ownership type and patient-reported hospital evaluation metrics. 
Surprisingly, basic financial metrics were less direct or consistent predictors of hospital closure.
""")
st.markdown(""" ###### Hospital Features

* **Hospital-specific features** such as ownership type represent meaningful contributors to closure risk.
* A hospital being non-profit emerges as the highest mean SHAP value and has a positive permutation feature importance score, indicating strong relationships with other features.
    * For-profit and government-owned hospitals tend to have lower risks of closure than non-profit hospitals.
""")
st.markdown(""" ###### Financial Metrics
            
* **Hospital financial metrics**, such as debt, equity, and employee salaries, were notably absent from the top model features by SHAP value and coefficient magnitude. 
* There is a positive permutation feature importance score associated with Net Profit Margin, indicating that feature might have non-linear relationships with other features that affect model predictions.
""")
st.markdown(""" ###### AHRF Features

* **Area Health Resource** features emerge as extremely important predictors of hospital closure. All of the 16 features with non-zero coefficients were either AHRF features or features that related to area geography.
* In summary, hospitals that are located in more affluent counties, with high healthcare availability and utilization, tend to have a lower risk of closure.
* The total number of area hospitals per capita tends to increase risk score, perhaps suggesting too much competition from area hospitals can be a factor leading up to hospital closure.            
""")

st.markdown(""" ###### Hospital Quality Metrics
* None of the **HCAHPS (Hospital Consumer Assessment of Healthcare Providers and Systems)** survey results had non-zero model coeffients, but many of them had relatively large average SHAP scores, indicating the values interact with other features to influence model predictions. 
* High scores (or affirmative answers) on the following questions tend to lower the risk of hospital closure:
    * How often did staff explain about medicines before giving them to patients? (explain_score)
    * Would patients recommend the hospital to friends and family? (recommend_score)
    * How often were the patients' rooms and bathrooms kept clean? (clean_score)
* Several HCAHPS features (nsurveys, explain_score, info_score, and understood_score) had negative permutation feature importance scores, suggesting their values do not meaningfully influence predictions.
* Process of Care scores, as well as mortality and readmission data, had too many missing values and so were excluded from the model.
""")

st.subheader('Limitations')
'''
As mentioned in the introduction, the **Rural Emergency Hospital (REH)** Medicare provider designation became effective on January 1, 2023. 
This designation was created explicitly to help prevent rural hospital closures by providing enhanced, fixed monthly facility payments from Medicare, among other benefits.

This event may have skewed the test data in this project, as there were likely some hospitals in our dataset that converted to Rural Emergency Hospitals (not marked as a closure/conversion in our dataset) that would have closed without the REH option.
This potentially invalidates the Proportional Hazards Assumption of Cox Regression models, which holds that the effect of the predictor variables on the hazard function must be constant over time. 
'''

st.subheader('Future Directions')
'''
More robust analysis can be done to test that the assumptions of a Cox Regression model are met. 

In addition, more work can be done to convert risk scores to probabilities, which would serve as a more straightforward decision support metric. Model calibration would need to be verified beforehand.
'''

st.subheader("Acknowledgements")
st.write(
"""
This project would not have been possible without the generous support of the following people:
* Michael Holloway, Nashville Software School DS9 Instructor
* Kenneth John Locey, author of the [HCRIS-databuilder](https://github.com/klocey/HCRIS-databuilder) GitHub repository
* Aditya Angara, author of the [AHRF_Project](https://github.com/adityanagara/AHRF_project) GitHub repository
* Adam Sacarny, author of the [hospital-compare](https://github.com/asacarny/hospital-compare/) GitHub repository
""")