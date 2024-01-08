import os

def remove_lines_from_file(input_filename, lines_to_remove):
    with open(input_filename, 'r') as file:
        lines = file.readlines()

    with open(input_filename, 'w') as file:
        for line_number, line in enumerate(lines, start=1):
            if line_number not in lines_to_remove:
                file.write(line)

def main():
    # Archivo output.txt con las líneas a eliminar
    output_filename = "output.txt"

    # Obtén las líneas a eliminar del archivo output.txt
    lines_to_remove = []
    with open(output_filename, 'r') as output_file:
        for line in output_file:
            line_number = int(line.split('-')[1])
            lines_to_remove.append(line_number)

    # Archivo pass.txt para eliminar las líneas
    pass_filename = "pass.txt"

    # Elimina las líneas señaladas del archivo pass.txt
    remove_lines_from_file(pass_filename, lines_to_remove)

    print("Las líneas señaladas han sido eliminadas del archivo pass.txt.")

if __name__ == "__main__":
    main()
