# Spotify Song Suggester

A web application allowing users to specify an artist and song to receive the names of five similar songs. 

### Built With
Python
Streamlit

The dataset utilitzed, [Spotify Tracks DB](https://www.kaggle.com/zaheenhamidani/ultimate-spotify-tracks-db), is sourced from Kaggle.
It contains information about 232,725 songs and differentiates their attributes with Spotify's calculated audio features:
acousticness, danceability, duration, energy, instrumentalness, key, liveness, loudness, mode, speechiness, tempo, time signature, and valence.

To determine song similarity by audio features, a predictive model is trained using K-Means clustering.
An interactive user interface, from which an artist name and song title can be input or selected in a dropdown menu, is created with Streamlit.

### Resources
[Movie Recommender System Project](https://youtu.be/1xtrIEwY_zY)

### Deployed App
Spotify Song Suggester is hosted on the Heroku cloud platform, located [here](https://spotifyrecommendation.herokuapp.com/).
