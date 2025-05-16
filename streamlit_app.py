
import streamlit as st
import os
import pandas as pd

st.set_page_config(page_title="FollowCheck", layout="centered")

st.title("📱 Instagram - Monitoramento de Seguidores")

st.markdown("### 👤 Digite o @username para iniciar")
username = st.text_input("Exemplo: @agenciauobhe", max_chars=30)

if username:
    st.info("🔍 Clique abaixo para simular a busca de seguidores...")
    if st.button("📥 Buscar Seguidores"):
        # Simulando scraping
        seguidores = [f"@seguidor{i}" for i in range(1, 51)]
        df = pd.DataFrame(seguidores, columns=["@username"])
        
        pasta = "dados_seguidores"
        os.makedirs(pasta, exist_ok=True)
        caminho = os.path.join(pasta, f"{username.strip('@')}_seguidores.csv")
        df.to_csv(caminho, index=False)
        
        with open(caminho, "rb") as f:
            st.download_button("📁 Download da lista de seguidores", f, file_name=f"{username}_seguidores.csv")
        
        st.success("✅ Lista gerada com sucesso! Salve o arquivo para comparar futuramente.")

st.markdown("---")
st.markdown("### 📊 Comparar seguidores")
st.markdown("Envie o arquivo anterior e o atual para ver quem saiu ou entrou.")

col1, col2 = st.columns(2)
with col1:
    arquivo_antigo = st.file_uploader("📤 Lista antiga", type=["csv"], key="antigo")
with col2:
    arquivo_novo = st.file_uploader("📥 Lista nova", type=["csv"], key="novo")

if arquivo_antigo and arquivo_novo:
    df_antigo = pd.read_csv(arquivo_antigo)
    df_novo = pd.read_csv(arquivo_novo)

    antigos = set(df_antigo["@username"])
    novos = set(df_novo["@username"])

    perdidos = antigos - novos
    novos_seguidores = novos - antigos
    mantidos = antigos & novos

    st.markdown("### 🔍 Resultado da Análise:")
    st.write(f"👋 Deixaram de seguir: {len(perdidos)}")
    st.write(f"➕ Novos seguidores: {len(novos_seguidores)}")
    st.write(f"✅ Seguidores mantidos: {len(mantidos)}")

    if perdidos:
        st.warning("🚫 Deixaram de seguir:")
        st.write(list(perdidos))
    if novos_seguidores:
        st.success("🎉 Novos seguidores:")
        st.write(list(novos_seguidores))
