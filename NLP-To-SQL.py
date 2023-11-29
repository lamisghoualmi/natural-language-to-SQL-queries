


import openai
import numpy as np
import streamlit as st

# Load OpenAI API key from secrets file
#openai.api_key=st.secrets["pass"]



st.sidebar.header('Natural language to SQL queries.  check my code on GitHub, I postponed this app because OPENAI API credit is in paid  (PS I commented the function for SQL query)')

st.sidebar.image("sql.png", use_column_width=True)

st.sidebar.write("""
         ######  This app uses streamlit and OpenAI APIs to translate natural language queries into SQL statements with ease. Simply input your natural language query, and our app will generate the corresponding SQL statement for you to execute, saving you valuable time and effort.
         """)
st.sidebar.write("""
         ######  Made by Lamis Ghoualmi  [LinkedIn](https://www.linkedin.com/in/lamisghoualmi/), [Github](https://lamisghoualmi.github.io/)
         """)



st.header('Translate natural language to SQL queries.')

st.info('Example: Write a query that prints a list of employee names from the Employee table in alphabetical order', icon="ℹ️")
query= st.text_input('Enter your text to generate SQL query', '')


#def generate_sql(query):
#    model_engine = "text-davinci-002"
#    prompt = (
#        f"Translate the following natural language query to SQL:\n"
#        f"{query}\n"
#        f"SQL:"
#    )
#    response = openai.Completion.create(
#        engine=model_engine,
#        prompt=prompt,
#        temperature=0,
#        max_tokens=150,
 #       top_p=1.0,
 #       frequency_penalty=0.0,
 #       presence_penalty=0.0,
#        stop=["#", ";"]
 #   )
 #   return response.choices[0].text.strip()


if st.button('Generate SQL script'):
  if len(query) > 0:
    Respo=generate_sql(query)
    st.write(Respo)
  else:
    st.warning('Please enter at least two words. Example: list of customers where country is United states', icon="⚠️")

  

