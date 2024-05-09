import pandas as pd
import matplotlib.pyplot as plt

"""
這段程式碼會讀取名為 "accident.csv" 的資料集，並計算每條國道的事故次數。
接著，使用長條圖來呈現每條國道的事故次數。
"""

# 設定中文字型
plt.rc('font', family='Microsoft JhengHei')

# 讀取名為 "accident.csv" 的資料集
accidents_df = pd.read_csv("accident.csv")

# 計算每條國道的事故次數
accidents_count = accidents_df["國道名稱"].value_counts()

# 繪製條形圖
plt.figure(figsize=(10, 6))
accidents_count.plot(kind="bar", color="skyblue")
plt.title("112年1-10月每條國道事故次數長條圖")
plt.xlabel("國道號")
plt.ylabel("事故次數")
plt.xticks(rotation=45)

# 調整 x 軸範圍
plt.xlim(-0.5, len(accidents_count)-0.5)

# 調整 y 軸範圍
plt.ylim(0, max(accidents_count) * 1.1)

# 調整圖表邊緣
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.2)

# 在每個條形上方添加數字標籤
for i, v in enumerate(accidents_count):
    plt.text(i, v + 1, str(v), ha='center', va='bottom')

plt.savefig("112年1-10月每條國道事故次數長條圖.png")
plt.show()