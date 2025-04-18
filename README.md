# 📊 Amazon Sales Dashboard

This is an interactive sales analysis dashboard built with **Streamlit** and **Plotly**, designed to analyze Amazon product sales, forecast trends, and visualize business insights.

---

## 🚀 Features

- 📈 **Yearly Sales by Product**  
  View year-wise sales for selected products with color-coded insights.

- 📦 **Probability of Sales (2016)**  
  Estimate and calculate the probability of a product's 2016 sales based on its 2014 & 2015 sales.

- 💰 **Top 5 Most Profitable Products**  
  Visualize the top profit-generating products across all categories.

- 🔮 **Sales Forecasting**  
  Predict future sales using a linear regression model.

---

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Visualization**: [Plotly Express](https://plotly.com/python/plotly-express/), [Plotly Graph Objects](https://plotly.com/python/graph-objects/)
- **Machine Learning**: `LinearRegression` from `scikit-learn`
- **Data Handling**: `Pandas`, `NumPy`

---

## 📁 Dataset

The app uses a cleaned version of the Amazon Sales dataset from Kaggle:

📎 **Dataset Link**: [Amazon Sales Dataset on Kaggle](https://www.kaggle.com/datasets/karkavelrajaj/amazon-sales-dataset)

---

## ▶️ How to Run

1. **Clone the repository**

```bash
git clone https://github.com/your-username/amazon-sales-dashboard.git
cd amazon-sales-dashboard
```
2. **Install dependencies**

```bash
pip install -r requirements.txt
```
3. **Install dependencies**

```bash
pip install streamlit pandas plotly scikit-learn numpy
```
4. **Run the app**

```bash
streamlit run app.py
```
## 📸 Screenshots

![image](https://github.com/user-attachments/assets/c03e7b4b-5748-4bd5-a6d4-69df57d1bc8b)
![image](https://github.com/user-attachments/assets/a6cc3c3b-6cd9-4b69-90f3-44a78125fe6b)
![image](https://github.com/user-attachments/assets/b6bb6197-1a74-4f4a-a52d-98ff9278ccfb)
![image](https://github.com/user-attachments/assets/290cfcda-d432-48a9-9ee9-04a165a98151)



## 💡 Future Improvements

- **Review sentiment analysis**
  
- **Advanced forecasting (ARIMA, Prophet)**
  
- **CSV/PDF download reports**
  
- **Deploy to Streamlit Cloud**

## 👨‍💻 Author

- **Medha Avhad (23101B2004)**
- **Chinmayee Deshmukh (23101B2006)**
- **Aishwarya Huddar (23101B2008)**
