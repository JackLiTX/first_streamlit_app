
import streamlit
import pandas as pd

streamlit.title("My Parent's new healthy dinner")
streamlit.header("Breakfast Menu")
streamlit.text("😊Ome a three and Blueberry Oatmeal")
streamlit.text("👂Kale, Spinacch & Rocket Smoothie")
streamlit.text("Hard-Boiled Free-Range Egg")


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
