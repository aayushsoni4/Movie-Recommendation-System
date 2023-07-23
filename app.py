import streamlit as st
import pickle
import pandas as pd


def recommend(movie):
    movie_idx = movies[movies['title']==movie].index[0]
    similar = similarity[movie_idx]
    movies_list = sorted(list(enumerate(similar)),reverse=True,key=lambda x: x[1])[1:11]
    
    recommended_movies=[]
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


movies_dict = pickle.load(open("movies_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open("similarity.pkl", "rb"))

st.title("Movie Recommendation System")

selected_movie = st.selectbox("Select the movie you like", movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    for i in recommendations:
        st.write(i)