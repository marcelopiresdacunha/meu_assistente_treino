from langchain.llms import OpenAI
from app.treino import gerar_treino
from app.cronometro import iniciar_cronometro

llm = OpenAI(model="gpt-4o", temperature=0.7)

def interagir_chatbot(mensagem):
    if "gerar treino" in mensagem.lower():
        treino = gerar_treino("Hipertrofia", 5, ["Halteres", "Barra"])
        return f"Aqui está seu treino:\n{treino}"
    elif "iniciar cronômetro" in mensagem.lower():
        iniciar_cronometro(60)
        return "Cronômetro concluído!"
    else:
        resposta = llm(f"{mensagem}")
        return resposta
