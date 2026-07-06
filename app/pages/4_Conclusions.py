import streamlit as st

st.set_page_config(
    page_title="Project Conclusions",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.subheader('Final Conclusions')
st.markdown(""" ###### Hospital Features

* **Hospital ownership structure** is the largest driver of closure risk, with high coefficient magnitudes and high permutation feature importances. 
* A hospital being structured as a **Voluntary Non-Profit - Private** hospital - owned by independent, secular community organizations or private foundations rather than a government entity or corporate shareholders - provides a large protective effect.
* On the other hand, a hospital operating as a **Voluntary Non-Profit - Other** facility - indicating it is owned by specific non-community groups, such as religious orders, universities, or a distinct not-for-profit corporation - increases risk of closure.
""")
st.markdown(""" ###### Financial Metrics
            
* Hospital financial metrics such as **debt ratio** and **equity ratio** affect a hospital's risk of closure (in opposite directions), but typically not to a high degree. 
* **Debt ratio** measures the proportion of a hospital's assets that are financed by debt. A higher debt ratio may indicate greater financial leverage and, potentially, higher financial risk.
* **Equity ratio** shows the proportion of assets financed by equity, representing the financial stability of the hospital. A higher ratio generally means a stronger financial position with less reliance on debt.
* **Total adjusted salaries** also appeared as an influential feature based on a positive permutation importance score and a relatively large mean SHAP score, but did not end up with a non-zero coefficient due to the amount of regularization imposed.
* No other hospital financial metrics emerged as important features to the model.
""")
st.markdown(""" ###### AHRF Features

* **Area Health Resource** features are a more complicated picture. Distribution of area hospitals that have a **very low average bed occupancy (0% - 39%)**, typically indicative of regions with underutilized or financially fragile hospital infrastructure, lowers the overall risk score but has a negative permutation importance score, so might not be relevant.
* **Short Term General Hospital Admissions** represent the strongest protective effect against closure based on the coefficient magnitude, as well as a high permutation importance score and mean SHAP score. This suggests that rural hospitals in counties with consistently utilized hospital infrastructure are more likely to be long-lasting.
* **Total Active D.O.s (Doctors of Osteopathic Medicine)** increases closure risk score; this could reflects a workforce more focused on primary care than specialized inpatient medicine that typically generates more revenue.
""")

st.markdown(""" ###### Hospital Quality Metrics
* No hospital quality metrics, such as patient satisfaction survey scores or mortality and readmission metrics, emerged as important features to the model. 
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