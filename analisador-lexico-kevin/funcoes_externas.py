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
        service_name="s3",
        aws_access_key_id="ASIA3WGSIV3SEC44QVPJ",
        aws_secret_access_key="ikFSUcEPMmLyRxHsIhqF9kgXQZs0EuQXfdeQI9kp",
        aws_session_token="FwoGZXIvYXdzEC0aDCf457M3mBdcty03zCLEAWDt2Xwh+o8tt5JqZcvFJESTI5gckqjHOfuMwXyRXmuRyU7qpFuwwCdomVW8zMBR85iICeJAQ+FQ0aSUtmiiaOhFyIgCqkcfu3jIlnZHTJmwQTFlgWck5Nms35CwJQBzwFRYg5jO6V6oHBSDRoi9KFkvhiO2iYjLw5b0rlO/wn2qU1rtwhudpRdjYPw2sFb6SsBHz/LtcA0OUohWULHpwYZvGnSV0Z/+YojfBVYeyiHEYpxobBhwtkC4vPN76tp6SSP2/5Mo7/jUpgYyLfCE3IxFt/+RoqOKq1FrUwXOkxQ1h9VxDmWjqYUnW4UF+s0NcojNsaZiJeXZ5w==",
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
    with open(f"{nomeArquivo}") as arquivo:
        arquivoLido = arquivo.read().splitlines()
    return arquivoLido