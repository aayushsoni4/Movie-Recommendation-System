import streamlit as st
import display

def movie_content(movie, temp):
    st.header(movie, divider=True)
    col1, col2 = st.columns([2.1,2])
    with col1:
        temp.display_poster()
    with col2:
        temp.display_movie()

class Recommend:
    def __init__(self, recommend):
        self.recommended_movies, self.posters, self.movies_id = recommend

    def display(self):
        tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])

        with tab1:
            temp = display.Display(self.recommended_movies[0],self.movies_id[0],self.posters[0])
            movie_content(self.recommended_movies[0], temp)

        with tab2:
            temp = display.Display(self.recommended_movies[1],self.movies_id[1],self.posters[1])
            movie_content(self.recommended_movies[1], temp)

        with tab3:
            temp = display.Display(self.recommended_movies[2],self.movies_id[2],self.posters[2])
            movie_content(self.recommended_movies[2], temp)
        
        with tab4:
            temp = display.Display(self.recommended_movies[3],self.movies_id[3],self.posters[3])
            movie_content(self.recommended_movies[3], temp)

        with tab5:
            temp = display.Display(self.recommended_movies[4],self.movies_id[4],self.posters[4])
            movie_content(self.recommended_movies[4], temp)
    
        with tab6:
            temp = display.Display(self.recommended_movies[5],self.movies_id[5],self.posters[5])
            movie_content(self.recommended_movies[5], temp)

        with tab7:
            temp = display.Display(self.recommended_movies[6],self.movies_id[6],self.posters[6])
            movie_content(self.recommended_movies[6], temp)

        with tab8:
            temp = display.Display(self.recommended_movies[7],self.movies_id[7],self.posters[7])
            movie_content(self.recommended_movies[7], temp)

        with tab9:        
            temp = display.Display(self.recommended_movies[8],self.movies_id[8],self.posters[8])
            movie_content(self.recommended_movies[8], temp)

        with tab10:
            temp = display.Display(self.recommended_movies[9],self.movies_id[9],self.posters[9])
            movie_content(self.recommended_movies[9], temp)