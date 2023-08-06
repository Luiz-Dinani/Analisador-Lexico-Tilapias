import funcoes_externas as fexternas
import re
def substituir_numeros_letras(texto):
    #Substitui "@" por "a" se não estiver no começo da frase
    #re.sub() substituir padrões em uma string.
    texto = re.sub(r'(?<!^)@', 'a', texto) 
    #Substitui números no meio de uma palavra por sua letra correspondente
    texto = re.sub(r'(?<=[a-zA-Z])0(?=[a-zA-Z])', 'o', texto)
    texto = re.sub(r'(?<=[a-zA-Z])1(?=[a-zA-Z])', 'i', texto)
    texto = re.sub(r'(?<=[a-zA-Z])3(?=[a-zA-Z])', 'e', texto)
    texto = re.sub(r'(?<=[a-zA-Z])5(?=[a-zA-Z])', 's', texto)
    texto = re.sub(r'(?<=[a-zA-Z])7(?=[a-zA-Z])', 't', texto)
    return texto

def tokenizar_texto(texto):
    ofensas = fexternas.separar_palavras_arquivo('palavroes.txt')
    palavras_boas = fexternas.separar_palavras_arquivo('palavras_boas.txt')
    palavras_ruins = fexternas.separar_palavras_arquivo('palavras_ruins.txt')

    palavras = texto.split()

    total_ofensas, total_palavras_boas, total_palavras_ruins = (0, 0, 0)
     
    palavras_sem_pontuacao = []
    for palavra in palavras:
        palavra = substituir_numeros_letras(palavra)
        palavra = re.sub(r'[^\w\s]', '', palavra)
        palavra = palavra.replace(".", "").lower()

        if palavra:
            palavras_sem_pontuacao.append(palavra)

    palavras_limpas = []
    for palavra in palavras_sem_pontuacao:
        if palavra in ofensas:
            palavra = ("*" * len(palavra))
            total_ofensas += 1               
        elif palavra in palavras_boas:
            total_palavras_boas += 1            
        elif palavra in palavras_ruins:
            total_palavras_ruins += 1
        
        palavras_limpas.append(palavra)

    print(f"Palavras ofensivas retiradas: {total_ofensas}")
    print(f"Palavras boas: {total_palavras_boas}")
    print(f"Palavras ruins: {total_palavras_ruins}")

    return (palavras_limpas, total_palavras_boas, total_palavras_ruins, total_ofensas)