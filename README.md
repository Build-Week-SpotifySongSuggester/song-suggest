# song-suggest

# Spotify Song Suggester

The dataset utilitzed, [Spotify Tracks DB](https://www.kaggle.com/zaheenhamidani/ultimate-spotify-tracks-db), was sourced from Kaggle.
It contains information about 232,725 songs and differentiates their attributes with Spotify's calculated audio features:
acousticness, danceability, duration, energy, instrumentalness, key, liveness, loudness, mode, speechiness, tempo, time signature, and valence.

To determine song similarity by audio features, a predictive model was trained using K-Means clustering.
An interactive user interface, from which an artist name and song title could be input or selected in a dropdown menu, was created with Streamlit.

### Resources
[Movie Recommender System Project](https://youtu.be/1xtrIEwY_zY)

### Deployed App
Spotify Song Suggester app is hosted on the Heroku cloud platform.  It is located [here](https://spotifyrecommendation.herokuapp.com/).
