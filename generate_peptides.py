from itertools import product
import subprocess
import os

def make_peptides(letters):
  pep_strs = list(map("".join, product(letters, repeat=3)))
  # print(pep_strs)
  for pep_str in pep_strs:
    pypept_args = [#'python3',
                   '/home/aiman/virtualenvs/diffdock/bin/run_pyPept',
                    '--fasta',
                    pep_str,
                    '--prefix',
                    pep_str]
    pypept_out = subprocess.check_output(pypept_args)
    
    obabel_args = ['/usr/bin/obabel', 
                   '-ipdb', 
                   f"{pep_str}.pdb", 
                   '-osdf',
                   '-O',
                   f"{pep_str}.sdf"]
    ob_out = subprocess.check_output(obabel_args)
    os.remove(f"{pep_str}.png")
    os.remove(f"{pep_str}.pdb")
    #exit()
  
  return pep_str

pepstr = ("ARNDEGCQHILKMFPSTWYV")
make_peptides(pepstr)
