import string
import os

def find_duplicate_passwords(input_filename, output_filename):
    password_set = set()
    duplicate_passwords = {}

    with open(input_filename, 'r') as file:
        with open(output_filename, 'w') as output_file:
            for line_number, password in enumerate(file, start=1):
                password = password.strip()
                if password in password_set:
                    if password not in duplicate_passwords:
                        duplicate_passwords[password] = [line_number]
                        output_file.write(f"{password}-{line_number}\n")
                    else:
                        duplicate_passwords[password].append(line_number)
                        output_file.write(f"{password}-{line_number}\n")
                else:
                    password_set.add(password)

    return duplicate_passwords

# Puedes llamar a esta función con los nombres de tus archivos
input_filename = "pass.txt"
output_filename = "output.txt"
duplicates = find_duplicate_passwords(input_filename, output_filename)

if not duplicates:
    print("No se encontraron contraseñas repetidas en el archivo.")
else:
    print("Contraseñas repetidas encontradas:")
    for password, lines in duplicates.items():
        print(f"Contraseña: {password}, Repetida en las líneas: {', '.join(map(str, lines))}")
