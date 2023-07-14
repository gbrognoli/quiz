import random

# Definir as perguntas e respostas
perguntas = [
    {
        'pergunta': 'Qual o símbolo químico para o elemento oxigênio?',
        'respostas': ['O', 'H', 'C', 'N'],
        'resposta_correta': 'O'
    },
    {
        'pergunta': 'Qual elemento tem o número atômico 6?',
        'respostas': ['Cálcio', 'Carbono', 'Cloro', 'Cobre'],
        'resposta_correta': 'Carbono'
    },
    {
        'pergunta': 'Qual o grupo do elemento sódio (Na) na tabela periódica?',
        'respostas': ['1', '2', '17', '18'],
        'resposta_correta': '1'
    },
    # Adicione aqui as demais perguntas
]

# Embaralhar as perguntas
random.shuffle(perguntas)

# Iniciar o quiz
pontuacao = 0

for i, pergunta in enumerate(perguntas):
    print(f"Questão {i+1}: {pergunta['pergunta']}\n")
    random.shuffle(pergunta['respostas'])
    
    for j, resposta in enumerate(pergunta['respostas']):
        print(f"{j+1}. {resposta}")
    
    resposta_usuario = input("Digite o número da resposta correta: ")
    resposta_correta = pergunta['resposta_correta']
    
    if resposta_usuario == resposta_correta:
        print("Resposta correta!\n")
        pontuacao += 1
    else:
        print(f"Resposta incorreta. A resposta correta é: {resposta_correta}\n")

# Mostrar a pontuação final
print(f"Seu total de pontos é: {pontuacao}/{len(perguntas)}")
