import recommend
import pandas as pd
import streamlit as st
import requests
import display

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=087c4d46a2f438619a5f3c6714775216&language=en-US'.format(movie_id))
    data = response.json()
    return 'http://image.tmdb.org/t/p/w500' + data['poster_path']

def content_recommendation(movie):
    movie_idx = title_id[movie]
    similar = features_similarity.loc[movie_idx]
    movies_list = sorted(list(enumerate(similar)),reverse=True,key=lambda x: x[1])[1:11]

    simi = list(features_similarity.loc[movie_idx].items())
    movies_list = sorted(simi, key=(lambda x: x[1]), reverse=True)[1:11]
    
    recommended_movies=[]
    recommended_movies_posters=[]
    recommended_movies_id=[]
    for i in movies_list:
        movie_id = int(float(i[0]))
        recommended_movies.append(id_title[movie_id])
        recommended_movies_posters.append(fetch_poster(movie_id))
        recommended_movies_id.append(movie_id)
        
    return recommended_movies,recommended_movies_posters,recommended_movies_id

def collaborative_recommendation(movie):
    movie_idx = title_id[movie]
    similar = items_similarity.loc[movie_idx]
    movies_list = sorted(list(enumerate(similar)),reverse=True,key=lambda x: x[1])[1:11]

    simi = list(items_similarity.loc[movie_idx].items())
    movies_list = sorted(simi, key=(lambda x: x[1]), reverse=True)[1:11]
    
    recommended_movies=[]
    recommended_movies_posters=[]
    recommended_movies_id=[]
    for i in movies_list:
        movie_id = int(float(i[0]))
        recommended_movies.append(id_title[movie_id])
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


movies = pd.read_csv(r'D:\Padhai\Projects\Completed Projects\Movie Recommendation System\dataset\movie_title_id.csv')

features_similarity = pd.read_csv(r'D:\Padhai\Projects\Completed Projects\Movie Recommendation System\models\features_similarity.csv')
items_similarity = pd.read_csv(r'D:\Padhai\Projects\Completed Projects\Movie Recommendation System\models\items_similarity.csv')

features_similarity.set_index('Unnamed: 0',inplace=True)
items_similarity.set_index('Unnamed: 0',inplace=True)

title_id = dict(zip(movies['title'], movies['id']))
id_title = dict(zip(movies['id'], movies['title']))

st.title("Movie Recommendation System")

selected_movie = st.selectbox("Select the movie you like", tuple(movies['title'].values))

if st.button('Recommend'):

    movie_id = title_id[selected_movie]
    poster = fetch_poster(movie_id)
    
    temp = display.Display(selected_movie,movie_id,poster)
    movie_content(temp)   
    
    st.header("Content Based Recommended Movies")    
    show_content = recommend.Recommend(content_recommendation(selected_movie))
    show_content.display()

    st.header("Collaborative Based Recommended Movies")    
    show_collaborative = recommend.Recommend(collaborative_recommendation(selected_movie))
    show_collaborative.display()