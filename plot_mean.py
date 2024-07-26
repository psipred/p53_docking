from openbabel import pybel
import math
import glob
import statistics
import numpy as np
import matplotlib.pyplot as plt


distance = []
peptide = []
a = range(0,21)

for b in a:
    for file in (glob.glob(f"GAA/rank{b}_confidence*.sdf")):
        with open(file, "r") as fhIn:
                content = fhIn.read()
                lines = content.split("\n")
                analysis_line = lines[4].lstrip()
                entries = analysis_line.split()
                if len(entries) < 16:
                    continue
        for mol in pybel.readfile('sdf', file):
                add = 0
                i = 0
                process_file = True
                for atom in mol:
                    coords = atom.coords
                    if np.isnan(coords[0]) or np.isnan(coords[1]) or np.isnan(coords[2]):
                        process_file = False
                if not process_file:
                    break
                for file1 in (glob.glob(f"GAA/rank1_confidence*.sdf")):
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
                pep = file[4:10] 
                if file != file1:
                    distance.append(avg)
                    peptide.append(pep)
    


ax = plt.subplot()
ax.hist(distance, bins=20, edgecolor='k')
plt.axvline(2.09515961, color='k', linestyle='dashed', linewidth=1)
plt.xlabel('Count')
plt.ylabel('Mean distance from rank1')
plt.title('GAA mean plot')
#ax.set_yticks(np.arange(12, 20.1, 0.5))
plt.show()
#print(peptide)