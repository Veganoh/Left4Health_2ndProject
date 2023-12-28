import routeFetcher
from hospitalDatabase import HospitalDatabase
from Ahp import Ahp

# Função para priorizar os hospitais com base na distância e tempo de espera utilizando o método AHP
def prioritize_hospitals(hospitals):
    # Mapeando os dados necessários para a análise AHP
    hospital_data = {hospital.name: {"distance": hospital.distance, "wait_time": hospital.wait_time} for hospital in hospitals}
    
    # Inicializando e usando a classe AHP
    ahp_system = Ahp(["distance", "wait_time"], hospital_data)
    ahp_system.compare_criteria()
    ahp_system.compare_alternatives()
    priorities = ahp_system.calculate_priority()

    # Ordenando os hospitais com base nas prioridades calculadas
    sorted_hospitals = sorted(hospitals, key=lambda x: priorities["distance"] * x.distance + priorities["wait_time"] * x.wait_time)
    
    return sorted_hospitals

def main():
    origin = "Rua Doutor António José de Almeida 628 Gueifães Maia 4470-017"
    destination = "Monte do Xisto Guifoes"

    # Instanciando a base de dados de hospitais e procura dos dados
    db = HospitalDatabase()
    db.fetch_hospitals_data()

    # Recolha da distância e duração para cada hospital
    for hospital in db.hospitals:
        distance, duration = routeFetcher.calculate_distance_duration(origin, hospital.address)
        hospital.distance = distance
        hospital.duration = duration

    # Priorização dos hospitais com base na distância e tempo de espera
    sorted_hospitals = prioritize_hospitals(db.hospitals)

    # Exibição dos hospitais priorizados
    print("Hospitals Prioritized:")
    for idx, hospital in enumerate(sorted_hospitals, 1):
        print(f"{idx}. {hospital.name} - Distance: {hospital.distance}, Wait Time: {hospital.wait_time}")

if __name__ == "__main__":
    main()