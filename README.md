# Movie Recommendation System
This project is a movie recommendation system that utilizes machine learning techniques to suggest the top 10 similar movies based on a user-selected movie. The system employs content-based filtering methods to provide personalized movie recommendations to the users.


## Introduction

In the vast world of movies, it can be challenging for users to discover films that match their interests. This movie recommendation system aims to alleviate that problem by suggesting similar movies to the ones users already like. The system uses content-based filtering to recommend movies based on specific features of the movies.

## How it Works

The movie recommendation system works in the following steps:

1. **Data Collection**: The system relies on a dataset containing movie information, including features like movie title, genre, director, actors, and user ratings.

2. **Preprocessing**: The dataset is preprocessed to handle missing data, normalize ratings, and convert categorical features into a numerical format suitable for machine learning algorithms.


3. **Content-Based Filtering**: Content-based filtering recommends movies based on the characteristics and features of the selected movie. It suggests movies with similar genres, directors, or actors.

4. **Recommendation Generation**: Using content-based filtering, the system calculates similarity between the selected movie and others based on their features like genre, overview, director, and actors. It then ranks the movies by similarity and generates a list of the top 10 recommended movies for the user.

5. **User Interface**: The system provides a user-friendly interface where users can input the movie of their choice and receive personalized recommendations.

## Requirements

To run this project, you will need the following dependencies:

- Python 3.x
- Pandas
- NumPy
- Scikit-learn
- Streamlit (for the web interface)


## Installation

1. Clone the repository to your local machine:
```
git clone https://github.com/aayushsoni4/Movie-Recommendation-System.git
cd Movie-Recommendation-System
```
2. Activate the virtual environment:
```
.\venv\Scripts\activate
```
3. Install all the libraries mentioned in the [requirements.txt](https://github.com/aayushsoni4/Movie-Recommendation-System/blob/main/requirements.txt) file with the command 
```
pip install -r requirements.txt
```
4. Run the application:
```
streamlit run app.py
```
5. Access the web interface in your browser by visiting: [`http://localhost:8501`](http://localhost:8501/)

6. Input the name of the movie you like into the search box.

7. Click the `Recommend` button to get the top 10 recommended movies.
