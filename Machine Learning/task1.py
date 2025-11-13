# -------------------------------
# 🏠 Linear Regression for House Price Prediction
# Using features: GrLivArea, BedroomAbvGr, FullBath
# -------------------------------

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import seaborn as sns
import matplotlib.pyplot as plt

# 1️⃣ Load Excel data
# Replace with your actual file name
df = pd.read_excel('train.xlsx', engine='openpyxl')

# 2️⃣ Select relevant columns
data = df[['GrLivArea', 'BedroomAbvGr', 'FullBath', 'SalePrice']]

# 3️⃣ Handle missing values
data = data.dropna()

# 4️⃣ Define features (X) and target (y)
X = data[['GrLivArea', 'BedroomAbvGr', 'FullBath']]
y = data['SalePrice']

# 5️⃣ Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 6️⃣ Create and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# 7️⃣ Make predictions
y_pred = model.predict(X_test)

# 8️⃣ Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("✅ Linear Regression Model Results")
print("----------------------------------")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R² Score: {r2:.4f}")

# 9️⃣ Example: Predict a new house price
# Example values → [GrLivArea, BedroomAbvGr, FullBath]
new_house = [[2000, 3, 2]]
predicted_price = model.predict(new_house)
print(f"\n💰 Predicted Price for a new house (2000 sqft, 3 bed, 2 bath): ${predicted_price[0]:,.2f}")

# 🔟 Show correlation heatmap
plt.figure(figsize=(6,4))
sns.heatmap(data.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap with SalePrice")
plt.show()
