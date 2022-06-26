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
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))['Apple','Grapes']

# Display the table on the page
streamlit.dataframe(my_fruit_list)
