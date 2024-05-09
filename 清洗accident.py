import pandas as pd

"""
清洗原始的交通事故資料
生成一個新的CSV檔案
"""

# 讀取原始交通事故資料
accident_data = pd.read_csv("accident_data.csv")

# 將年、月、日、時、分合併成日期時間欄位
accident_data['日期時間'] = accident_data['年'].astype(str) + '/' + accident_data['月'].astype(str) + '/' + accident_data['日'].astype(str) + ' ' + accident_data['時'].astype(str) + ':' + accident_data['分'].astype(str)

# 顯示整合後的資料
print(accident_data[['年', '月', '日', '時', '分', '日期時間']].head())