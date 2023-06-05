import re

numero = 1

def substituir_caracteres(texto):
    #Substitui "@" por "a" se não estiver no começo da frase
    #re.sub() substituir padrões em uma string.
    texto = re.sub(r'(?<!^)@', 'a', texto) 
    #Substitui "3" entre duas letras por "e"
    texto = re.sub(r'(?<=[a-zA-Z])3(?=[a-zA-Z])', 'e', texto)
    return texto

def tokenizar_texto(texto):
    palavras = texto.split()#split é aplicado na string e retorna uma lista de substrings

    total_ofensas = 0
    total_frases_boas = 0
    total_frases_ruins = 0
    total_palavras_chaves = 0

    palavras_sem_pontuacao = []
    for palavra in palavras:
        # tirando pontuação
        palavra = re.sub(r'[^\w\s]', '', palavra)
        # tirando pontos finais
        palavra = palavra.replace(".", "")
        if palavra:
            palavras_sem_pontuacao.append(palavra)

    palavras_censuradas = []
    palavroes = ["merda","caralho","foda-se","porra","puta","cacete","cu","bosta","corno","vai se foder","filho da puta","vadia","pinto","vagabundo","desgraça","foder","buceta","arrombado","desgraçado","chupar",]
    frases_ruins = ["ruim","terrível","horrível","desagradável","péssimo","detestável","desastroso","insuportável","desanimador","deprimente","aborrecido","desalentador","desastroso","desconfortável","lamentável","desfavorável","desgastante","desolador","desprezível","desagradecido",]
    frases_boas = ["bom","ótimo","excelente","maravilhoso","fantástico","incrível","espetacular","fenomenal","excepcional","impecável","perfeito","sensacional","surpreendente","formidável","brilhante","notável","agradável","gratificante","encantador","radiante"]
    frases_chaves = ["camarao", "camarão","camarões","camaroes" "camarão de pata branca","camarão pata branca","camarao de pata branca", "camarao pata branca"]

    for palavra in palavras_sem_pontuacao:
        if palavra.lower() in palavroes:
            #Substitui caractere por "*"
            palavra = re.sub(r'\S', '*', palavra)
            total_ofensas += 1
        palavras_censuradas.append(palavra)

    for palavra in palavras_sem_pontuacao:
        if palavra.lower() in frases_boas:
            total_frases_boas += 1

    for palavra in palavras_sem_pontuacao:
        if palavra.lower() in frases_ruins:
            total_frases_ruins += 1

    for frase_chave in frases_chaves:
        if frase_chave.lower() in texto.lower():
           
            total_frases_boas += 1
            total_palavras_chaves += 1

    print(f"\n{numero}:")
    print(f"Palavras censuradas: {total_ofensas}")
    print(f"Palavras boas: {total_frases_boas}")
    print(f"Palavras ruins: {total_frases_ruins}")
    print(f"Palavras-chave: {total_palavras_chaves}")

    return palavras_censuradas

tweets = [
    "Os camarões estão com um exelente preço",
    "Os camarões de pata branca tiveram um t3rrível aumento no seu custo",
    "Caralho pedi um c@marão na praia e me mandaram essa m3rda cru"
]

for elemento in tweets:
    elemento = substituir_caracteres(elemento)
    tokens = tokenizar_texto(elemento)

    print(tokens)
    numero += 1
