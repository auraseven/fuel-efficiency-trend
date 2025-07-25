
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import os

# Create output directory if not exist
os.makedirs("images", exist_ok=True)

# Load the dataset
df = pd.read_csv("aircraft_data.csv")

# Encode the categorical 'Engine Type' column
df_encoded = pd.get_dummies(df, columns=["Engine Type"], drop_first=True)

# Define features (X) and target (y)
X = df_encoded.drop(["Aircraft", "Fuel Burn (L/passenger/100km)"], axis=1)
y = df_encoded["Fuel Burn (L/passenger/100km)"]

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train the model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.3f}")

# Plot actual vs predicted values
plt.figure(figsize=(6, 4))
plt.scatter(y_test, y_pred, color='blue')
plt.xlabel("Actual Fuel Burn")
plt.ylabel("Predicted Fuel Burn")
plt.title("Fuel Burn Prediction Accuracy")
plt.grid(True)
plt.savefig("images/prediction_plot.png")
plt.show()

# Feature importance
print("\nFeature Importances:")
importances = model.feature_importances_
for name, score in zip(X.columns, importances):
    print(f"{name}: {score:.2f}")
