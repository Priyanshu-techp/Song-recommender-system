import pandas as pd
import streamlit as st
import joblib
from sklearn.metrics.pairwise import linear_kernel
import streamlit.components.v1 as components

df = pd.read_csv('Data/spotify_library.csv')
tf_vectorize = joblib.load('Deploying/tf_vectorizer.pkl')
vector = joblib.load('Deploying/vector.pkl')

def recommand(song_name):
    try:
        song_index = df[df['Track Name'] == song_name].index[0]
        similarity = linear_kernel(vector[song_index], vector).flatten()
        similar_song = similarity.argsort()[-6:-1][::-1]
        return [df.iloc[x]['Spotify URL'] for x in similar_song]
    except IndexError:
        return []

st.title('Song Recommendation System')
song_list = df['Track Name'].values
selected_song = st.selectbox('Choose your song', song_list)

if st.button('Recommend Song'):
    selected_url = df[df['Track Name'] == selected_song]['Spotify URL'].values[0]
    selected_embed = selected_url.replace("open.spotify.com/track/", "open.spotify.com/embed/track/")

    st.subheader("Now Playing: " + selected_song)
    components.iframe(selected_embed, width=400, height=200, scrolling=False)


    recommandations = recommand(selected_song)
    if recommandations:
        st.subheader("Recommended Songs")
        cols = st.columns(2)

        for i, url in enumerate(recommandations):
            embed_url = url.replace("open.spotify.com/track/", "open.spotify.com/embed/track/")
            with cols[i % 2]:
                    st.markdown(
                        """
                          <div style="border-radius:15px; 
                          background-color:#1DB95420; 
                          padding:20px; 
                          margin-bottom:25px; 
                          box-shadow: 0 6px 14px rgba(0,0,0,0.3);">
                        ""","""
                        unsafe_allow_html=True
            )

            components.iframe(embed_url, width=400, height=200, scrolling=False)
            st.markdown("</div>", unsafe_allow_html=True)




# streamlit run 'Deploying/song_rec.py'
