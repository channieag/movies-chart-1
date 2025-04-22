# Truy cập các thư viện
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Sidebar
st.sidebar.title("🫵 About you")
st.sidebar.text_input("Full Name")
st.sidebar.text_input("Email address")
st.sidebar.radio("Pick your gender",["Male","Female"])
st.sidebar.write("Pick your age range")
st.sidebar.checkbox("Under 12 ")
st.sidebar.checkbox("12-18 ")
st.sidebar.checkbox("Above 18 ")
st.sidebar.title("🎥 Your Movie Preferences")
favorite_genre = st.sidebar.selectbox(
    "What's your favorite movie genre?",
    ["Action", "Comedy", "Drama", "Horror", "Romance", "Sci-Fi", "Animation"])
watch_frequency = st.sidebar.slider(
    "How many movies do you watch per week?",
    min_value = 0,
    max_value = 21,
    value = 7)

# Content
st.title("🍿 Your Movie Watching Preferences")
st.write(f"**Favorite Genre:** {favorite_genre}")
st.write(f"**Movies per week:** {watch_frequency}")

# Vẽ biểu đồ đường thể hiện số phim coi mỗi ngày trong tuần
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

movies_data = pd.read_csv("https://raw.githubusercontent.com/nv-thang/Data-Visualization-Course/main/Dataset%20for%20Practice/movies.csv")
avg_time = movies_data.groupby("year")["runtime"].mean().round(2).reset_index()
year = avg_time["year"]

fig1 = plt.figure(figsize=(20, 12))
plt.plot(year, avg_time, marker = 'o', linestyle = '--', color = 'g', markersize = 10)
plt.title("Number of Movies Watched per Day", fontsize = 20, weight = 'bold')
plt.xlabel("Day", fontsize = 14, weight = 550)
plt.ylabel("Number of Movies", fontsize = 14, weight = 550)
plt.grid(alpha = 0.5)
st.pyplot(fig1)

# Vẽ biểu đồ cột ngang thể hiện điểm trung bình phim theo quốc qia (top 15)
st.title("🎬 Average Movie Score by Country")
st.subheader("✔️ Choose Countries")

countries = st.multiselect(
    "Countries",
    movies_data.country.unique(),
    ["United Kingdom", "United States", "Lebanon", "Iran", "Argentina", "India", "Colombia", "South Korea"])

movies_data = movies_data.dropna()

avg_score = movies_data.groupby("country")["score"].mean().round(2).reset_index()
avg_score = avg_score.sort_values(by = "score", ascending = False)
avg_score = avg_score.head(15)

country = avg_score["country"]
score = avg_score["score"]

fig2 = plt.figure(figsize=(20, 12))
bars = plt.bar(country, score, color ="g", edgecolor = "black")

for bar in bars:
    yval = bar.get_width()
    plt.text(yval + 0.1, bar.get_y() + bar.get_height()/2.0, f"{yval:.2f}", va ='center', fontsize = 10)
    
plt.xlabel("Average Score", fontsize = 14, weight = 550)
plt.ylabel("Country", fontsize = 14, weight = 550)
plt.xticks(rotation = 60)
plt.title("Matplotlib Bar Chart Showing the Average Score of Movies in Each Country", fontsize = 18, weight = 700)
plt.grid(axis = 'y', linestyle = '--', alpha = 0.5)
st.pyplot(fig2)
