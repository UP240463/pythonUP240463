
# Day 16

from datetime import datetime

# Ejercicio 1: Obtener el día, mes, año, hora, minuto y timestamp
now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()

print(f'Día: {day}, Mes: {month}, Año: {year}, Hora: {hour}, Minuto: {minute}')
print('Timestamp:', timestamp)

# Ejercicio 2: Formatear la fecha actual con el formato "%m/%d/%Y, %H:%M:%S"
formatted_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("Fecha formateada:", formatted_time)

# Ejercicio 3: Convertir una cadena de texto a un objeto datetime
date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("Objeto datetime:", date_object)

# Ejercicio 4: Calcular la diferencia de tiempo hasta el nuevo año (1 de enero)
new_year = datetime(year=2024, month=1, day=1)
time_left = new_year - now
print('Tiempo restante para el nuevo año:', time_left)

# Ejercicio 5: Calcular la diferencia entre el 1 de enero de 1970 y ahora
epoch_time = datetime(year=1970, month=1, day=1)
time_since_epoch = now - epoch_time
print('Tiempo transcurrido desde el 1 de enero de 1970:', time_since_epoch)
