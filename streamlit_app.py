
import streamlit
import pandas as pd

streamlit.title("My Parent's new healthy dinner")
streamlit.header("Breakfast Menu")
streamlit.text("😊Ome a three and Blueberry Oatmeal")
streamlit.text("👂Kale, Spinacch & Rocket Smoothie")
streamlit.text("Hard-Boiled Free-Range Egg")


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#add pick list
streamlit.multiselect("Pick some fruit", list(my_fruit_list.index), ['Avocado', 'Strawberries'])

#display the table on the page
streamlit.dataframe(my_fruit_list)
