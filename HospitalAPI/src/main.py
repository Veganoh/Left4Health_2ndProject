import routeFetcher
from hospitalDatabase import HospitalDatabase

origin = "Rua Doutor António José de Almeida 628 Gueifães Maia 4470-017"
destination = "Monte do Xisto Guifoes"

db = HospitalDatabase()
db.fetch_hospitals_data()
print(db)

distance, duration = routeFetcher.calculate_distance_duration(origin, destination)
print(f"Distance: {distance}")
print(f"Duration: {duration}")