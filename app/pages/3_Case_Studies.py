import streamlit as st

st.set_page_config(
    page_title="Case Study",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Case study 1: a hospital that the model labels as 'at-risk': OLMSTED MEDICAL CENTER 

st.subheader('Case Study: Olmsted Medical Center')
'''
Olmsted Medical Center is a non-profit community healthcare provider in Rochester, Minnesota. 
It operates a 61-bed acute care hospital, a 24-hour Level IV trauma emergency department, and more than 20 regional clinic locations offering over 35 medical specialties.
'''
st.image("./images/Olmsted_Health.png", width=600)
st.caption('Covenant Health Hobbs Hospital in in Rochester, MN')

'''
Plotting the closure risk scores for Olmsted Health shows a sharp increase between 2023 and 2024. 
The risk score plateaus at around 1 for 2024 and 2025, which is not particularly high, but represents a major increase from the low of almost -10 in 2022.

This paints the picture of a hospital that is "at-risk" - it is not in immediate danger of closing, but may be losing some of the protective factors that influenced the low risk score in 2022.
'''

try:
    st.image('images/olmsted_scores.png', width=600)
except st.runtime.media_file_storage.MediaFileStorageError:
    st.image('../images/olmsted_scores.png', width=600)
'''
The SHAP plots for Olmsted Health for 2023 and 2024 help illustrate which features are contributing to the large uptick in risk. 
'''
try:
    st.image('images/case_study_1.png')
except st.runtime.media_file_storage.MediaFileStorageError:
    st.image('../images/case_study_1.png')
st.caption('SHAP Waterfall Plot for Olmsted Health, 2023')

st.markdown("""
In 2023, Olmsted Health benefited from several protective factors related to positive area health utilization metrics, such as a high number of M.D.s per capita, a high rate of Medicare inpatient days, and a high rate of short term general hospital admissions.
""")

st.space('small')

try:
    st.image('images/case_study_2.png')
except st.runtime.media_file_storage.MediaFileStorageError:
    st.image('../images/case_study_2.png')
st.caption('SHAP Waterfall Plot for Olmsted Health, 2024')

st.markdown("""
By 2024, most of those area health metrics have reversed; the only feature that lowers the risk score is a high cleanliness score based on patient surveys. 
Features that raise the risk score in 2024 include high area unemployment, a higher than average patient recommendation score (which is counterintuitive), and declining area population.
            
Real-world evidence helps to underline the importance of these model features. 
The entire southeastern Minnesota region started out 2024 with elevated unemployment numbers; the 2024 average for Olmsted County was 3.1%, up from an average of 2.2% in 2023. 
<a href='#cite-1'>[1]</a>. """, unsafe_allow_html=True)

st.markdown("""
 The relative decline in M.D.s per capita and total Medicare inpatient days per capita could be due to population growth diluting the physician population, high physician retirement rates, and/or an increase in physician assistants over traditional M.D.s.
            
Plots like the ones above can help hospital executives asses the factors that influence their risk of closure in either direction, as well as monitor year-over-year trends.
""")


st.subheader("References")
st.markdown("<span id='cite-1'>[1]</span> *All of Southeast Minnesota Started 2024 With Higher Unemployment*. KROC News, Rochester, MN. 2024 March 17.", unsafe_allow_html=True)

