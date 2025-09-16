import streamlit as st
import pickle
import pandas as pd
import requests

#skipping this api integration
# def fetch_poster(movie_id):
#     response=requests.get('https://api.themoviedb.org/3/movie/{}?language=en-US&api_key=4eb870b9774b3b0453d8d1ce9189a68c'.format(movie_id))
#     data= response.json()
#     return data['poster_path']

def recommend(movie):
    # Find the index of the selected movie from the movies DataFrame
    movie_index = movies[movies['title'] == movie].index[0]

    # Get the similarity scores for that movie
    distances = similarity[movie_index]

    # Sort the movies based on similarity scores
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:

        movie_id=i[0]
        # fetch poster from API


        # Append the title of the recommended movie using its index
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


# Load the similarity matrix
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Load the movies dictionary and convert it to a DataFrame
movies_dict = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

st.title('Movie Recommender System')

# Use the 'title' column from the DataFrame for the selectbox
selected_movie_name = st.selectbox(
    "Select a movie:",
    movies['title'].values
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)