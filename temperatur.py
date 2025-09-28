import csv

# 3.1 Funksjon for å lese temperaturer per måned fra fila

def read_monthly_temperatures(filename):
    temps = {}
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) < 2:
                continue
            month, temp = row[0], float(row[1])
            temps[month] = temp
    return temps

# Teste funksjonen å skrive ut samlingen
monthly_temps = read_monthly_temperatures('max_temperatures_per_month.csv')
print("Monthly temperature records:")
print(monthly_temps)

# 3.2 Progg for å finne nye varmerekorder i 2018

def print_new_records(monthly_temps, daily_filename):
    with open(daily_filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) < 3:
                continue
            month, day, temp = row[0], row[1], float(row[2])
            if month in monthly_temps and temp > monthly_temps[month]:
                print(f"New record in {month} on day {day}: {temp}°C (old: {monthly_temps[month]}°C)")

# Kalle tilbake funksjonen
print_new_records(monthly_temps, 'max_daily_temperature_2018.csv')

# 3.3 Funksjon for å oppdatere rekordene

def update_records(monthly_temps, daily_filename):
    updated = monthly_temps.copy()
    with open(daily_filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) < 3:
                continue
            month, _, temp = row[0], row[1], float(row[2])
            if month in updated and temp > updated[month]:
                updated[month] = temp
    return updated

# Teste oppdateringa
updated_temps = update_records(monthly_temps, 'max_daily_temperature_2018.csv')
print("Updated monthly records:")
print(updated_temps)

# 3.4 Funksjon for å lagre til ny fil

def save_monthly_temperatures(temps, filename):
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for month, temp in temps.items():
            writer.writerow([month, temp])

# Teste lagringa
save_monthly_temperatures(updated_temps, 'updated_max_temperatures_per_month.csv')