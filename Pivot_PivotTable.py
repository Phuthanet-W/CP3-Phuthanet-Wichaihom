import pandas as pd

movies_df = pd.read_csv('IMDb movies.csv', dtype={'year':int})

select_new_movies = movies_df[movies_df['year'] >= 2016]

select_new_movies = select_new_movies[select_new_movies['budget'].notna() 
& select_new_movies['worlwide_gross_income'].notna()][['imdb_title_id', 'budget', 'worlwide_gross_income']]

filter_movies = select_new_movies['budget'].str.slice(stop=1)
#code in row10 เป็นการแสดงอักษรตัวแรกสุดของ data ใน column budget ทั้งหมด ด้วยคำสั่ง slice(stop=1) ถ้าจะเอาอักษร2 ตัวก็ stop = 2
filter_movies = select_new_movies['budget'].str.slice(stop=1) == '$'
#code in row11 เป็นการเลือกเฉพาะ row ที่ขึ้นตันด้วย $ ==> จะแสดงค่าเป็น true/false
filter_movies = select_new_movies[select_new_movies['budget'].str.slice(stop=1) == '$']
#code in row14 เพิ่ม select_new_movies ไว้หน้าสุด เพื่อให้แสดงผลเป็นตารางแบบเดิม

filter2 = filter_movies[['worlwide_gross_income'].apply(lambda m : int(m.split()[1])) - filter_movies['budget'].apply(lambda m : int(m.split()[1]))]
print(filter2)