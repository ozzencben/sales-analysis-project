import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import os

os.makedirs("figures", exist_ok=True)


folder_path = "C:/Python/sales-analysis-project/data/sales_data.csv"
df = pd.read_csv(folder_path)

if "Total" not in df.columns:
    df["Total"] = df[["Food", "Clothes", "Electronic"]].sum(axis=1)

with PdfPages("figures/sales_report.pdf") as pdf:

    plt.figure(figsize=(10,5))
    plt.bar(df["Ay"], df["Total"], color="skyblue")
    plt.title("Montly Total Sales")
    plt.xlabel("Month")
    plt.ylabel("Sales amount")
    plt.tight_layout()
    pdf.savefig()
    plt.close()

    category_totals = df[["Food", "Clothes", "Electronic"]].sum()
    plt.figure(figsize=(6, 6))
    plt.pie(category_totals, labels=category_totals.index, autopct="%1.1f%%", startangle=90)
    plt.title("Sales Distribution by Category")
    plt.tight_layout()
    pdf.savefig()
    plt.close()

print("PDF folder is created: figures/sales_report.pdf")