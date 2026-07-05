import streamlit as st

st.set_page_config(layout="wide")

st.title('Predicting Rural Hospital Closures', text_alignment='center')

st.space('small')

st.subheader('Executive summary')
'''
This project combines financial health, operational metrics, and local demographic data to predict the likelihood that a rural US acute care hospital will close or convert their operations at a certain point in time. 
Features include operating margins, hospital quality, ownership structure (for-profit vs. non-profit), and regional healthcare utilization and demographic data.
'''

st.subheader('Background')
'''
There have been 154 Rural hospital Closures and Conversions since 2010, with the annual total of rural hospital closures spiking in 2023. 
Rural hospital closures and conversions often leave nearby residents without access to proximate health care. 
'''
st.markdown("Hospital closures have severe repercussions including the availability of health care in many communities, the travel time to distant alternative facilities, increased unemployment for health care workers, and stagnation in local economies. A better understanding of hospital closures, therefore, could help inform hospital managers and guide corrective actions to avoid closures <a href='#cite-1'>[1]</a>.", unsafe_allow_html=True)

st.markdown(""" Over the same period (since 2010), rural adults have experienced higher rates of mortality from heart disease, cancer, unintentional injury, and stroke relative to urban adults.
This dual challenge of declining access and diminishing health status for rural populations has presented one of the most formidable policy challenges for US health care <a href='#cite-2'>[2]</a>. """, unsafe_allow_html=True)

st.image("./images/closure_plot.png")

st.subheader('Project scope')

st.markdown("The scope of this project is limited to rural acute care hospitals in the United States. The Sheps dataset on rural hospital closures (see <a href='#cite-4'>[4]</a>) was extremely helpful for this project; it would have required a significant manual effort to amass the same closure data on non-rural hospitals. Thus, it made sense to scope the entire project to rural hospitals so as not to compare strictly rural closed hospitals with both rural and non-rural operational hospitals.", unsafe_allow_html=True)


st.subheader('What is a hospital closure?')

st.markdown(""" "We follow the convention of the Office of Inspector General that a closed hospital is ***'A facility that stopped providing general, short-term, acute inpatient care.'*** We did not consider a hospital closed if it: Merged with, or was sold to, another hospital but the physical plant continued to provide inpatient acute care, Converted to a Critical Access Hospital, Converted to a Rural Emergency Hospital, or Both closed and reopened during the same calendar year and at the same physical location.

A facility that no longer provides health services is considered a "complete closure." Note that a facility that closed its inpatient unit but continued to provide other health services, like urgent or emergent care services, rehabilitation, and/or outpatient services, at the same physical location would be considered a 'converted closure'. Likewise, a facility that dramatically scaled back its inpatient services (e.g., from 70 beds to 2 beds) would be considered 'open' because it continues to provide inpatient services (albeit in a vastly reduced manner).

*A conversion to a rural emergency hospital is not considered a closure.*" <a href='#cite-4'>[4]</a>. """, unsafe_allow_html=True)
'''
A Rural Emergency Hospital (REH) is a Medicare provider designation created by Congress in 2021 to prevent rural hospital closures. REHs provide 24/7 emergency care and observation services but do not have inpatient beds. They receive enhanced Medicare payments to sustain outpatient care. The REH designation became effective on January 1, 2023.
'''

st.subheader('What is a rural hospital?')
st.markdown("""
The Federal Office of Rural Health Policy's (FORHP) has a specific definition of a rural area; this definition is used to determine whether a hospital can apply for rural health grants, for example. 
FORHP defines the following areas as rural:
* Non-metropolitan counties
* Outlying metropolitan counties with no population from an urban area of 50,000 or more people
* Census tracts with RUCA codes 4-10 in metropolitan counties
* Census tracts of at least 400 square miles in area with population density of 35 or fewer people per square mile with RUCA codes 2-3 in metropolitan counties
* Census tracts with RRS 5 and RUCA codes 2-3 that are at least 20 square miles in area in metropolitan counties

Based on 2020 Census data, FORHP considers 19.3% of the population (64.5 million people) and 87.7% of the land area of the country to be rural.

The United States Census Bureau (Census), the Office of Management and Budget (OMB), and the United States Department of Agriculture Economic Research Service (ERS) each has their own definition of rural for their own purposes, but none of these are granular enough to use for rural health policy. 
The use of Rural-Urban Commuting Area (RUCA) codes and Road Ruggedness Scale (RRS) codes allows the assessment of rurality on a smaller, census-tract level. 
<a href='#cite-3'>[3]</a>. """, unsafe_allow_html=True)

st.subheader('Data Sources')

st.markdown(""" **Financial data**
The Centers for Medicare & Medicaid Services (CMS) Healthcare Cost Report Information System (HCRIS) includes annual cost reports containing revenue, costs, facility characteristics, utilization data, and financial statements.
""")

st.markdown(""" **Area Health Resource Data** was sourced from the Area Health Resources Files.
This dataset provides current as well as historic data for more than 6,000 variables for each of the nation's counties, as well as state and national data. It contains information on health facilities, health professions, measures of resource scarcity, health status, economic activity, health training programs, and socioeconomic and environmental characteristics.
County-level ARHF data was associated with each rural hospital in this project.
""")

st.markdown(""" **Hospital quality data** comes from the Centers for Medicare & Medicaid Services' Provider Data Catalog, which contains hospital quality ratings and compliance data.
This data includes Process of Care Scores (shares of patients receiving evidence-based treatments for AMI, CHF, pneumonia, surgical care, and outpatient care),
Hospital Consumer Assessment of Healthcare Providers and Systems/HCAHPS (average scores for the aggregated questions in HCAHPS patient satisfaction survey), 
and mortality/readmission data (estimates of AMI, CHF, and pneumonia mortality and readmission rates).
""")

st.markdown("""**Hospital Closure Data** 
The Sheps Center Rural Hospital Closures Database (from the North Carolina Rural Health Research Program) contains data on rural hospital closures and conversions since 2005. 
The Cecil G. Sheps Center for Health Services Research seeks to improve the health of individuals, families, and populations by understanding the problems, issues and alternatives in the design and delivery of health care services.
""")

st.subheader('How was risk evaluated?')
'''
This project uses a penalized Cox Proportional Hazards regression model, which is a semi-parametric method used in survival analysis to model the time it takes for an event to occur while accounting for multiple predictor variables. Cox Regression models can be used either to test hypotheses about the independent variables or to build a predictive model; in this case, a predictive model is used.
Survival analysis was an appropriate framework to use here since based on recent trends, we expect more rural hospitals to close over the coming years. However, these closures are not captured in our data, even as certain predictor values might be indicating an imminent closure. This is referred to in survival analysis as "right-censoring". 
The model predictions take the form of a Hazard Ratio (HR), which indicates how much more or less likely a hospital is to close at any given time compared to a baseline group. 
The scikit-survival library was used to implement the model, since its penalized Cox model supports Ridge and Lasso regularization. This coefficient penalization is helpful for the high-dimensional data in this project. Many of the features are related to one another (high multicollinearity), which breaks normal Cox regression models, but penalized Cox models can prune features more aggressively to deal with this issue.
'''

st.subheader("References")
st.markdown("<span id='cite-1'>[1]</span> Pai DR, Hosseini H, Brown RS. *Does efficiency and quality of care affect hospital closures?* Health Syst (Basingstoke). 2017 Dec 7;8(1):17-30. doi: 10.1080/20476965.2017.1405874. PMID: 31214352; PMCID: PMC6508065.", unsafe_allow_html=True)
st.markdown("<span id='cite-2'>[2]</span> Chatterjee P. Causes and consequences of rural hospital closures. J Hosp Med. 2022 Nov;17(11):938-939. doi: 10.1002/jhm.12973. Epub 2022 Oct 3. PMID: 36190813; PMCID: PMC9633454.", unsafe_allow_html=True)
st.markdown("<span id='cite-3'>[3]</span> US Health Resources and Services Administration. *'How We Define Rural'*. https://www.hrsa.gov/rural-health/about-us/what-is-rural", unsafe_allow_html=True)
st.markdown("<span id='cite-4'>[4]</span> North Carolina Rural Health Research Program, 2014, The University of North Carolina at Chapel Hill. https://www.shepscenter.unc.edu/programs-projects/rural-health/rural-hospital-closures/", unsafe_allow_html=True)
