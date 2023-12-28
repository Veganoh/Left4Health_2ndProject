import routeFetcher
from hospitalDatabase import HospitalDatabase

db = HospitalDatabase()


# Este método preenche a database com os hospitais que tem urgencias, e depois preenche o atribute wait_time de cada hospital com
# o tempo de espera da urgencia geral de cada hospital
# isto é tudo da api do sns n precisamos de mais nada
# COMO A API DO SNS É UMA MERDA E AS VEZES FUNCIONA OUTRA VEZES NAO, ELE TENTA 3 VEZES POR HOSPITAL
# pedir o tempo de espera, se falhar 3 vezes fica [] , ele leva timeout passado 10 segunso e volta a tentar
# ou seja worst case scenario esse método demora 30 segundos para preencher a database e os tempos

#VVVVVVVVVVVVVVVVVV Pra testares
#db.fetch_and_process_hospitals_data()
#print(db)

# para a api do google tambem é simples
# apenas vais meter a origem do que o utilizador escrever no frontend, e a morada de cada hospital o metodo retorna a distancia e a duração
# N TE ESQUEÇAS DE COLOCAR O FICHEIRO .ENV SE NAO O ROUTE FETCHER N FUNCIONA
origin = "Rua Doutor António José de Almeida 628 Gueifães Maia 4470-017"
destination = "Monte do Xisto Guifoes"

resposta = routeFetcher.calculate_distance_duration(origin, destination)
print(resposta)