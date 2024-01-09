import routeFetcher
from hospitalDatabase import HospitalDatabase
from topsis import Topsis

db = HospitalDatabase()
db.fetch_and_process_hospitals_data()

origin = "Rua Doutor Antonio José de Almeida, 4470-017"
# Mode: driving, walking, bicycling, transit

duration_times = routeFetcher.calculate_distance_duration(origin, "walking", db.hospitals)
wait_times = db.get_hospitals_by_color("Yellow")

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
print(tp.print_evaluation_matrix())
