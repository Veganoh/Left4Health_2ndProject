from hospitalDatabase import HospitalDatabase
import routeFetcher

class Ahp:
    def __init__(self, criteria, alternatives, api_key):
        self.criteria = criteria
        self.alternatives = alternatives
        self.criteria_weights = {}
        self.alternative_scores = {}
        self.db = HospitalDatabase()
        self.api_key = api_key

    def fetch_hospitals_data(self):
        self.db.fetch_and_process_hospitals_data()

    def compare_criteria(self, criteria_comparison_data):
        self.criteria_weights = criteria_comparison_data

    def compare_alternatives(self, alternatives_comparison_data):
        self.alternative_scores = alternatives_comparison_data

    def calculate_priority_with_api(self):
        hospitals_data = self.db.hospitals

        origin = "Rua Doutor António José de Almeida 628 Gueifães Maia 4470-017"
        for hospital in hospitals_data:
            destination = hospital.address
            distance, duration = routeFetcher.calculate_distance_duration(origin, destination, self.api_key)
            pass
            # Lógica para calcular a prioridade 

# Exemplo de uso
criteria = ['criterion1', 'criterion2']
alternatives = ['alternative1', 'alternative2', 'alternative3']
api_key = ' ' # chave API do Google Maps
ahp = Ahp(criteria, alternatives, api_key)

# Obtém os dados dos hospitais da API do SNS
ahp.fetch_hospitals_data()

# Suponhamos que já tens os dados de comparação predefinidos da API
criteria_comparison_data = {
    'criterion1': {'criterion1': 1, 'criterion2': 3},
    'criterion2': {'criterion1': 0.33, 'criterion2': 1},
}

alternatives_comparison_data = {
    'criterion1': {
        'alternative1': 0.8,
        'alternative2': 1.2,
        'alternative3': 0.9
    },
    'criterion2': {
        'alternative1': 1.5,
        'alternative2': 1.1,
        'alternative3': 0.7
    }
}

ahp.compare_criteria(criteria_comparison_data)
ahp.compare_alternatives(alternatives_comparison_data)

ahp.calculate_priority_with_api()



