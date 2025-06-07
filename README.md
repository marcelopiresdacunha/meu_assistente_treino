# Organizador de Treino GPT

Este projeto é um assistente virtual para organizar seus treinos na academia com cronômetro, integração com Google Agenda e chatbot interativo.

## Como usar

1. Instale as dependências:
```
pip install -r requirements.txt
```

2. Rode o assistente via linha de comando:
```
python main.py
```

3. Rode o chatbot via Gradio:
```
python chatbot/chatbot_gradio.py
```

## Integração com Google Agenda
- Ative a API do Google Calendar no [Google Cloud Console](https://console.cloud.google.com/).
- Crie credenciais e baixe o arquivo `credentials.json` para a pasta `config/`.

## Personalização
- Modifique os treinos em `app/treino.py` conforme sua necessidade.
- Ajuste o cronômetro em `app/cronometro.py`.

# Organizador de Treino GPT 🚀

Um assistente virtual para organizar treinos de academia, com cronômetro, integração com o Google Calendar e chatbot interativo.

## 📦 Funcionalidades
✅ Gerar treino com grupos musculares  
✅ Cronômetro de exercícios  
✅ Sincronização com o Google Calendar  
✅ Chatbot interativo com Gradio

## 🚀 Como executar
```bash
git clone https://github.com/seu_usuario/meu_assistente_treino.git
cd meu_assistente_treino
pip install -r requirements.txt
python main.py

Divirta-se e bons treinos! 💪🚀
