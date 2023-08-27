import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

title = "The Best Company"
description = """
The word 'talent' has become a buzzword in our society. Everyone wants to have a talent, but many people do not know what that means. Some believe that talent is a natural ability that you were born with. Others think that talent is something you learn from an early age. Either way, people think that talent can help you reach your goals. However, talent is only useful when you use it. The primary problem with talent is that it can be misleading. A person may have talent for singing, but they will probably fail without proper training.
"""
heading1 = "Our Team"

st.title(title)
st.write(description)
st.subheader(heading1)

col1, empty1, col2, empty2, col3 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5])

employees = pd.read_csv("data.csv")
num_employees = len(employees)
num_emps_col1 = num_employees // 3
num_emps_col2 = num_employees // 3 * 2

with col1:
    for index, row in employees[:num_emps_col1].iterrows():
        name = f"{row['first name']} {row['last name']}"
        st.image("images/" + row["image"], width=200)
        st.subheader(name)
        st.write(row["role"])

with col2:
    for index, row in employees[num_emps_col1:num_emps_col2].iterrows():
        name = f"{row['first name']} {row['last name']}"
        st.image("images/" + row["image"], width=200)
        st.subheader(name)
        st.write(row["role"])
with col3:
    for index, row in employees[num_emps_col2:].iterrows():
        name = f"{row['first name']} {row['last name']}"
        st.image("images/" + row["image"], width=200)
        st.subheader(name)
        st.write(row["role"])