import streamlit as st
import pandas as pd
import seaborn as sns
st.title('Hello Wilders, welcome to my application!')
st.write("La création de l'application par Jouini Zied")
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_voiture = pd.read_csv(link)
df_voiture
viz_correlation = sns.heatmap(df_voiture.corr(), center=0,cmap = sns.color_palette("vlag", as_cmap=True))
st.pyplot(viz_correlation.figure)


#continent = st.selectbox(label = "Choose a continent", options = continent_list)
# put all widgets in sidebar and have a subtitle
with st.sidebar:
    continent_list = list(df_voiture['continent'].unique())
    st.subheader("Configure the plot")
    # widget to choose which continent to display
    continent = st.selectbox(label = "Choose a continent", options = continent_list)
    

st.line_chart(df_voiture['hp'])





   




                                  


