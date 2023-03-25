import pandas as pd
import streamlit as st
import pickle



def recommend(songs):
    song_index = data[data['song'] == songs].index[0]
    distance = similarity[song_index]
    song_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:11]
    recommended_songs = []

    for i in range(len(song_list)):

        recommended_songs.append(data.iloc[song_list[i][0]].song)
    return recommended_songs


songs_dict = pickle.load(open('data_dict.pk1', 'rb'))
data = pd.DataFrame(songs_dict)

similarity = pickle.load(open('similarity.pk1', 'rb'))

st.title('Music Recommendation System')

selected_song_name = st.selectbox(
    'SEARCH AND SELECT THE SONG YOU LIKED MOST',
    data['song'].values)

if st.button('Recommend'):
    names = recommend(selected_song_name)
    names


