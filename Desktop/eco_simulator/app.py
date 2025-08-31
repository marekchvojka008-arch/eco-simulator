import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Ekonomicko-ekologický simulátor", layout="centered")

st.title("🌍 Ekonomicko-ekologický simulátor")
st.write("Nastav parametre a pozri sa, ako sa bude vyvíjať ekonomika a emisie v nasledujúcich rokoch.")

# 🛠️ Parametre od používateľa
roky = st.slider("Počet rokov simulácie", 10, 100, 30)
populacia = st.number_input("Počiatočná populácia (milióny)", 1.0, 200.0, 5.0) * 1_000_000
rast_pop = st.slider("Ročný rast populácie (%)", 0.0, 5.0, 1.0) / 100
spotreba_na_osobu = st.number_input("Spotreba na osobu (jednotky)", 100, 10000, 1000)
emisie_na_jednotku = st.number_input("Emisie na jednotku spotreby (kg CO₂)", 0.01, 10.0, 0.5)
investicia_do_eko = st.slider("Investícia do ekológie (% ročne)", 0.0, 10.0, 1.0) / 100

# 📊 Výpočty
pop = []
spotreba = []
emisie = []

for rok in range(roky):
    populacia *= (1 + rast_pop)
    spotreba_spolu = populacia * spotreba_na_osobu
    emisie_spolu = spotreba_spolu * emisie_na_jednotku
    
    # investícia do ekológie znižuje emisie
    emisie_na_jednotku *= (1 - investicia_do_eko)
    
    pop.append(populacia)
    spotreba.append(spotreba_spolu)
    emisie.append(emisie_spolu)

# 📈 Vizualizácia
fig, ax = plt.subplots()
ax.plot(range(roky), spotreba, label="Spotreba")
ax.plot(range(roky), emisie, label="Emisie CO₂")
ax.legend()
ax.set_xlabel("Roky")
ax.set_ylabel("Hodnota")
ax.set_title("Vývoj ekonomiky a emisií")

st.pyplot(fig)
