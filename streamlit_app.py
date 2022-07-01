import streamlit
streamlit.title('My Parents New Healthy Dinner')
streamlit.header('Breakfast Menu')
streamlit.text('100g of Soaked Peanut \N{Peanuts} and 2 Bananas \N{banana}\N{banana}')
streamlit.text('Sprouts of Greengram, Readgram with Carrot Slices \N{carrot}')

streamlit.header('\N{mango}\N{banana}\N{Cucumber} Make Your Own Fruit Diet \N{grapes}\N{cherries}')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Apple','Grapes'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page
streamlit.dataframe(fruits_to_show)

#New Section to display fruityvice api responds
streamlit.header('Fruityvice Fruit Advice!')
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
# take the json version of the response and normalize it 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it the screen as table
streamlit.dataframe(fruityvice_normalized)


