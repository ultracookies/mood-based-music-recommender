from re import search
import streamlit as st
from recommend import get_recommendations
from mood_analysis import analyze_text_mood

from utils.spotify_utils import search_tracks

# --- Streamlit UI ---

st.set_page_config(page_title="Mood-based Music Recommender 🎵", layout="centered")

st.title("🎧 Mood-based Music Recommender")
st.write("Get music recommendations based on your current mood.")

# Option 1: Pick a mood from a list
mood = st.selectbox(
    "Select your mood:",
    ["Happy", "Sad", "Energetic", "Calm", "Romantic", "Angry", "Focus", "Party"]
)

# Option 2: Input freeform mood description
custom_mood_text = st.text_input("Or describe your mood:", "")

# Combine logic
if custom_mood_text:
    mood = analyze_text_mood(custom_mood_text)  # NLP-based mood classification

if st.button("Get Recommendations"):
    with st.spinner("Finding tracks that match your vibe..."):
        tracks = get_recommendations(mood)
        print(tracks)
        
        if not tracks:
            st.warning("No tracks found. Try a different mood.")
        else:
            st.success(f"Showing tracks for mood: **{mood}**")
            for track in tracks:
                st.markdown(f"""
                    **🎵 {track['name']}** by {track['artist']}  
                    [Listen on Spotify]({track['url']})  
                """)
