import re

def ler_arquivo_texto(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        palavras = conteudo.split()
    return palavras

def tokenizar_texto(texto):
    palavras = texto.split()

    total_ofensas = 0
    total_palavras_boas = 0
    total_palavras_ruins = 0

    palavras_sem_pontuacao = []
    for palavra in palavras:
        palavra = re.sub(r'[^\w\s]', '', palavra)
        palavra = palavra.replace(".", "").lower()
        if palavra:
            palavras_sem_pontuacao.append(palavra)

    palavras_limpas = []
    
    for palavra in palavras_sem_pontuacao:
        if palavra in ofensas:
            palavras_limpas.append(palavra)
            total_ofensas += 1        
            
        
        if palavra in palavras_boas:
            total_palavras_boas += 1
        
        if palavra in palavras_ruins:
            total_palavras_ruins += 1

    print(f"Palavras ofensivas retiradas: {total_ofensas}")
    print(f"Palavras boas: {total_palavras_boas}")
    print(f"Palavras ruins: {total_palavras_ruins}")


    return palavras_limpas

def main():    
    global ofensas, palavras_boas, palavras_ruins
    
    ofensas = ler_arquivo_texto('palavroes.txt')
    palavras_boas = ler_arquivo_texto('palavras_boas.txt')
    palavras_ruins = ler_arquivo_texto('palavras_ruins.txt')

    with open("tweets.txt") as arquivo:
        tweets = arquivo.readlines()

    for tweet in tweets:
        tweetAtual = 1        
        print(f"\n\n{tweetAtual}:")
        tokens = tokenizar_texto(tweet)
        print(tokens)
        tweetAtual += 1

main()