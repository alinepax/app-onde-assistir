import requests
import streamlit as st
import os
from dotenv import load_dotenv

# Eu carrego minhas chaves secretas do arquivo .env
load_dotenv()
WATCHMODE_API_KEY = os.getenv("WATCHMODE_API_KEY")
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

# --- MINHAS FUNÇÕES DE BUSCA ---

def buscar_filmes(nome_filme):
    """Busca uma LISTA de filmes que correspondem ao nome, tratando variações."""
    busca_com_and = nome_filme.replace('&', 'and')
    busca_com_e_comercial = nome_filme.replace(' and ', ' & ')
    termos_de_busca = list(set([busca_com_and, busca_com_e_comercial]))
    todos_os_resultados = []
    ids_vistos = set()
    for termo in termos_de_busca:
        url_base = "https://api.watchmode.com/v1/search/"
        parametros = {
            'apiKey': WATCHMODE_API_KEY,
            'search_field': 'name',
            'search_value': termo,
            'types': 'movie'
        }
        try:
            resposta = requests.get(url_base, params=parametros)
            resposta.raise_for_status()
            resultados = resposta.json().get("title_results", [])
            for filme in resultados:
                if filme.get('id') and filme.get('id') not in ids_vistos:
                    todos_os_resultados.append(filme)
                    ids_vistos.add(filme.get('id'))
        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar por '{termo}': {e}")
    return todos_os_resultados

def buscar_detalhes_filme(tmdb_id):
    """Busca detalhes, incluindo o pôster, no TMDb."""
    url = f"https://api.themoviedb.org/3/movie/{tmdb_id}?api_key={TMDB_API_KEY}&language=pt-BR"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        if dados.get('poster_path'):
            dados['poster_url'] = f"https://image.tmdb.org/t/p/w500{dados.get('poster_path')}"
        else:
            dados['poster_url'] = ""
        return dados
    return None

def buscar_fontes_streaming(watchmode_id):
    """Busca as fontes de streaming no Watchmode."""
    url = f"https://api.watchmode.com/v1/title/{watchmode_id}/sources/?apiKey={WATCHMODE_API_KEY}&regions=BR"
    resposta = requests.get(url)
    return resposta.json() if resposta.status_code == 200 else []

# --- MINHA INTERFACE STREAMLIT ---

st.set_page_config(page_title="Onde Assistir?", page_icon="🎬")
st.title('🎬 Onde Assistir?')
st.subheader('Nunca mais perca tempo procurando um filme!')

# Eu uso o session_state para "lembrar" do estado da aplicação
if 'resultados' not in st.session_state:
    st.session_state.resultados = []
if 'filme_selecionado' not in st.session_state:
    st.session_state.filme_selecionado = None

# --- Tela Inicial (Busca) ---
if not st.session_state.filme_selecionado and not st.session_state.resultados:
    with st.form(key='search_form'):
        filme_desejado = st.text_input('Digite o nome de um filme (em inglês):', key='search_input')
        submit_button = st.form_submit_button(label='Buscar')

        if submit_button and filme_desejado:
            with st.spinner('Buscando filmes...'):
                resultados_busca = buscar_filmes(filme_desejado)
                if not resultados_busca:
                    st.warning('Nenhum filme encontrado com esse nome.')
                elif len(resultados_busca) == 1:
                    st.session_state.filme_selecionado = resultados_busca[0]
                    st.rerun()
                else:
                    st.session_state.resultados = sorted(resultados_busca, key=lambda x: x.get('year', 0), reverse=True)

# --- Tela de Seleção (Múltiplos Resultados) ---
if st.session_state.resultados:
    st.subheader("Encontrei estes filmes, qual você quer ver?")
    for filme in st.session_state.resultados:
        if st.button(f"{filme.get('name')} ({filme.get('year')})", key=filme.get('id')):
            st.session_state.filme_selecionado = filme
            st.session_state.resultados = [] # Limpo a lista para não aparecer mais
            st.rerun()

# --- Tela de Detalhes (Filme Selecionado) ---
if st.session_state.filme_selecionado:
    if st.button('⬅️ Fazer Nova Busca'):
        st.session_state.resultados = []
        st.session_state.filme_selecionado = None
        st.rerun()

    filme = st.session_state.filme_selecionado
    with st.spinner('Buscando detalhes do filme selecionado...'):
        watchmode_id = filme.get("id")
        tmdb_id = filme.get("tmdb_id")
        
        detalhes = buscar_detalhes_filme(tmdb_id)
        fontes = buscar_fontes_streaming(watchmode_id)
        
        if detalhes:
            st.header(f"{detalhes.get('title')} ({detalhes.get('release_date', 'N/A')[:4]})")
            col1, col2 = st.columns([1, 2])
            with col1:
                if detalhes['poster_url']:
                    st.image(detalhes['poster_url'])
            with col2:
                st.metric(label="Nota Média (TMDb)", value=f"{detalhes.get('vote_average', 0):.1f}/10")
                st.write(f"**Sinopse:** {detalhes.get('overview', 'Não disponível.')}")
            
            st.subheader('Onde Assistir no Brasil:')
            fontes_por_tipo = {"sub": set(), "rent": set(), "buy": set()}
            for fonte in fontes:
                tipo = fonte.get("type")
                nome = fonte.get("name")
                if tipo in fontes_por_tipo and nome:
                    fontes_por_tipo[tipo].add(nome)

            if fontes_por_tipo["sub"]:
                st.write("**Por Assinatura:**")
                for nome in sorted(list(fontes_por_tipo["sub"])):
                    st.write(f"- {nome.replace('Globalplay', 'Globoplay')}")
            if fontes_por_tipo["rent"]:
                st.write("**Para Alugar:**")
                for nome in sorted(list(fontes_por_tipo["rent"])):
                    st.write(f"- {nome.replace('Globalplay', 'Globoplay')}")
            if fontes_por_tipo["buy"]:
                st.write("**Para Comprar:**")
                for nome in sorted(list(fontes_por_tipo["buy"])):
                    st.write(f"- {nome.replace('Globalplay', 'Globoplay')}")
            if not any(fontes_por_tipo.values()):
                st.warning("Não encontrei informações de onde assistir para este filme no Brasil.")

# --- RODAPÉ E CRÉDITOS ---
st.markdown("---")
st.markdown("""
<div style="text-align: center; font-size: 0.9em; color: grey;">
    <p>Desenvolvido com ❤️ por <strong>Aline Paz</strong></p>
    <p>Dados de filmes fornecidos por <a href="https://www.themoviedb.org/" target="_blank">TMDb</a> | Dados de streaming fornecidos por <a href="https://watchmode.com/" target="_blank">Watchmode</a>.</p>
</div>
""", unsafe_allow_html=True)