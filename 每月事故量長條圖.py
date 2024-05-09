import pandas as pd
import matplotlib.pyplot as plt

# 設定中文字型
plt.rc('font', family='Microsoft JhengHei')

# 讀取資料集
accidents_df = pd.read_csv("accident.csv")

# 計算每月的事故次數
accidents_count = accidents_df["月"].value_counts()

# 根據月份進行排序
accidents_count = accidents_count.sort_index()

# 繪製長條圖
plt.figure(figsize=(10, 6))
accidents_count.plot(kind="bar", color="skyblue")
plt.title("112年1-10月每月事故量長條圖")
plt.xlabel("月份")
plt.ylabel("事故次數")

# 設定 x 軸刻度為排序後的月份
plt.xticks(range(len(accidents_count)), accidents_count.index, rotation=45)

# 在每個條形上方添加數字標籤
for i, v in enumerate(accidents_count):
    plt.text(i, v + 1, str(v), ha='center', va='bottom')

plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.2)

plt.savefig("112年1-10月每月事故量長條圖.png")
plt.show()