# African Climate Trend Analysis

##  Overview

This project analyzes historical climate data (2015–2026) for five African countries — Ethiopia, Kenya, Sudan, Tanzania, and Nigeria — using data from the NASA POWER database.
The goal is to identify climate trends, variability, and extreme events to support data-driven insights for climate policy discussions ahead of COP32.

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone <https://github.com/Simbogj/climate-challenge-week0.git>
cd climate-challenge-week0
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Project Structure

```
├── notebooks/        # EDA notebooks per country
├── src/              # reusable scripts
├── scripts/          # helper scripts
├── tests/            # test files
├── data/             # local datasets (ignored in Git)
├── requirements.txt
└── README.md
```

---

## Key Tasks

* Data cleaning and preprocessing
* Exploratory Data Analysis (EDA)
* Cross-country climate comparison
* Climate vulnerability ranking
* (Optional) Streamlit dashboard

---

## How to Run

* Open notebooks in the `notebooks/` folder to explore analysis
* Run Python scripts from `src/` if available

---

## Notes

* Dataset is excluded from GitHub (`data/` is in `.gitignore`)
* Missing values (`-999`) are handled during preprocessing

---

## Author

Simbo Getachew
