import numpy as np
import pandas as pd
import streamlit as st
import requests
import pickle
import display

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=087c4d46a2f438619a5f3c6714775216&language=en-US'.format(movie_id))
    data = response.json()
    return 'http://image.tmdb.org/t/p/w500' + data['poster_path']

def recommend(movie):
    movie_idx = movies[movies['title']==movie].index[0]
    similar = similarity[movie_idx]
    movies_list = sorted(list(enumerate(similar)),reverse=True,key=lambda x: x[1])[1:11]
    
    recommended_movies=[]
    recommended_movies_posters=[]
    recommended_movies_id=[]
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
        recommended_movies_id.append(movie_id)
        
    return recommended_movies,recommended_movies_posters,recommended_movies_id

def movie_content(movie_detail):
    st.header(movie_detail.recommended_movie, divider=True)
    col1, col2 = st.columns([2.1,2])
    with col1:
        temp.display_poster()
    with col2:
        temp.display_movie()


movies_dict = pickle.load(open("movies_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

similarity_1 = pickle.load(open("similarity_1.pkl", "rb"))
similarity_2 = pickle.load(open("similarity_2.pkl", "rb"))

similarity = np.concatenate((similarity_1, similarity_2), axis=0)

st.title("Movie Recommendation System")

selected_movie = st.selectbox("Select the movie you like", tuple(movies['title'].values))

if st.button('Recommend'):
    recommended_movies,posters,movies_id = recommend(selected_movie)

    movie_idx = movies[movies['title']==selected_movie].index[0]
    poster = fetch_poster(movies.iloc[movie_idx].id)
    
    temp = display.Display(selected_movie,movies.iloc[movie_idx].id,poster)
    movie_content(temp)   
           
    st.header("Recommended Movies")
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])

    with tab1:
        temp = display.Display(recommended_movies[0],movies_id[0],posters[0])
        movie_content(temp)

    with tab2:
        temp = display.Display(recommended_movies[1],movies_id[1],posters[1])
        movie_content(temp)

    with tab3:
        temp = display.Display(recommended_movies[2],movies_id[2],posters[2])
        movie_content(temp)
    
    with tab4:
        temp = display.Display(recommended_movies[3],movies_id[3],posters[3])
        movie_content(temp)

    with tab5:
        temp = display.Display(recommended_movies[4],movies_id[4],posters[4])
        movie_content(temp)
   
    with tab6:
        temp = display.Display(recommended_movies[5],movies_id[5],posters[5])
        movie_content(temp)

    with tab7:
        temp = display.Display(recommended_movies[6],movies_id[6],posters[6])
        movie_content(temp)

    with tab8:
        temp = display.Display(recommended_movies[7],movies_id[7],posters[7])
        movie_content(temp)

    with tab9:        
        temp = display.Display(recommended_movies[8],movies_id[8],posters[8])
        movie_content(temp)

    with tab10:
        temp = display.Display(recommended_movies[9],movies_id[9],posters[9])
        movie_content(temp)