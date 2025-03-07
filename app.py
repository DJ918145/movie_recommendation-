import streamlit as st
import pandas as pd
import pickle


movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)),reverse = True,key = lambda x:x[1])[1:6]
    recommend_movies = []
    for i in movies_list:
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies
        
st.title("Movie Rocomandaiton System")
 
selected_movie_name = st.selectbox('Select a Movie which was you watched ? ', movies['title'].values)
if st.button('Recommend'):
    recommandation = recommend(selected_movie_name)
    for i in recommandation:
        st.write(i)
    
