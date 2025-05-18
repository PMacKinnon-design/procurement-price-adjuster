# 📈 Procurement Price Adjuster

The **Procurement Price Adjuster** is a lightweight Streamlit web app that helps procurement teams adjust historical prices paid for goods and services to present-day values using Consumer Price Index (CPI) data.

This tool is ideal for sourcing professionals, analysts, and procurement consultants who want to:

- Normalize past purchase data for year-over-year comparisons
- Understand inflationary impact on spend
- Support should-cost modeling and budget forecasting

---

## 🚀 Features

- 📤 Upload CSV with historical procurement data  
- 🧠 Adjust prices using static CPI (2025 estimate)  
- 📊 View original vs. adjusted prices and % change  
- 📥 Download results as a CSV  

---

## 🛠️ File Upload Format

Your CSV should look like this:

| Item | Purchase Date | Price | Category |
|------|----------------|--------|----------|
| Steel Beam | 2018-01-01 | 120.00 | Metals |

- **Purchase Date** must be in `YYYY-MM-DD` format
- **Price** should be numeric

---

## 📦 Requirements

- Python 3.8+
- Streamlit
- Pandas
- Requests
- Matplotlib

Install with:
```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run Locally

1. Clone the repo:
```bash
git clone https://github.com/YOUR_USERNAME/procurement-price-adjuster.git
cd procurement-price-adjuster
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the Streamlit app:
```bash
streamlit run app.py
```

---

## 🌐 Deployment (Streamlit Cloud)

You can deploy the app for free at [https://share.streamlit.io](https://share.streamlit.io) by linking this GitHub repo.

---

## 📌 Roadmap

- ✅ V1: CPI-based price adjustment
- 🔜 V2: Live CPI from FRED API
- 🔜 V3: Category-based commodity inflation
- 🔜 V4: FX rate adjustments and visual dashboards

---

## 📄 License

MIT License – See `LICENSE` file for details

---

## 🤝 Contact

Developed by MacKinnon Consulting  
Website: [www.mackinnonconsulting.com](https://www.mackinnonconsulting.com)

For questions or contributions, please open an issue or email us.