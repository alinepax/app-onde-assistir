# 🎬 Onde Assistir?

Um aplicativo web simples criado para resolver um problema do dia a dia: descobrir rapidamente em quais serviços de streaming um filme está disponível no Brasil.

**[Clique aqui para ver a demonstração ao vivo!](https://onde-assistir.streamlit.app/)**

---

## 🎯 O Problema

Na era da fragmentação dos streamings, encontrar um filme específico pode se tornar uma tarefa frustrante, exigindo a busca manual em diversos aplicativos como Netflix, Prime Video, Max, etc. Este projeto nasceu para centralizar essa busca em uma interface única e amigável.

## ✨ Funcionalidades

* **Busca Simples:** Digite o nome de um filme (em inglês) para iniciar a busca.
* **Detalhes Completos:** O aplicativo retorna o pôster do filme, a sinopse em português e a nota média de avaliação.
* **Fontes de Streaming:** Exibe uma lista clara dos serviços de assinatura onde o filme está disponível no Brasil.
* **Interface Web Interativa:** Construído com Streamlit para uma experiência de usuário limpa e responsiva.

![Demonstração do App](URL_DE_UMA_IMAGEM_DO_SEU_APP_FUNCIONANDO_AQUI)

---

## 🛠️ Tecnologias Utilizadas

Este projeto foi uma oportunidade para praticar a orquestração de diferentes ferramentas e serviços:

* **Linguagem:** Python
* **Interface Web:** Streamlit
* **APIs Externas:**
    * **Watchmode API:** Para obter os dados de disponibilidade nos serviços de streaming.
    * **The Movie Database (TMDb) API:** Para buscar os detalhes dos filmes, como pôster, sinopse e avaliação.
* **Gerenciamento de Dependências:** `pip` e `requirements.txt`
* **Segurança:** Utilização de variáveis de ambiente (`.env`) para proteger as chaves de API.

---

## 🚀 Como Executar Localmente

Você pode rodar este projeto na sua própria máquina seguindo os passos abaixo:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    cd seu-repositorio
    ```

2.  **Crie o arquivo de ambiente:**
    * Crie um arquivo chamado `.env` na raiz do projeto.
    * Dentro dele, adicione suas chaves de API:
        ```
        WATCHMODE_API_KEY="SUA_CHAVE_DO_WATCHMODE"
        TMDB_API_KEY="SUA_CHAVE_DO_TMDB"
        ```

3.  **Instale as dependências:**
    ```bash
    python -m pip install -r requirements.txt
    ```

4.  **Execute o aplicativo Streamlit:**
    ```bash
    streamlit run buscador.py
    ```

5.  Abra seu navegador e acesse o endereço `http://localhost:8501`.

---

## 👩‍💻 Sobre a Autora

Desenvolvido por **[Aline Paz](https://github.com/alinepax)**  
📫 Me encontre no [LinkedIn](https://www.linkedin.com/in/alinedapaz/)  
📧 Email para parcerias: aline.santospaz@gmail.com  
🎯 Este projeto faz parte do meu portfólio como profissional em transição para a área de Dados e Tecnologia.

---

⭐ Se você gostou, deixe uma estrela no repositório!
