import streamlit as st
import pandas as pd
import plotly.express as px

# =========================
# PAGINA-INSTELLINGEN
# =========================
st.set_page_config(
    page_title="Dashboard - Hartstikke Gezond",
    page_icon="❤️",
    layout="wide"
)

# =========================
# CSS-STYLING
# =========================
st.markdown("""
<style>
    .stApp {
        background-color: #f3efe8;
        color: #111111;
    }

    .main-title {
        background-color: white;
        padding: 14px;
        border-radius: 25px;
        text-align: center;
        font-size: 28px;
        font-weight: 700;
        margin-bottom: 20px;
    }

    .card {
        background-color: white;
        padding: 24px;
        border-radius: 28px;
        text-align: center;
        min-height: 230px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }

    .small-card {
        background-color: white;
        padding: 22px;
        border-radius: 28px;
        min-height: 180px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }

    .metric-title {
        font-size: 24px;
        font-weight: 600;
        margin-bottom: 12px;
    }

    .metric-value {
        font-size: 38px;
        font-weight: 800;
    }

    .metric-unit {
        font-size: 22px;
        font-weight: 500;
    }

    .status-normal {
        background-color: #92ad96;
        color: #111111;
        padding: 8px 18px;
        border-radius: 14px;
        display: inline-block;
        margin-top: 18px;
        font-size: 18px;
    }

    .status-warning {
        background-color: #ffb347;
        color: #111111;
        padding: 8px 18px;
        border-radius: 14px;
        display: inline-block;
        margin-top: 18px;
        font-size: 18px;
    }

    .sidebar-box {
        background-color: #d5cbbd;
        padding: 18px;
        border-radius: 20px;
    }

    .footer {
        background-color: white;
        padding: 10px 18px;
        border-radius: 18px;
        margin-top: 18px;
        font-size: 15px;
    }

    .recommendation {
        margin-bottom: 16px;
        font-size: 16px;
    }

    .recommendation strong {
        font-size: 18px;
    }

    div[data-testid="stSidebar"] {
        background-color: #d5cbbd;
    }
</style>
""", unsafe_allow_html=True)


# =========================
# TESTDATA
# =========================
heart_rate = 80
hrv = 35
steps_today = 1200
risk_score = 2

heart_data = pd.DataFrame({
    "Dag": ["21", "22", "23", "24", "25"],
    "Hartslag": [80, 90, 60, 120, 80]
})

steps_data = pd.DataFrame({
    "Dag": ["Ma", "Di", "Wo", "Do", "Vr"],
    "Stappen": [1200, 5000, 9000, 5000, 6500]
})

blood_pressure_data = pd.DataFrame({
    "Dag": ["Ma", "Di", "Wo", "Do", "Vr"],
    "Systolisch": [115, 120, 128, 134, 148],
    "Diastolisch": [75, 80, 88, 92, 100]
})

cholesterol_data = pd.DataFrame({
    "Type": ["Totaal", "LDL", "HDL", "Triglyceriden"],
    "Percentage": [55, 25, 15, 5]
})


# =========================
# SIDEBAR NAVIGATIE
# =========================
st.sidebar.markdown("## Navigatie")

pagina = st.sidebar.radio(
    "Ga naar:",
    [
        "Home",
        "Historie",
        "Persoonlijke gegevens",
        "Instellingen",
        "Delen",
        "Contact/Help"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("❤️ **Hartstikke Gezond**")
st.sidebar.markdown("Dashboard team 3 - 7.2")


# =========================
# HEADER
# =========================
st.markdown(
    '<div class="main-title">Dashboard - Naam Achternaam</div>',
    unsafe_allow_html=True
)


# =========================
# HOME PAGINA
# =========================
if pagina == "Home":
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div class="card">
            <div class="metric-title">Hartslag</div>
            <div style="font-size:58px;">❤️</div>
            <div class="metric-value">{heart_rate}</div>
            <div class="metric-unit">BPM</div>
            <div class="status-normal">normaal</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="card">
            <div class="metric-title">HRV</div>
            <div class="metric-value">{hrv}</div>
            <div class="metric-unit">ms</div>
            <div class="status-normal">normaal</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="card">
            <div class="metric-title">Activiteit<br>(vandaag)</div>
            <div style="font-size:58px;">👟</div>
            <div class="metric-value">{steps_today:,}</div>
            <div class="metric-unit">Stappen</div>
            <div class="status-warning">Je bent er bijna!</div>
        </div>
        """.replace(",", "."), unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="card">
            <div class="metric-title">Risicoscore</div>
            <div style="font-size:58px;">🛡️</div>
            <div class="metric-value">{risk_score}%</div>
            <div class="status-normal">Laag risico</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("")

    col_a, col_b, col_c = st.columns([2.2, 1, 1])

    with col_a:
        st.markdown("""
        <div class="small-card">
            <h3>Aanbevelingen</h3>

            <div class="recommendation">
                🚶 <strong>Blijf actief!</strong><br>
                Probeer deze week 5 dagen 20 minuten te wandelen.
            </div>

            <div class="recommendation">
                🍎 <strong>Eet minder zout</strong><br>
                Kies vaker voor verse producten in plaats van fast food.
            </div>

            <div class="recommendation">
                🌙 <strong>Voldoende nachtrust</strong><br>
                Zorg voor genoeg slaap.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_b:
        st.markdown("""
        <div class="small-card" style="text-align:center;">
            <h4>Eerstvolgende Hartstikke gezond-week</h4>
            <div style="font-size:52px;">📅</div>
            <h2>18 Sept<br>2026</h2>
        </div>
        """, unsafe_allow_html=True)

    with col_c:
        st.markdown("""
        <div class="small-card" style="text-align:center;">
            <h3>Historie</h3>
            <div style="font-size:72px;">📖</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="footer">
        ℹ️ Deze gegevens zijn niet bedoeld als medisch advies. Raadpleeg bij twijfel altijd een arts.
        <span style="float:right;">12:00 &nbsp;&nbsp; 21-04-2026</span>
    </div>
    """, unsafe_allow_html=True)


# =========================
# HISTORIE / DETAILS PAGINA
# =========================
elif pagina == "Historie":
    st.subheader("Details / Historie")

    top_left, top_right = st.columns([2, 1.3])

    with top_left:
        st.markdown('<div class="small-card">', unsafe_allow_html=True)
        st.markdown("### Hartslag (bpm) - laatste 7 dagen")
        fig_heart = px.line(
            heart_data,
            x="Dag",
            y="Hartslag",
            markers=True,
            range_y=[0, 130]
        )
        fig_heart.update_layout(
            height=330,
            margin=dict(l=20, r=20, t=20, b=20)
        )
        st.plotly_chart(fig_heart, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with top_right:
        st.markdown('<div class="small-card">', unsafe_allow_html=True)
        st.markdown("### Activiteit (stappen)")
        fig_steps = px.bar(
            steps_data,
            x="Dag",
            y="Stappen"
        )
        fig_steps.update_layout(
            height=330,
            margin=dict(l=20, r=20, t=20, b=20)
        )
        st.plotly_chart(fig_steps, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    bottom_left, bottom_right = st.columns([2, 1.3])

    with bottom_left:
        st.markdown('<div class="small-card">', unsafe_allow_html=True)
        st.markdown("### Bloeddruk trend")
        fig_bp = px.line(
            blood_pressure_data,
            x="Dag",
            y=["Systolisch", "Diastolisch"],
            markers=True
        )
        fig_bp.update_layout(
            height=330,
            margin=dict(l=20, r=20, t=20, b=20),
            legend_title_text=""
        )
        st.plotly_chart(fig_bp, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with bottom_right:
        st.markdown('<div class="small-card">', unsafe_allow_html=True)
        st.markdown("### Bloeddruk / laatste meting")
        fig_chol = px.pie(
            cholesterol_data,
            names="Type",
            values="Percentage",
            hole=0.2
        )
        fig_chol.update_layout(
            height=330,
            margin=dict(l=20, r=20, t=20, b=20)
        )
        st.plotly_chart(fig_chol, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.info("Deze gegevens zijn niet bedoeld als medisch advies. Raadpleeg bij twijfel altijd een arts.")


# =========================
# PERSOONLIJKE GEGEVENS
# =========================
elif pagina == "Persoonlijke gegevens":
    st.subheader("Persoonlijke gegevens")

    naam = st.text_input("Naam", "Naam Achternaam")
    leeftijd = st.number_input("Leeftijd", min_value=0, max_value=120, value=72)
    geslacht = st.selectbox("Geslacht", ["Man", "Vrouw", "Anders / zeg ik liever niet"])
    lengte = st.number_input("Lengte in cm", min_value=100, max_value=230, value=170)
    gewicht = st.number_input("Gewicht in kg", min_value=30, max_value=200, value=75)

    st.success("Persoonlijke gegevens zijn ingevuld. In deze demo worden ze nog niet opgeslagen.")


# =========================
# INSTELLINGEN
# =========================
elif pagina == "Instellingen":
    st.subheader("Instellingen")

    col1, col2 = st.columns(2)

    with col1:
        thema = st.radio("Thema", ["Licht", "Donker"], horizontal=True)
        taal = st.selectbox("Taal", ["Nederlands", "Engels"])
        lettergrootte = st.slider("Lettergrootte", 10, 24, 12)

    with col2:
        st.markdown("""
        <div class="small-card">
            <h2>Voorbeeld instellingen</h2>
            <p>Hier kun je later instellingen koppelen aan het dashboard.</p>
            <p>Bijvoorbeeld: groter lettertype, taalkeuze of donkere modus.</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("Gekozen thema:", thema)
    st.write("Gekozen taal:", taal)
    st.write("Lettergrootte:", lettergrootte)


# =========================
# DELEN
# =========================
elif pagina == "Delen":
    st.subheader("Delen")

    st.markdown("""
    Hier kan later een functie komen om het dashboard of een samenvatting te delen
    met bijvoorbeeld een zorgverlener, familielid of begeleider.
    """)

    email = st.text_input("E-mailadres ontvanger")
    toestemming = st.checkbox("Ik geef toestemming om mijn gegevens te delen.")

    if st.button("Delen"):
        if email and toestemming:
            st.success(f"Dashboard zou gedeeld worden met: {email}")
        else:
            st.warning("Vul een e-mailadres in en geef toestemming.")


# =========================
# CONTACT / HELP
# =========================
elif pagina == "Contact/Help":
    st.subheader("Contact / Help")

    zoekterm = st.text_input("Waar heb je hulp bij?")

    st.markdown("""
    ### Veelgestelde vragen

    **Wat betekent HRV?**  
    HRV staat voor hartslagvariabiliteit. Dit zegt iets over de variatie tussen hartslagen.

    **Wat betekent risicoscore?**  
    De risicoscore geeft een eenvoudige inschatting op basis van de beschikbare gegevens.

    **Is dit medisch advies?**  
    Nee. Raadpleeg bij twijfel altijd een arts.
    """)

    if zoekterm:
        st.info(f"Je zoekt naar hulp over: {zoekterm}")
