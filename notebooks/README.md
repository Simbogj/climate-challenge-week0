# Climate Analysis Notebooks

This directory contains the Exploratory Data Analysis (EDA) and Cross-Country Comparison notebooks for the African Climate Trend Analysis project.

## EDA Notebooks
Each notebook focuses on a specific country, performing data cleaning, sentinel value replacement (-999), outlier detection, and visualization of climate trends (2015–2026).

- [ethiopia_eda.ipynb](ethiopia_eda.ipynb): Ethiopia analysis.
- [kenya_eda.ipynb](kenya_eda.ipynb): Kenya analysis.
- [sudan_eda.ipynb](sudan_eda.ipynb): Sudan analysis.
- [tanzania_eda.ipynb](tanzania_eda.ipynb): Tanzania analysis.
- [nigeria_eda.ipynb](nigeria_eda.ipynb): Nigeria analysis.

## Comparison Notebook
- [compare_countries.ipynb](compare_countries.ipynb): Synthesizes cleaned data from all five countries to identify relative vulnerabilities and extreme heat/precipitation trends for COP32.

## How to use
1. Place raw CSV datasets in the `data/` directory.
2. Run each country EDA notebook to generate cleaned `*_clean.csv` files.
3. Run the `compare_countries.ipynb` once all cleaned files are generated.
