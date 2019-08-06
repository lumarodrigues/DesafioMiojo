'''

Calcula o tempo para cozinhar um miojo no tempo exato sendo
duas ampulhetas diferentes e com tempos maiores os unicos
medidores disponiveis.

'''

def TempoMiojo(tempoMiojo, amp1, amp2):
    if amp1 > tempoMiojo and amp2 > tempoMiojo:
        if (amp1 - amp2 > 0) == True:
            tempoTotal = (tempoMiojo + amp1)
            voltas = tempoTotal/amp2
        else:
            tempoTotal = (tempoMiojo + amp2)
            voltas = tempoTotal/amp1
        if voltas != int(voltas):
            print("Não é possível cozinhar o miojo no tempo exato.")
        else:
            print("O miojo ficará pronto em {} minutos. {} voltas na ampulheta menor.".format(tempoTotal,int(voltas)))
    else:
        print("Erro! Tente usar ampulhetas com tempos maiores.")


