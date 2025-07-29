import requests
import streamlit as st
import os
from dotenv import load_dotenv

# Eu carrego minhas chaves secretas do arquivo .env
load_dotenv()
WATCHMODE_API_KEY = os.getenv("WATCHMODE_API_KEY")
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

def buscar_id_filme(nome_filme):
    """Busca os IDs do filme no Watchmode."""
    url = f"https://api.watchmode.com/v1/search/?apiKey={WATCHMODE_API_KEY}&search_field=name&search_value={nome_filme}&types=movie"
    resposta = requests.get(url)
    if resposta.status_code != 200: return None, None
    dados = resposta.json()
    if dados.get("title_results"):
        primeiro_resultado = dados["title_results"][0]
        return primeiro_resultado.get("id"), primeiro_resultado.get("tmdb_id")
    return None, None

def buscar_detalhes_filme(tmdb_id):
    """Busca detalhes, incluindo o pôster, no TMDb."""
    url = f"https://api.themoviedb.org/3/movie/{tmdb_id}?api_key={TMDB_API_KEY}&language=pt-BR"
    resposta = requests.get(url)
    if resposta.status_code != 200: return None
    dados = resposta.json()
    if dados.get('poster_path'):
        dados['poster_url'] = f"https://image.tmdb.org/t/p/w500{dados.get('poster_path')}"
    else:
        dados['poster_url'] = ""
    return dados

def buscar_fontes_streaming(watchmode_id):
    """Busca as fontes de streaming no Watchmode."""
    url = f"https://api.watchmode.com/v1/title/{watchmode_id}/sources/?apiKey={WATCHMODE_API_KEY}&regions=BR"
    resposta = requests.get(url)
    return resposta.json() if resposta.status_code == 200 else []

# --- INTERFACE DO STREAMLIT ---
st.set_page_config(page_title="Onde Assistir?", page_icon="🎬")
st.title('🎬 Onde Assistir?')
st.subheader('Nunca mais perca tempo procurando um filme!')

filme_desejado = st.text_input('Digite o nome de um filme (em inglês):')

if st.button('Buscar'):
    if filme_desejado:
        with st.spinner('Buscando informações... Por favor, aguarde.'):
            watchmode_id, tmdb_id = buscar_id_filme(filme_desejado)
            if watchmode_id and tmdb_id:
                detalhes = buscar_detalhes_filme(tmdb_id)
                fontes = buscar_fontes_streaming(watchmode_id)

                if detalhes:
                    st.header(f"{detalhes.get('title', 'Filme não encontrado')} ({detalhes.get('release_date', 'N/A')[:4]})")
                    
                    col1, col2 = st.columns([1, 2])
                    with col1:
                        if detalhes['poster_url']:
                            st.image(detalhes['poster_url'])
                    with col2:
                        st.metric(label="Nota Média", value=f"{detalhes.get('vote_average', 0):.1f}/10")
                        st.write(f"**Sinopse:** {detalhes.get('overview', 'Não disponível.')}")
                    
                    st.subheader('Disponível para assinatura em:')
                    
                    # --- VERSÃO FINAL E LIMPA ---
                    fontes_assinatura = [f for f in fontes if f.get("type") == "sub"]
                    
                    if not fontes_assinatura:
                        st.warning('Este filme não está disponível em nenhum serviço de assinatura no Brasil no momento.')
                    else:
                        # Agora eu simplesmente mostro os nomes em uma lista.
                        for fonte in fontes_assinatura:
                            st.write(f"- {fonte['name']}")

            else:
                st.error(f"Não foi possível encontrar o filme '{filme_desejado}'. Verifique o título e tente novamente.")
    else:
        st.warning('Por favor, digite o nome de um filme.')
