import matplotlib.pyplot as plt
import matplotlib as mpl

plt.rcParams['font.family'] = 'Noto Sans CJK JP'

mpl.rcParams['axes.unicode_minus'] = False



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import numpy as np

df = pd.read_csv("hotel_simplified.csv")

def extract_score(text):
    match = re.search(r'(\d\.\d+)', str(text))
    return float(match.group(1)) if match else np.nan

def extract_discount(text):
    match = re.search(r'(\d+)%', str(text))
    return int(match.group(1)) if match else 0

def extract_price(text):
    match = re.search(r'(\d{1,3}(,\d{3})*)円', str(text))
    if match:
        price_str = match.group(1).replace(',', '')
        return int(price_str)
    return np.nan

df["スコア"] = df["Like12"].apply(extract_score)
df["割引%"] = df["justifycenter"].apply(extract_discount)
df["価格（円）"] = df["textgray80016"].apply(extract_price)
hotel_names = df["タイトル"]

plt.figure(figsize=(12, 6))
sns.barplot(x=df["スコア"], y=hotel_names, palette="coolwarm")
plt.title("ホテルごとのスコア")
plt.xlabel("スコア")
plt.ylabel("ホテル名")
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
sns.barplot(x=df["割引%"], y=hotel_names, palette="YlGnBu")
plt.title("ホテルごとの割引率（%）")
plt.xlabel("割引率（%）")
plt.ylabel("ホテル名")
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
sns.barplot(x=df["価格（円）"], y=hotel_names, palette="OrRd")
plt.title("ホテルごとの最低価格（円）")
plt.xlabel("価格（円）")
plt.ylabel("ホテル名")
plt.tight_layout()
plt.show()
