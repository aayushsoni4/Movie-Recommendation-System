import streamlit as st
import requests
import trailer_finder

class Display:
    def __init__(self,recommended_movie, movie_id, poster):
        self.recommended_movie = recommended_movie
        self.movie_id = movie_id
        self.poster = poster
    
    def display_poster(self):
        st.image(self.poster, width=350)
    
    def display_movie(self):
        response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=087c4d46a2f438619a5f3c6714775216&language=en-US'.format(self.movie_id))
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
        video_url = trailer_finder.findYTtrailer(query)
        st.link_button("Trailer", video_url)
