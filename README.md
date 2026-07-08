# Predicting US Rural Hospital Closures

This project combines financial health, operational metrics, and local demographic data to predict the likelihood that a rural US acute care hospital will close or convert their operations between 2010 and 2025. 

Features include operating margins, hospital quality, ownership structure (for-profit vs. non-profit), and regional healthcare utilization and demographic data. A penalized Cox Regression machine learning model is fit to the data to predict closure risk scores. 

### How to use this repo:

* If you are interested in recreating the dataset that was used for this project, follow these steps:

    <details>
    <summary>Hospital Information Gathering</summary>
  
  First, run “notebooks/Nominatim Geocoding Notebook.ipynb”. This takes in “Hospital_General_Information.csv” (downloaded from here: https://data.cms.gov/provider-data/sites/default/files/resources/893c372430d9d71a1c52737d01239d47_1777413958/Hospital_General_Information.csv), which is a list provided by CMS of all hospitals that have been registered with Medicare. The list includes addresses, phone numbers, hospital type, and overall hospital rating. The notebook also takes in “Closures-Database-for-Web.xlsx” (downloaded from here: https://www.shepscenter.unc.edu/download/11619/?tmstv=1782256414), a dataset on rural hospital closures since 2005 provided by the Cecil G. Sheps Center for Health Services Research. The notebook will merge those 2 datasets, geocode each hospital using the Nominatim geocoding tool via the GeoPy python package, and output a file called nominatim_geocoded.csv, containing facility name (hospital name), address, and coordinates (latitude and longitude).

    Next, run “notebooks/Hospital Base Data Gathering Notebook.ipynb”. This requires nominatim_geocoded.csv to exist, as well as “Hospital_General_Information.csv” and “Closures-Database-for-Web.xlsx” discussed in the previous bulletpoint. The notebook uses the Nominatim-geocoded addresses as a starting point, and uses the Census geocoding API (which also pulls in FIPS codes as well as census tract numbers) and the Google maps geocoding API to fill in missing coordinates. The notebook adds an indicator column showing whether the given facility closed down or is still active (there is a third indicator that represents facilities that scaled down operations, usually axing their inpatient care and remaining open as a strictly outpatient facility). It also fills in missing RUCA (Rural-Urban Commuting Area code) values, which are a way to designate rural vs urban locations using a crosswalk downloaded from the USDA here (available in the repo under data/RUCA-codes-2020-zipcode.xlsx): https://www.ers.usda.gov/media/5444/2020-rural-urban-commuting-area-codes-zip-codes.csv?v=32139. Missing census tracts were filled in via a spatial join using IPUMS census tract shapefiles (downloaded from here: https://usa.ipums.org/usa-action/data_requests/download) for US states, and using individual US census tigerline shapefiles (downloaded from here: https://www.census.gov/cgi-bin/geo/shapefiles/index.php?year=2025&layergroup=Census+Tracts) for US territories. It then narrows down the hospitals of interest to just rural acute care hospitals using census tract code. The “rural” designation is based on the Federal Office of Rural Health Policy's (FORHP) definition of a rural area. (crosswalk available at data/rural-health-areas-data-set.xlsx; downloaded from here: https://www.hrsa.gov/sites/default/files/hrsa/rural-health/about/rural-health-areas-data-set.xlsx). It then merges in CBSA (Core-Based Statistical Area) data for each hospital using this FIPS-CBSA crosswalk (saved in the repository as data/cbsa2fipsxw_2023.csv): https://www.nber.org/research/data/census-core-based-statistical-area-cbsa-federal-information-processing-series-fips-county-crosswalk (FIPS information had to be added manually for Guam and Northern Mariana Islands. Source: https://maps.redcross.org/website/Maps/Images/CNMI/guam_cnty.pdf). Finally, some missing CCNs are filled in using information from the American Hospital Directory (https://www.ahd.com/). NPI numbers are also added, using the following crosswalk from the National Bureau of Economic Research (available in the repository at data/npi_medicarexw.csv): https://www.nber.org/research/data/national-provider-identifier-npi-medicare-ccn-crosswalk. The notebook will output hospitals_master.csv, a canonical table containing identifying information as well as the closure status for each hospital in scope for this project.

    </details>

    <details>
    <summary>Gathering Yearly Hospital Data</summary>
  
    Then, run “notebooks/Financial Report Data Gathering Notebook.ipynb”. This notebook is almost exactly identical to the “generate_main_df.ipynb” sourced from this GitHub repository: https://github.com/klocey/HCRIS-databuilder, which is meant to democratize access to the large, complex hospital financial data files from the Centers for Medicare and Medicaid Services (CMS) Healthcare Cost Report Information System (HCRIS). The one enhancement made was to narrow down to just the hospitals in scope for this project before processing the HCRIS data (this was done by pulling the CCNs from hospitals_master.csv and comparing them against the “prvdr_num” column in the HCRIS dataset). The notebook outputs a file called “data/HCRIS_filtered.csv”, containing financial data related to the hospitals of interest for this project from fiscal year 2010 onward.
    
    After that, run the “hospital-compare-master/process_hospital_compare_data.py” script in order to produce the processed CMS Hospital Compare data. This script was heavily influenced by the “process.do” file in the following GitHub repo: https://github.com/asacarny/hospital-compare/. The python script requires the raw CMS Hospital Compare data to be present in the “hospital-compare-master/source” directory (these can be downloaded from the National Bureau of Economic Research here: https://www.nber.org/research/data/centers-medicare-medicaid-services-cms-hospital-compare-data). The script should output 3 files in the “hospital-compare-master/output” directory: poc.csv, hcahps.csv, and mortreadm.csv. These contain information about Process of Care Scores (Shares of patients receiving evidence-based treatments for heart attacks, congestive heart failure, pneumonia, surgical care, and outpatient care for all patients), HCAHPS scores (Average scores for the aggregated questions in HCAHPS patient satisfaction survey for all patients) and mortality and readmission statistics (Estimates of heart attack, congestive heart failure, and pneumonia mortality and readmission rates for Medicare FFS patients only), respectively. 
    
    Next, run “notebooks/ARHF Exploration”, which parses AHRF (Area Health Resource File) data (available for download from the HRSA (Health Resources and Service Administration) website here: https://data.hrsa.gov/data/download). The notebook relies on a parser tool included in the following GitHub repo: https://github.com/adityanagara/AHRF_project, which parses and formats older AHRF datasets which are only available in ASCII format. The notebook extracts particular columns of interest in the categories of hospital utilization, demographics, and medical resources at the county level for the years that this project focuses on (2010-2025). The notebook saves this data to “data/ARHF_Full.csv”

    </details>

    <details>
    <summary>Data Aggregation and Cleaning</summary>
  
  Finally, run “notebooks/Hospital Trends Data Gathering” to aggregate hospital financial data, quality data, and Area Health Resource data together. It first merges “data/hospitals_master.csv” with “/data/HCRIS_databuilder/filtered_datasets/HCRIS_filtered.csv”, performing several data cleanup steps before merging in the other datasets. This includes things like validating the dataset has a single row per hospital per year (which led to reconciling duplicate cost reports) and making sure that we retain rows for hospital-years that are missing from the financial dataset, so that we can interpolate those missing values later. This notebook also adds 2 columns which will be used as the target columns in the predictive model; the Status column is a boolean indicator representing whether or not the given hospital closed or converted operations in that year, and the Time column represents the number of years of data the dataset contains for the given hospital. Then the notebook merges in the hospital quality and AHRF data, using year and CCN as the merge keys. Finally, all monetary values were converted to 2025 purchasing power using the Consumer Price Index so that they can be appropriately compared (Annual CPI values can be downloaded here: https://data.bls.gov/timeseries/CUUR0000SA0). The notebook exports the full dataset as “data/hospitals_full.csv”). 
    </details>


* If you are interested in viewing the technical details of the machine learning model, check out the "Modeling Hospital Closures" notebook and the "Model Interpretability and Explainability" notebook (both in the notebooks folder).

* If you are interested in exploring the accompanying Streamlit application, which contains background information on the project, details about the model, an interactive dashboard for generating model predictions, and project conclusions - download this repository and run "streamlit run ./apps/Introduction.py" from the root of the repo. The application is also published on Streamlit Community Cloud at https://predictingruralhospitalclosuresmlmodel.streamlit.app/. 

### Data Sources:

* The Centers for Medicare & Medicaid Services (CMS) Healthcare Cost Report Information System (HCRIS) includes annual cost reports containing revenue, costs, facility characteristics, utilization data, and financial statements.

* **Area Health Resource Data** was sourced from Area Health Resources Files, which are made available via the US Health Resources and Services Administration's Data Warehouse.
    * This dataset provides current as well as historic data for more than 6,000 variables for each of the nation's counties, as well as state and national data. It contains information on health facilities, health professions, measures of resource scarcity, health status, economic activity, health training programs, and socioeconomic and environmental characteristics.
    * County-level ARHF data was associated with each rural hospital in this project.

* **Hospital quality data** comes from the Centers for Medicare & Medicaid Services' Provider Data Catalog, which contains hospital quality ratings and compliance data.
    * This data includes Process of Care Scores (shares of patients receiving evidence-based treatments for AMI, CHF, pneumonia, surgical care, and outpatient care), Hospital Consumer Assessment of Healthcare Providers and Systems/HCAHPS (average scores for the aggregated questions in HCAHPS patient satisfaction survey), and mortality/readmission data (estimates of AMI, CHF, and pneumonia mortality and readmission rates).
*  The **Sheps Center Rural Hospital Closures Database** (from the North Carolina Rural Health Research Program) contains data on rural hospital closures and conversions since 2005. 
    * The Cecil G. Sheps Center for Health Services Research seeks to improve the health of individuals, families, and populations by understanding the problems, issues and alternatives in the design and delivery of health care services.

### Conclusions 

* **Hospital ownership structure** is the largest driver of closure risk, with high coefficient magnitudes and high permutation feature importances. 
* A hospital being structured as a **Voluntary Non-Profit - Private** hospital - owned by independent, secular community organizations or private foundations rather than a government entity or corporate shareholders - provides a large protective effect.
* On the other hand, a hospital operating as a **Voluntary Non-Profit - Other** facility - indicating it is owned by specific non-community groups, such as religious orders, universities, or a distinct not-for-profit corporation - increases risk of closure.

##### Financial Metrics
            
* Hospital financial metrics such as **debt ratio** and **equity ratio** affect a hospital's risk of closure (in opposite directions), but typically not to a high degree. 
* **Debt ratio** measures the proportion of a hospital's assets that are financed by debt. A higher debt ratio may indicate greater financial leverage and, potentially, higher financial risk.
* **Equity ratio** shows the proportion of assets financed by equity, representing the financial stability of the hospital. A higher ratio generally means a stronger financial position with less reliance on debt.
* **Total adjusted salaries** also appeared as an influential feature based on a positive permutation importance score and a relatively large mean SHAP score, but did not end up with a non-zero coefficient due to the amount of regularization imposed.
* No other hospital financial metrics emerged as important features to the model.

##### AHRF Features

* **Area Health Resource** features are a more complicated picture. Distribution of area hospitals that have a **very low average bed occupancy (0% - 39%)**, typically indicative of regions with underutilized or financially fragile hospital infrastructure, lowers the overall risk score but has a negative permutation importance score, so might not be relevant.
* **Short Term General Hospital Admissions** represent the strongest protective effect against closure based on the coefficient magnitude, as well as a high permutation importance score and mean SHAP score. This suggests that rural hospitals in counties with consistently utilized hospital infrastructure are more likely to be long-lasting.
* **Total Active D.O.s (Doctors of Osteopathic Medicine)** increases closure risk score; this could reflects a workforce more focused on primary care than specialized inpatient medicine that typically generates more revenue.

##### Hospital Quality Metrics

* No hospital quality metrics, such as patient satisfaction survey scores or mortality and readmission metrics, emerged as important features to the model. 

### Limitations
* The **Rural Emergency Hospital (REH)** Medicare provider designation became effective on January 1, 2023. 
This designation was created explicitly to help prevent rural hospital closures by providing enhanced, fixed monthly facility payments from Medicare, among other benefits.

* This event may have skewed the test data in this project, as there were likely some hospitals in our dataset that converted to Rural Emergency Hospitals (not marked as a closure/conversion in our dataset) that would have closed without the REH option.
This potentially invalidates the Proportional Hazards Assumption of Cox Regression models, which holds that the effect of the predictor variables on the hazard function must be constant over time. 


### Future Directions
* More robust analysis can be done to test that the assumptions of a Cox Regression model are met. 

* In addition, more work can be done to convert risk scores to probabilities, which would serve as a more straightforward decision support metric. Model calibration would need to be verified beforehand.
