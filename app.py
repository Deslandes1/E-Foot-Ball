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
        width: 100%; height: 65px; font-size: 24px !important;
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
    
    # --- GOAL DETECTION LOGIC ---
    # Detects if player enters the Golden Goal zone
    if st.session_state.player_x > 440 and 110 < st.session_state.player_y < 190:
        st.session_state.score += 1
        st.session_state.player_x = 250  
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

# --- SCOREBOARD ---
col_sc1, col_sc2 = st.columns(2)
with col_sc1:
    st.markdown("<h2 style='text-align:right; color:white; margin-top:10px;'>MATCH SCORE:</h2>", unsafe_allow_html=True)
with col_sc2:
    st.markdown(f"<h2 style='text-align:left; color:#FFD700; margin-top:10px;'>{st.session_state.score}</h2>", unsafe_allow_html=True)

# --- CONTROLS ---
st.markdown("<br>", unsafe_allow_html=True)
c_up, c_res = st.columns([2, 1])
with c_up:
    if st.button("🔼 UP"): move_player("UP")
with c_res:
    if st.button("🔄 RESET"): 
        st.session_state.score = 0
        st.session_state.player_x = 250
        st.session_state.player_y = 150

c_l, c_d, c_r = st.columns(3)
with c_l:
    if st.button("◀️ LEFT"): move_player("LEFT")
with c_d:
    if st.button("🔽 DOWN"): move_player("DOWN")
with c_r:
    if st.button("▶️ RIGHT"): move_player("RIGHT")

# --- FOOTER ---
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("""
    <div style="text-align:center; color: #888; font-family:monospace;">
        © 2026 GLOBALINTERNET.PY | DESIGNED BY GESNER DESLANDES<br>
        <b>OPTIMIZED FOR CROSS-PLATFORM PERFORMANCE</b>
    </div>
    """, unsafe_allow_html=True)
