#!/usr/bin/env python3
import sys

numeroZ_to_symbol = {
    1: 'H', 2: 'He', 3: 'Li', 4: 'Be', 5: 'B', 6: 'C',
    7: 'N', 8: 'O', 9: 'F', 10: 'Ne', 11: 'Na', 12: 'Mg',
    13: 'Al', 14: 'Si', 15: 'P', 16: 'S', 17: 'Cl', 18: 'Ar',
    19: 'K', 20: 'Ca', 21: 'Sc', 22: 'Ti', 23: 'V', 24: 'Cr',
    25: 'Mn', 26: 'Fe', 27: 'Co', 28: 'Ni', 29: 'Cu', 30: 'Zn',
    31: 'Ga', 32: 'Ge', 33: 'As', 34: 'Se', 35: 'Br', 36: 'Kr',
    37: 'Rb', 38: 'Sr', 39: 'Y', 40: 'Zr', 41: 'Nb', 42: 'Mo',
    43: 'Tc', 44: 'Ru', 45: 'Rh', 46: 'Pd', 47: 'Ag', 48: 'Cd',
    49: 'In', 50: 'Sn', 51: 'Sb', 52: 'Te', 53: 'I', 54: 'Xe'
}

def read_atom_coordinates(lines, start_line):
    # Dictionnaire pour stocker les coordonnées des atomes
    atom_coordinates = {}

    # Parcourir les lignes à partir de la ligne de départ
    for i in range(start_line, len(lines)):
        line = lines[i].strip()
#        print("sub",line)
        # Arrêter si on atteint les tirets
        if '-----' in line:
            break

        # Ignorer les lignes vides
        if not line:
            continue

        # Diviser la ligne en colonnes
        columns = line.split()
        # print("sub",columns[0])

        # Récupérer les informations sur l'atome
        atom_number = int(columns[0])
        numeroZ = int(columns[1])  # Utiliser la colonne 2 comme numeroZ
        x_coord = float(columns[3])
        y_coord = float(columns[4])
        z_coord = float(columns[5])

        # Récupérer le symbole de l'élément à partir de numeroZ_to_symbol
        symbol = numeroZ_to_symbol.get(numeroZ, f"Element{numeroZ}")


        # Stocker les coordonnées dans le dictionnaire avec le numéro d'atome et numeroZ
        atom_coordinates[atom_number] = {'numeroZ': numeroZ,'symbol': symbol, 'x': x_coord, 'y': y_coord, 'z': z_coord}

    return atom_coordinates

def find_geometry_start(nom_fic):
    # Lire toutes les lignes du fichier
    with open(nom_fic, 'r') as file:
        lines = file.readlines()

    # Chercher le motif marquant le début des coordonnées de la géométrie
    start_indices = [i +3 for i, line in enumerate(lines) if "Coordinates (Angstroms)" in line]
    return start_indices

def process_arguments(nom_fic, option=None):
    # Afficher le nom du fichier
    print(f"Nom du fichier : {nom_fic}")

    # Afficher l'option si elle est spécifiée
    if option is not None:
        print(f"Option : {option}")

def print_xyz_coordinates(atom_coordinates,opt):
    """
    Print atom coordinates in formatted XYZ style.

    Parameters:
    - atom_coordinates (dict): Dictionary containing atom coordinates.
    """
    if opt == '':
       print("{:<4} {:>12} {:>12} {:>12}".format("Atom", "X", "Y", "Z"))
       print("-" * 42)  # Separator line

    for atom_number, info in atom_coordinates.items():
        symbol = info['symbol']
        x_coord, y_coord, z_coord = info['x'], info['y'], info['z']
        print("{:<4} {:12.6f} {:12.6f} {:12.6f}".format(symbol, x_coord, y_coord, z_coord))



if __name__ == "__main__":
    # Vérifier le nombre d'arguments
    if len(sys.argv) == 2:
        nom_fic = sys.argv[1]
        option = ''
        #process_arguments(nom_fic)
    elif len(sys.argv) == 3:
        nom_fic = sys.argv[1]
        option = sys.argv[2]
        #process_arguments(nom_fic, option)
    else:
        print("Usage: {} <nom_fichier> [option]".format(sys.argv[0]))

    start_indices = find_geometry_start(nom_fic)
#    print("Indices des lignes de début de géométrie:", start_indices)
    
    # Lire toutes les lignes du fichier
    with open(nom_fic, 'r') as file:
        lines = file.readlines()

    # Call read_atom_coordinates function for each start index
    for start_index in start_indices:
        atom_coordinates = read_atom_coordinates(lines, start_index)
        # print("Atom Coordinates:", atom_coordinates)

    print_xyz_coordinates(atom_coordinates,option)

