from chatbot import StudyIA

bot = StudyIA()

print("=" * 50)
print("StudyIA - Assistente Virtual")
print("Digite 'sair' para encerrar.")
print("=" * 50)

while True:

    pergunta = input("\nVocê: ")

    if pergunta.lower() == "sair":
        print("\nStudyIA: Até logo! Bons estudos.")
        break

    resposta = bot.responder(pergunta)

    print("\nStudyIA:", resposta)
