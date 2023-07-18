import streamlit as st
import numpy as np
import pandas as pd
import pickle

similarity = pickle.load(open('similarity_scores.pkl','rb')) 

books_df = pickle.load(open('books.pkl','rb')) 
books = pd.DataFrame(books_df)

pt_df = pickle.load(open('pt.pkl','rb'))
pt = pd.DataFrame(pt_df)

popular_df = pickle.load(open('popular.pkl','rb'))
popular = pd.DataFrame(popular_df)

def recommend(book):
    name=[]
    poster=[]
    author=[]
    index = np.where(pt.index==book)[0][0]
    similar_books = sorted(list(enumerate(similarity[index])), key=lambda x: x[1], reverse=True)[1:5]
    for i in similar_books:
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        name.append(temp_df.drop_duplicates('Book-Title')['Book-Title'].values[0])
        poster.append(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values[0])
        author.append(temp_df.drop_duplicates('Book-Title')['Book-Author'].values[0])
    return name, poster, author

st.title('Book Recommender System')

selected_book = st.selectbox(
    'Select a Book',
    popular['Book-Title'].values)

if st.button('Recommend'):
    name, poster, author = recommend(selected_book)
    col1,col2 = st.columns(2)
    st.divider()
    col3,col4 = st.columns(2)
    st.divider()
    for i in range(1):
        with col1:
            st.image(poster[0])
            st.text(name[0])
        with col2:
            st.image(poster[1])
            st.text(name[1])
    for i in range(1):
        with col3:
            st.image(poster[2])
            st.text(name[2])
        with col4:
            st.image(poster[3])
            st.text(name[3])   


st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<h5 style="text-align: center;">Could not find what u were searching for? <br>Here are the books most recommended by avid readers</h5>', unsafe_allow_html=True)

name = popular['Book-Title']
poster = popular['Image-URL-M']

col1, col2, col3, col4, col5 = st.columns(5)
st.divider() 
col6, col7, col8, col9, col10 = st.columns(5)
st.divider() 

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

    
