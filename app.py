import streamlit as st
import requests
import pandas as pd
from datetime import datetime

# --- CONFIGURAÇÕES INICIAIS DA PÁGINA E DA API ---
st.set_page_config(
    page_title="Dashboard de Ativos B3",
    page_icon="🇧🇷",
    layout="wide"
)

# Cole aqui o seu Token da API brapi
TOKEN_API = "ceV6VTy3JpwPvCPYiZNNnv" # <<<<< COLOQUE SEU TOKEN AQUI

# Lista de ativos que queremos monitorar
LISTA_DE_ATIVOS = "ITUB4"

# --- FUNÇÃO PARA BUSCAR DADOS NA API ---
@st.cache_data(ttl=600) # Cache para não sobrecarregar a API (atualiza a cada 10 minutos)
def buscar_dados_ativos(token, ativos):
    """
    Busca os dados de cotação mais recentes para uma lista de ativos na API da brapi.
    """
    try:
        url = f"https://brapi.dev/api/quote/{ativos}?token={token}"
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()
        df = pd.DataFrame(dados['results'])
        df_organizado = df[['symbol', 'regularMarketPrice', 'regularMarketChangePercent', 'logourl']]
        df_organizado.columns = ['Ativo', 'Preço', 'Variação (%)', 'Logo']
        return df_organizado
    except Exception as e:
        st.error(f"Erro ao buscar dados da API: {e}")
        return pd.DataFrame()

# --- CONSTRUÇÃO DO DASHBOARD ---

# Título e cabeçalho
st.title("📈 Dashboard de Monitoramento de Ativos - B3")
st.markdown(f"Última atualização: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

# Busca os dados
dados_df = buscar_dados_ativos(TOKEN_API, LISTA_DE_ATIVOS)

if not dados_df.empty:
    # Exibição dos cards de métricas
    st.subheader("Resumo dos Ativos")
    
    # Criando colunas para os cards
    cols = st.columns(len(dados_df))
    
    for i, row in dados_df.iterrows():
        with cols[i]:
            # Define a cor da variação
            cor_delta = "normal"
            if row['Variação (%)'] < 0:
                cor_delta = "inverse"
            
            st.metric(
                label=row['Ativo'],
                value=f"R$ {row['Preço']:.2f}",
                delta=f"{row['Variação (%)']:.2f}%",
                delta_color=cor_delta
            )

    # Tabela com dados detalhados
    st.subheader("Detalhes dos Ativos")
    
    # Configuração da exibição da imagem na tabela
    st.dataframe(
        dados_df,
        column_config={
            "Logo": st.column_config.ImageColumn("Logo da Empresa"),
            "Preço": st.column_config.NumberColumn(
                "Preço (R$)",
                format="R$ %.2f"
            ),
            "Variação (%)": st.column_config.NumberColumn(
                "Variação Diária",
                format="%.2f%%"
            ),
        },
        hide_index=True,
        use_container_width=True
    )
    
    # Botão para forçar a atualização dos dados
    if st.button('Atualizar Dados'):
        st.cache_data.clear()
        st.rerun()

else:
    st.warning("Não foi possível buscar os dados dos ativos. Verifique seu token da API ou a conexão.")