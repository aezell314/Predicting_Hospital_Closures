# Predicting US Hospital and Clinic Closures

This project combines financial health, operational metrics, and local demographic data to predict the likelihood that a rural US acute care hospital will close within the next 5 or 10 years. I'll use XGBoost or Random Forest to analyze 5- and 10-year longitudinal data, looking at features including operating margins, patient volume, ownership structure (for-profit vs. non-profit), and regional population changes. 

Key datasets:

1. Core Hospital Financial & Operational Data (CMS) \
The Centers for Medicare & Medicaid Services (CMS) provides the most comprehensive data on hospital financial health.
CMS Healthcare Cost Report Information System (HCRIS): This is the definitive source. It includes annual cost reports, containing revenue, costs, facility characteristics, utilization data, and financial statements organized by CMS Certification Number (CCN).

AHRQ Hospital Financial Measures Database (HFMD): Created by the Agency for Healthcare Research and Quality, this database contains measures of profitability, liquidity, and capital structure specifically for short-term acute care hospitals, covering 2016–2019. 
Provider Data Catalog / Care Compare: Contains hospital quality ratings and compliance data, which can serve as indicators of operational issues. 

3. Hospital Closure & Regional Data (Government & Academic)
Sheps Center Rural Hospital Closures Database: The definitive list of rural hospital closures and conversions (stop-start inpatient services) since 2005. Helpful for labeling the target variable (closure). 
HRSA Area Health Resources Files (AHRF): A comprehensive county-level database covering health professions, health facilities, population demographics, economics, and utilization. 
USDA Rural Economy & Population Data: Useful for finding socioeconomic factors that contribute to regional healthcare failure. 

4. Alternative/Complementary Data Sources
IRS Form 990 (Non-profit data): Nonprofit hospitals must file Form 990, which contains detailed financial information and can be retrieved through platforms like ProPublica’s Nonprofit Explorer.
RAND Hospital Price Transparency Study: Offers insights into hospital pricing relative to Medicare rates.
Electronic Municipal Market Access (EMMA): Provides audited financial statements for hospitals that issue municipal debt. 

Initial plan:
Target: Create a binary column to indicate closure within 5 (or 10) years using the Sheps Center data.
Feature Engineering:
-Calculate operating margin, total margin, and debt-to-equity ratio from HCRIS data.
-Use 5-10 years of prior data to calculate year-over-year changes.
-Include population density, median income, and uninsured rate from AHRF. 
-Will use XGBoost, Random Forest, or Logistic Regression. 
-Will likely need to handle high class imbalance (many more open hospitals than closed) using something like SMOTE or undersampling
