# song-suggest

### Spotify Song Suggester

## Method

The dataset utilitzed, [Spotify Tracks DB](https://www.kaggle.com/zaheenhamidani/ultimate-spotify-tracks-db), was sourced from Kaggle.
It contains information about 232,725 songs, differentiating song qualities using thirteen of Spotify's calculated audio features:
acousticness, danceability, duration, energy, instrumentalness, key, liveness, loudness, mode, speechiness, tempo, time signature, and valence.

A predictive model for song similarity determined by audio features was trained using K-Means clustering.

The app framework Steamlit was used to make an interactive interface from which an artist name and song title could be input or selected in a dropdown menu.
