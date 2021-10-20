import pickle
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import func
from sklearn.metrics.pairwise import cosine_similarity
auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)
df = pd.read_csv('songs.csv')


st.title('Music Recommend System')
musics_dict = pickle.load(open('music_dict.pkl', 'rb'))
musics = pd.DataFrame(musics_dict)
selected_music = st.selectbox(
    "Type or select a music from the dropdown",
    musics['track_name'].values
)
selected_artist = st.selectbox(
    "Type or select a music from the dropdown",
    musics['artist_name'].values
)


# def recommend(music):
#     database = df[df.popularity > 0.5].reset_index(drop=True)
#     # indx_names = database[['track_name', 'artist_name', 'Cluster']]
#     songs_train = database.drop(
#         ['track_name', 'artist_name', 'Cluster'], axis=1)
#     cos_dists = cosine_similarity(songs_train, songs_train)

#     index = df[df['track_name'] == music].index[0]
#     distances = sorted(
#         list(enumerate(cos_dists[index])), reverse=True, key=lambda x: x[1])
#     recommended_music = []
#     for i in distances[1:6]:
#         recommended_music.append(musics.iloc[i[0]].title)
#     return recommended_music


if st.button('Recommend'):
    st.write(func.playlist_song(selected_music, selected_artist, df))

    # def create_app():
    #     app = Flask(__name__)

    #     #app.config["SQLALCHEMY_DATABASE_URI"] = config("DATABASE_URI")
    #     #app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    #     # Create tables
    #     # with app.app_context():
    #     # db.create_all()

    #     @app.route('/')
    #     def root():
    #         return 'Hello hello hellooooooooooo'

    #     return app
kjk
