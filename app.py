import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Coopératives & Agroécologie",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- CUSTOM CSS ----------
def get_colorful_css():
    return """
    <style>
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #e9f5e9 100%);
    }
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
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #2c3e2f, #1e3b2a);
        border-right: 3px solid #f39c12;
    }
    [data-testid="stSidebar"] * {
        color: #ffffff !important;
    }
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
    .lesson-card {
        background: rgba(255,255,240,0.95);
        border-radius: 30px;
        padding: 1rem;
        box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
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

# ---------- LESSONS WITH FULL TRANSLATIONS (20 DAYS) ----------
lessons = {
    1: {
        "title_en": "Day 1: Introduction to Agroecology",
        "title_fr": "Jour 1 : Introduction à l'agroécologie",
        "title_es": "Día 1: Introducción a la Agroecología",
        "text_en": "Agroecology is a holistic approach that applies ecological principles to agriculture. It aims to create sustainable, productive, and resilient farming systems. Instead of relying on chemical inputs, agroecology works with nature: building healthy soils, encouraging biodiversity, and integrating crops and livestock. By mimicking natural ecosystems, farmers can reduce costs, protect the environment, and produce healthy food. Agroecology also respects local knowledge and empowers farmers to become innovators. This first day sets the foundation for our 20‑day journey into regenerative farming.",
        "text_fr": "L'agroécologie est une approche holistique qui applique les principes écologiques à l'agriculture. Elle vise à créer des systèmes agricoles durables, productifs et résilients. Au lieu de dépendre des intrants chimiques, l'agroécologie travaille avec la nature : construire des sols sains, encourager la biodiversité et intégrer cultures et élevage. En imitant les écosystèmes naturels, les agriculteurs peuvent réduire leurs coûts, protéger l'environnement et produire des aliments sains. L'agroécologie respecte également les savoirs locaux et donne aux agriculteurs les moyens de devenir des innovateurs. Ce premier jour pose les bases de notre voyage de 20 jours vers une agriculture régénératrice.",
        "text_es": "La agroecología es un enfoque holístico que aplica principios ecológicos a la agricultura. Su objetivo es crear sistemas agrícolas sostenibles, productivos y resilientes. En lugar de depender de insumos químicos, la agroecología trabaja con la naturaleza: construyendo suelos saludables, fomentando la biodiversidad e integrando cultivos y ganadería. Al imitar los ecosistemas naturales, los agricultores pueden reducir costos, proteger el medio ambiente y producir alimentos saludables. La agroecología también respeta el conocimiento local y empodera a los agricultores para que sean innovadores. Este primer día sienta las bases de nuestro viaje de 20 días hacia la agricultura regenerativa.",
        "image": "https://images.pexels.com/photos/164504/pexels-photo-164504.jpeg"
    },
    2: {
        "title_en": "Day 2: The Importance of Soil Health",
        "title_fr": "Jour 2 : L'importance de la santé des sols",
        "title_es": "Día 2: La importancia de la salud del suelo",
        "text_en": "Healthy soil is the living, breathing foundation of any farm. It is not just dirt – it is a complex ecosystem of microorganisms, fungi, earthworms, and organic matter. Good soil structure allows water to infiltrate, roots to grow deep, and nutrients to cycle naturally. Practices like cover cropping, reduced tillage, and adding compost rebuild soil organic matter. Soil health directly affects crop resilience, yields, and nutritional quality. Today we learn how to assess your soil and simple ways to improve it without expensive chemicals.",
        "text_fr": "Un sol sain est le fondement vivant et respirant de toute ferme. Ce n'est pas seulement de la terre – c'est un écosystème complexe de micro-organismes, champignons, vers de terre et matière organique. Une bonne structure du sol permet à l'eau de s'infiltrer, aux racines de pousser profondément et aux nutriments de circuler naturellement. Des pratiques comme les cultures de couverture, le travail réduit du sol et l'ajout de compost reconstruisent la matière organique du sol. La santé du sol affecte directement la résilience des cultures, les rendements et la qualité nutritionnelle. Aujourd'hui, nous apprenons à évaluer votre sol et des moyens simples de l'améliorer sans produits chimiques coûteux.",
        "text_es": "Un suelo sano es la base viva y respirante de cualquier granja. No es solo tierra – es un ecosistema complejo de microorganismos, hongos, lombrices y materia orgánica. Una buena estructura del suelo permite que el agua se infiltre, las raíces crezcan profundamente y los nutrientes circulen naturalmente. Prácticas como cultivos de cobertura, labranza reducida y agregar compost reconstruyen la materia orgánica del suelo. La salud del suelo afecta directamente la resiliencia de los cultivos, los rendimientos y la calidad nutricional. Hoy aprendemos a evaluar su suelo y formas sencillas de mejorarlo sin costosos químicos.",
        "image": "https://images.pexels.com/photos/247405/pexels-photo-247405.jpeg"
    },
    3: {
        "title_en": "Day 3: Water Management and Weather Importance",
        "title_fr": "Jour 3 : Gestion de l'eau et importance du climat",
        "title_es": "Día 3: Manejo del agua e importancia del clima",
        "text_en": "Water is life, but too much or too little can destroy crops. Understanding local weather patterns – rainfall, droughts, storms – is crucial for planning. Techniques like rainwater harvesting, drip irrigation, mulching, and contour farming help capture and use water efficiently. Weather forecasting tools and simple on‑farm weather stations allow farmers to make timely decisions. Sanitation around water sources prevents contamination. Today we explore how to manage water wisely in the face of climate variability.",
        "text_fr": "L'eau est la vie, mais trop ou trop peu peut détruire les récoltes. Comprendre les régimes météorologiques locaux – précipitations, sécheresses, tempêtes – est crucial pour la planification. Des techniques comme la collecte des eaux de pluie, l'irrigation goutte à goutte, le paillage et l'agriculture en courbes de niveau aident à capturer et utiliser l'eau efficacement. Les outils de prévision météorologique et les simples stations météo à la ferme permettent aux agriculteurs de prendre des décisions opportunes. L'assainissement autour des sources d'eau évite la contamination. Aujourd'hui, nous explorons comment gérer l'eau intelligemment face à la variabilité climatique.",
        "text_es": "El agua es vida, pero demasiada o muy poca puede destruir los cultivos. Comprender los patrones climáticos locales – lluvias, sequías, tormentas – es crucial para la planificación. Técnicas como la recolección de agua de lluvia, el riego por goteo, el acolchado y la agricultura en curvas de nivel ayudan a capturar y usar el agua de manera eficiente. Las herramientas de pronóstico del tiempo y las simples estaciones meteorológicas en la granja permiten a los agricultores tomar decisiones oportunas. El saneamiento alrededor de las fuentes de agua evita la contaminación. Hoy exploramos cómo manejar el agua sabiamente frente a la variabilidad climática.",
        "image": "https://images.pexels.com/photos/292114/pexels-photo-292114.jpeg"
    },
    4: {
        "title_en": "Day 4: Reducing Chemical Inputs – Natural Alternatives",
        "title_fr": "Jour 4 : Réduire les intrants chimiques – Alternatives naturelles",
        "title_es": "Día 4: Reducción de insumos químicos – Alternativas naturales",
        "text_en": "Chemical fertilizers and pesticides can harm soil life, pollinators, and human health. There are many natural alternatives: compost tea, neem oil, beneficial insects, and crop rotation. By observing your fields regularly, you can identify problems early and use targeted organic solutions. This lesson presents a step‑by‑step guide to transition away from synthetic inputs, starting with one field or crop. Small changes lead to big benefits for your wallet and the environment.",
        "text_fr": "Les engrais chimiques et les pesticides peuvent nuire à la vie du sol, aux pollinisateurs et à la santé humaine. Il existe de nombreuses alternatives naturelles : purin d'ortie, huile de neem, insectes bénéfiques et rotation des cultures. En observant régulièrement vos champs, vous pouvez identifier les problèmes tôt et utiliser des solutions organiques ciblées. Cette leçon présente un guide étape par étape pour s'éloigner des intrants synthétiques, en commençant par un champ ou une culture. De petits changements apportent de grands avantages pour votre portefeuille et l'environnement.",
        "text_es": "Los fertilizantes químicos y los pesticidas pueden dañar la vida del suelo, los polinizadores y la salud humana. Existen muchas alternativas naturales: té de compost, aceite de neem, insectos benéficos y rotación de cultivos. Al observar sus campos regularmente, puede identificar problemas temprano y usar soluciones orgánicas específicas. Esta lección presenta una guía paso a paso para alejarse de los insumos sintéticos, comenzando con un campo o cultivo. Pequeños cambios generan grandes beneficios para su bolsillo y el medio ambiente.",
        "image": "https://images.pexels.com/photos/1264320/pexels-photo-1264320.jpeg"
    },
    5: {
        "title_en": "Day 5: Crop Rotation and Diversity",
        "title_fr": "Jour 5 : Rotation des cultures et diversité",
        "title_es": "Día 5: Rotación de cultivos y diversidad",
        "text_en": "Growing the same crop year after year depletes nutrients and invites pests. Crop rotation means changing the plant family in each field every season. For example, follow a nitrogen‑fixing legume with a heavy feeder like corn. Intercropping (mixing crops) also reduces pest outbreaks and improves soil health. Diversity creates resilience. Today we design a simple rotation plan for a small garden and learn why polycultures outperform monocultures.",
        "text_fr": "Cultiver la même culture année après année épuise les nutriments et attire les ravageurs. La rotation des cultures consiste à changer la famille de plantes dans chaque champ à chaque saison. Par exemple, faites suivre une légumineuse fixatrice d'azote par une plante gourmande comme le maïs. La culture intercalaire (mélange de cultures) réduit également les épidémies de ravageurs et améliore la santé du sol. La diversité crée la résilience. Aujourd'hui, nous concevons un plan de rotation simple pour un petit jardin et apprenons pourquoi les polycultures surpassent les monocultures.",
        "text_es": "Cultivar el mismo cultivo año tras año agota los nutrientes y atrae plagas. La rotación de cultivos significa cambiar la familia de plantas en cada campo cada temporada. Por ejemplo, siga una leguminosa fijadora de nitrógeno con un cultivo exigente como el maíz. El cultivo intercalado (mezcla de cultivos) también reduce los brotes de plagas y mejora la salud del suelo. La diversidad crea resiliencia. Hoy diseñamos un plan de rotación simple para un pequeño jardín y aprendemos por qué los policultivos superan a los monocultivos.",
        "image": "https://images.pexels.com/photos/101708/pexels-photo-101708.jpeg"
    },
    6: {
        "title_en": "Day 6: Composting and Organic Fertilizers",
        "title_fr": "Jour 6 : Compostage et engrais organiques",
        "title_es": "Día 6: Compostaje y fertilizantes orgánicos",
        "text_en": "Compost turns farm waste into black gold. Anything that once lived – plant residues, manure, kitchen scraps – can be composted. A good compost pile balances greens (nitrogen) and browns (carbon), with enough moisture and air. After a few months, you get a rich, earthy fertilizer that feeds soil microbes. We also explore other organic fertilizers like worm castings, green manure, and biochar. This lesson teaches how to build a simple compost heap and use it effectively.",
        "text_fr": "Le compost transforme les déchets de ferme en or noir. Tout ce qui a vécu – résidus végétaux, fumier, déchets de cuisine – peut être composté. Un bon tas de compost équilibre les matières vertes (azote) et brunes (carbone), avec suffisamment d'humidité et d'air. Après quelques mois, vous obtenez un engrais riche et terreux qui nourrit les microbes du sol. Nous explorons également d'autres engrais organiques comme le lombricompost, l'engrais vert et le biochar. Cette leçon apprend à construire un simple tas de compost et à l'utiliser efficacement.",
        "text_es": "El compost convierte los desechos de la granja en oro negro. Cualquier cosa que una vez vivió – residuos vegetales, estiércol, restos de cocina – se puede compostar. Una buena pila de compost equilibra los materiales verdes (nitrógeno) y marrones (carbono), con suficiente humedad y aire. Después de unos meses, obtiene un fertilizante rico y terroso que alimenta los microbios del suelo. También exploramos otros fertilizantes orgánicos como el humus de lombriz, el abono verde y el biocarbón. Esta lección enseña cómo construir una pila de compost simple y usarla de manera efectiva.",
        "image": "https://images.pexels.com/photos/5849561/pexels-photo-5849561.jpeg"
    },
    7: {
        "title_en": "Day 7: Pest Management without Pesticides",
        "title_fr": "Jour 7 : Gestion des ravageurs sans pesticides",
        "title_es": "Día 7: Manejo de plagas sin pesticidas",
        "text_en": "Integrated Pest Management (IPM) uses observation, prevention, and natural controls. Start by encouraging beneficial insects (ladybugs, lacewings) by planting flowers. Use physical barriers like nets or traps. When needed, apply botanical sprays (neem, garlic) that break down quickly. Rotate crops and remove infested plants. This approach reduces pesticide resistance and protects pollinators. Today we identify common garden pests and their natural enemies.",
        "text_fr": "La lutte intégrée (IPM) utilise l'observation, la prévention et les contrôles naturels. Commencez par encourager les insectes bénéfiques (coccinelles, chrysopes) en plantant des fleurs. Utilisez des barrières physiques comme des filets ou des pièges. Si nécessaire, appliquez des pulvérisations botaniques (neem, ail) qui se dégradent rapidement. Alternez les cultures et éliminez les plantes infestées. Cette approche réduit la résistance aux pesticides et protège les pollinisateurs. Aujourd'hui, nous identifions les ravageurs courants du jardin et leurs ennemis naturels.",
        "text_es": "El Manejo Integrado de Plagas (MIP) utiliza observación, prevención y controles naturales. Comience fomentando insectos benéficos (mariquitas, crisopas) plantando flores. Use barreras físicas como redes o trampas. Cuando sea necesario, aplique aerosoles botánicos (neem, ajo) que se descomponen rápidamente. Rote los cultivos y elimine las plantas infestadas. Este enfoque reduce la resistencia a los pesticidas y protege a los polinizadores. Hoy identificamos las plagas comunes del jardín y sus enemigos naturales.",
        "image": "https://images.pexels.com/photos/79621/pexels-photo-79621.jpeg"
    },
    8: {
        "title_en": "Day 8: The Role of Cooperatives in Agriculture",
        "title_fr": "Jour 8 : Le rôle des coopératives en agriculture",
        "title_es": "Día 8: El papel de las cooperativas en la agricultura",
        "text_en": "Individual farmers often struggle to access markets, get fair prices, or buy inputs cheaply. Cooperatives – groups of farmers who work together – solve these problems. They pool resources, share knowledge, and negotiate better deals. In Laos and Cambodia, cooperatives have helped members increase incomes and adopt sustainable practices. Today we learn how to start or join a cooperative: rules, benefits, and success stories from the field.",
        "text_fr": "Les agriculteurs individuels ont souvent du mal à accéder aux marchés, à obtenir des prix équitables ou à acheter des intrants à moindre coût. Les coopératives – groupes d'agriculteurs qui travaillent ensemble – résolvent ces problèmes. Elles mettent en commun les ressources, partagent les connaissances et négocient de meilleures offres. Au Laos et au Cambodge, les coopératives ont aidé les membres à augmenter leurs revenus et à adopter des pratiques durables. Aujourd'hui, nous apprenons comment créer ou rejoindre une coopérative : règles, avantages et réussites sur le terrain.",
        "text_es": "Los agricultores individuales a menudo luchan por acceder a los mercados, obtener precios justos o comprar insumos a bajo costo. Las cooperativas – grupos de agricultores que trabajan juntos – resuelven estos problemas. Reúnen recursos, comparten conocimientos y negocian mejores acuerdos. En Laos y Camboya, las cooperativas han ayudado a los miembros a aumentar sus ingresos y adoptar prácticas sostenibles. Hoy aprendemos cómo iniciar o unirse a una cooperativa: reglas, beneficios e historias de éxito en el campo.",
        "image": "https://images.pexels.com/photos/6646839/pexels-photo-6646839.jpeg"
    },
    9: {
        "title_en": "Day 9: Certification and Market Access",
        "title_fr": "Jour 9 : Certification et accès aux marchés",
        "title_es": "Día 9: Certificación y acceso a mercados",
        "text_en": "Certification schemes (organic, fair trade, Rainforest Alliance) help farmers prove their products are sustainable. They open doors to premium markets and build consumer trust. However, certification can be expensive. Group certification for cooperatives reduces costs. This lesson explains the steps to get certified, the documents needed, and how to find buyers who value sustainability. Case studies from Southeast Asia show how certification changed farmers' lives.",
        "text_fr": "Les systèmes de certification (bio, commerce équitable, Rainforest Alliance) aident les agriculteurs à prouver que leurs produits sont durables. Ils ouvrent les portes des marchés haut de gamme et renforcent la confiance des consommateurs. Cependant, la certification peut être coûteuse. La certification de groupe pour les coopératives réduit les coûts. Cette leçon explique les étapes pour obtenir la certification, les documents nécessaires et comment trouver des acheteurs qui valorisent la durabilité. Des études de cas en Asie du Sud-Est montrent comment la certification a changé la vie des agriculteurs.",
        "text_es": "Los esquemas de certificación (orgánico, comercio justo, Rainforest Alliance) ayudan a los agricultores a demostrar que sus productos son sostenibles. Abren puertas a mercados premium y generan confianza en los consumidores. Sin embargo, la certificación puede ser costosa. La certificación grupal para cooperativas reduce costos. Esta lección explica los pasos para certificarse, los documentos necesarios y cómo encontrar compradores que valoren la sostenibilidad. Estudios de caso del Sudeste Asiático muestran cómo la certificación cambió la vida de los agricultores.",
        "image": "https://images.pexels.com/photos/4488638/pexels-photo-4488638.jpeg"
    },
    10: {
        "title_en": "Day 10: Post-Harvest Handling and Sanitation",
        "title_fr": "Jour 10 : Manutention post-récolte et assainissement",
        "title_es": "Día 10: Manejo postcosecha y saneamiento",
        "text_en": "After harvest, fruits and vegetables continue to breathe. Poor handling leads to rot and waste. Sanitation is key: clean storage areas, wash hands, use clean water, and separate produce from soil. Techniques like curing, cooling, and proper packaging extend shelf life. This lesson covers simple low‑cost methods to reduce post‑harvest losses, improve food safety, and increase profits. Good hygiene also prevents foodborne illnesses.",
        "text_fr": "Après la récolte, les fruits et légumes continuent de respirer. Une mauvaise manipulation entraîne la pourriture et le gaspillage. L'assainissement est essentiel : zones de stockage propres, lavage des mains, utilisation d'eau propre et séparation des produits du sol. Des techniques comme le séchage, le refroidissement et un emballage approprié prolongent la durée de conservation. Cette leçon couvre des méthodes simples et peu coûteuses pour réduire les pertes post-récolte, améliorer la sécurité alimentaire et augmenter les bénéfices. Une bonne hygiène prévient également les maladies d'origine alimentaire.",
        "text_es": "Después de la cosecha, las frutas y verduras siguen respirando. Una mala manipulación provoca putrefacción y desperdicio. El saneamiento es clave: áreas de almacenamiento limpias, lavarse las manos, usar agua limpia y separar los productos del suelo. Técnicas como el curado, enfriamiento y empaque adecuado prolongan la vida útil. Esta lección cubre métodos simples y de bajo costo para reducir las pérdidas poscosecha, mejorar la seguridad alimentaria y aumentar las ganancias. Una buena higiene también previene enfermedades transmitidas por alimentos.",
        "image": "https://images.pexels.com/photos/6210278/pexels-photo-6210278.jpeg"
    },
    11: {
        "title_en": "Day 11: Seed Saving and Biodiversity",
        "title_fr": "Jour 11 : Conservation des semences et biodiversité",
        "title_es": "Día 11: Conservación de semillas y biodiversidad",
        "text_en": "Saving your own seeds saves money and adapts crops to your local conditions. Choose open‑pollinated varieties, not hybrids. Learn how to harvest, dry, and store seeds properly. Seed banks and farmer networks preserve genetic diversity. This lesson explains how to save seeds from common vegetables like tomatoes, beans, and squash. Biodiversity in the field also means planting heirloom varieties that resist diseases naturally.",
        "text_fr": "Conserver vos propres semences permet d'économiser de l'argent et d'adapter les cultures à vos conditions locales. Choisissez des variétés à pollinisation libre, pas des hybrides. Apprenez à récolter, sécher et stocker les semences correctement. Les banques de semences et les réseaux d'agriculteurs préservent la diversité génétique. Cette leçon explique comment conserver les semences de légumes courants comme les tomates, les haricots et les courges. La biodiversité dans le champ signifie également planter des variétés anciennes qui résistent naturellement aux maladies.",
        "text_es": "Guardar sus propias semillas ahorra dinero y adapta los cultivos a sus condiciones locales. Elija variedades de polinización abierta, no híbridas. Aprenda a cosechar, secar y almacenar semillas correctamente. Los bancos de semillas y las redes de agricultores preservan la diversidad genética. Esta lección explica cómo guardar semillas de vegetales comunes como tomates, frijoles y calabazas. La biodiversidad en el campo también significa plantar variedades autóctonas que resisten enfermedades naturalmente.",
        "image": "https://images.pexels.com/photos/789658/pexels-photo-789658.jpeg"
    },
    12: {
        "title_en": "Day 12: Agroforestry and Tree Integration",
        "title_fr": "Jour 12 : Agroforesterie et intégration des arbres",
        "title_es": "Día 12: Agroforestería e integración de árboles",
        "text_en": "Agroforestry combines trees with crops or livestock. Trees provide shade, windbreaks, fruits, timber, and improve soil fertility through leaf litter. They also sequester carbon. In tropical countries, alley cropping with fast‑growing trees like gliricidia enriches the soil. This lesson introduces different agroforestry systems and how to choose the right trees for your farm. We also see examples from Laos where agroforestry restored degraded land.",
        "text_fr": "L'agroforesterie combine les arbres avec les cultures ou l'élevage. Les arbres fournissent de l'ombre, des brise‑vent, des fruits, du bois et améliorent la fertilité des sols grâce à la litière de feuilles. Ils séquestrent également le carbone. Dans les pays tropicaux, la culture en couloirs avec des arbres à croissance rapide comme le gliricidia enrichit le sol. Cette leçon présente différents systèmes agroforestiers et comment choisir les bons arbres pour votre ferme. Nous voyons également des exemples du Laos où l'agroforesterie a restauré des terres dégradées.",
        "text_es": "La agroforestería combina árboles con cultivos o ganado. Los árboles proporcionan sombra, cortavientos, frutas, madera y mejoran la fertilidad del suelo a través de la hojarasca. También secuestran carbono. En países tropicales, el cultivo en callejones con árboles de rápido crecimiento como gliricidia enriquece el suelo. Esta lección presenta diferentes sistemas agroforestales y cómo elegir los árboles adecuados para su granja. También vemos ejemplos de Laos donde la agroforestería restauró tierras degradadas.",
        "image": "https://images.pexels.com/photos/247478/pexels-photo-247478.jpeg"
    },
    13: {
        "title_en": "Day 13: Climate-Resilient Farming",
        "title_fr": "Jour 13 : Agriculture résiliente au climat",
        "title_es": "Día 13: Agricultura resiliente al clima",
        "text_en": "Climate change brings more extreme weather: droughts, floods, heatwaves. Resilient farms adapt by diversifying crops, improving water storage, using drought‑tolerant varieties, and building healthy soil that holds moisture. Agroecological practices like mulching, windbreaks, and contour farming reduce risks. Today we explore a checklist to assess your farm's vulnerability and a toolkit of resilience strategies that have worked in Cambodia and Laos.",
        "text_fr": "Le changement climatique apporte des conditions météorologiques plus extrêmes : sécheresses, inondations, vagues de chaleur. Les fermes résilientes s'adaptent en diversifiant les cultures, en améliorant le stockage de l'eau, en utilisant des variétés tolérantes à la sécheresse et en construisant un sol sain qui retient l'humidité. Les pratiques agroécologiques comme le paillage, les brise‑vent et l'agriculture en courbes de niveau réduisent les risques. Aujourd'hui, nous explorons une liste de contrôle pour évaluer la vulnérabilité de votre ferme et une boîte à outils de stratégies de résilience qui ont fonctionné au Cambodge et au Laos.",
        "text_es": "El cambio climático trae condiciones climáticas más extremas: sequías, inundaciones, olas de calor. Las granjas resilientes se adaptan diversificando cultivos, mejorando el almacenamiento de agua, utilizando variedades tolerantes a la sequía y construyendo suelos saludables que retienen la humedad. Las prácticas agroecológicas como el acolchado, los cortavientos y la agricultura en curvas de nivel reducen los riesgos. Hoy exploramos una lista de verificación para evaluar la vulnerabilidad de su granja y un conjunto de herramientas de estrategias de resiliencia que han funcionado en Camboya y Laos.",
        "image": "https://images.pexels.com/photos/1301856/pexels-photo-1301856.jpeg"
    },
    14: {
        "title_en": "Day 14: Small-Scale Irrigation Techniques",
        "title_fr": "Jour 14 : Techniques d'irrigation à petite échelle",
        "title_es": "Día 14: Técnicas de riego a pequeña escala",
        "text_en": "Not every farm has a river. Small‑scale irrigation can be as simple as a bucket and a hose, or more advanced like drip kits. Rainwater harvesting from roofs, small ponds, or underground tanks provides water during dry spells. Solar pumps are becoming affordable. This lesson compares different low‑cost irrigation methods, their water efficiency, and how to maintain them. We also discuss water sanitation to avoid algal growth.",
        "text_fr": "Toutes les fermes n'ont pas une rivière. L'irrigation à petite échelle peut être aussi simple qu'un seau et un tuyau, ou plus avancée comme des kits goutte à goutte. La collecte des eaux de pluie à partir des toits, de petits étangs ou de réservoirs souterrains fournit de l'eau pendant les périodes sèches. Les pompes solaires deviennent abordables. Cette leçon compare différentes méthodes d'irrigation à faible coût, leur efficacité hydrique et comment les entretenir. Nous discutons également de l'assainissement de l'eau pour éviter la croissance d'algues.",
        "text_es": "No todas las granjas tienen un río. El riego a pequeña escala puede ser tan simple como un balde y una manguera, o más avanzado como kits de goteo. La recolección de agua de lluvia de techos, pequeños estanques o tanques subterráneos proporciona agua durante los períodos secos. Las bombas solares se están volviendo asequibles. Esta lección compara diferentes métodos de riego de bajo costo, su eficiencia hídrica y cómo mantenerlos. También discutimos el saneamiento del agua para evitar el crecimiento de algas.",
        "image": "https://images.pexels.com/photos/1081483/pexels-photo-1081483.jpeg"
    },
    15: {
        "title_en": "Day 15: Livestock Integration in Agroecology",
        "title_fr": "Jour 15 : Intégration de l'élevage en agroécologie",
        "title_es": "Día 15: Integración ganadera en agroecología",
        "text_en": "Animals and crops work better together. Chickens eat pests and provide manure; pigs can be rotated on crop residues; cattle graze cover crops. Integrating livestock recycles nutrients, reduces waste, and creates multiple income streams. However, it requires careful management to prevent overgrazing and water contamination. Today we learn rotational grazing, manure composting, and how to design a mixed farm using the Cambodian experience.",
        "text_fr": "Les animaux et les cultures fonctionnent mieux ensemble. Les poules mangent les ravageurs et fournissent du fumier ; les porcs peuvent être alternés sur les résidus de culture ; les bovins pâturent les cultures de couverture. L'intégration de l'élevage recycle les nutriments, réduit les déchets et crée de multiples sources de revenus. Cependant, elle nécessite une gestion minutieuse pour éviter le surpâturage et la contamination de l'eau. Aujourd'hui, nous apprenons le pâturage rotatif, le compostage du fumier et comment concevoir une ferme mixte en utilisant l'expérience cambodgienne.",
        "text_es": "Los animales y los cultivos funcionan mejor juntos. Las gallinas comen plagas y proporcionan estiércol; los cerdos pueden rotarse en residuos de cultivos; el ganado pasta cultivos de cobertura. La integración ganadera recicla nutrientes, reduce desechos y crea múltiples fuentes de ingresos. Sin embargo, requiere un manejo cuidadoso para evitar el sobrepastoreo y la contaminación del agua. Hoy aprendemos pastoreo rotacional, compostaje de estiércol y cómo diseñar una granja mixta utilizando la experiencia camboyana.",
        "image": "https://images.pexels.com/photos/2487312/pexels-photo-2487312.jpeg"
    },
    16: {
        "title_en": "Day 16: Women and Youth in Agriculture",
        "title_fr": "Jour 16 : Femmes et jeunes en agriculture",
        "title_es": "Día 16: Mujeres y jóvenes en la agricultura",
        "text_en": "Women and young people are vital to the future of farming, but they often lack access to land, credit, and training. Empowering them with leadership roles in cooperatives and decision‑making increases productivity and family well‑being. This lesson showcases successful projects from Laos where women‑led vegetable gardens and youth agri‑entrepreneurship transformed communities. We discuss practical steps to make agriculture more inclusive.",
        "text_fr": "Les femmes et les jeunes sont essentiels à l'avenir de l'agriculture, mais ils manquent souvent d'accès à la terre, au crédit et à la formation. Leur donner des rôles de leadership dans les coopératives et la prise de décision augmente la productivité et le bien-être familial. Cette leçon présente des projets réussis du Laos où des potagers dirigés par des femmes et l'entrepreneuriat agricole des jeunes ont transformé des communautés. Nous discutons des mesures pratiques pour rendre l'agriculture plus inclusive.",
        "text_es": "Las mujeres y los jóvenes son vitales para el futuro de la agricultura, pero a menudo carecen de acceso a la tierra, crédito y capacitación. Empoderarlos con roles de liderazgo en cooperativas y toma de decisiones aumenta la productividad y el bienestar familiar. Esta lección muestra proyectos exitosos de Laos donde huertos liderados por mujeres y el emprendimiento agrícola juvenil transformaron comunidades. Discutimos pasos prácticos para hacer la agricultura más inclusiva.",
        "image": "https://images.pexels.com/photos/1423607/pexels-photo-1423607.jpeg"
    },
    17: {
        "title_en": "Day 17: Policy and Support for Farmers",
        "title_fr": "Jour 17 : Politique et soutien aux agriculteurs",
        "title_es": "Día 17: Política y apoyo a los agricultores",
        "text_en": "Government policies can help or hinder sustainable agriculture. Subsidies for chemicals, trade agreements, and land tenure laws all affect farmers. This lesson guides you on how to advocate for supportive policies – joining farmer networks, participating in consultations, and using media. We also present examples of successful policy changes in Southeast Asia that promoted agroecology and cooperative development.",
        "text_fr": "Les politiques gouvernementales peuvent aider ou entraver l'agriculture durable. Les subventions aux produits chimiques, les accords commerciaux et les lois sur le régime foncier affectent tous les agriculteurs. Cette leçon vous guide sur la façon de plaider pour des politiques favorables – rejoindre des réseaux d'agriculteurs, participer à des consultations et utiliser les médias. Nous présentons également des exemples de changements politiques réussis en Asie du Sud-Est qui ont favorisé l'agroécologie et le développement des coopératives.",
        "text_es": "Las políticas gubernamentales pueden ayudar o dificultar la agricultura sostenible. Los subsidios a productos químicos, los acuerdos comerciales y las leyes de tenencia de la tierra afectan a los agricultores. Esta lección lo guía sobre cómo abogar por políticas de apoyo – unirse a redes de agricultores, participar en consultas y usar los medios. También presentamos ejemplos de cambios políticos exitosos en el Sudeste Asiático que promovieron la agroecología y el desarrollo cooperativo.",
        "image": "https://images.pexels.com/photos/6750745/pexels-photo-6750745.jpeg"
    },
    18: {
        "title_en": "Day 18: Learning from Others – Exchange Visits (Laos Example)",
        "title_fr": "Jour 18 : Apprendre des autres – Visites d'échange (exemple du Laos)",
        "title_es": "Día 18: Aprender de otros – Visitas de intercambio (ejemplo de Laos)",
        "text_en": "Visiting other farms and countries opens your mind. A recent exchange from Cambodia to Laos (March 31 – April 5, 2026) taught four key lessons: (1) Agroecology works in practice; (2) Certification opens markets; (3) Cooperatives bring fairer incomes; (4) Cross‑learning builds lasting networks. Today we dive into these lessons and how you can organize your own exchange visits, even locally, to boost innovation.",
        "text_fr": "Visiter d'autres fermes et pays ouvre l'esprit. Un récent échange du Cambodge vers le Laos (31 mars – 5 avril 2026) a enseigné quatre leçons clés : (1) L'agroécologie fonctionne dans la pratique ; (2) La certification ouvre les marchés ; (3) Les coopératives apportent des revenus plus équitables ; (4) L'apprentissage croisé construit des réseaux durables. Aujourd'hui, nous approfondissons ces leçons et comment vous pouvez organiser vos propres visites d'échange, même localement, pour stimuler l'innovation.",
        "text_es": "Visitar otras granjas y países abre la mente. Un reciente intercambio de Camboya a Laos (31 de marzo – 5 de abril de 2026) enseñó cuatro lecciones clave: (1) La agroecología funciona en la práctica; (2) La certificación abre mercados; (3) Las cooperativas traen ingresos más justos; (4) El aprendizaje cruzado construye redes duraderas. Hoy profundizamos en estas lecciones y cómo puede organizar sus propias visitas de intercambio, incluso localmente, para impulsar la innovación.",
        "image": "https://images.pexels.com/photos/129115/pexels-photo-129115.jpeg"
    },
    19: {
        "title_en": "Day 19: Building a Local Food System",
        "title_fr": "Jour 19 : Construire un système alimentaire local",
        "title_es": "Día 19: Construcción de un sistema alimentario local",
        "text_en": "Shortening the distance from farm to fork reduces emissions and keeps money in the community. Local food systems include farmers’ markets, community‑supported agriculture (CSA), school feeding programs, and farm‑to‑restaurant partnerships. This lesson explains how to map your local food actors, create a brand, and use social media to sell directly. We also cover food safety regulations and storytelling to attract customers.",
        "text_fr": "Raccourcir la distance de la ferme à l'assiette réduit les émissions et maintient l'argent dans la communauté. Les systèmes alimentaires locaux comprennent les marchés de producteurs, l'agriculture soutenue par la communauté (ASC), les programmes d'alimentation scolaire et les partenariats de la ferme à la restauration. Cette leçon explique comment cartographier les acteurs alimentaires locaux, créer une marque et utiliser les médias sociaux pour vendre directement. Nous couvrons également les réglementations en matière de sécurité alimentaire et la narration pour attirer les clients.",
        "text_es": "Acortar la distancia desde la granja hasta la mesa reduce las emisiones y mantiene el dinero en la comunidad. Los sistemas alimentarios locales incluyen mercados de agricultores, agricultura apoyada por la comunidad (CSA), programas de alimentación escolar y asociaciones de la granja al restaurante. Esta lección explica cómo mapear los actores alimentarios locales, crear una marca y usar las redes sociales para vender directamente. También cubrimos regulaciones de seguridad alimentaria y narración de historias para atraer clientes.",
        "image": "https://images.pexels.com/photos/618776/pexels-photo-618776.jpeg"
    },
    20: {
        "title_en": "Day 20: The Future of Farming – Technology and Tradition",
        "title_fr": "Jour 20 : L'avenir de l'agriculture – Technologie et tradition",
        "title_es": "Día 20: El futuro de la agricultura – Tecnología y tradición",
        "text_en": "The best agriculture marries ancient wisdom with modern tools. Drones, soil sensors, mobile apps for weather, and blockchains for traceability can complement traditional knowledge. But technology is only a tool; the heart remains the farmer’s connection to land and community. On this final day, we reflect on the 20‑day journey and encourage you to pick one new practice to implement. A sustainable future is built step by step, together.",
        "text_fr": "La meilleure agriculture marie la sagesse ancienne avec les outils modernes. Les drones, les capteurs de sol, les applications météo mobiles et les blockchains pour la traçabilité peuvent compléter les connaissances traditionnelles. Mais la technologie n'est qu'un outil ; le cœur reste le lien de l'agriculteur avec la terre et la communauté. En ce dernier jour, nous réfléchissons au voyage de 20 jours et vous encourageons à choisir une nouvelle pratique à mettre en œuvre. Un avenir durable se construit pas à pas, ensemble.",
        "text_es": "La mejor agricultura une la sabiduría antigua con las herramientas modernas. Los drones, sensores de suelo, aplicaciones móviles para el clima y blockchains para la trazabilidad pueden complementar el conocimiento tradicional. Pero la tecnología es solo una herramienta; el corazón sigue siendo la conexión del agricultor con la tierra y la comunidad. En este último día, reflexionamos sobre el viaje de 20 días y lo alentamos a elegir una nueva práctica para implementar. Un futuro sostenible se construye paso a paso, juntos.",
        "image": "https://images.pexels.com/photos/3873696/pexels-photo-3873696.jpeg"
    }
}

# ---------- AUDIO FUNCTION ----------
def text_to_speech_button(text, lang_code, button_label):
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

    with st.sidebar:
        st.markdown("## 🌟 **Gesner Deslandes**")
        st.markdown("👨‍💻 *Chief Engineer at GlobalInternet.py*")
        st.markdown("🌍 **We build softwares on demand**")
        st.markdown("---")
        st.markdown("#### 📚 Training Summary")
        st.markdown("20 lessons covering:\n✅ Agroecology\n✅ Soil & Water\n✅ Cooperatives\n✅ Certification\n✅ Pest Management\n✅ Post‑harvest\n✅ Agroforestry\n✅ Climate resilience\n✅ Exchange visits (Laos)\n✅ Local food systems")
        st.markdown("---")
        st.markdown("🔊 *Each lesson includes text, image, and audio*")
        st.markdown("---")
        if st.button(logout_btn, use_container_width=True):
            st.session_state.authenticated = False
            st.rerun()

    for day in range(1, 21):
        lesson = lessons[day]
        if lang_code == 'en':
            title = lesson["title_en"]
            text = lesson["text_en"]
        elif lang_code == 'fr':
            title = lesson["title_fr"]
            text = lesson["text_fr"]
        else:
            title = lesson["title_es"]
            text = lesson["text_es"]

        with st.expander(f"📖 {day_prefix} {day}: {title}"):
            col1, col2 = st.columns([2, 1])
            with col1:
                st.markdown(f"<div class='lesson-card'><h3>{title}</h3>", unsafe_allow_html=True)
                st.write(text)
                audio_html = text_to_speech_button(text, lang_code, listen_btn)
                st.components.v1.html(audio_html, height=80)
                st.markdown("</div>", unsafe_allow_html=True)
            with col2:
                st.image(lesson["image"], use_container_width=True, caption=f"{day_prefix} {day}")

    st.markdown('<div class="footer">© GlobalInternet.py – Coopératives & Agroécologie – Empowering farmers with sustainable knowledge</div>', unsafe_allow_html=True)

# ---------- RUN ----------
if check_password():
    main_app()
