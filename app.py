import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=7cd213ab184e8cbcefd3700aa05d26fc&language=en-US".format(movie_id)
    response = requests.get(url)
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:13]

    recommended_movie_name = []
    recommended_movie_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_name.append(movies.iloc[i[0]].title)
        # Fetch movie posters
        recommended_movie_poster.append(fetch_poster(movie_id))
    return recommended_movie_name, recommended_movie_poster

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox('Select a movie', movies['title'].values)

if st.button('Recommend'):
    recommended_movie_name, recommended_movie_poster = recommend(selected_movie_name)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image(recommended_movie_poster[0])
        st.text(recommended_movie_name[0])
    with col2:
        st.image(recommended_movie_poster[1])
        st.text(recommended_movie_name[1])
    with col3:
        st.image(recommended_movie_poster[2])
        st.text(recommended_movie_name[2])
    with col4:
        st.image(recommended_movie_poster[3])
        st.text(recommended_movie_name[3])

    col5, col6, col7, col8 = st.columns(4)
    with col5:
        st.image(recommended_movie_poster[4])
        st.text(recommended_movie_name[4])
    with col6:
        st.image(recommended_movie_poster[5])
        st.text(recommended_movie_name[5])
    with col7:
        st.image(recommended_movie_poster[6])
        st.text(recommended_movie_name[6])
    with col8:
        st.image(recommended_movie_poster[7])
        st.text(recommended_movie_name[7])

    col9, col10, col11, col12 = st.columns(4)
    with col9:
        st.image(recommended_movie_poster[8])
        st.text(recommended_movie_name[8])
    with col10:
        st.image(recommended_movie_poster[9])
        st.text(recommended_movie_name[9])
    with col11:
        st.image(recommended_movie_poster[10])
        st.text(recommended_movie_name[10])
    with col12:
        st.image(recommended_movie_poster[11])
        st.text(recommended_movie_name[11])