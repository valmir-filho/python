# Faça um jogo de perguntas e respostas com alternativas.

print("∞∞∞∞∞ Quizz Conhecimentos Gerais ∞∞∞∞∞")

while True:
    entrada = input(
        "Vamos comecar? Digite [I] para iniciar ou [S] para sair: ").upper()

    if entrada not in "IS":
        print("Erro!")

    if entrada == "S":
        break

    if entrada == "I":
        perguntas = [
            {
                "pergunta": "Quem foi Ernesto Che Guevara?",
                "alternativas":
                [
                    "Um médico Brasileiro",
                    "Um jogador de futebol",
                    "Um guerrilheiro em Cuba",
                    "Um cantor Colombiano",
                    "Um jornalista Espanhol"
                ],
                "resposta": "Um guerrilheiro em Cuba"
            },
            {
                "pergunta": "Onde o jogador de futebol Ronaldinho Gaúcho nasceu?",
                "alternativas":
                [
                    "São Paulo",
                    "Porto Alegre",
                    "Curitiba",
                    "Salvador",
                    "Rio de Janeiro"
                ],
                "resposta": "Porto Alegre"
            },
            {
                "pergunta": "Quem escreveu o livro 100 Anos de Solidão?",
                "alternativas":
                [
                    "Gabriel Garcia Marques",
                    "Raul Pompeu",
                    "Machado de Assis",
                    "Carlos Drummond de Andrade",
                    "Clarice Lispector"
                ],
                "resposta": "Gabriel Garcia Marques"
            },
            {
                "pergunta": "Como era o nome do pai do jogador de futebol Pelé?",
                "alternativas":
                [
                    "Duilinho",
                    "Jorginho",
                    "Mineirinho",
                    "Luizinho",
                    "Dondinho"
                ],
                "resposta": "Dondinho"
            },
            {
                "pergunta": "Qual cantor e compositor foi batizado com o nome de Luiz Maurício Pragana dos Santos?",
                "alternativas":
                [
                    "Mauricio Manieri",
                    "Lulu Santos",
                    "Elimar Santos",
                    "Luiz Melodia",
                    "Luiz Alves"
                ],
                "resposta": "Lulu Santos"
            },
            {
                "pergunta": "Quem era o presidente Americano, quando ocorreu o ataque terrorista as torres gêmeas de Nova York?",
                "alternativas":
                [
                    "George W. Bush",
                    "Barack Obama",
                    "Ronald Reagan",
                    "Donald Trump",
                    "Joe Biden"
                ],
                "resposta": "George W. Bush"
            },
            {
                "pergunta": "Qual é a altura do monumento do Cristo Redentor, localizado na cidade do Rio de Janeiro?",
                "alternativas":
                [
                    "42 metros",
                    "30 metros",
                    "38 metros",
                    "25 metros",
                    "60 metros"
                ],
                "resposta": "38 metros"
            },
            {
                "pergunta": 'Quem é o autor da frase: "Penso, logo existo"?',
                "alternativas":
                [
                    "Platão",
                    "Descartes",
                    "Galileu",
                    "Francis Bacon",
                    "Sócrates"
                ],
                "resposta": "Descartes"
            },
            {
                "pergunta": "Qual é o menor país do mundo?",
                "alternativas":
                [
                    "Rússia",
                    "Nauru",
                    "Malta",
                    "Mônaco",
                    "Vaticano"
                ],
                "resposta": "Vaticano"
            },
            {
                "pergunta": "Quanto tempo, aproximadamente, demora para a luz do sol chegar à terra?",
                "alternativas":
                [
                    "2 horas",
                    "1 dia",
                    "8 minutos",
                    "60 segundos",
                    "5 minutos"
                ],
                "resposta": "8 minutos"
            }
        ]

        contador = 0

        def jogo(pergunta):
            global contador
            print(pergunta["pergunta"])

            for opcao, alternativa in enumerate(pergunta["alternativas"], start=1):
                print(f"{opcao}. {alternativa}")

            while True:
                resposta = input("Digite o número da sua resposta: ")

                if resposta.isdigit():
                    resposta = int(resposta)

                    if 1 <= resposta <= len(pergunta["alternativas"]):
                        resposta = pergunta["alternativas"][resposta - 1]

                        if resposta == pergunta["resposta"]:
                            print("Resposta correta!")
                            contador += 1
                            break
                        else:
                            print(
                                f"Resposta incorreta! A resposta correta é: {pergunta['resposta']}.")
                            break
                    else:
                        print("Erro! Opção inválida.")
                else:
                    print("Erro! Digite um número válido.")

        for pergunta in perguntas:
            jogo(pergunta)
            input("Pressione Enter para a próxima pergunta...")
        print(f"Você acertou {contador} de {len(perguntas)} perguntas.")
        break

print("Obrigado por participar!")
