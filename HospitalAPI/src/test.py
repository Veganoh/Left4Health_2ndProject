import routeFetcher
from hospitalDatabase import HospitalDatabase
from topsis import Topsis


db = HospitalDatabase()

# Mudei o código outra vez, agora para ligar a base de dados só precisamos de fazer 1 vez quando ligarmos a API (no futuro) ou seja
# só vai demorar muito uma vez e depois é sempre instantâneo
# Este método abaixo vai buscar os dados de todos os hospitais e os tempos de espera de todas as cores
db.fetch_and_process_hospitals_data()

# Para fazeres a matriz vais precisares de uma lista com as distâncias entre a origem e cada hospital
# este método recebe a origem, os hospitais e o método de transporte e retorna uma lista de par ID de Hospistal e Tempo
origin = "Rua Doutor Antonio José de Almeida, 4470-017"
# Mode: driving, walking, bicycling, transit
duration_times = routeFetcher.calculate_distance_duration(origin, "walking", db.hospitals)
print(duration_times)
# Este método faz a mesma coisa  que o de cima só que recebe uma cor e retorna uma lista de par ID de Hospistal e Tempo de Espera no Hospital
wait_times = db.get_hospitals_by_color("Yellow")
print(wait_times)
# Dicionário para armazenar a soma para cada ID
result_dict = {}

for entry in duration_times:
    id = entry['ID']
    duration = entry['Duration']
    result_dict[id] = result_dict.get(id, {'ID': id, 'Wait Time': 0})
    result_dict[id]['Wait Time'] += duration

for entry in wait_times:
    id = entry['ID']
    wait = entry.get('Wait Time', 0)
    result_dict[id] = result_dict.get(id, {'ID': id, 'Wait Time': 0})
    result_dict[id]['Wait Time'] += wait

result_list = sorted(result_dict.values(), key=lambda x: x['Wait Time'])

print(result_list)

weights = [0.5, 0.5]

tp = Topsis(wait_times, duration_times, weights)
print(tp.get_best_alternatives())


