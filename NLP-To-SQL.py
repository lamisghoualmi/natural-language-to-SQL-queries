import openai
import numpy as np
import streamlit as st
import time

# Load OpenAI API key from secrets file
openai.api_key = st.secrets["pass"]

st.sidebar.header('Natural language to SQL queries.')

# ... (rest of your code remains unchanged)

def generate_sql(query):
    model_engine = "text-davinci-002"
    prompt = (
        f"Translate the following natural language query to SQL:\n"
        f"{query}\n"
        f"SQL:"
    )

    retries = 3  # Number of retries
    for attempt in range(retries):
        try:
            response = openai.Completion.create(
                engine=model_engine,
                prompt=prompt,
                temperature=0,
                max_tokens=150,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0,
                stop=["#", ";"]
            )
            return response.choices[0].text.strip()
        except openai.error.RateLimitError as e:
            st.warning(f"Rate limit exceeded. Retrying in {2**attempt} seconds...")
            time.sleep(2**attempt)

    st.error("Exceeded maximum number of retries. Please try again later.")
    return None

if st.button('Generate SQL script'):
    if len(query) > 0:
        Respo = generate_sql(query)
        if Respo is not None:
            st.write(Respo)
    else:
        st.warning('Please enter at least two words. Example: list of customers where country is United states', icon="⚠️")
