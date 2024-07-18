import Bio.PDB
from Bio.PDB import *
from openbabel import pybel
import math
import glob

for file in (glob.glob(f"/home/aiman/p53_docking/fin_results/*/rank1_confidence*.sdf")): 
    for mol in pybel.readfile('sdf', file):
        max_dist = 0
        for atom in mol:
            for mol2 in pybel.readfile('sdf', file):
                for atom2 in mol2:
                    coord1 = atom.coords
                    coord2 = atom2.coords
                    P = coord1
                    Q = coord2
                    moldistance = math.dist(P,Q)
                    if moldistance >= max_dist:
                        max_dist = moldistance

    print(f"{file[36:39]},{max_dist}")