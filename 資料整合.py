import pandas as pd
import numpy as np

"""
參考步驟
"""
# 讀取交通事故資料
accident_data = pd.read_csv("accident_data.csv")

# 讀取道路施工資料
construction_data = pd.read_csv("construction_data.csv")

# 以事件編號為關聯欄位，合併兩個資料集
merged_data = pd.merge(accident_data, construction_data, on="事件編號", how="inner")

# 顯示合併後的資料
print(merged_data.head())