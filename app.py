import streamlit as st
import pickle
import pandas as pd


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]  # fetching of index
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),
        reverse=True,key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
      movie_id = movies.iloc[i[0]].movie_id
      recommended_movies.append(movies.iloc[i[0]].title)
      
    return recommended_movies


movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)



similarity = pickle.load(open('similarity.pkl','rb'))



st.title('Movies for you')

selected_movie_name = st.selectbox(
 'which movie did you watched ?',
 movies['title'].values)



if st.button('Recommend'):
   names= recommend(selected_movie_name)
   'your recommended Movies Are !! '
   for i in names:
         st.write(i)


   st.success(" Thanks for asking come here again after completing all these !!! ")

