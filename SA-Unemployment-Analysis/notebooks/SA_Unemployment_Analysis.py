import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -----------------------------
# Step 1: Define path to CSV
# -----------------------------
# Portable version: works relative to the Python file
current_dir = os.path.dirname(__file__)  # folder of this script
data_path = os.path.join(current_dir, '..', 'data', 'sa_unemployment.csv')

# If this fails, you can use absolute path as a backup:
# data_path = r"C:\Users\princ\Desktop\SA-Unemployment-Analysis\data\sa_unemployment.csv"

# -----------------------------
# Step 2: Load the dataset
# -----------------------------
df = pd.read_csv(data_path)

# -----------------------------
# Step 3: Explore the data
# -----------------------------
print("First 5 rows of the dataset:")
print(df.head())

print("\nData Info:")
print(df.info())

print("\nData Statistics:")
print(df.describe())

# -----------------------------
# Step 4: Generate line chart
# -----------------------------
plt.figure(figsize=(10,6))
sns.lineplot(data=df, x='Year', y='Unemployment_Rate', marker='o')
plt.title('South Africa Unemployment Rate Over Years')
plt.xlabel('Year')
plt.ylabel('Unemployment Rate (%)')
plt.grid(True)

# -----------------------------
# Step 5: Save chart
# -----------------------------
# Save in images folder
images_dir = os.path.join(current_dir, '..', 'images')
os.makedirs(images_dir, exist_ok=True)  # make folder if it doesn't exist
plt.savefig(os.path.join(images_dir, 'unemployment_trend.png'))

# Show the chart
plt.show()