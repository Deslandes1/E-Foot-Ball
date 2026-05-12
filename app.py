import streamlit as st
import pandas as pd
import numpy as np
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="E-FOOTBALL | Gesner Deslandes",
    page_icon="⚽",
    layout="centered"
)

# --- ADVANCED CSS FOR GAMING UI ---
st.markdown("""
    <style>
    .stApp { background-color: #050a0e; }
    .game-title { 
        text-align: center; color: #FFD700; font-size: 50px; 
        font-weight: 900; text-shadow: 0 0 30px #FF0000; margin-bottom: 0px;
    }
    .dev-credit { 
        text-align: center; color: #00FF00; font-size: 20px; 
        font-family: 'Courier New', monospace; font-weight: bold; margin-bottom: 20px;
    }
    .game-container {
        display: flex; justify-content: center;
        border: 4px solid #FFD700; border-radius: 20px;
        background-color: #1a1a1a; padding: 5px;
        box-shadow: 0 0 50px rgba(0, 255, 0, 0.2);
    }
    /* Mobile-Friendly Button Styling */
    .stButton>button {
        width: 100%; height: 60px; font-size: 24px !important;
        font-weight: 900 !important; border-radius: 15px !important;
        background-color: #222 !important; color: gold !important;
        border: 2px solid #FFD700 !important;
    }
    .stButton>button:active {
        background-color: #FFD700 !important; color: black !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SESSION STATE INITIALIZATION ---
if 'player_x' not in st.session_state:
    st.session_state.player_x = 250
if 'player_y' not in st.session_state:
    st.session_state.player_y = 150
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'match_time' not in st.session_state:
    st.session_state.match_time = 90

# --- GAME HEADER ---
st.markdown('<p class="game-title">E-FOOTBALL ENGINE</p>', unsafe_allow_html=True)
st.markdown('<p class="dev-credit">ENGINEERED BY GESNER DESLANDES</p>', unsafe_allow_html=True)

# --- GAME LOGIC FUNCTIONS ---
def move_player(direction):
    step = 25
    if direction == "UP" and st.session_state.player_y > 30:
        st.session_state.player_y -= step
    if direction == "DOWN" and st.session_state.player_y < 270:
        st.session_state.player_y += step
    if direction == "LEFT" and st.session_state.player_x > 30:
        st.session_state.player_x -= step
    if direction == "RIGHT" and st.session_state.player_x < 470:
        st.session_state.player_x += step
    
    # --- GOAL DETECTION (GOLD ZONE) ---
    if st.session_state.player_x > 440 and 110 < st.session_state.player_y < 190:
        st.session_state.score += 1
        st.session_state.player_x = 250  # Reset position
        st.session_state.player_y = 150
        st.balloons()

# --- THE HD VISUAL PITCH (SVG) ---
pitch_svg = f"""
<svg width="100%" height="auto" viewBox="0 0 500 300" style="border-radius: 15px;">
    <defs>
        <linearGradient id="grass" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#2ecc71;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#27ae60;stop-opacity:1" />
        </linearGradient>
        <radialGradient id="playerGlow">
            <stop offset="10%" style="stop-color:#ffffff;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#0000FF;stop-opacity:1" />
        </radialGradient>
    </defs>

    <!-- Pitch Grass -->
    <rect width="500" height="300" fill="url(#grass)" />
    
    <!-- White Markings -->
    <line x1="250" y1="0" x2="250" y2="300" stroke="rgba(255,255,255,0.7)" stroke-width="3" />
    <circle cx="250" cy="150" r="45" stroke="rgba(255,255,255,0.7)" stroke-width="3" fill="none" />
    
    <!-- Penalty Boxes -->
    <rect x="0" y="75" width="60" height="150" stroke="white" stroke-width="2" fill="rgba(255,255,255,0.1)" />
    <rect x="440" y="75" width="60" height="150" stroke="white" stroke-width="2" fill="rgba(255,255,255,0.1)" />
    
    <!-- GOLDEN GOAL POST -->
    <rect x="490" y="115" width="10" height="70" fill="#FFD700" rx="3">
        <animate attributeName="opacity" values="1;0.5;1" dur="1s" repeatCount="indefinite" />
    </rect>

    <!-- THE PLAYER (NO. 10) -->
    <circle cx="{st.session_state.player_x}" cy="{st.session_state.player_y}" r="15" fill="url(#playerGlow)" stroke="#FFD700" stroke-width="3" />
    <text x="{st.session_state.player_x - 7}" y="{st.session_state.player_y + 5}" fill="white" font-size="14" font-family="Arial Black" font-weight="900">10</text>
    
    <!-- Signature inside graphic -->
    <text x="10" y="290" fill="rgba(255,255,255,0.4)" font-size="10" font-family="monospace">GLOBALINTERNET.PY FOOTBALL ENGINE</text>
</svg>
"""

st.markdown(f'<div class="game-container">{pitch_svg}</div>', unsafe_allow_html=True)

# --- LIVE SCOREBOARD ---
c1, c2 = st.columns(2)
with c1:
    st.markdown(f"<h1 style='text-align:right; color:white;'>GOALS:</h1>", unsafe_allow_html=True)
with c2:
    st.markdown(f"<h1 style='text-align:left; color:#FFD700;'>{st.session_state.score}</h1>", unsafe_allow_html=True)

# --- MOBILE & LAPTOP CONTROLS ---
st.markdown("<br>", unsafe_allow_html=True)
ctrl_up, ctrl_reset = st.columns([2, 1])
with ctrl_up:
    if st.button("🔼 MOVE UP"): move_player("UP")
with ctrl_reset:
    if st.button("🔄 RESET"): 
        st.session_state.score = 0
        st.session_state.player_x = 250
        st.session_state.player_y = 150

ctrl_l, ctrl_d, ctrl_r = st.columns(3)
with ctrl_l:
    if st.button("◀️ LEFT"): move_player("LEFT")
with ctrl_d:
    if st.button("🔽 DOWN"): move_player("DOWN")
with ctrl_r:
    if st.button("▶️ RIGHT"): move_player("RIGHT")

# --- FOOTER ---
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("""
    <div style="text-align:center; color: #555; font-weight:bold;">
        © 2026 GLOBALINTERNET.PY | VERSION 2.0 HD<br>
        PROUDLY DEVELOPED IN HAITI BY GESNER DESLANDES
    </div>
    """, unsafe_allow_html=True)
