# Analisador de Dados com IA (Gemini GenAI) 

## Sobre o Projeto
Este é um motor de extração e análise de dados construído em Python. O sistema consome uma base de dados estruturada de clientes, isola o histórico de compras e utiliza a nova SDK do Google Gemini (GenAI) para gerar automaticamente um parecer inteligente sobre o risco de perda (churn) de cada cliente.

## Tecnologias Utilizadas
* **Python 3:** Linguagem base do sistema.
* **Pandas:** Para ingestão estruturada e manipulação do arquivo CSV.
* **Google GenAI SDK:** Para comunicação com a API do Gemini 3.5 Flash.
* **Variáveis de Ambiente:** Isolamento de credenciais de API por questões de segurança.

## Como rodar o projeto localmente
1. Certifique-se de ter o Python instalado.
2. Instale as dependências executando:
   `pip install pandas google-genai`
3. Crie um arquivo `.env` na raiz do projeto e adicione a sua chave de API:
   `GEMINI_API_KEY=sua_chave_aqui`
4. Execute o arquivo principal:
   `python main.py`
