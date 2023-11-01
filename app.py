import streamlit as st
import pickle
import pandas as pd
import requests
import numpy as np
import trailer_finder

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
    st.header(selected_movie)
        
    col1, col2 = st.columns([2.1,2])
    with col1:
        poster = fetch_poster(movies.iloc[movie_idx].id)
        st.image(poster, width=350)
    with col2:
        response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=087c4d46a2f438619a5f3c6714775216&language=en-US'.format(movies.iloc[movie_idx].id))
        data = response.json()
        s = ""
        st.write("***OVERVIEW***: ", data['overview'])
        for i in data['genres']:
            s+=i['name']+", "
        st.write("***GENRES***: ", s[:-2])
        st.write("***RELEASE DATE***: ", data['release_date'][8:]+'-'+data['release_date'][5:7]+'-'+data['release_date'][:4])
        st.write("***RUNTIME***: ", data['runtime'], "mins")
        s = ""
        for i in data['spoken_languages']:
            s+=i['english_name']+", "
        st.write("***LANGUAGES***: ", s[:-2])
        st.write("***RATING***: ", data['vote_average'], "/10")
        st.write("***STATUS***: ", data['status'])     
        
        query = selected_movie+" "+str(data['release_date'][:4])+" official trailer"
        video_url = trailer_finder.findYTtrailer(query)
        st.link_button("Trailer", video_url)



    st.header("Recommended Movies")

    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])

    with tab1:
        st.header(recommended_movies[0])
        
        col1, col2 = st.columns([2.1,2])
        with col1:
            st.image(posters[0], width=350)
        with col2:
            response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=087c4d46a2f438619a5f3c6714775216&language=en-US'.format(movies_id[0]))
            data = response.json()
            s = ""
            st.write("***OVERVIEW***: ", data['overview'])
            for i in data['genres']:
                s+=i['name']+", "
            st.write("***GENRES***: ", s[:-2])
            st.write("***RELEASE DATE***: ", data['release_date'][8:]+'-'+data['release_date'][5:7]+'-'+data['release_date'][:4])
            st.write("***RUNTIME***: ", data['runtime'], "mins")
            s = ""
            for i in data['spoken_languages']:
                s+=i['english_name']+", "
            st.write("***LANGUAGES***: ", s[:-2])
            st.write("***RATING***: ", data['vote_average'], "/10")
            st.write("***STATUS***: ", data['status'])
            
            
            query = recommended_movies[0]+" "+str(data['release_date'][:4])+" official trailer"
            video_url = trailer_finder.findYTtrailer(query)
            st.link_button("Trailer", video_url)
            

    with tab2:
        st.header(recommended_movies[1])
        
        col1, col2 = st.columns([2.1,2])
        with col1:
            st.image(posters[1], width=350)
        with col2:
            response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=087c4d46a2f438619a5f3c6714775216&language=en-US'.format(movies_id[1]))
            data = response.json()
            s = ""
            st.write("***OVERVIEW***: ", data['overview'])
            for i in data['genres']:
                s+=i['name']+", "
            st.write("***GENRES***: ", s[:-2])
            st.write("***RELEASE DATE***: ", data['release_date'][8:]+'-'+data['release_date'][5:7]+'-'+data['release_date'][:4])
            st.write("***RUNTIME***: ", data['runtime'], "mins")
            s = ""
            for i in data['spoken_languages']:
                s+=i['english_name']+", "
            st.write("***LANGUAGES***: ", s[:-2])
            st.write("***RATING***: ", data['vote_average'], "/10")
            st.write("***STATUS***: ", data['status'])        
            
            query = recommended_movies[1]+" "+str(data['release_date'][:4])+" official trailer"
            video_url = trailer_finder.findYTtrailer(query)
            st.link_button("Trailer", video_url)


    with tab3:
        st.header(recommended_movies[2])
        
        col1, col2 = st.columns([2.1,2])
        with col1:
            st.image(posters[2], width=350)
        with col2:
            response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=087c4d46a2f438619a5f3c6714775216&language=en-US'.format(movies_id[2]))
            data = response.json()
            s = ""
            st.write("***OVERVIEW***: ", data['overview'])
            for i in data['genres']:
                s+=i['name']+", "
            st.write("***GENRES***: ", s[:-2])
            st.write("***RELEASE DATE***: ", data['release_date'][8:]+'-'+data['release_date'][5:7]+'-'+data['release_date'][:4])
            st.write("***RUNTIME***: ", data['runtime'], "mins")
            s = ""
            for i in data['spoken_languages']:
                s+=i['english_name']+", "
            st.write("***LANGUAGES***: ", s[:-2])
            st.write("***RATING***: ", data['vote_average'], "/10")
            st.write("***STATUS***: ", data['status'])    
            
            query = recommended_movies[2]+" "+str(data['release_date'][:4])+" official trailer"
            video_url = trailer_finder.findYTtrailer(query)
            st.link_button("Trailer", video_url)
    
    with tab4:
        st.header(recommended_movies[3])
        
        col1, col2 = st.columns([2.1,2])
        with col1:
            st.image(posters[3], width=350)
        with col2:
            response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=087c4d46a2f438619a5f3c6714775216&language=en-US'.format(movies_id[3]))
            data = response.json()
            s = ""
            st.write("***OVERVIEW***: ", data['overview'])
            for i in data['genres']:
                s+=i['name']+", "
            st.write("***GENRES***: ", s[:-2])
            st.write("***RELEASE DATE***: ", data['release_date'][8:]+'-'+data['release_date'][5:7]+'-'+data['release_date'][:4])
            st.write("***RUNTIME***: ", data['runtime'], "mins")
            s = ""
            for i in data['spoken_languages']:
                s+=i['english_name']+", "
            st.write("***LANGUAGES***: ", s[:-2])
            st.write("***RATING***: ", data['vote_average'], "/10")
            st.write("***STATUS***: ", data['status'])  
            
            query = recommended_movies[3]+" "+str(data['release_date'][:4])+" official trailer"
            video_url = trailer_finder.findYTtrailer(query)
            st.link_button("Trailer", video_url)
   

    with tab5:
        st.header(recommended_movies[4])
        
        col1, col2 = st.columns([2.1,2])
        with col1:
            st.image(posters[4], width=350)
        with col2:
            response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=087c4d46a2f438619a5f3c6714775216&language=en-US'.format(movies_id[4]))
            data = response.json()
            s = ""
            st.write("***OVERVIEW***: ", data['overview'])
            for i in data['genres']:
                s+=i['name']+", "
            st.write("***GENRES***: ", s[:-2])
            st.write("***RELEASE DATE***: ", data['release_date'][8:]+'-'+data['release_date'][5:7]+'-'+data['release_date'][:4])
            st.write("***RUNTIME***: ", data['runtime'], "mins")
            s = ""
            for i in data['spoken_languages']:
                s+=i['english_name']+", "
            st.write("***LANGUAGES***: ", s[:-2])
            st.write("***RATING***: ", data['vote_average'], "/10")
            st.write("***STATUS***: ", data['status'])       
            
            query = recommended_movies[4]+" "+str(data['release_date'][:4])+" official trailer"
            video_url = trailer_finder.findYTtrailer(query)
            st.link_button("Trailer", video_url)
    
    with tab6:
        st.header(recommended_movies[5])
        
        col1, col2 = st.columns([2.1,2])
        with col1:
            st.image(posters[5], width=350)
        with col2:
            response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=087c4d46a2f438619a5f3c6714775216&language=en-US'.format(movies_id[5]))
            data = response.json()
            s = ""
            st.write("***OVERVIEW***: ", data['overview'])
            for i in data['genres']:
                s+=i['name']+", "
            st.write("***GENRES***: ", s[:-2])
            st.write("***RELEASE DATE***: ", data['release_date'][8:]+'-'+data['release_date'][5:7]+'-'+data['release_date'][:4])
            st.write("***RUNTIME***: ", data['runtime'], "mins")
            s = ""
            for i in data['spoken_languages']:
                s+=i['english_name']+", "
            st.write("***LANGUAGES***: ", s[:-2])
            st.write("***RATING***: ", data['vote_average'], "/10")
            st.write("***STATUS***: ", data['status'])      
            
            query = recommended_movies[5]+" "+str(data['release_date'][:4])+" official trailer"
            video_url = trailer_finder.findYTtrailer(query)
            st.link_button("Trailer", video_url)

    with tab7:
        st.header(recommended_movies[6])
        
        col1, col2 = st.columns([2.1,2])
        with col1:
            st.image(posters[6], width=350)
        with col2:
            response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=087c4d46a2f438619a5f3c6714775216&language=en-US'.format(movies_id[6]))
            data = response.json()
            s = ""
            st.write("***OVERVIEW***: ", data['overview'])
            for i in data['genres']:
                s+=i['name']+", "
            st.write("***GENRES***: ", s[:-2])
            st.write("***RELEASE DATE***: ", data['release_date'][8:]+'-'+data['release_date'][5:7]+'-'+data['release_date'][:4])
            st.write("***RUNTIME***: ", data['runtime'], "mins")
            s = ""
            for i in data['spoken_languages']:
                s+=i['english_name']+", "
            st.write("***LANGUAGES***: ", s[:-2])
            st.write("***RATING***: ", data['vote_average'], "/10")
            st.write("***STATUS***: ", data['status'])         
            
            query = recommended_movies[6]+" "+str(data['release_date'][:4])+" official trailer"
            video_url = trailer_finder.findYTtrailer(query)
            st.link_button("Trailer", video_url)   

    with tab8:
        st.header(recommended_movies[7])
        
        col1, col2 = st.columns([2.1,2])
        with col1:
            st.image(posters[7], width=350)
        with col2:
            response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=087c4d46a2f438619a5f3c6714775216&language=en-US'.format(movies_id[7]))
            data = response.json()
            s = ""
            st.write("***OVERVIEW***: ", data['overview'])
            for i in data['genres']:
                s+=i['name']+", "
            st.write("***GENRES***: ", s[:-2])
            st.write("***RELEASE DATE***: ", data['release_date'][8:]+'-'+data['release_date'][5:7]+'-'+data['release_date'][:4])
            st.write("***RUNTIME***: ", data['runtime'], "mins")
            s = ""
            for i in data['spoken_languages']:
                s+=i['english_name']+", "
            st.write("***LANGUAGES***: ", s[:-2])
            st.write("***RATING***: ", data['vote_average'], "/10")
            st.write("***STATUS***: ", data['status'])          
            
            query = recommended_movies[7]+" "+str(data['release_date'][:4])+" official trailer"
            video_url = trailer_finder.findYTtrailer(query)
            st.link_button("Trailer", video_url)   

    
    with tab9:
        st.header(recommended_movies[8])
        
        col1, col2 = st.columns([2.1,2])
        with col1:
            st.image(posters[8], width=350)
        with col2:
            response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=087c4d46a2f438619a5f3c6714775216&language=en-US'.format(movies_id[8]))
            data = response.json()
            s = ""
            st.write("***OVERVIEW***: ", data['overview'])
            for i in data['genres']:
                s+=i['name']+", "
            st.write("***GENRES***: ", s[:-2])
            st.write("***RELEASE DATE***: ", data['release_date'][8:]+'-'+data['release_date'][5:7]+'-'+data['release_date'][:4])
            st.write("***RUNTIME***: ", data['runtime'], "mins")
            s = ""
            for i in data['spoken_languages']:
                s+=i['english_name']+", "
            st.write("***LANGUAGES***: ", s[:-2])
            st.write("***RATING***: ", data['vote_average'], "/10")
            st.write("***STATUS***: ", data['status'])           
            
            query = recommended_movies[8]+" "+str(data['release_date'][:4])+" official trailer"
            video_url = trailer_finder.findYTtrailer(query)
            st.link_button("Trailer", video_url)   

    with tab10:
        st.header(recommended_movies[9])
        
        col1, col2 = st.columns([2.1,2])
        with col1:
            st.image(posters[9], width=350)
        with col2:
            response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=087c4d46a2f438619a5f3c6714775216&language=en-US'.format(movies_id[9]))
            data = response.json()
            s = ""
            st.write("***OVERVIEW***: ", data['overview'])
            for i in data['genres']:
                s+=i['name']+", "
            st.write("***GENRES***: ", s[:-2])
            st.write("***RELEASE DATE***: ", data['release_date'][8:]+'-'+data['release_date'][5:7]+'-'+data['release_date'][:4])
            st.write("***RUNTIME***: ", data['runtime'], "mins")
            s = ""
            for i in data['spoken_languages']:
                s+=i['english_name']+", "
            st.write("***LANGUAGES***: ", s[:-2])
            st.write("***RATING***: ", data['vote_average'], "/10")
            st.write("***STATUS***: ", data['status'])                
            
            query = recommended_movies[9]+" "+str(data['release_date'][:4])+" official trailer"
            video_url = trailer_finder.findYTtrailer(query)
            st.link_button("Trailer", video_url)   