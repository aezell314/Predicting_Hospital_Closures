import streamlit as st

st.set_page_config(layout="wide")

st.title('Predicting Rural Hospital Closures', text_alignment='center')

st.space('small')

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.markdown("Additional project information and data files can be found in the [GitHub repository](https://github.com/aezell314/Predicting_Hospital_Closures)")

# -----------------------------
# Main page
# -----------------------------
st.subheader('Executive summary')
'''
This project combines financial health, ownership structure, operational metrics, and local healthcare utilization data to predict the likelihood that a rural US acute care hospital will close or convert their operations between 2010 and 2025. 
'''

st.subheader('Background')
'''
Rural hospitals are in a crisis. There have been 154 rural hospital closures and conversions since 2010 (86 complete closures and 68 converted closures). 
'''
st.markdown("Hospital closures have severe repercussions including the availability of health care in many communities, the travel time to distant alternative facilities, increased unemployment for health care workers, and stagnation in local economies. A better understanding of hospital closures, therefore, could help inform hospital managers and guide corrective actions to avoid closures <a href='#cite-1'>[1]</a>.", unsafe_allow_html=True)

st.markdown(""" Over the same period (since 2010), rural adults have experienced higher rates of mortality from heart disease, cancer, unintentional injury, and stroke relative to urban adults.
Declining healthcare access combined with worsening health outcomes for rural populations represents a major policy challenges for US healthcare <a href='#cite-2'>[2]</a>. """, unsafe_allow_html=True)

try:
    st.image('images/closure_plot.png', width=600)
except st.runtime.media_file_storage.MediaFileStorageError:
    st.image('../images/closure_plot.png', width=600)

st.subheader('What is a hospital closure?')

st.markdown(""" "We follow the convention of the Office of Inspector General that a closed hospital is ***'A facility that stopped providing general, short-term, acute inpatient care.'*** We did not consider a hospital closed if it: Merged with, or was sold to, another hospital but the physical plant continued to provide inpatient acute care, Converted to a Critical Access Hospital, Converted to a Rural Emergency Hospital, or Both closed and reopened during the same calendar year and at the same physical location.

A facility that no longer provides health services is considered a "complete closure." Note that a facility that closed its inpatient unit but continued to provide other health services, like urgent or emergent care services, rehabilitation, and/or outpatient services, at the same physical location would be considered a 'converted closure'. Likewise, a facility that dramatically scaled back its inpatient services (e.g., from 70 beds to 2 beds) would be considered 'open' because it continues to provide inpatient services (albeit in a vastly reduced manner).

*A conversion to a rural emergency hospital is not considered a closure.*" <a href='#cite-4'>[4]</a>. """, unsafe_allow_html=True)
'''
A Rural Emergency Hospital (REH) is a Medicare provider designation created by Congress in 2021 to prevent rural hospital closures. REHs provide 24/7 emergency care and observation services but do not have inpatient beds. They receive enhanced Medicare payments to sustain outpatient care. The REH designation became effective on January 1, 2023.
'''

st.subheader('What is a rural hospital?')
st.markdown("""
For the purposes of this project, a rural hospital is defined as:
* A Critical Access Hospital, or
* A Rural Emergency Hospital, or
* Any short-term, general acute, non-federal hospital that meets the Federal Office of Rural Health Policy's (FORHP) definition of a rural area; this definition is used to determine whether a hospital can apply for rural health grants, for example. 
    * FORHP defines the following areas as rural:
        * Non-metropolitan counties
        * Outlying metropolitan counties with no population from an urban area of 50,000 or more people
        * Census tracts with RUCA codes 4-10 in metropolitan counties
        * Census tracts of at least 400 square miles in area with population density of 35 or fewer people per square mile with RUCA codes 2-3 in metropolitan counties
        * Census tracts with RRS 5 and RUCA codes 2-3 that are at least 20 square miles in area in metropolitan counties

The United States Census Bureau (Census), the Office of Management and Budget (OMB), and the United States Department of Agriculture Economic Research Service (ERS) each has their own definition of rural for their own purposes, but none of these are granular enough to use for rural health policy. 
The use of Rural-Urban Commuting Area (RUCA) codes and Road Ruggedness Scale (RRS) codes allows the assessment of rurality on a smaller, census-tract level. 
<a href='#cite-3'>[3]</a>. """, unsafe_allow_html=True)

st.subheader('Data Sources')

fin_col1, fin_col2 = st.columns([2, 1], vertical_alignment='center')

with fin_col1:
    st.markdown(""" **Financial data**
    The Centers for Medicare & Medicaid Services (CMS) Healthcare Cost Report Information System (HCRIS) includes annual cost reports containing revenue, costs, facility characteristics, utilization data, and financial statements.
    """)

with fin_col2:
    try:
        st.image('images/CMS.png', width=250)
    except st.runtime.media_file_storage.MediaFileStorageError:
        st.image('../images/CMS.png', width=250)

arhf_col1, arhf_col2 = st.columns([1, 3], vertical_alignment='center')

with arhf_col1:
    try:
        st.image('images/HRSA.jpg', width=200)
    except st.runtime.media_file_storage.MediaFileStorageError:
        st.image('../images/HRSA.jpg', width=200)

with arhf_col2:
    st.markdown(""" **Area Health Resource Data** was sourced from Area Health Resources Files, which are made available via the US Health Resources and Services Administration's Data Warehouse.
    This dataset provides current as well as historic data for more than 6,000 variables for each of the nation's counties, as well as state and national data. It contains information on health facilities, health professions, measures of resource scarcity, health status, economic activity, health training programs, and socioeconomic and environmental characteristics.
    County-level ARHF data was associated with each rural hospital in this project.
    """)

st.markdown(""" **Hospital quality data** comes from the Centers for Medicare & Medicaid Services' Provider Data Catalog, which contains hospital quality ratings and compliance data.
This data includes Process of Care Scores (shares of patients receiving evidence-based treatments for AMI, CHF, pneumonia, surgical care, and outpatient care),
Hospital Consumer Assessment of Healthcare Providers and Systems/HCAHPS (average scores for the aggregated questions in HCAHPS patient satisfaction survey), 
and mortality/readmission data (estimates of AMI, CHF, and pneumonia mortality and readmission rates).
""")

hosp_col1, hosp_col2 = st.columns([2, 1], vertical_alignment='center')

with hosp_col1:
    st.markdown("""**Hospital Closure Data** 
    The Sheps Center Rural Hospital Closures Database (from the North Carolina Rural Health Research Program) contains data on rural hospital closures and conversions since 2005. 
    The Cecil G. Sheps Center for Health Services Research seeks to improve the health of individuals, families, and populations by understanding the problems, issues and alternatives in the design and delivery of health care services.
    """)

with hosp_col2:
    try:
        st.image('images/Sheps.png', width=200)
    except st.runtime.media_file_storage.MediaFileStorageError:
        st.image('../images/Sheps.png', width=200)

st.subheader("References")
st.markdown("<span id='cite-1'>[1]</span> Pai DR, Hosseini H, Brown RS. *Does efficiency and quality of care affect hospital closures?* Health Syst (Basingstoke). 2017 Dec 7;8(1):17-30. doi: 10.1080/20476965.2017.1405874. PMID: 31214352; PMCID: PMC6508065.", unsafe_allow_html=True)
st.markdown("<span id='cite-2'>[2]</span> Chatterjee P. Causes and consequences of rural hospital closures. J Hosp Med. 2022 Nov;17(11):938-939. doi: 10.1002/jhm.12973. Epub 2022 Oct 3. PMID: 36190813; PMCID: PMC9633454.", unsafe_allow_html=True)
st.markdown("<span id='cite-3'>[3]</span> US Health Resources and Services Administration. *'How We Define Rural'*. https://www.hrsa.gov/rural-health/about-us/what-is-rural", unsafe_allow_html=True)
st.markdown("<span id='cite-4'>[4]</span> North Carolina Rural Health Research Program, 2014, The University of North Carolina at Chapel Hill. https://www.shepscenter.unc.edu/programs-projects/rural-health/rural-hospital-closures/", unsafe_allow_html=True)
