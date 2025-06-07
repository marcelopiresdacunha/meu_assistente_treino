def gerar_treino(objetivo, dias_semana, equipamentos):
    treino = {}
    grupos = ['Peito', 'Costas', 'Pernas', 'Ombros', 'Braços']
    for i in range(dias_semana):
        grupo = grupos[i % len(grupos)]
        treino[f'Dia {i+1}'] = {
            'Grupo Muscular': grupo,
            'Exercícios': [
                f'{grupo} - Exercício 1',
                f'{grupo} - Exercício 2',
                f'{grupo} - Exercício 3'
            ],
            'Séries': 3,
            'Repetições': 12,
            'Descanso': '60 segundos'
        }
    return treino
