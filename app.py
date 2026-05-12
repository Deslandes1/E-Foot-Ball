import streamlit as st
import pandas as pd
import numpy as np
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="E-FOOTBALL | Gesner Deslandes", layout="centered")

# --- CUSTOM CSS FOR STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .game-title { 
        text-align: center; color: #FFD700; font-size: 45px; 
        font-weight: 900; text-shadow: 0 0 20px #FF0000; 
    }
    .dev-credit { 
        text-align: center; color: white; font-size: 18px; 
        margin-bottom: 20px; font-style: italic;
    }
    .game-container {
        border: 5px solid #FFD700; border-radius: 15px;
        background-color: #228B22; padding: 10px;
    }
    .control-btn {
        background-color: #444; color: white; border-radius: 10px;
        padding: 20px; text-align: center; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- GAME HEADER ---
st.markdown('<p class="game-title">E-FOOTBALL ENGINE</p>', unsafe_allow_html=True)
st.markdown('<p class="dev-credit">Architected by Gesner Deslandes</p>', unsafe_allow_html=True)

# --- SESSION STATE INITIALIZATION ---
if 'player_x' not in st.session_state:
    st.session_state.player_x = 250
if 'player_y' not in st.session_state:
    st.session_state.player_y = 150
if 'score' not in st.session_state:
    st.session_state.score = 0

# --- GAME LOGIC FUNCTIONS ---
def move_player(direction):
    step = 20
    if direction == "UP" and st.session_state.player_y > 20:
        st.session_state.player_y -= step
    if direction == "DOWN" and st.session_state.player_y < 280:
        st.session_state.player_y += step
    if direction == "LEFT" and st.session_state.player_x > 20:
        st.session_state.player_x -= step
    if direction == "RIGHT" and st.session_state.player_x < 480:
        st.session_state.player_x += step
    
    # Goal Detection Logic
    if st.session_state.player_x > 450 and 120 < st.session_state.player_y < 180:
        st.session_state.score += 1
        st.session_state.player_x = 250 # Reset to center after goal
        st.balloons()

# --- THE VISUAL PITCH (SVG Canvas) ---
# This creates a beautiful, colorful pitch that scales on mobile
pitch_svg = f"""
<svg width="500" height="300" viewBox="0 0 500 300" style="background-color: #2ecc71; border: 3px solid white; border-radius: 10px;">
    <!-- Field Lines -->
    <line x1="250" y1="0" x2="250" y2="300" stroke="white" stroke-width="2" />
    <circle cx="250" cy="150" r="40" stroke="white" stroke-width="2" fill="none" />
    
    <!-- Penalty Areas -->
    <rect x="0" y="75" width="50" height="150" stroke="white" stroke-width="2" fill="none" />
    <rect x="450" y="75" width="50" height="150" stroke="white" stroke-width="2" fill="none" />
    
    <!-- The Goal Target -->
    <rect x="490" y="120" width="10" height="60" fill="#FFD700" />
    
    <!-- THE PLAYER (Controlled by Session State) -->
    <circle cx="{st.session_state.player_x}" cy="{st.session_state.player_y}" r="12" fill="#0000FF" stroke="white" stroke-width="3" />
    <text x="{st.session_state.player_x - 5}" y="{st.session_state.player_y + 5}" fill="white" font-size="10" font-weight="bold">10</text>
</svg>
"""

st.markdown(f'<div class="game-container">{pitch_svg}</div>', unsafe_allow_html=True)

# --- SCOREBOARD ---
st.markdown(f"<h2 style='text-align:center; color:white;'>GOALS: {st.session_state.score}</h2>", unsafe_allow_html=True)

# --- CONTROLS (Laptop & Mobile Compatible) ---
st.markdown("### 🎮 TOUCH CONTROLS")
col1, col2, col3 = st.columns([1,1,1])

with col2:
    if st.button("🔼 UP", use_container_width=True): move_player("UP")

col_left, col_down, col_right = st.columns([1,1,1])
with col_left:
    if st.button("◀️ LEFT", use_container_width=True): move_player("LEFT")
with col_down:
    if st.button("🔽 DOWN", use_container_width=True): move_player("DOWN")
with col_right:
    if st.button("▶️ RIGHT", use_container_width=True): move_player("RIGHT")

# --- FOOTER ---
st.markdown("---")
st.markdown("""
    <div style="text-align:center; color: #888;">
        © 2026 GLOBALINTERNET.PY | Engine: E-Football v1.0<br>
        <b>Software Powered by Python & Gesner Deslandes</b>
    </div>
    """, unsafe_allow_html=True)
