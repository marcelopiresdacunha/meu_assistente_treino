import gradio as gr
from app.treino import gerar_treino
from app.cronometro import iniciar_cronometro

def responder(mensagem):
    if "gerar treino" in mensagem.lower():
        treino = gerar_treino("Hipertrofia", 5, ["Halteres", "Barra"])
        return f"Aqui está seu treino:\n{treino}"
    elif "iniciar cronômetro" in mensagem.lower():
        iniciar_cronometro(10)  # teste rápido
        return "Cronômetro concluído!"
    else:
        return "Desculpe, não entendi."

iface = gr.Interface(fn=responder, inputs="text", outputs="text")
iface.launch()
