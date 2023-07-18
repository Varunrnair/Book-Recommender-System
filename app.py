import streamlit as st
import pandas as pd
import pickle
import requests

similarity = pickle.load(open('similarity_scores.pkl','rb')) 
books = pickle.load(open('books.pkl','rb')) 
books_df = pd.DataFrame(books)

pt = pickle.load(open('pt.pkl','rb'))
pt_df = pd.DataFrame(pt)

popular = pickle.load(open('popular.pkl','rb'))
popular_df = pd.DataFrame(popular)


st.title('Book Recommender System')

selected_book = st.selectbox(
    'Select a Book',
    popular_df['Book-Title'].values)





st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<h5 style="text-align: center;">Could not find what u were searching for? <br>Here are the books most recommended by avid readers</h5>', unsafe_allow_html=True)

name = popular_df['Book-Title']
poster = popular_df['Image-URL-M']

# Divide the columns into two sets
col1, col2, col3, col4, col5 = st.columns(5)
st.divider() 
col6, col7, col8, col9, col10 = st.columns(5)
st.divider() 

# Display images and text in the columns
with col1:
    st.image(poster.iloc[0])
    st.text(name.iloc[0])

with col2:
    st.image(poster.iloc[1])
    st.text(name.iloc[1])

with col3:
    st.image(poster.iloc[2])
    st.text(name.iloc[2])

with col4:
    st.image(poster.iloc[3])
    st.text(name.iloc[3])

with col5:
    st.image(poster.iloc[4])
    st.text(name.iloc[4])

with col6:
    st.image(poster.iloc[5])
    st.text(name.iloc[5])

with col7:
    st.image(poster.iloc[6])
    st.text(name.iloc[6])

with col8:
    st.image(poster.iloc[7])
    st.text(name.iloc[7])

with col9:
    st.image(poster.iloc[8])
    st.text(name.iloc[8])

with col10:
    st.image(poster.iloc[9])
    st.text(name.iloc[9])

    
