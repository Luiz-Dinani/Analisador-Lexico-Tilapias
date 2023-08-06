import funcoes_texto as ftexto
import funcoes_externas as fexternas

def main():    
    dadosCsv = [["id", "QtdBoas", "QtdRuins", "QtdPalavrões"]]
    
    tweets = fexternas.ler_arquivo("tweets.txt")
    
    tweetAtual = 1        
    for tweet in tweets:               
        print(f"\n\n{tweetAtual}:")
        retorno = ftexto.tokenizar_texto(tweet)
        print(retorno[0])
        dadosCsv.append([tweetAtual, retorno[1], retorno[2], retorno[3]])
        tweetAtual += 1

    fexternas.escreverCsv(dadosCsv)
    fexternas.upload_s3("analiseLexica.csv", "bucket-trusted-tilapias")

main()