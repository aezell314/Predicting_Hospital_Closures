import streamlit as st

st.set_page_config(
    page_title="Case Study",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Case study 1: a hospital with a high likelihood of closing: COVENANT HEALTH HOBBS HOSPITAL in 2024 (index 759)
#https://www.enr.com/articles/53675-hospital-stuck-between-hard-rock-remote-location

st.subheader('Case Study: Covenant Health Hobbs Hospital')
'''
Covenant Health Hobbs Hospital is a 99-bed acute care facility in Hobbs, NM. 

From MOREgroup, Inc. (the corporation that designed the hospital): "The hospital provides convenient access to healthcare in eastern New Mexico to people who would otherwise have to travel for care. 
The three-story community hospital has 60 patient beds and an Emergency Department, Intensive Care Unit, Operating Rooms, and a Birthing Center."
'''
st.image("./images/Covenant_Health.jpg", width=600)
st.caption('Covenant Health Hobbs Hospital in in Hobbs, NM')

'''
The model assigned Covenant Health Hobbs Hospital a risk score of 14.677 in 2024 - one of the highest risk scores in the entire dataset. 
The factors that contributed to that risk score can be visualized with a SHAP waterfall plot. It is clear that a high debt ratio and a low equity ratio are the biggest drivers of the high risk score.
'''

st.image('./images/covenant_health_hobbs_2024.png')
st.caption('SHAP Waterfall Plot for Covenant Health Hobbs Hospital, 2024')


st.markdown("""
The real-world evidence backs this up. Covenant reports a 10% increase in staffing costs, 7% increase in pharmaceutical costs, and a nearly 15% increase in the cost of medical supplies since 2022.
In addition, inadequate reimbursement rates from major insurance providers have failed to cover the actual cost of treating patients. 
In 2025, Covenant Health attempted to negotiate a new contract with Blue Cross Blue Shield, requesting adequate reimbursement that accounts for the rising cost of patient care.
<a href='#cite-1'>[1]</a>. """, unsafe_allow_html=True)


'''
However, this elevated risk score seems to have been a temporary spike, isolated to 2024.
'''
st.image('./images/covenant_scores.png', width=400)

st.markdown("""
What changed? In 2025, Covenant's parent organization, Providence St. Joseph Health, implemented deleveraging efforts and cash management strategies that restored healthier cash-to-adjusted debt margins across its hospital network.
<a href='#cite-2'>[2]</a>. """, unsafe_allow_html=True)

st.markdown("""            
Additionally, new state tax incentive agreement was reached with the Lea County Board of Commissioners, helping offset operating expenses and improving Covenant's bottom line.

The State of New Mexico provides an incentive to construct Sole Community Provider Hospitals. The incentive provides a gross receipts tax (GRT) deduction on the purchase of construction equipment, materials, and engineering,
architectural and construction services used in the construction of Sole Community Provider Hospitals by a nonprofit organization.

When planning for the new Hospital, Hobbs Hospital did not know that it would qualify for the "Sole Community Provider" GRT deduction.
            
On November 28, 2023, the City of Hobbs was in agreement and voted to allow Covenant Health Hobbs Hospital to apply in retrospect to the State to receive the funds.
Covenant received over $4.2 million from this agreement. 
<a href='#cite-3'>[3]</a>. """, unsafe_allow_html=True)

'''
Evidence that Covenant Health Hobbs improved its financial bottom line in 2025 is bolstered by the SHAP waterfall plot for that year, which does not feature debt ratio or equity ratio among the most impactful features. 
'''
st.image('./images/covenant_health_hobbs_2025.png')
st.caption('SHAP Waterfall Plot for Covenant Health Hobbs Hospital, 2025')



st.subheader("References")
st.markdown("<span id='cite-1'>[1]</span> Hall, Madeleine. *Blue Cross Blue Shield 'unwilling' to negotiate with Covenant Health: Thousands at risk of losing in-network coverage*. KCDB News, Lubbock, TX. 2025 July 24.", unsafe_allow_html=True)
st.markdown("<span id='cite-2'>[2]</span> PROVIDENCE CONTINUING DISCLOSURE QUARTERLY REPORT. https://www.providence.org/-/media/project/psjh/providence/socal/files/about/financial-statements/continuing-disclosure-quarterly-report-2025-q2.pdf?rev=15efa10190da43779ef066c90c3c6c9b&hash=699682E9F67F2F42FF1203FFCC77C186", unsafe_allow_html=True)
st.markdown("<span id='cite-3'>[3]</span> LCBCC Regular Meeting 01-11-2024 Item 02.08.02. https://www.leacounty.gov/DocumentCenter/View/1725/Consideration-of-Lea-County-Resolution-No-24-JAN-006R-Authorizing-an-Agreement-Between-Lea-County-and-Covenant-Health-Hobbs-Hospital?bidId=", unsafe_allow_html=True)
