import googleapiclient
import streamlit as st
import requests
import trailer_finder
import os
from dotenv import load_dotenv

load_dotenv()

class Display:
    def __init__(self,recommended_movie, movie_id, poster):
        self.recommended_movie = recommended_movie
        self.movie_id = movie_id
        self.poster = poster
    
    def display_poster(self):
        st.image(self.poster, width=350)
    
    def display_movie(self):
        TMDB_API = os.environ['TMDB_API_KEY']
        response = requests.get(f'https://api.themoviedb.org/3/movie/{self.movie_id}?api_key={TMDB_API}&language=en-US')
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
        
        query = self.recommended_movie+" "+str(data['release_date'][:4])+" official trailer"
        try:
            video_url = trailer_finder.findYTtrailer(query)
        except (googleapiclient.errors.HttpError, Exception) as e:
            try:
                video_url = trailer_finder.findYTtrailerbs4(query)
            except Exception as e:
                video_url = None
        if video_url:
            st.link_button("Trailer", video_url)

