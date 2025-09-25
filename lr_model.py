import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

df = pd.read_csv(r"C:\Users\nwjoy\OneDrive\Documents\SkillCraft\SCT-1\cleaned_houses.csv")

X = df[["GrLivArea", "BedroomAbvGr", "FullBath"]]
y = df["SalePrice"]

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "house_price_model.pkl")
