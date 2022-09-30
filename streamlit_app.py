
import streamlit
import pandas as pd
import requests
import snowflake.connector

from urllib.error import URLError

#create the repeatable code block
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ this_fruit_choice)
   return pd.json_normalize(fruityvice_response.json())
   

streamlit.title("My Parent's new healthy dinner")
streamlit.header("Breakfast Menu")
streamlit.text("😊Ome a three and Blueberry Oatmeal")
streamlit.text("👂Kale, Spinacch & Rocket Smoothie")
streamlit.text("Hard-Boiled Free-Range Egg")


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#add pick list
fruit_selected=streamlit.multiselect("Pick some fruit", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruit_to_show = my_fruit_list.loc[fruit_selected]

#display the table on the page
streamlit.dataframe(fruit_to_show)

streamlit.header("Fruityvice Fruit Advice!")

try:

  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get informtion.")
  else:
    streamlit.dataframe( get_fruityvice_data(fruit_choice))
except URLError as e:
    streamlit.error()

streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list containts:")
streamlit.dataframe(my_data_rows)

add_my_fruit = streamlit.text_input('What fruit would you like to add?','')
if(add_my_fruit):
  streamlit.write('Thanks for adding ', add_my_fruit)

my_cur.execute("insert into fruit_load_list values ('from streamlit')");


