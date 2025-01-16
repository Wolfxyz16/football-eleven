"""
Este es un pequeño script que sirve para eliminar las filas que contengan algún elemento vacio de un archivo csv
"""
import csv

# Ruta del archivo CSV
input_file = "data/players-2324.csv"
output_file = "data/players-2324-good.csv"

# Leer el archivo CSV y filtrar filas no vacías
with open(input_file, mode="r", newline='', encoding="utf-8") as infile:
    reader = csv.reader(infile)
    rows = [row for row in reader if all(cell.strip() for cell in row)]  # Filtra filas no vacías

# Escribir las filas filtradas a un nuevo archivo CSV
with open(output_file, mode="w", newline='', encoding="utf-8") as outfile:
    writer = csv.writer(outfile)
    writer.writerows(rows)

print(f"Filas no vacías guardadas en {output_file}")
