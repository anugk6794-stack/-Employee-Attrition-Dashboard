import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Employee Attrition", layout="wide")
st.title("Employee Attrition & HR Dashboard")

data = {
    'Department': ['Sales','HR','R&D','Sales','R&D','HR','Sales','R&D','Sales','HR']*15,
    'Attrition': ['Yes','No','No','Yes','No','Yes','No','No','Yes','No']*15,
    'Age': [34,28,45,32,41,29,38,36,30,42]*15,
    'Income': [5000,3000,8000,4500,9000,3200,5500,7500,4800,3500]*15,
    'Years': [2,5,10,1,8,2,3,7,1,4]*15
}
df = pd.DataFrame(data)

c1,c2,c3 = st.columns(3)
c1.metric("Total Employees", len(df))
c2.metric("Attrition Count", len(df[df['Attrition']=='Yes']))
c3.metric("Attrition Rate", f"{round(len(df[df['Attrition']=='Yes'])/len(df)*100,1)}%")

st.divider()
fig1 = px.bar(df.groupby(['Department','Attrition']).size().reset_index(name='Count'), x='Department', y='Count', color='Attrition', barmode='group', title="Attrition by Department")
st.plotly_chart(fig1, use_container_width=True)

fig2 = px.scatter(df, x='Years', y='Income', color='Attrition', size='Age', title="Income vs Years at Company")
st.plotly_chart(fig2, use_container_width=True)

st.dataframe(df.head(20))
st.success("Deployed by Anu GK - Project 2")
