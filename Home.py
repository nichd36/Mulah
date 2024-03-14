import streamlit as st
import pandas as pd

st.title("Nicholas Dylan's Assessment")

def load_data():
        df = pd.read_csv("Table_Input.csv")
        return df

def get_value(index):
        value = table1.loc[table1['Index #'] == index, 'Value'].values[0]
        return value

table1 = load_data()

st.write("Table 1 (input)")
table1

# Alpha = A5 + A20
alpha = get_value("A5") + get_value("A20")
# Beta = A15 / A7
beta = get_value("A15") / get_value("A7")
# Charlie = A13 * A12
charlie = get_value("A13") * get_value("A12")

st.header("Code snippet:")
st.image("code_snippet.jpeg")

st.write("Table 2 (output)")
table2 = [['Alpha', alpha], ['Beta', beta], ['Charlie', charlie]]
df = pd.DataFrame(table2, columns=['Category', 'Value'])
df
