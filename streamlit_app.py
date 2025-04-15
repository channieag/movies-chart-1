import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("🎬 Average Movie Score by Country")
st.sidebar.title("🫵 About you")
st.sidebar.text_input("Full Name")
st.sidebar.text_input("Email address")
st.sidebar.radio("Pick your gender",["Male","Female"])
st.sidebar.checkbox("Dưới 12 tuổi")
st.sidebar.checkbox("12-18 tuổi")
st.sidebar.checkbox("Trên 18 tuổi")

st.sidebar.title("🎥 Your Movie Preferences")
favorite_genre = st.sidebar.selectbox(
    "What's your favorite movie genre?",
    ["Action", "Comedy", "Drama", "Horror", "Romance", "Sci-Fi", "Animation"]
)
watch_frequency = st.sidebar.slider(
    "How many movies do you watch per week?",
    min_value=0,
    max_value=21,
    value=3
)

st.subheader("🍿 Your Movie Watching Preferences")
st.write(f"**Favorite Genre:** {favorite_genre}")
st.write(f"**Movies per week:** {watch_frequency}")

# Show a multiselect widget with the countries using `st.multiselect`.
st.sidebar.title("✔️ Choose Countries")
movies_data = pd.read_csv("https://raw.githubusercontent.com/nv-thang/Data-Visualization-Course/main/Dataset%20for%20Practice/movies.csv")
countries = st.sidebar.multiselect(
    "Countries",
    movies_data.country.unique(),
    ["United Kingdom", "United States", "Canada", "China", "West Germany", "Australia", "Italy"],
)

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# Sinh số ngẫu nhiên cho mỗi ngày sao cho tổng cộng lại bằng số phim trong tuần
np.random.seed(42)  # Để đảm bảo tính tái tạo của kết quả
daily_movies_random = np.random.rand(7)  # Tạo ra 7 số ngẫu nhiên
daily_movies_random = daily_movies_random / daily_movies_random.sum()  # Chuẩn hóa về tổng = 1
daily_movies_random = daily_movies_random * watch_frequency  # Nhân với tổng số phim trong tuần

# Làm tròn kết quả để không có số thập phân
daily_movies_random = np.round(daily_movies_random, 0)

# Vẽ biểu đồ đường
fig1 = plt.figure(figsize=(20, 12))
plt.plot(days, daily_movies_random, marker='o', linestyle='--', color='g', markersize=10)
plt.title("Number of Movies Watched per Day", fontsize = 20, weight = 'bold')
plt.xlabel("Day", fontsize = 14, weight = 550)
plt.ylabel("Number of Movies", fontsize = 14, weight = 550)
plt.grid(alpha = 0.5)

# Hiển thị biểu đồ trên Streamlit
st.pyplot(fig1)



# Đọc dữ liệu và loại bỏ giá trị thiếu
movies_data = movies_data.dropna()

# Tính điểm trung bình theo quốc gia
avg_score = movies_data.groupby("country")["score"].mean().round(2).reset_index()
avg_score = avg_score.sort_values(by = "score", ascending = False)
 
# Giới hạn top 15 quốc gia
avg_score = avg_score.head(15)

# Tách cột
country = avg_score["country"]
score = avg_score["score"]

# Vẽ biểu đồ cột ngang
fig2 = plt.figure(figsize=(20, 12))
bars = plt.barh(country, score, color ="g", edgecolor = "black")

# Thêm điểm số bên phải mỗi cột
for bar in bars:
    xval = bar.get_width()
    plt.text(xval + 0.1, bar.get_y() + bar.get_height()/2.0, f"{xval:.2f}", va='center', fontsize=9)

# Cải thiện hiển thị
plt.xlabel("Average Score", fontsize = 14, weight = 550)
plt.ylabel("Country", fontsize = 14, weight = 550)
plt.title("Matplotlib Bar Chart Showing the Average Score of Movies in Each Country", fontsize=18, weight = 700)
plt.grid(axis = 'x', linestyle = '--', alpha = 0.5)
plt.tight_layout()

# Hiển thị trên Streamlit
st.write("""Biểu đồ thể hiện điểm trung bình phim theo quốc gia (Top 15)""")
st.pyplot(fig2)
