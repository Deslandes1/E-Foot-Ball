import streamlit as st
import base64
from datetime import datetime

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Coopératives & Agroécologie",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- CUSTOM CSS FOR VIBRANT COLORS ----------
def get_colorful_css():
    return """
    <style>
    /* Global background gradient */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #e9f5e9 100%);
    }
    /* Login page container */
    .login-container {
        text-align: center;
        background: linear-gradient(145deg, #fff8e7, #fceabb);
        padding: 2.5rem;
        border-radius: 60px;
        box-shadow: 0 20px 35px rgba(0,0,0,0.2);
        max-width: 500px;
        margin: 10% auto;
        border: 2px solid #ffb347;
    }
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    @keyframes shine {
        0% { opacity: 0.6; text-shadow: 0 0 2px gold; }
        50% { opacity: 1; text-shadow: 0 0 20px orange, 0 0 5px yellow; }
        100% { opacity: 0.6; text-shadow: 0 0 2px gold; }
    }
    @keyframes bounce {
        0%,100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }
    .spinning-icon {
        animation: spin 4s linear infinite;
        display: inline-block;
        font-size: 3.5rem;
        margin: 0 10px;
    }
    .shining-text {
        animation: shine 2s ease-in-out infinite;
        font-weight: bold;
        background: linear-gradient(45deg, #ff6b6b, #feca57, #48dbfb);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        font-size: 2.2rem;
    }
    .bouncing-icon {
        animation: bounce 1.5s infinite;
        display: inline-block;
        font-size: 2rem;
    }
    /* Colorful button */
    div.stButton > button {
        background: linear-gradient(90deg, #ff8c00, #ff2e00);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 0.6rem 1.8rem;
        font-weight: bold;
        font-size: 1.1rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        transition: 0.3s;
    }
    div.stButton > button:hover {
        transform: scale(1.02);
        background: linear-gradient(90deg, #ff9f2e, #ff4411);
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    }
    /* Sidebar customization */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #2c3e2f, #1e3b2a);
        border-right: 3px solid #f39c12;
    }
    [data-testid="stSidebar"] * {
        color: #ffffff !important;
    }
    .sidebar-content {
        background-color: rgba(0,0,0,0.2);
        padding: 1rem;
        border-radius: 20px;
    }
    /* Lesson expander headers */
    .streamlit-expanderHeader {
        background: linear-gradient(95deg, #ffecd2, #fcb69f);
        border-radius: 30px;
        font-weight: bold;
        font-size: 1.2rem;
        color: #2d2d2d !important;
        border: 1px solid #ffaa44;
    }
    .streamlit-expanderHeader:hover {
        background: linear-gradient(95deg, #ffe0b5, #ffa559);
    }
    /* Lesson content card */
    .lesson-card {
        background: rgba(255,255,240,0.95);
        border-radius: 30px;
        padding: 1rem;
        box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    /* Footer */
    .footer {
        text-align: center;
        margin-top: 3rem;
        padding: 1rem;
        background: linear-gradient(90deg, #2ecc71, #27ae60);
        border-radius: 30px;
        color: white;
        font-weight: bold;
    }
    </style>
    """

# ---------- AUTHENTICATION ----------
PASSWORD = "20082010"

def check_password():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if not st.session_state.authenticated:
        st.markdown(get_colorful_css(), unsafe_allow_html=True)
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        st.markdown("""
            <div>
                <span class="spinning-icon">🌾</span>
                <span class="spinning-icon">🍎</span>
                <span class="spinning-icon">🥕</span>
                <span class="spinning-icon">🌽</span>
            </div>
            <h1 class="shining-text">🌱 COOPÉRATIVES & AGROÉCOLOGIE 🌱</h1>
            <p style="font-size:1.2rem;">Built by <strong>Gesner Deslandes</strong> / GlobalInternet.py</p>
            <p style="font-size:1rem;">🍅 Enter the password to access the 20‑day farming training 🧑‍🌾</p>
        """, unsafe_allow_html=True)
        password = st.text_input("🔐 Password", type="password", key="login_pass")
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            if st.button("🌻 Unlock the Farm 🌻", use_container_width=True):
                if password == PASSWORD:
                    st.session_state.authenticated = True
                    st.rerun()
                else:
                    st.error("❌ Incorrect password. Access denied.")
        st.markdown('</div>', unsafe_allow_html=True)
        return False
    return True

# ---------- LESSONS DATA (same as before) ----------
lessons = {
    1: {
        "title": "Day 1: Introduction to Agroecology",
        "text": "Agroecology is a holistic approach that applies ecological principles to agriculture. It aims to create sustainable, productive, and resilient farming systems. Instead of relying on chemical inputs, agroecology works with nature: building healthy soils, encouraging biodiversity, and integrating crops and livestock. By mimicking natural ecosystems, farmers can reduce costs, protect the environment, and produce healthy food. Agroecology also respects local knowledge and empowers farmers to become innovators. This first day sets the foundation for our 20‑day journey into regenerative farming.",
        "image": "https://images.pexels.com/photos/164504/pexels-photo-164504.jpeg?auto=compress&cs=tinysrgb&w=600"
    },
    2: {
        "title": "Day 2: The Importance of Soil Health",
        "text": "Healthy soil is the living, breathing foundation of any farm. It is not just dirt – it is a complex ecosystem of microorganisms, fungi, earthworms, and organic matter. Good soil structure allows water to infiltrate, roots to grow deep, and nutrients to cycle naturally. Practices like cover cropping, reduced tillage, and adding compost rebuild soil organic matter. Soil health directly affects crop resilience, yields, and nutritional quality. Today we learn how to assess your soil and simple ways to improve it without expensive chemicals.",
        "image": "https://images.pexels.com/photos/247405/pexels-photo-247405.jpeg?auto=compress&cs=tinysrgb&w=600"
    },
    3: {
        "title": "Day 3: Water Management and Weather Importance",
        "text": "Water is life, but too much or too little can destroy crops. Understanding local weather patterns – rainfall, droughts, storms – is crucial for planning. Techniques like rainwater harvesting, drip irrigation, mulching, and contour farming help capture and use water efficiently. Weather forecasting tools and simple on‑farm weather stations allow farmers to make timely decisions. Sanitation around water sources prevents contamination. Today we explore how to manage water wisely in the face of climate variability.",
        "image": "https://images.pexels.com/photos/292114/pexels-photo-292114.jpeg?auto=compress&cs=tinysrgb&w=600"
    },
    4: {
        "title": "Day 4: Reducing Chemical Inputs – Natural Alternatives",
        "text": "Chemical fertilizers and pesticides can harm soil life, pollinators, and human health. There are many natural alternatives: compost tea, neem oil, beneficial insects, and crop rotation. By observing your fields regularly, you can identify problems early and use targeted organic solutions. This lesson presents a step‑by‑step guide to transition away from synthetic inputs, starting with one field or crop. Small changes lead to big benefits for your wallet and the environment.",
        "image": "https://images.pexels.com/photos/1264320/pexels-photo-1264320.jpeg?auto=compress&cs=tinysrgb&w=600"
    },
    5: {
        "title": "Day 5: Crop Rotation and Diversity",
        "text": "Growing the same crop year after year depletes nutrients and invites pests. Crop rotation means changing the plant family in each field every season. For example, follow a nitrogen‑fixing legume with a heavy feeder like corn. Intercropping (mixing crops) also reduces pest outbreaks and improves soil health. Diversity creates resilience. Today we design a simple rotation plan for a small garden and learn why polycultures outperform monocultures.",
        "image": "https://images.pexels.com/photos/101708/pexels-photo-101708.jpeg?auto=compress&cs=tinysrgb&w=600"
    },
    6: {
        "title": "Day 6: Composting and Organic Fertilizers",
        "text": "Compost turns farm waste into black gold. Anything that once lived – plant residues, manure, kitchen scraps – can be composted. A good compost pile balances greens (nitrogen) and browns (carbon), with enough moisture and air. After a few months, you get a rich, earthy fertilizer that feeds soil microbes. We also explore other organic fertilizers like worm castings, green manure, and biochar. This lesson teaches how to build a simple compost heap and use it effectively.",
        "image": "https://images.pexels.com/photos/5849561/pexels-photo-5849561.jpeg?auto=compress&cs=tinysrgb&w=600"
    },
    7: {
        "title": "Day 7: Pest Management without Pesticides",
        "text": "Integrated Pest Management (IPM) uses observation, prevention, and natural controls. Start by encouraging beneficial insects (ladybugs, lacewings) by planting flowers. Use physical barriers like nets or traps. When needed, apply botanical sprays (neem, garlic) that break down quickly. Rotate crops and remove infested plants. This approach reduces pesticide resistance and protects pollinators. Today we identify common garden pests and their natural enemies.",
        "image": "https://images.pexels.com/photos/79621/pexels-photo-79621.jpeg?auto=compress&cs=tinysrgb&w=600"
    },
    8: {
        "title": "Day 8: The Role of Cooperatives in Agriculture",
        "text": "Individual farmers often struggle to access markets, get fair prices, or buy inputs cheaply. Cooperatives – groups of farmers who work together – solve these problems. They pool resources, share knowledge, and negotiate better deals. In Laos and Cambodia, cooperatives have helped members increase incomes and adopt sustainable practices. Today we learn how to start or join a cooperative: rules, benefits, and success stories from the field.",
        "image": "https://images.pexels.com/photos/6646839/pexels-photo-6646839.jpeg?auto=compress&cs=tinysrgb&w=600"
    },
    9: {
        "title": "Day 9: Certification and Market Access",
        "text": "Certification schemes (organic, fair trade, Rainforest Alliance) help farmers prove their products are sustainable. They open doors to premium markets and build consumer trust. However, certification can be expensive. Group certification for cooperatives reduces costs. This lesson explains the steps to get certified, the documents needed, and how to find buyers who value sustainability. Case studies from Southeast Asia show how certification changed farmers' lives.",
        "image": "https://images.pexels.com/photos/4488638/pexels-photo-4488638.jpeg?auto=compress&cs=tinysrgb&w=600"
    },
    10: {
        "title": "Day 10: Post-Harvest Handling and Sanitation",
        "text": "After harvest, fruits and vegetables continue to breathe. Poor handling leads to rot and waste. Sanitation is key: clean storage areas, wash hands, use clean water, and separate produce from soil. Techniques like curing, cooling, and proper packaging extend shelf life. This lesson covers simple low‑cost methods to reduce post‑harvest losses, improve food safety, and increase profits. Good hygiene also prevents foodborne illnesses.",
        "image": "https://images.pexels.com/photos/6210278/pexels-photo-6210278.jpeg?auto=compress&cs=tinysrgb&w=600"
    },
    11: {
        "title": "Day 11: Seed Saving and Biodiversity",
        "text": "Saving your own seeds saves money and adapts crops to your local conditions. Choose open‑pollinated varieties, not hybrids. Learn how to harvest, dry, and store seeds properly. Seed banks and farmer networks preserve genetic diversity. This lesson explains how to save seeds from common vegetables like tomatoes, beans, and squash. Biodiversity in the field also means planting heirloom varieties that resist diseases naturally.",
        "image": "https://images.pexels.com/photos/789658/pexels-photo-789658.jpeg?auto=compress&cs=tinysrgb&w=600"
    },
    12: {
        "title": "Day 12: Agroforestry and Tree Integration",
        "text": "Agroforestry combines trees with crops or livestock. Trees provide shade, windbreaks, fruits, timber, and improve soil fertility through leaf litter. They also sequester carbon. In tropical countries, alley cropping with fast‑growing trees like gliricidia enriches the soil. This lesson introduces different agroforestry systems and how to choose the right trees for your farm. We also see examples from Laos where agroforestry restored degraded land.",
        "image": "https://images.pexels.com/photos/247478/pexels-photo-247478.jpeg?auto=compress&cs=tinysrgb&w=600"
    },
    13: {
        "title": "Day 13: Climate-Resilient Farming",
        "text": "Climate change brings more extreme weather: droughts, floods, heatwaves. Resilient farms adapt by diversifying crops, improving water storage, using drought‑tolerant varieties, and building healthy soil that holds moisture. Agroecological practices like mulching, windbreaks, and contour farming reduce risks. Today we explore a checklist to assess your farm's vulnerability and a toolkit of resilience strategies that have worked in Cambodia and Laos.",
        "image": "https://images.pexels.com/photos/1301856/pexels-photo-1301856.jpeg?auto=compress&cs=tinysrgb&w=600"
    },
    14: {
        "title": "Day 14: Small-Scale Irrigation Techniques",
        "text": "Not every farm has a river. Small‑scale irrigation can be as simple as a bucket and a hose, or more advanced like drip kits. Rainwater harvesting from roofs, small ponds, or underground tanks provides water during dry spells. Solar pumps are becoming affordable. This lesson compares different low‑cost irrigation methods, their water efficiency, and how to maintain them. We also discuss water sanitation to avoid algal growth.",
        "image": "https://images.pexels.com/photos/1081483/pexels-photo-1081483.jpeg?auto=compress&cs=tinysrgb&w=600"
    },
    15: {
        "title": "Day 15: Livestock Integration in Agroecology",
        "text": "Animals and crops work better together. Chickens eat pests and provide manure; pigs can be rotated on crop residues; cattle graze cover crops. Integrating livestock recycles nutrients, reduces waste, and creates multiple income streams. However, it requires careful management to prevent overgrazing and water contamination. Today we learn rotational grazing, manure composting, and how to design a mixed farm using the Cambodian experience.",
        "image": "https://images.pexels.com/photos/2487312/pexels-photo-2487312.jpeg?auto=compress&cs=tinysrgb&w=600"
    },
    16: {
        "title": "Day 16: Women and Youth in Agriculture",
        "text": "Women and young people are vital to the future of farming, but they often lack access to land, credit, and training. Empowering them with leadership roles in cooperatives and decision‑making increases productivity and family well‑being. This lesson showcases successful projects from Laos where women‑led vegetable gardens and youth agri‑entrepreneurship transformed communities. We discuss practical steps to make agriculture more inclusive.",
        "image": "https://images.pexels.com/photos/1423607/pexels-photo-1423607.jpeg?auto=compress&cs=tinysrgb&w=600"
    },
    17: {
        "title": "Day 17: Policy and Support for Farmers",
        "text": "Government policies can help or hinder sustainable agriculture. Subsidies for chemicals, trade agreements, and land tenure laws all affect farmers. This lesson guides you on how to advocate for supportive policies – joining farmer networks, participating in consultations, and using media. We also present examples of successful policy changes in Southeast Asia that promoted agroecology and cooperative development.",
        "image": "https://images.pexels.com/photos/6750745/pexels-photo-6750745.jpeg?auto=compress&cs=tinysrgb&w=600"
    },
    18: {
        "title": "Day 18: Learning from Others – Exchange Visits (Laos Example)",
        "text": "Visiting other farms and countries opens your mind. A recent exchange from Cambodia to Laos (March 31 – April 5, 2026) taught four key lessons: (1) Agroecology works in practice; (2) Certification opens markets; (3) Cooperatives bring fairer incomes; (4) Cross‑learning builds lasting networks. Today we dive into these lessons and how you can organize your own exchange visits, even locally, to boost innovation.",
        "image": "https://images.pexels.com/photos/129115/pexels-photo-129115.jpeg?auto=compress&cs=tinysrgb&w=600"
    },
    19: {
        "title": "Day 19: Building a Local Food System",
        "text": "Shortening the distance from farm to fork reduces emissions and keeps money in the community. Local food systems include farmers’ markets, community‑supported agriculture (CSA), school feeding programs, and farm‑to‑restaurant partnerships. This lesson explains how to map your local food actors, create a brand, and use social media to sell directly. We also cover food safety regulations and storytelling to attract customers.",
        "image": "https://images.pexels.com/photos/618776/pexels-photo-618776.jpeg?auto=compress&cs=tinysrgb&w=600"
    },
    20: {
        "title": "Day 20: The Future of Farming – Technology and Tradition",
        "text": "The best agriculture marries ancient wisdom with modern tools. Drones, soil sensors, mobile apps for weather, and blockchains for traceability can complement traditional knowledge. But technology is only a tool; the heart remains the farmer’s connection to land and community. On this final day, we reflect on the 20‑day journey and encourage you to pick one new practice to implement. A sustainable future is built step by step, together.",
        "image": "https://images.pexels.com/photos/3873696/pexels-photo-3873696.jpeg?auto=compress&cs=tinysrgb&w=600"
    }
}

# ---------- AUDIO FUNCTION (TTS) ----------
def text_to_speech_button(text, lang_code, button_label="🔊 Listen"):
    lang_map = {'en': 'en-US', 'fr': 'fr-FR', 'es': 'es-ES'}
    tts_lang = lang_map.get(lang_code, 'en-US')
    safe_text = text.replace("'", "\\'").replace('"', '\\"')
    html = f"""
    <button id="ttsBtn" style="background-color:#ffaa44; border:none; border-radius:30px; padding:8px 18px; margin:5px; cursor:pointer; font-weight:bold; color:#2c2c2c;">{button_label}</button>
    <script>
    (function() {{
        const btn = document.getElementById('ttsBtn');
        if (!btn) return;
        btn.onclick = function() {{
            let utterance = new SpeechSynthesisUtterance("{safe_text}");
            utterance.lang = "{tts_lang}";
            window.speechSynthesis.cancel();
            window.speechSynthesis.speak(utterance);
        }};
    }})();
    </script>
    """
    return html

# ---------- MAIN APP ----------
def main_app():
    st.markdown(get_colorful_css(), unsafe_allow_html=True)

    # Language selection
    lang = st.selectbox("🌐 Language / Idioma / Langue", ["English", "Français", "Español"], index=0)
    if lang == "English":
        lang_code = "en"
        welcome = "🌾 COOPÉRATIVES & AGROÉCOLOGIE – 20‑Day Training Book 🌾"
        day_prefix = "Day"
        listen_btn = "🔊 Listen to this lesson"
        logout_btn = "🚪 Logout"
    elif lang == "Français":
        lang_code = "fr"
        welcome = "🌾 COOPÉRATIVES & AGROÉCOLOGIE – Livre de formation en 20 jours 🌾"
        day_prefix = "Jour"
        listen_btn = "🔊 Écouter cette leçon"
        logout_btn = "🚪 Déconnexion"
    else:
        lang_code = "es"
        welcome = "🌾 COOPÉRATIVES & AGROÉCOLOGIE – Libro de capacitación de 20 días 🌾"
        day_prefix = "Día"
        listen_btn = "🔊 Escuchar esta lección"
        logout_btn = "🚪 Cerrar sesión"

    st.title(welcome)
    st.markdown("---")

    # Sidebar
    with st.sidebar:
        st.markdown("## 🌟 **Gesner Deslandes**")
        st.markdown("👨‍💻 *Chief Engineer at GlobalInternet.py*")
        st.markdown("🌍 **We build softwares on demand**")
        st.markdown("---")
        st.markdown("#### 📚 Training Summary")
        st.markdown("20 lessons covering:")
        st.markdown("✅ Agroecology\n✅ Soil & Water\n✅ Cooperatives\n✅ Certification\n✅ Pest Management\n✅ Post‑harvest\n✅ Agroforestry\n✅ Climate resilience\n✅ Exchange visits (Laos)\n✅ Local food systems")
        st.markdown("---")
        st.markdown("🔊 *Each lesson includes text, image, and audio*")
        st.markdown("---")
        if st.button(logout_btn, use_container_width=True):
            st.session_state.authenticated = False
            st.rerun()

    # Display lessons in colorful expanders
    for day in range(1, 21):
        lesson = lessons[day]
        with st.expander(f"📖 {day_prefix} {day}: {lesson['title']}"):
            col1, col2 = st.columns([2, 1])
            with col1:
                st.markdown(f"<div class='lesson-card'><h3>{lesson['title']}</h3>", unsafe_allow_html=True)
                st.write(lesson['text'])
                audio_html = text_to_speech_button(lesson['text'], lang_code, listen_btn)
                st.components.v1.html(audio_html, height=80)
                st.markdown("</div>", unsafe_allow_html=True)
            with col2:
                st.image(lesson['image'], use_container_width=True, caption=f"Day {day} illustration")
    st.markdown('<div class="footer">© GlobalInternet.py – Coopératives & Agroécologie – Empowering farmers with sustainable knowledge</div>', unsafe_allow_html=True)

# ---------- RUN ----------
if check_password():
    main_app()
