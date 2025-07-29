# 🎬 Onde Assistir?

Um aplicativo web que resolve um problema do dia a dia: descobrir rapidamente em quais serviços de streaming um filme está disponível no Brasil.  
O projeto consome e combina dados de duas APIs distintas para fornecer uma resposta completa e centralizada ao usuário.

**[Clique aqui para ver a demonstração ao vivo!](https://onde-assistir.streamlit.app/)**

---

## 🎯 Objetivos do Projeto

- **Resolver um problema real**: Acabar com a necessidade de buscar manualmente por um filme em múltiplos aplicativos de streaming.
- **Orquestrar APIs**: Desenvolver a lógica para consumir, combinar e apresentar dados de duas fontes diferentes (Watchmode e TMDb).
- **Construir uma Interface Web**: Utilizar a biblioteca Streamlit para criar uma interface de usuário limpa, interativa e amigável.
- **Adotar Boas Práticas de Desenvolvimento**: Implementar o uso de variáveis de ambiente para proteger chaves de API e criar um projeto pronto para deploy.

---

## 📄 Fonte dos Dados (Data Source)

Este projeto não utiliza um dataset estático. Ele consome dados em tempo real de duas APIs RESTful, garantindo que as informações estejam sempre atualizadas:

- **[Watchmode API](https://watchmode.com/api/)**  
  Fonte principal para descobrir em quais serviços de streaming (Netflix, Prime Video, etc.) um título está disponível, filtrando por região (Brasil).

- **[TMDb API (The Movie Database)](https://developer.themoviedb.org/docs)**  
  Utilizada para enriquecer os dados, buscando informações detalhadas como sinopse em português, nota média e pôster oficial.

---

## ✨ Funcionalidades

* **Busca Simples:** Digite o nome de um filme (em inglês) para iniciar a busca.
* **Detalhes Completos:** O aplicativo retorna o pôster do filme, a sinopse em português e a nota média de avaliação.
* **Fontes de Streaming:** Exibe uma lista clara dos serviços de assinatura onde o filme está disponível no Brasil.
* **Interface Web Interativa:** Construído com Streamlit para uma experiência de usuário limpa e responsiva.

![Demonstração do App](imgs/print1.png)

![Demonstração do App 2](imgs/print2.png)

---

## 🧰 Ferramentas Utilizadas

- ✅ **Python** — Lógica de backend e aplicação
- ✅ **Streamlit** — Criação da interface web
- ✅ **Requests** — Consumo das APIs via HTTP
- ✅ **Dotenv** — Gerenciamento seguro das chaves de API
- ✅ **Git & GitHub** — Versionamento e hospedagem do código
- ✅ **Streamlit Community Cloud** — Deploy gratuito do app

---

## 🤖 Arquitetura da Solução

```text
+--------------------------------+
| 🌐 Interface Web (Streamlit)   |
|--------------------------------|
|   Campo de busca de filme      |
|   (Input do Usuário)           |
+--------------------------------+
                 |
                 ▼
(1. Busca pelo nome do filme em inglês na Watchmode)
                 |
                 ▼
+--------------------------------+
| 🤖 API Watchmode (Busca)       |
|--------------------------------|
|  Retorna o ID do Watchmode     |
|  e o ID do TMDb do filme       |
+--------------------------------+
        |                          |
        ▼                          ▼
(2. Busca por detalhes)      (3. Busca por fontes)
    via TMDb API               via Watchmode API
        ▼                          ▼
+----------------+        +-----------------+
| 🤖 API TMDb    |        | 🤖 API Watchmode|
|----------------|        |-----------------|
| - Sinopse (PT) |        | - Streamings    |
| - Nota Média   |        |   disponíveis   |
| - Pôster       |        +-----------------+
+----------------+
        |
        ▼
(4. Combina e exibe os dados)
        ▼
+--------------------------------+
| 🌐 Interface Web (Streamlit)   |
|--------------------------------|
| Resultado completo e organizado|
+--------------------------------+


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

## ©️ Atribuição e Créditos

Este projeto utiliza dados e imagens fornecidos por terceiros.

* Todos os dados detalhados de filmes, como sinopse, nota de avaliação e pôsteres, são fornecidos pela **[The Movie Database (TMDb) API](https://www.themoviedb.org/)**. Este produto usa a API do TMDb, mas não é endossado ou certificado pelo TMDb.
* As informações sobre a disponibilidade dos filmes nos serviços de streaming são fornecidas pela **[Watchmode API](https://watchmode.com/)**.

---

## 👩‍💻 Sobre a Autora

Desenvolvido por **[Aline Paz](https://github.com/alinepax)**  
📫 Me encontre no [LinkedIn](https://www.linkedin.com/in/alinedapaz/)  
📧 Email para parcerias: aline.santospaz@gmail.com  
🎯 Este projeto faz parte do meu portfólio como profissional em transição para a área de Dados e Tecnologia.

---

⭐ Se você gostou, deixe uma estrela no repositório!
