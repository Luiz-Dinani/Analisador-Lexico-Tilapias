import csv
import boto3

def separar_palavras_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        palavras = conteudo.split()

    return palavras

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