import pandas as pd
import matplotlib.pyplot as plt

folder_path = "C:/Python/sales-analysis-project/data/sales_data.csv"
df = pd.read_csv(folder_path, encoding="utf-8-sig")

category_total = df[["Food", "Clothes", "Electronic"]].sum()

plt.figure(figsize=(8,6))
plt.pie(category_total, labels=category_total.index, autopct="%1.1f%%", startangle=90)
plt.title("Total Sales Distribution by Product Categories")
plt.axis("equal")
plt.tight_layout()
plt.show()

