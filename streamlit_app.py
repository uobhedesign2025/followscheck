
import streamlit as st
import pandas as pd

st.set_page_config(page_title="FollowCheck", page_icon="🔍", layout="centered")

st.title("🔍 FollowCheck — Análise de Seguidores no Instagram")

st.markdown("Compare duas listas de seguidores (antiga e nova) e descubra quem deixou de seguir, quem começou a seguir e quem permaneceu.")

# Upload de arquivos CSV
col1, col2 = st.columns(2)
with col1:
    old_file = st.file_uploader("📂 Lista antiga", type=["csv"], key="old")
with col2:
    new_file = st.file_uploader("📂 Lista nova", type=["csv"], key="new")

if old_file and new_file:
    old_df = pd.read_csv(old_file)
    new_df = pd.read_csv(new_file)

    # Extrai só os nomes de usuário (assumindo que a coluna relevante se chame 'username' ou similar)
    old_usernames = set(old_df.iloc[:, 0].dropna().astype(str).str.strip())
    new_usernames = set(new_df.iloc[:, 0].dropna().astype(str).str.strip())

    lost_followers = sorted(list(old_usernames - new_usernames))
    new_followers = sorted(list(new_usernames - old_usernames))
    maintained = sorted(list(old_usernames & new_usernames))

    # Resultados
    st.subheader("🔎 Resultado da Análise:")
    st.write(f"📉 Total de seguidores antigos: **{len(old_usernames)}**")
    st.write(f"📈 Total de seguidores atuais: **{len(new_usernames)}**")
    st.write(f"👋 Deixaram de seguir: **{len(lost_followers)}**")
    st.write(f"➕ Novos seguidores: **{len(new_followers)}**")
    st.write(f"✅ Seguidores mantidos: **{len(maintained)}**")

    # Mostrar listas
    with st.expander("👋 Ver quem deixou de seguir"):
        if lost_followers:
            st.write(lost_followers)
        else:
            st.write("Ninguém deixou de seguir.")

    with st.expander("➕ Ver novos seguidores"):
        if new_followers:
            st.write(new_followers)
        else:
            st.write("Nenhum novo seguidor.")

    with st.expander("✅ Ver seguidores mantidos"):
        st.write(maintained)
