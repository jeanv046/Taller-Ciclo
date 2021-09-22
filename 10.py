import random

def Encuestas():
    votosPrimerCandidato = 0
    votosSegundoCandidato = 0
    votosTercerCandidato = 0
    for i in range(50000):
        candidatos = random.randint(1, 3)
        if candidatos == 1:
            votosPrimerCandidato += 1
        elif candidatos == 2:
            votosSegundoCandidato += 1
        else:
            votosTercerCandidato += 1
    if votosPrimerCandidato > votosSegundoCandidato and votosPrimerCandidato > votosTercerCandidato:
        print("Gano el primer candidato")
        print(f'Tuvo un total de votos {votosPrimerCandidato}')
    elif votosSegundoCandidato > votosPrimerCandidato and votosSegundoCandidato > votosTercerCandidato:
        print("Gano el segundo candidato")
        print(f'Tuvo un total de votos {votosSegundoCandidato}')
    elif votosTercerCandidato > votosPrimerCandidato and votosTercerCandidato > votosSegundoCandidato:
        print("Gano el tercer candidato")
        print(f'Tuvo un total de votos {votosTercerCandidato}')
    elif votosPrimerCandidato == votosSegundoCandidato and votosPrimerCandidato == votosTercerCandidato:
        print(f'Los 3 candidatos empataron con un numero de votos de: {votosPrimerCandidato}')
    elif votosPrimerCandidato == votosSegundoCandidato:
        print(f'El primer candidato empato con el segundo candidato con un total de votos de: {votosPrimerCandidato}')
    elif votosPrimerCandidato == votosTercerCandidato:
        print(f'El primer candidato empato con el tercer candidato con un total de votos de: {votosPrimerCandidato}')
    elif votosSegundoCandidato == votosTercerCandidato:
        print(f'El segundo candidato empato con el tercer candidato con un total de votos de: {votosSegundoCandidato}')

Encuestas()