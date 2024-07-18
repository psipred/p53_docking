import Bio.PDB
from Bio.PDB import *
from openbabel import pybel
import math
import glob
import statistics
import numpy as np

print("Peptide,Average,Standard Deviation")
for file0 in glob.glob(f"/home/aiman/p53_docking/fin_results/*/"):
    if "ACE" not in file0[36:39]:
        continue
    distance = []
    avg_dist = 0
    
    for file in (glob.glob(f"{file0}rank*_confidence*.sdf")):
        for mol in pybel.readfile('sdf', file):
            add = 0
            i = 0
            process = True
            for atom in mol:
                coords = atom.coords
                if np.isnan(coords[0]) or np.isnan(coords[1]) or np.isnan(coords[2]):
                    process = False
            if not process:
                break
            for file1 in (glob.glob(f"{file0}rank1_confidence*.sdf")):
                for mol2 in pybel.readfile('sdf', file1):
                    for idx, atom in enumerate(mol):
                    # print(file, file1)
                        atom2 = list(mol2)[idx]
                        coord1 = atom2.coords
                        if (atom2.idx == atom.idx):
                            coord2 = atom.coords
                            P = coord1
                            Q = coord2
                            moldistance = math.dist(P,Q)
                            # print(coord1, coord2, moldistance)
                                                            
                add += moldistance
                i += 1
            avg = add/i 
            distance.append(avg)
    avg_dist = statistics.mean(distance)
    stdev = statistics.stdev(distance)
    print (f"{file0[36:39]},{str(avg_dist)},{str(stdev)}")
    
