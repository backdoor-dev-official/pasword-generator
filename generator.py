import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_passwords(length, count):
    passwords = set()
    while len(passwords) < count:
        password = generate_password(length)
        passwords.add(password)
        yield password  # Generador para una contraseña a la vez

def save_passwords_to_file(passwords, filename):
    with open(filename, 'w') as f:
        for password in passwords:
            f.write(password + '\n')

def main():
    # Preguntar al usuario la longitud de las contraseñas
    while True:
        try:
            length = int(input("Ingrese la longitud de las contraseñas: "))
            break
        except ValueError:
            print("Debe ingresar un número entero.")

    # Generar las contraseñas
    passwords = generate_passwords(length, 100000000)  # 100 millones

    # Escritura de las contraseñas en un archivo
    save_passwords_to_file(passwords, "pass.txt")
    print("\nLas contraseñas han sido generadas y guardadas en 'pass.txt' correctamente.")

if __name__ == "__main__":
    main()
