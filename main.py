from app.treino import gerar_treino
from app.cronometro import iniciar_cronometro
from app.agenda import autenticar_google_calendar, criar_evento
from datetime import datetime, timedelta

def main():
    print("🎯 Bem-vindo ao Organizador de Treino GPT!")
    objetivo = input("Qual é o seu objetivo? ")
    dias_semana = int(input("Quantas vezes por semana você quer treinar? "))
    equipamentos = input("Quais equipamentos você tem? (separados por vírgula) ").split(',')

    treino = gerar_treino(objetivo, dias_semana, equipamentos)
    for dia, detalhes in treino.items():
        print(f"{dia}: {detalhes}")

    if input("Deseja adicionar os treinos à sua agenda? (s/n) ").lower() == 's':
        service = autenticar_google_calendar()
        calendario_id = 'primary'
        horario_base = input("Qual o horário de início do treino? (ex.: 2025-06-07 07:00) ")
        horario_base = datetime.fromisoformat(horario_base)
        for i in range(dias_semana):
            criar_evento(service, calendario_id, f"Treino - Dia {i+1}",
                         horario_base + timedelta(days=i), 60)

    if input("Deseja iniciar o cronômetro para o treino de hoje? (s/n) ").lower() == 's':
        iniciar_cronometro(60)

if __name__ == "__main__":
    main()
