meme_dict = {
"CRINGE": "Algo vergonhoso ou constrangedor",
"STALKEAR": "Investigar a vida de alguém online",
"SHIPPAR": "Torcer para que duas pessoas fiquem juntas",
"BISCOITAR": "Fazer algo esperando receber elogios ou atenção",
"HATER": "Pessoa que critica ou demonstra ódio por alguém",
"TREND": "Algo que está fazendo muito sucesso no momento",
"FLOPAR": "Quando algo não faz sucesso ou não alcança o resultado esperado"
}


print("Digite uma palavra em LETRAS MAIÚSCULAS para descobrir o que ela significa.")
print("Você poderá consultar 5 palavras.\n")

for i in range(5):
word = input("Digite uma palavra moderna: ")

if word in meme_dict:
print("Significado:", meme_dict[word])
else:
print("😕 Desculpe, ainda não conheço essa palavra.")

print() # Pula uma linha para organizar o programa

print("📚 Obrigado por usar o dicionário!")
