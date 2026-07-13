# Data Dictionary for Rural Hospital Closures Project:

This data dictionary describes all features that are present in the final dataset. Some features were not included in the machine learning model due to excessive missingness; these are marked with an asterisk. 

The objective is to clearly explain all features, especially those whose column names are ambiguous. Data types are also included. All financial values were converted to 2025 purchasing power.

### Model Targets
* Status (boolean): represents whether or not the given hospital closed in the given year. 
* Time (int): the total number of years of data the dataset contains for the given hospital.

### Hospital info features
* Hospital Type (string): Identifies hospital ownership type as "non-profit", "for-profit", and "government" based on the following groupings of ownership types:
    * Government:
        * Government - Hospital District or Authority
        * Governmental-Hospital District
        * Government - Federal
        * Governmental- Federal
        * Government - Local
        * Government - State
        * Governmental-County
        * Governmental-City
        * Governmental-City-County
        * Governmental-Other
        * Tribal
    * Non-Profit:
        * Voluntary / Non-profit groupings
        * Voluntary non-profit - Private
        * Voluntary Nonprofit-Other
        * Voluntary non-profit - Other
        * Voluntary non-profit - Church
        * Voluntary Nonprofit-Church
    * For-Profit:
        * Proprietary, Corporation
        * Proprietary-Corporation
        * Proprietary, Partnership
        * Proprietary-Partnership
        * Proprietary-Individual
        * Proprietary, Other
        * Physician
* Emergency Services (boolean): Whether or not the hospital facility provided emergency services  
* RUCA (string): Rural-Urban Commuting Area code; a detailed classification system that measures the rural or urban status of U.S. geographic areas using population density, urbanization, and daily work commuting data
* Metro_Status (string): either "metropolitan", "micropolitan", or "neither". Defines whether a U.S. county belongs to a major urban labor market, a smaller urban cluster, or a rural/non-core area. These classifications are set by the Office of Management and Budget (OMB) under Core-Based Statistical Areas (CBSAs).

### Financial features
* Donations, Land Improvements* (float): fair market value of donated land improvements acquired during the cost reporting period  
* NUMBER OF BEDS - Total Hospital (float): total number of general inpatient hospital beds 
* BALANCE SHEET - Total Current Assets (G_C1THRU4_11) (float): short-term economic resources expected to be converted to cash, sold, or consumed within one year  
* Total Bad Debt expense (float): total facility charges or amounts written off as uncollectible during the cost reporting period for services rendered, where an expectation and ability to pay existed 
* RECONCILIATION OF CAPITAL COST CENTERS - Depreciation, Total (A7_3_C9_3) (float): total depreciation expense for buildings, fixtures, and movable equipment  
* BALANCE SHEET - Inventory (G_C1THRU4_7) (float): cost of unused supplies, drugs, and merchandise owned by the healthcare facility at the close of the accounting period  
* BALANCE SHEET - Cash on Hand and in Banks (G_C1THRU4_1) (float): total physical cash (money kept on hand for minor or petty cash disbursements), bank deposits (general, payroll, and other checking or deposit accounts immediately available for financing activities), and short-term savings (savings accounts, certificates of deposit (CDs), treasury bills, and treasury notes)  
* Net Revenue from Medicaid (float): total inpatient and outpatient payments received or expected by a hospital for Title XIX (Medicaid) covered services  
* Total Charges (float): total of gross charges accumulated across all hospital departments, covering charges associated with inpatient routine care, ancillary services, and outpatient care  
* BALANCE SHEET - Accounts Receivable (G_C1THRU4_4) (float): total unpaid inpatient and outpatient billings, including direct patient balances for deductibles and co-insurance  
* IPPS Interim payment (float): total interim or periodic payments made to a hospital by Medicare for acute inpatient services during the cost reporting period before final settlement reconciliation  
* Medicaid charges (float): total billed charges for hospital services provided to patients covered under a state Medicaid program  
* Total Costs (float): total hospital costs  
* Total Inpatient Days (float): total number of inpatient days for all classes of patients (adults and peds) for the main hospital facility  
* ADJUSTED SALARIES, Subtotal Salaries (float): net wage and salary costs after removing excluded areas and applying reclassifications  
* REIMBURSEMENT SETTLEMENT - Interim payments (float): total tentative, periodic cash advances paid by Medicare to a hospital throughout its fiscal year before final reconciliation  
* Cost of Uncompensated Care (float): aggregate cost of care provided for which no compensation was received, combining charity care and non-Medicare/non-reimbursable bad debt  
* BALANCE SHEET - Prepaid expenses (G_C1THRU4_8) (float): total advance payments for goods or services properly chargeable to future accounting periods
* BED DAYS - Total Hospital (float): total capacity of inpatient hospital beds ready for use over the course of the cost-reporting period
* BALANCE SHEET - Total Assets (G_C1THRU4_36) (float): sum of all current assets, fixed assets, and other assets owned by the healthcare provider
* NUMBER OF BEDS - ICU (float): count of intensive care unit beds that are set up and staffed for use at the end of the cost reporting period
* NUMBER OF BEDS - Adults & Pediatrics (float): count of general routine hospital care beds available for use at the end of the cost reporting period
* TRIAL BALANCE OF EXPENSE ACCOUNTS - Interest Expense (A_C2_113)* (float): total non-salary interest expenses paid before any accounting reclassifications or adjustments are made
* Total cost of charity care (float): direct cost incurred for providing free or discounted care to eligible low-income and uninsured patients
* STATEMENT OF REVENUES AND EXPENSES - Net Income (G3_C1_29) (float): final net income (or net loss) for the designated fiscal reporting period
* IPPS Payment amount (unadjusted) (float): baseline inpatient prospective payment calculated before final program adjustments
* REIMBURSEMENT SETTLEMENT - Subtotal (float): net tentative Medicare or program reimbursement due to or from the facility prior to final offsets like interim payments
* REIMBURSEMENT SETTLEMENT - Payment to cost ratio* (float): total interim and final settlement dollars paid by Medicare or another payer divided by total allowable, step-down expenses calculated for delivering services to program beneficiaries
* Total Liabilities (float): sum of all short-term and long-term financial obligations 
* Total Days Title XVIII (float): Total Medicare (Title XVIII) Inpatient Days for the adults and pediatrics (general routine) hospital care complex
* BALANCE SHEET - Temporary Investments (G_C1THRU4_2)* (float): short-term securities, marketable stocks, bonds, or cash equivalents that the healthcare facility plans to convert to cash within one year
* BALANCE SHEET - Total Current Liabilities (G_C1THRU4_45) (float): short-term financial obligations due within one year, including accounts payable, notes payable, and accrued expenses
* Total Salaries (float): gross, unadjusted salary expense reported directly from the facility's general ledger or trial balances
* Number of Interns & Residents (float): Full-Time Equivalent (FTE) count of interns and residents in an approved teaching program for the main hospital
* HAC reduction adjustment amount* (float): financial penalty applied to a hospital's Medicare payments under the Hospital-Acquired Condition Reduction Program (HACRP)
* Cost To Charge Ratio (float): total costs divided by total charges; a financial metric used to convert a hospital's gross billed charges into an estimate of the actual operational costs incurred
* FTE Employees on Payroll* (float): average number of full-time equivalent employees on a hospital's payroll during the reporting period
* Total discharges (float): total count of inpatient hospital stays completed (including patient deaths, but excluding newborns and dead-on-arrivals (DOAs)) across all payers
* HVBP payment adjustment amount (float): net dollar adjustment (either a positive incentive bonus or a negative penalty) applied to a hospital's inpatient DRG (Diagnosis-Related Group) payments based on quality performance
* STATEMENT OF REVENUES AND EXPENSES - Net Patient Revenue (G3_C1_3) (float): total facility-wide patient revenue after accounting for deductions
* Financial Indicators - Total Net Assets (float): total fund balance or net equity, calculated as total assets minus total liabilities
* S-10 DATA - Medicaid Costs (float): total uncompensated and indigent care, tracking specific elements like Medicaid non-covered charges, charity care, and bad debt to estimate total uncompensated care costs
* Financial Indicators - Cash Reserves (float): sum of Temporary Investments (G_C1THRU4_2) and Cash on Hand and in Banks (G_C1THRU4_1)
* Financial Indicators - Net Profit Margin (float): Net Income (G3_C1_29) divided by Net Patient Revenue (G3_C1_3); represents portion of Net Patient Revenue retained by the hospital
* Financial Indicators - Operating Profit (float): Net Patient Revenue minus Hospital Operating Costs
* Financial Indicators - Operating Profit Margin (float): Operating Profit (Loss) divided by Net Patient Revenue; captures earnings on hospital patient services, excluding non-patient related income and costs
* Financial Indicators - LIQUIDITY current ratio (float): Total Current Assets (G_C1THRU4_11) divided by Total Current Liabilities (G_C1THRU4_45); measures current assets (those that can reasonably be converted to cash in one year) against current liabilities
* Financial Indicators - LIQUIDITY acid-test ratio (float): sum of Cash and Cash Equivalents, Short-Term Investments, and Accounts Receivable divided by current liabilities
* Financial Indicators - LIQUIDITY acid-test ratio (variation) (float): a variation of the quick/acid-test ratio simply subtracts inventory from current assets, making it a bit more generous; Current Assets minus Inventories minus Prepaid Costs divided by Current Liabilities
* Financial Indicators - LIQUIDITY cash ratio (float): the most exacting of the liquidity ratios. Excluding accounts receivable, as well as inventories and other current assets, it defines liquid assets strictly as cash or cash equivalents. More than the current ratio or acid-test ratio, the cash ratio assesses an entity's ability to stay solvent in case of an emergency on the grounds that even highly profitable companies can run into trouble if they do not have the liquidity to react to unforeseen events. Formula is Cash and Cash Equivalents divided by Current Liabilities
* Financial Indicators - SOLVENCY Debt-to-Equity Ratio (float): Formula is total liabilities divided by total net assets or equity, where equity (net assets) is total assets minus total liabilities. This ratio indicates how much debt a facility is using to finance its assets relative to equity. A higher ratio suggests more debt relative to equity, which may indicate financial risk (Can also be a measure of leverage).
* Financial Indicators - SOLVENCY Debt Ratio (float): Formula is total liabilities divided by total assets. This ratio measures the proportion of a hospital's assets that are financed by debt. A higher debt ratio may indicate greater financial leverage and, potentially, higher financial risk (Can also be a measure of leverage).
* Financial Indicators - SOLVENCY Equity Ratio (float): Formula is (Total Net Assets or Equity) / Total Assets. This ratio shows the proportion of assets financed by equity, representing the financial stability of the hospital. A higher ratio generally means a stronger financial position with less reliance on debt (Can also be a measure of leverage).
* Financial Indicators - SOLVENCY Interest Coverage Ratio* (float): Formula is (Operating Income + Depreciation) / Interest Expense. While interest expenses may not always be separated out in CMS cost reports, this ratio shows the ability to meet interest obligations with operating income, providing insight into how well debt obligations are covered.
* Financial Indicators - SOLVENCY total assets less total liabilities (float): Assets minus liabilities is the quickest way to assess a company's solvency. The solvency ratio calculates net income + depreciation and amortization / total liabilities. This ratio is commonly used first when building out a solvency analysis.
* Financial Indicators - EFFICIENCY asset turnover ratio (float): Formula: Total Revenue / Total Assets. This ratio shows how efficiently the hospital uses its assets to generate revenue.
* Financial Indicators - EFFICIENCY Accounts Receivable Turnover Ratio (float): Formula: Total Revenue / Patient Accounts Receivable. This ratio indicates how quickly the hospital collects its receivables.


### Hospital quality features:
#### Process of care features:
* ami1_denom* (float): total number of heart attack patients admitted who met the criteria to receive aspirin at arrival
* ami2_denom* (float): total number of heart attack patients discharged who met the criteria to receive aspirin
* ami3_denom* (float): total number of heart attack patients meeting the criteria to receive an ACE Inhibitor for Left Ventricular Systolic Dysfunction (LVSD)
* ami4_denom* (float): total number of heart attack patients meeting the criteria to receive smoking cessation advice/counseling
* ami5_denom* (float): total number of heart attack patients meeting the criteria to receive Beta Blocker at discharge
* ami7_denom* (float): total number of heart attack patients meeting the criteria to receive Thrombolytic Medication Within 30 Minutes Of Arrival
* ami8_denom* (float): total number of heart attack patients meeting the criteria to receive PCI Within 120 Minutes Of Arrival
* cac1_denom* (float): total number of children's asthma care patients meeting the criteria to receive reliever medication while hospitalized for asthma
* cac2_denom* (float): total number of children's asthma care patients meeting the criteria to receive systemic corticosteroid medication (oral and IV medication that reduces inflammation and controls symptoms) while hospitalized for asthma
* cac3_denom* (float): total number of children's asthma care patients meeting the criteria to be discharged with a completed home management plan
* hf1_denom* (float): total number of heart failure patients meeting the criteria to be given discharge instructions
* hf2_denom* (float): total number of heart failure patients meeting the criteria to be given assessment of Left Ventricular Function (LVF)
* hf3_denom* (float): total number of heart failure patients meeting the criteria to be given ACE Inhibitor for Left Ventricular Systolic Dysfunction (LVSD)
* hf4_denom* (float): total number of heart failure patients meeting the criteria to be given Adult Smoking Cessation Advice/Counseling
* op2_denom* (float): total number of outpatient emergency room heart attack and chest pain patients meeting the criteria to receive clot-dissolving fibrinolytic therapy
* op3_denom* (float): total number of outpatient emergency room heart attack and chest pain patients who meet the criteria for a transfer for acute coronary intervention 
* op4_denom* (float): total number of outpatient emergency room heart attack and chest pain patients who meet the criteria to receive aspirin
* op5_denom* (float): total number of outpatient emergency room heart attack and chest pain patients who meet the criteria to receive an ECG
* op6_denom* (float): total number of outpatient emergency room heart attack and chest pain patients who meet the criteria to receive preventive (prophylactic) antibiotics within the appropriate timeframe prior to surgery
* op7_denom* (float): total number of outpatient emergency room heart attack and chest pain patients who meet the criteria to receive the appropriate, guideline-recommended first- or second-generation cephalosporin antibiotic for specific outpatient surgical procedures
* pn2_denom* (float): total number of pneumonia patients eligible for a pneumococcal vaccination
* pn3_denom* (float): total number of pneumonia patients eligible for a blood culture performed prior to first antibiotic received in hospital
* pn4_denom* (float): total number of pneumonia patients eligible for Adult Smoking Cessation Advice/Counseling
* pn5_denom* (float): total number of pneumonia patients eligible to be given an Initial Antibiotic(s) within 4 Hours After Arrival
* pn6_denom* (float): total number of pneumonia patients eligible to be given the Most Appropriate Initial Antibiotic(s)
* pn7_denom* (float): total number of pneumonia patients eligible to be given Influenza Vaccination
* scipcard2_denom* (float): total number of surgical patients eligible to receive a Beta-Blocker During the Perioperative Period
* scipinf1_denom* (float): total number of surgical patients who were eligible to receive prophylactic (preventative) antibiotics within one hour prior to their surgical incision
* scipinf2_denom* (float): total number of surgical patients who were eligible to receive the Appropriate Preventative Antibiotic(s) for Their Surgery
* scipinf3_denom* (float): total number of surgical patients meeting the criteria to have their prophylactic antibiotics stopped within 24 hours of surgery ending (or 48 hours for cardiac surgeries)
* scipinf4_denom* (float): total number of eligible cardiac surgery patients who met the inclusion criteria for the specific Surgical Care Improvement Project (SCIP) glucose-control measure
* scipinf6_denom* (float): total number of eligible surgery patients evaluated for appropriate hair removal
* scipinf9_denom* (float): total number of selected surgical patients who had an indwelling urinary catheter postoperatively
* scipvte1_denom* (float): total number of patients eligible to receive Treatments to Prevent Blood Clots (Venous Thromboembolism) For Certain Types of Surgeries
* scipvte2_denom* (float): total number of patients eligible to receive treatment To Prevent Blood Clots Within 24 Hours Before or After Selected Surgeries 
* op2_share* (float): percentage of eligible outpatient emergency room heart attack and chest pain patients who received clot-dissolving fibrinolytic therapy
* op4_share* (float): percentage of eligible outpatient emergency room heart attack and chest pain patients who received aspirin
* op6_share* (float): percentage of outpatient emergency room heart attack and chest pain patients who received preventive (prophylactic) antibiotics within the appropriate timeframe prior to surgery
* ami10_denom* (float): total number of heart attack patients meeting the criteria to receive a statin cholesterol-lowering drug at discharge
* op1_denom* (float): total number of outpatient emergency room heart attack and chest pain patients who meet the criteria for receiving clot-dissolving (fibrinolytic) medication 
* scipinf10_denom* (float): total number of adult patients who underwent a qualified major surgical procedure under general or neuraxial anesthesia lasting 60 minutes or longer, and who had no evidence of a prior infection
* ami10_share* (float): percentage of heart attack patients who received a statin cholesterol-lowering drug at discharge
* ami2_share* (float): percentage of heart attack patients discharged who received aspirin
* ami7_share* (float): percentage of heart attack patients who received Thrombolytic Medication Within 30 Minutes Of Arrival
* ami8_share* (float): percentage of heart attack patients who received PCI Within 120 Minutes Of Arrival
* cac1_share* (float): percentage of children's asthma care patients who received reliever medication while hospitalized for asthma
* cac2_share* (float): percentage of children's asthma care patients who received systemic corticosteroid medication (oral and IV medication that reduces inflammation and controls symptoms) while hospitalized for asthma
* cac3_share* (float): percentage of children's asthma care patients who were discharged with a completed home management plan
* hf1_share* (float): percentage of heart failure patients who were given discharge instructions
* hf2_share* (float): percentage of heart failure patients who were given assessment of Left Ventricular Function (LVF)
* hf3_share* (float): percentage of heart failure patients who were given ACE Inhibitor for Left Ventricular Systolic Dysfunction (LVSD)
* op7_share* (float): percentage of outpatient emergency room heart attack and chest pain patients who received the appropriate, guideline-recommended first- or second-generation cephalosporin antibiotic for specific outpatient surgical procedures
* pn3_share* (float): percentage of pneumonia patients who received a blood culture prior to first antibiotic received in hospital
* pn6_share* (float): percentage of pneumonia patients who were given the Most Appropriate Initial Antibiotic(s)
* scipcard2_share* (float): percentage of surgical patients who received a Beta-Blocker During the Perioperative Period
* scipinf10_share* (float): percentage of surgery patients who had active warming or maintained normal body temperature (normothermia) during surgery to lower infection risks
* scipinf1_share* (float): percentage of eligible surgical patients who received prophylactic (preventative) antibiotics within one hour prior to their surgical incision
* scipinf2_share* (float): percentage of surgical patients who received the Appropriate Preventative Antibiotic(s) for Their Surgery
* scipinf3_share* (float): percentage of eligible surgical patients having their prophylactic antibiotics stopped within 24 hours of surgery ending (or 48 hours for cardiac surgeries)
* scipinf4_share* (float): percentage of cardiac surgery patients who achieve controlled blood glucose levels (specifically less than or equal to 200 mg/dL at 6:00 AM) on postoperative days one and two
* scipinf9_share* (float): percentage of surgical patients whose urinary catheters were removed on the first or second day after surgery
* scipvte1_share* (float): percentage of patients who received Treatments to Prevent Blood Clots (Venous Thromboembolism) For Certain Types of Surgeries
* scipvte2_share* (float): total number of patients who received treatment To Prevent Blood Clots Within 24 Hours Before or After Selected Surgeries 
#### HCAHPS (Hospital Consumer Assessment of Healthcare Providers and Systems) features:
* nsurveys (float): total count of valid patient responses a hospital collected during the reporting period. A hospital needs at least 25 completed surveys to have its data publicly reported
* rrate (float): percentage of contacted patients who actually finished the survey
* clean_score (float): average patient feedback score corresponding to the cleanliness of their hospital room and bathroom during a stay
* commdoc_score (float): average patient feedback score corresponding to whether doctors treated them with courtesy and respect, listened carefully, and explained things clearly during a stay
* commnurse_score (float): average patient feedback score corresponding to whether nurses treated them with courtesy and respect, listened carefully, and explained things clearly during a stay
* explain_score (float): average patient feedback score corresponding to how clearly doctors or nurses explained care to the patient
* help_score (float): average patient feedback score corresponding to staff responsiveness; tracks how often patients report receiving prompt assistance from nurses and hospital staff
* info_score (float): average patient feedback score corresponding to whether a patient felt they were given adequate information regarding post-discharge recovery
* overall_score (float): average numerical rating of the hospital on a 0 to 10 scale; reflects patient satisfaction and experiences during their inpatient stay
* pain_score (float): average patient feedback score corresponding to how well patients felt that hospital staff managed their pain
* quiet_score (float): average patient feedback score corresponding to  how often the area around their room was quiet
* recommend_score (float): average patient feedback score corresponding to whether they would definitely recommend the hospital to friends and family
* understood_score (float): average feedback score corresponding to patient comprehension regarding their self-care and medications after discharge
#### Mortality and readmission features:
* ami_mort_rate (float): 30-day risk-standardized mortality rate for patients admitted with an acute myocardial infarction (AMI) (heart attack)
* ami_readm_rate (float): risk-standardized 30-day readmission rate for acute myocardial infarction (heart attack)
* hf_mort_rate (float): risk-standardized rate of patient deaths from heart failure within 30 days post-admission 
* hf_readm_rate (float): risk-standardized percentage of patients who return to an acute care hospital within 30 days of being discharged after an initial hospital stay for heart failure
* pn_mort_rate (float): percentage of pneumonia patients who die within 30 days of their initial hospital admission
* pn_readm_rate (float): percentage of patients who unexpectedly return to any acute care hospital within 30 days of being discharged from an initial hospital stay for pneumonia
* ami_mort_npatients (float): number of patients used to calculate the acute myocardial infarction (AMI) mortality measure 
* ami_readm_npatients (float): number of patients used to calculate the acute myocardial infarction (AMI) readmission measure 
* hf_mort_npatients (float): number of patients used to calculate the heart failure mortality measure 
* hf_readm_npatients (float): number of patients used to calculate the heart failure readmission measure 
* pn_mort_npatients (float): number of patients used to calculate the pneumonia mortality measure 
* pn_readm_npatients (float): number of patients used to calculate the pneumonia readmission measure 
* all_readm_rate (float): all-cause, risk-standardized 30-day readmission rate
* hk_readm_rate (float): percentage of patients who experience an unplanned return to the hospital within 30 days of an elective primary hip or knee joint replacement surgery
* all_readm_npatients (float): number of patients or patient stays used as the denominator to calculate a hospital's all-cause readmission rate
* hk_readm_npatients (float): number of patients used to calculate the hip or knee joint replacement surgery readmission measure 
* copd_mort_rate (float): percentage of chronic obstructive pulmonary disease (COPD) patients who die within 30 days of their initial hospital admission
* copd_readm_rate (float): percentage of chronic obstructive pulmonary disease (COPD) patients who experience an unplanned return to the hospital within 30 days of their initial hospital admission
* stk_mort_rate (float): 30-day risk-standardized mortality rate (RSMR) for patients hospitalized with an acute ischemic stroke
* stk_readm_rate (float): percentage of patients with an acute ischemic stroke who return to any acute care hospital for an unplanned readmission within 30 days of their initial hospital discharge
* copd_mort_npatients (float): number of patients used to calculate the COPD mortality measure 
* copd_readm_npatients (float): number of patients used to calculate the COPD readmission measure 
* stk_mort_npatients (float): number of stroke patients included in the calculation of the 30-day mortality measure for ischemic stroke
* stk_readm_npatients (float): number of stroke patients included in the calculation of the 30-day readmission measure for ischemic stroke
* cabg_mort_rate (float): 30-day risk-standardized mortality rate following coronary artery bypass graft (CABG) surgery
* cabg_readm_rate (float): 30-day readmission rate for coronary artery bypass graft surgery
* cabg_mort_npatients (float): number of patients included in the hospital's 30-day mortality rate calculation following an isolated Coronary Artery Bypass Graft (CABG) surgery
* cabg_readm_npatients (float): 30-day risk-standardized all-cause readmission rate for patients who underwent coronary artery bypass graft (CABG) surgery

### Area Health Resource features:
*All AHRF features are measured at the county level*
* % <65 without Health Insurance (float): share of the civilian, non-elderly population (under the age of 65) lacking public or private health coverage
* Dist Hosp By 00 - 39% Util Rate Short Term General Hospitals (float): distribution of short-term general hospitals grouped by an average bed occupancy rate of 0% to 39% 
* Dist Hosp By 40 - 59% Util Rate Short Term General Hospitals (float): distribution of short-term general hospitals grouped by an average bed occupancy rate of 40% to 59%  
* Dist Hosp By 60 - 79% Util Rate Short Term General Hospitals (float): distribution of short-term general hospitals grouped by an average bed occupancy rate of 60% to 79%  
* Dist Hosp By 80+% Util Rate Short Term General Hospitals (float): distribution of short-term general hospitals grouped by an average bed occupancy rate of 80% or more 
* Median Household Income (float): median income of all households in the county
* Per Capita # Short Term General Hosps (float): per capita number of non-federal, acute-care facilities providing general medical, surgical, and related care where the average patient stay is less than 30 days
* Per Capita Hospital Admissions (float): total number of patient stays or discharges per capita
* Per Capita Hospital Beds (float): per capita count of inpatient care capacities, including total beds, acute care beds, and non-federal beds
* Per Capita Inpatient Days in ST Gen Hosp (float): total per capita number of days that patients spend receiving overnight care in short-term general hospitals
* Per Capita Personal Income (float): total resident income from wages, proprietor earnings, property income, and government transfers per capita
* Per Capita Phys,Primary Care, Patient Care Non-Fed (float): per capita count of non-federal physicians engaged in direct patient care within primary care specialties
* Per Capita Short Term Gen Hosp Admissions (float): total annual count of inpatient hospital stays in non-federal, acute-care facilities per capita 
* Per Capita Short Term General Hosp Beds (float): total per capita acute care inpatient capacity measured by beds set up and staffed for use
* Per Capita Total Active D.O.s Non-Federal (float): per capita count of practicing Doctors of Osteopathic Medicine working outside of federal government service
* Per Capita Total Active M.D.s Non-Federal (float): per capita total count of practicing, licensed Doctors of Medicine (M.D.s) who are actively working and not employed by the federal government 
* Per Capita Total Medicare Inpatient Days Short Term General Hospitals (float): count of inpatient days provided to Medicare beneficiaries per capita
* Per Capita Total Number Hospitals (float): total hospital facility count 
* Percent Persons in Poverty (float): share of the county's population living below the federal poverty threshold
* Population Estimate (float): total county population estimate using decennial census counts and the Census Bureau's Population Estimates Program
* Unemployment Rate, 16+ (float): percentage of the civilian, non-institutionalized population aged 16 and older who are jobless, available for work, and actively seeking employment


*\* Feature was excluded from the model due to excessive missingness (<80%).*