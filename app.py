import streamlit as st
import pandas as pd 

import streamlit as st
import pandas as pd 
import pickle


def recommend(movie):
    movie_index = movies[movies.title == movie ].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)) , reverse=True , key=lambda x:x[1])[1:6]
    
    recommended_movies = []
    for i in movie_list:
        print(recommended_movies.append(movies.iloc[i[0]].title))
    return recommended_movies
    

movies_dict = pickle.load(open('movie_dict.pkl' , 'rb'))

# print(type(movies_dict))
movies = pd.DataFrame(movies_dict)

similarity =  pickle.load(open('similarity.pkl' , 'rb'))

st.title("Movie Reccommended System")

selected_movie_name = st.selectbox(
    '!How would you like to be contracted',
    movies.title.values)

if st.button("Reccommend"):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)

# st.markdown("""
#     <style>
#     .bottom-right {
#         position: fixed;
#         bottom: 10px;
#         right: 10px;
#         background-color: #f0f2f6;
#         color: #31333f;
#         padding: 10px 15px;
#         border-radius: 10px;
#         box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
#         font-size: 16px;
#         z-index: 9999;
#     }
#     </style>
#     <div class="bottom-right">Thanks for visiting!</div>
# """, unsafe_allow_html=True)

st.markdown("""
    <style>
    @keyframes clink {
        0%   { transform: scale(1); color: #ff4b4b; }
        25%  { transform: scale(1.1); color: #ffa94d; }
        50%  { transform: scale(1.2); color: #ffe14d; }
        75%  { transform: scale(1.1); color: #4dff88; }
        100% { transform: scale(1); color: #4dd2ff; }
    }

    .bottom-right {
        position: fixed;
        bottom: 20px;
        right: 20px;
        font-size: 20px;
        font-weight: bold;
        animation: clink 2s infinite;
        z-index: 9999;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    </style>

    <div class="bottom-right">✨ Thanks for visiting! ✨</div>
""", unsafe_allow_html=True)