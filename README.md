# Housing Price Prediction

A machine learning project to predict house prices using **Linear Regression**, wrapped in a **Streamlit web app** for an interactive user interface.

---
## Features
- Train a Linear Regression model on housing data  
- Save and load the trained model (`house_price_model.pkl`)  
- Interactive **Streamlit UI** for making predictions  
- Lightweight and easy to run locally  

---
## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/joysonnw/SCT_ML_1.git
   cd SCT_ML_1
   ```
2. Install dependencies:

   ```bash
   pip install numpy pandas scikit-learn streamlit
   ```
3. Usage
   
Train the Model by Running the training script to fit the model and save it as house_price_model.pkl:

   ```bash
   python lr_model.py
   ````
Launch the Streamlit App
   ```bash
    streamlit run simple_gui.py
   ```
This will start a local server.

---
## Data
Dataset: cleaned_houses.csv (cleaned dataset (i.e. missing values addressed, features normalized or engineered, etc.))
