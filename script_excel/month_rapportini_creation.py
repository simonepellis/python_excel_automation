import openpyxl
from datetime import datetime
import calendar
import os
from openpyxl.utils import get_column_letter

# Creazione del file Excel
workbook = openpyxl.Workbook()
sheet = workbook.active

# Ottenere i giorni del mese corrente
now = datetime.now()
year = now.year
month = now.month
num_days = calendar.monthrange(year, month)[1]
month_name = now.strftime("%B")

# Aggiunta dei giorni come colonne
for day in range(1, num_days + 1):
    column_letter = get_column_letter(day + 2)  # day + 1 per evitare di sovrascrivere la colonna A e B
    cell = f"{column_letter}1"
    sheet[cell] = f"{day} {month_name}"

# Aggiunta delle righe argomento
sheet["A2"] = "argomento 1"
sheet["A3"] = "argomento 2"

# Creazione della directory se non esiste
directory = "file_rapportini"
if not os.path.exists(directory):
    os.makedirs(directory)

# Salvataggio del file Excel
filename = f"file_rapportini/tabella_{month_name.lower()}.xlsx"
workbook.save(filename)
print(f"File {filename} creato correttamente.")