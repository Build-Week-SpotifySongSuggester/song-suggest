import pickle
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import func

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)
df = pd.read_csv('songs.csv')

st.title('Music Recommend System')
musics_dict = pickle.load(open('music_dict.pkl', 'rb'))
musics = pd.DataFrame(musics_dict)

selected_artist = st.selectbox(
    "Type or select an artist from the dropdown",
    musics['artist_name'].values,
    index=8000
)

selected_music = st.selectbox(
    "Type or select a song from the dropdown",
    musics[musics['artist_name']==selected_artist]['track_name'].values,
    index=8000
)

if st.button('Recommend'):
    st.write(func.playlist_song(selected_music, selected_artist, df))
if st.button('Tempo'):
    st.write(func.find_similar(selected_music, selected_artist, df))
