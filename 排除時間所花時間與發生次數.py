import pandas as pd
import matplotlib.pyplot as plt

# 設定中文字型
plt.rc('font', family='Microsoft JhengHei')

# 讀取原始交通事故資料
accident_data = pd.read_csv("accident_data.csv")

# 將年、月、日、時、分合併成日期時間欄位
accident_data['日期時間'] = accident_data['年'].astype(str) + '/' + accident_data['月'].astype(str) + '/' + accident_data['日'].astype(str) + ' ' + accident_data['時'].astype(str) + ':' + accident_data['分'].astype(str)

# 檢查是否為00:00時間格式，若不是則嘗試轉換成00:00時間格式
accident_data['事件排除'] = accident_data['事件排除'].apply(lambda x: '00:00' if len(x) < 5 else x)
accident_data['事件發生'] = accident_data['事件發生'].apply(lambda x: '00:00' if len(x) < 5 else x)

# 檢查 "事件發生" 欄位中的資料格式，並對不符合 "%H:%M" 格式的資料進行處理
accident_data['事件發生'] = accident_data['事件發生'].apply(lambda x: '00' + x if x.startswith(':') else x)

# 將 ";" 替換為 ":"，然後將 "事件發生" 和 "事件排除" 轉換為分鐘數
accident_data['事件發生'] = accident_data['事件發生'].str.replace(';', ':').apply(lambda x: int(x.split(':')[0]) * 60 + int(x.split(':')[1]))
accident_data['事件排除'] = accident_data['事件排除'].str.replace(';', ':').apply(lambda x: int(x.split(':')[0]) * 60 + int(x.split(':')[1]))

# 計算 "事件排除" 和 "事件發生" 的時間差，並將結果轉換為一個整數表示的分鐘數
# 如果 "事件排除" 的時間小於 "事件發生" 的時間，則加上一天
accident_data['事件排除所花時間'] = accident_data['事件排除'] - accident_data['事件發生']
accident_data.loc[accident_data['事件排除所花時間'] < 0, '事件排除所花時間'] += 24 * 60

# 顯示整合後的資料
# print(accident_data[['日期時間', '事件排除所花時間']].head())

# 以排除時間所花時間與發生次數做一張長條圖
# 以5分鐘為間隔
# x 軸為排除時間所花時間 (分鐘) ex. 0-5, 5-10, 10-15, ...
# 在每個條形上方添加數字標籤
# 將超過100分鐘的資料合併為100分鐘以上
# y 軸為發生次數
accident_data['事件排除所花時間'] = accident_data['事件排除所花時間'].apply(lambda x: 100 if x > 100 else x // 5 * 5)
accident_data['事件排除所花時間'].value_counts().sort_index().plot(kind='bar', color='skyblue')
plt.title("排除時間所花時間與發生次數(5分鐘為間隔)(100分鐘以上合併)")
plt.xlabel("排除時間所花時間 (分鐘)")
plt.ylabel("發生次數")
plt.xticks(rotation=0)
for i, v in enumerate(accident_data['事件排除所花時間'].value_counts().sort_index()):
    plt.text(i, v + 1, str(v), ha='center', va='bottom')
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.2)
# plt.savefig("排除時間所花時間與發生次數.png")
plt.show()

# 生成新的excel檔案
# 不包含原本的年月日時分時間欄位、事件發生欄位、事件排除欄位
# accident_data.drop(columns=['年', '月', '日', '時', '分', '事件發生', '事件排除']).to_excel("accident_data_new.xlsx", index=False)