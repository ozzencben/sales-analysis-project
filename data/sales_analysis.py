import os.path
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Ay": ["JUN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"],
    "Food": [15000, 18000, 17000, 16000, 20000, 21000, 22000, 23000, 19000, 17500, 16500, 18000],
    "Clothes": [7000, 7500, 8200, 7800, 8300, 8500, 9000, 8700, 8000, 7700, 7600, 8000],
    "Electronic": [12000, 11000, 13000, 12500, 14000, 15000, 16000, 15500, 14500, 13500, 13000, 14000]
}

dataframe = pd.DataFrame(data)
folder_path = "C:/Python/sales-analysis-project/data/sales_data.csv"

if not os.path.exists((folder_path)):
    dataframe.to_csv("C:/Python/sales-analysis-project/data/sales_data.csv", index=False, encoding="utf-8-sig")
    print("CSV folder is created")

dataframe = pd.read_csv(folder_path)

dataframe["Total"] = dataframe["Food"] + dataframe["Clothes"] + dataframe["Electronic"]
most_sales_mount = dataframe[dataframe["Total"] == dataframe["Total"].max()]

plt .figure(figsize=(10,6))
plt.bar(dataframe["Ay"], dataframe["Total"], color="coral")
plt.title("Montly Total Sales")
plt.xlabel("Month")
plt.ylabel("Total Sales (TL)")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()