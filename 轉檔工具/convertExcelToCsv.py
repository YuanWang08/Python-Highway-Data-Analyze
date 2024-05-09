import pandas as pd

"""
在這段程式碼中，你需要將 your_excel_file.xlsx 替換成你想要轉換的Excel檔案路徑
程式會讀取該Excel檔案並將其儲存為 output_csv_file.csv 的CSV檔案。
"""

# 讀取 Excel 檔案
excel_file = '112年1-10月道路施工路段資料.xlsx'
df = pd.read_excel(excel_file)

# 寫入 CSV 檔案
csv_file = 'output_csv_file.csv'
df.to_csv(csv_file, index=False)

print(f'{excel_file} 已成功轉換成 {csv_file}')