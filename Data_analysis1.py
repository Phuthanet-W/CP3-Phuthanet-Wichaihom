import pandas as pd

df = pd.read_csv("IMDb movies.csv", encoding="utf-8")
title_principals = pd.read_csv("IMDb title_principals.csv", encoding="utf-8")

a = df[df['genre'].apply(lambda member: 'Action' in member)]
#apply function ในการหาคำว่า Action ใน column genre

b = a.merge(title_principals, how='inner', left_on='imdb_title_id',right_on='imdb_title_id')
#merge file 2 (file a กับ title_principals)อันโดยอ้างอิงจาก data ใน column ที่เหมือนกัน

c = b[b['category'].isin(['actor','actress'])]
#การกรอง data in column name'category' โดยหา row ที่เป็น actor and actress
#โดยใน code: b['category'].isin(['actor','actress']) >> result will be boolean (true/false) 
#เราจะต้องคืนค่ากลับมาเป็น data เดิม ด้วยการเพิ่ม b อีกอันเป็น b[b['category'].isin(['actor','actress'])]

IMDb_names = pd.read_csv("IMDb names.csv", encoding="utf-8")

d = c.merge(IMDb_names, how='inner', left_on='imdb_name_id', right_on='imdb_name_id')[['imdb_name_id','name']].drop_duplicates()
#รวมตาราง c กับ IMDb names 
#ใส่ code: [['imdb_name_id','name']] เพื่อให้แสดงแค่ column imdb_name_id กับ name เท่านั้น
#และตัดข้อความซ้ำด้วย .drop_duplicates()

df['genre'] = df['genre'].apply(lambda m: m.split(', '))
#apply function split เพื่อแยก string ที่มีหลายข้อความใน cell เดียวและคั่นด้วย ', ' ใน column 'genre'
#eeee=e.explode('genre') 
#หลังจาก split แล้วเราจะให้ data ใน cell แยก row กัน ด้วยคำสั้ง explode

ff = df.explode('genre')
gg = ff.groupby('genre')['votes'].sum().nlargest(10)


print(gg)
#ff.to_csv("fsdfsdafsdfs.csv")