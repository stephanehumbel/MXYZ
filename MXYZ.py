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
    49: 'In', 50: 'Sn', 51: 'Sb', 52: 'Te', 53: 'I', 54: 'Xe',
    78: 'Pt'
}
def is_num(txt):
    chiffres = "0123456789"
    return all([car in chiffres for car in txt])

       ##   print_xyz_displ(atom_displ,Nfreq)

def read_atom_displ(lines, start_line,size):
    # ne lit que la  1  iere freq
    # Dictionnaire pour stocker les deplacements des atomes
    atom_displ = {}
    Ifreq=0
    Nfreq=size
    # Parcourir les lignes à partir de la ligne de départ
    for i in range(start_line+5, start_line+5+size):
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
#        print(line)
#        print("sub",columns,len(columns))

        # Récupérer les informations sur l'atome
        atom_number = int(columns[0])
        numeroZ = int(columns[1])  # Utiliser la colonne 2 comme numeroZ
        symbol = numeroZ_to_symbol.get(numeroZ, f"Element{numeroZ}")
        x_coord = float(columns[2])
        y_coord = float(columns[3])
        z_coord = float(columns[4])
#        print("gGG",Ifreq,Nfreq,float(columns[2]),float(columns[5]))
#        if len(columns) >= 5 and ifreq < Nfreq:
#           x_coord2 = float(columns[5])
#           y_coord2 = float(columns[6])
#           z_coord2 = float(columns[7])
##           print(Ifreq,x_coord2)
#           ifreq+=1
#           if len(columns) >= 8 and ifreq < Nfreq:
#              x_coord3 = float(columns[8])
#              y_coord3 = float(columns[9])
#              z_coord3 = float(columns[10])
#              ifreq+=1
#        #print(Ifreq,x_coord2)
        # Stocker les displ dans le dictionnaire avec le numéro d'atome et numeroZ
        atom_displ[atom_number] = {'symbol': symbol,'numeroZ': numeroZ, 'x': x_coord, 'y': y_coord, 'z': z_co
ord}
##       print(atom_displ)

    return atom_displ



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
        atom_coordinates[atom_number] = {'numeroZ': numeroZ,'symbol': symbol, 'x': x_coord, 'y': y_coord, 'z'
: z_coord}

    return atom_coordinates

def find_geometry_start(nom_fic):
    # Lire toutes les lignes du fichier
    with open(nom_fic, 'r') as file:
        lines = file.readlines()
    start_indices=0
    pos_Done=0
    pos_NImag=0
    pos_Frequencies=0
    # Chercher le motif marquant le début des coordonnées de la géométrie i et autres infos
    start_indices = [i +3 for i, line in enumerate(lines) if "Coordinates (Angstroms)" in line]
    pos_Done = [i for i, line in enumerate(lines) if "SCF Done:" in line]
    pos_NImag = [i for i, line in enumerate(lines) if "imaginary frequencies (" in line]
    if pos_NImag !=0 :
      pos_Frequencies = [i for i, line in enumerate(lines) if "Frequencies -- " in line]
#    print(start_indices,pos_Done,pos_NImag,pos_Frequencies)
    return start_indices,pos_Done, pos_NImag,pos_Frequencies

def process_arguments(nom_fic, option=None):
    # Afficher le nom du fichier
    print(f"Nom du fichier : {nom_fic}")

    # Afficher l'option si elle est spécifiée
    if option is not None:
        print(f"Option : {option}")

def print_xyz_displ(atom_displ,opt):
    for atom_number, info in atom_displ.items():
        symbol = info['symbol']
        x_coord, y_coord, z_coord = info['x'], info['y'], info['z']
        print("{:<4} {:6.3f} {:6.3f} {:6.3f}".format(symbol, x_coord, y_coord, z_coord))

def print_xyz_coordinates(atom_coordinates,opt):
    """
    Print atom coordinates in formatted XYZ style.

    Parameters:
    - atom_coordinates (dict): Dictionary containing atom coordinates.
    """
    #if opt == '':
    #   print("{:<4} {:>12} {:>12} {:>12}".format("Atom", "X", "Y", "Z"))
    #   print("-" * 42)  # Separator line

    for atom_number, info in atom_coordinates.items():
        symbol = info['symbol']
        x_coord, y_coord, z_coord = info['x'], info['y'], info['z']
        print("{:<4} {:12.5f} {:12.5f} {:12.5f}".format(symbol, x_coord, y_coord, z_coord))

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

    start_indices,pos_Done,pos_NImag,pos_Frequencies = find_geometry_start(nom_fic)
#    print("sort",start_indices,pos_Done,pos_NImag,pos_Frequencies)

    # Lire toutes les lignes du fichier
    with open(nom_fic, 'r') as file:
        lines = file.readlines()
    if len(pos_Frequencies)!=0:
      if len(pos_NImag)!=0:
        NImag=int(lines[pos_NImag[0]].split()[1])
      else:
        NImag=0
      Freq=[]
      for  i in range (1,2+min(NImag,2)):
         Freq.append(float(lines[pos_Frequencies[0]].split()[1+i]))
      print("Freq=",Freq)
    else:
        NImag=-1
    # Call read_atom_coordinates function for each start index
    for start_index in start_indices:
        atom_coordinates = read_atom_coordinates(lines, start_index)
        # print("Atom Coordinates:", atom_coordinates)
    if option == '':
       #print(pos_Done)
       if len(pos_Done)!=0:
          line=lines[int(pos_Done[len(pos_Done)-1])]
          energy=line.split()[4]
       else :
          energy='00'
       print(len(atom_coordinates))
       print(nom_fic,"energy=",energy,end='')
       if NImag >=0 : 
            print("  NImag=",NImag)               
       else :
            print(" No Freq")
    print_xyz_coordinates(atom_coordinates,option)
    if len(pos_Frequencies) !=0 :
       Nfreq=min(NImag,3)
       print()
       phrase="NORMALMODES:  -----"+str(NImag)+" imaginary frequencies: "+str(Freq)
       try: 
          Nfreq=int(input(phrase))
       except:
          pass
#       for start_index in pos_Frequencies:
       size=len(atom_coordinates)
       atom_displ = read_atom_displ(lines, pos_Frequencies[0],size)
       print_xyz_displ(atom_displ,Nfreq)
       print("   ",Freq[0])
       
   
