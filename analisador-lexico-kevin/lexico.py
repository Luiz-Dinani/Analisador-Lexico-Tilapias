import re
import csv
import boto3

def separar_palavras_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        palavras = conteudo.split()

    return palavras

def tokenizar_texto(texto):
    palavras = texto.split()

    total_ofensas, total_palavras_boas, total_palavras_ruins = (0, 0, 0)
     
    palavras_sem_pontuacao = []
    for palavra in palavras:
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

def escreverCsv(dadosCsv):
    with open("analiseLexica.csv", mode="w", newline='') as arquivoCsv:
        writer = csv.writer(arquivoCsv)
        writer.writerows(dadosCsv)

def upload_s3(nomeArquivo, nomeBucket):
    s3_client = boto3.client(
        service_name='s3',
        aws_access_key_id="ASIA3WGSIV3SHHKT4OJ3",
        aws_secret_access_key="3XxG/FbEt9iOBjGh+QHdfIsxmy3W38XCujGOsiMv",
        aws_session_token="FwoGZXIvYXdzEMz//////////wEaDCh8fQTVBfQLKpYH4CLEAWs0256cjsgzwGDnNCV0YhsamrS3+nkR08+Vrq0RnIJltFVb2rLaZd2ym3CAhZD5EUy9xH0Zx/R6tdCPVKqFyTjZlDkNGegCx+LL6So5oyw4lIXO0U/duDpoLa2Pv/xgbERAKh7je+yUM/IG8tqKbH5egeXrSuCcZmIUF9OBz38GR6BwEuAn69wGcvXS4WSBXynjhtRvkFT6nH1uJQvECZC3firwweAXRoGzdWv1Z3wSfZuBXuL8M03Jn3FwTzpiIb0c5hko5NG/pgYyLevGYFSwIDY+UwS+F5Oht9kowAbMutuX+ym3zTmANe2EKYkdO4CohRV2/YM5GQ==",
        region_name='us-east-1' # voce pode usar qualquer regiao
    )
    try:
        response = s3_client.upload_file(nomeArquivo, nomeBucket, nomeArquivo)
        print(f"\n\nArquivo: {nomeArquivo} subiu para o bucket {nomeBucket}" )        
    except Exception as ex:
        print(ex)         
        return False

    return True

def ler_arquivo(nomeArquivo):
    with open("tweets.txt") as arquivo:
        tweets = arquivo.readlines()
    return tweets

def main():    
    global ofensas, palavras_boas, palavras_ruins

    dadosCsv = [["id", "QtdBoas", "QtdRuins", "QtdPalavrões"]]

    ofensas = separar_palavras_arquivo('palavroes.txt')
    palavras_boas = separar_palavras_arquivo('palavras_boas.txt')
    palavras_ruins = separar_palavras_arquivo('palavras_ruins.txt')

    tweets = ler_arquivo("tweets.txt")
    
    tweetAtual = 1        
    for tweet in tweets:               
        print(f"\n\n{tweetAtual}:")
        retorno = tokenizar_texto(tweet)
        print(retorno[0])
        dadosCsv.append([tweetAtual, retorno[1], retorno[2], retorno[3]])
        tweetAtual += 1

    escreverCsv(dadosCsv)
    upload_s3("analiseLexica.csv", "bucket-trusted-tilapias")
main()