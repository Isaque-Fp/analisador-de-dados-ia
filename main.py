import os
import pandas as pd
from dotenv import load_dotenv
from google import genai 

load_dotenv()
chave = os.getenv("GEMINI_API_KEY")
print(repr(chave))
print(len(chave))

load_dotenv()
chave_secreta = os.getenv("GEMINI_API_KEY")
if chave_secreta is None:
    print("Erro crítico: Chave de API não encontrada no arquivo .env!")
    exit() 
else:
        print("Sucesso: Credenciais carregadas e seguras.")
client = genai.Client(api_key=chave_secreta)

tabela = pd.read_csv("clientes.csv")

for indice, linha in tabela.iterrows():
  nome_do_cliente = linha["Nome"]
  historico_de_compra = linha["Historico"]

  print(f"Analisando o cliente: {nome_do_cliente}")
  print(f"Histórico de compra: {historico_de_compra}")
  print("-" * 40)

  prompt = f"Analise o histórico de compras do cliente {nome_do_cliente} e forneça insights sobre seus padrões de compra e preferências. Histórico: {historico_de_compra}"
            
            
  resposta = client.models.generate_content(
                model="gemini-3.5-flash",
                contents=prompt
            )
            
            
  print(f"Insights para {nome_do_cliente}:\n{resposta.text}")
  print("=" * 40)

