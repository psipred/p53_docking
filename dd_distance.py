import Bio.PDB
from Bio.PDB import *
from openbabel import pybel
import math

parser = PDBParser()
structure = parser.get_structure("1YCR", "1YCR.pdb")
print("Residue,ResidueId,Atom.pdb,Atom.sdf,AtomId.sdf,Distance")
for model in structure:
    for chain in model:
        for residue in chain:
            for atom1 in residue:
                min_dist = 10000
                closest_lig_atom_type = ''
                closest_lig_atom_id = 0
                coord1 = atom1.get_coord()
                for mol in pybel.readfile('sdf', 'rank1.sdf'):
                    for atom2 in mol:
                        coord2 = atom2.coords
                        P = coord1
                        Q = coord2
                        moldistance = math.dist(P,Q)
                        if moldistance < min_dist:
                            min_dist = moldistance
                            closest_lig_atom_id = atom2.idx
                            closest_lig_atom_type = atom2.type
                pdb_atom_type = atom1.get_id ()
                residue_name = residue.get_resname()
                residue_id = residue.full_id[3][1]
                print (f"{residue_name},{residue_id},{pdb_atom_type},{closest_lig_atom_type},{closest_lig_atom_id},{min_dist}")
                
                        



                    
            
            

   


    
    