
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
streamlit.text("πOme a three and Blueberry Oatmeal")
streamlit.text("πKale, Spinacch & Rocket Smoothie")
streamlit.text("Hard-Boiled Free-Range Egg")


streamlit.header('ππ₯­ Build Your Own Fruit Smoothie π₯π')

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

streamlit.header("View Our Fruit List - Add Your Favorites!")

#snowflake-related functions
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list");
    return my_cur.fetchall()

#Add a button to load the fruit
if streamlit.button('Get Fruit List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])  
  my_data_rows = get_fruit_load_list()
  my_cnx.close()
  streamlit.dataframe(my_data_rows)

def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values ('"+new_fruit+"')");
    return "Thanks for adding " + new_fruit
 
add_my_fruit = streamlit.text_input('What fruit would you like to add?')

if streamlit.button('Add a Fruit to the List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])  
  
  streamlit.text(insert_row_snowflake(add_my_fruit))
  my_cnx.close()
  




