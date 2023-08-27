import funcoes_texto as ftexto
import funcoes_externas as fexternas

def main():    
    dadosCsv = [["Tweet", "QtdOfensas",	"QtdPalavraBoas", "QtdPalavrasRuins"]]
    tweets = fexternas.ler_arquivo("tweets.txt")
    
    idTweetAtual = 1        
    for tweet in tweets:               
        print(f"\n\n{idTweetAtual}:")
        retorno = ftexto.tokenizar_texto(tweet)
        print(retorno[0])
        dadosCsv.append([tweet, retorno[3], retorno[1], retorno[2]])
        idTweetAtual += 1

    fexternas.escreverCsv(dadosCsv)
    fexternas.upload_s3("analiseLexica.csv", "bucket-trusted-tilapias")

main()
