import time

def iniciar_cronometro(tempo):
    print(f"⏱️ Iniciando cronômetro: {tempo} segundos")
    while tempo:
        mins, secs = divmod(tempo, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        tempo -= 1
    print('\n🚨 Tempo esgotado!')
