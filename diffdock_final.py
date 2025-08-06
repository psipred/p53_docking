from itertools import islice
import subprocess
import glob
import os
import re
from itertools import product

def run_diff():
    
    for file in glob.glob(f"/home/aiman/p53_docking/peptides/*.sdf"):
        pep_str = file[33:36]
        print("ANALYSING:", pep_str)
        parameter_args = ['/home/aiman/virtualenvs/diffdock/bin/python',
                            '-m',
                            "inference",
                            '--protein_path',
                            "/home/aiman/DiffDock/3JZK.pdb",
                            '--ligand', 
                            file,
                            '--out_dir',
                            "/home/aiman/p53_docking/mdm2_results/",
                            '--complex_name',
                            f'{pep_str}',
                            #change parameters according to preference
                            '--inference_steps',
                            '80',
                            '--samples_per_complex',
                            '15']
        os.chdir("/home/aiman/DiffDock/")
        parameter_out = subprocess.check_output(parameter_args)
            # break
        # break
            
# run_diff()

#Print rank1 for every peptide
print("peptide,conf")
for file in glob.glob(f"/home/aiman/p53_docking/mdm2_results/*/rank1_confidence*.sdf"):
    # print(file)
    m = re.search('^/home/aiman/p53_docking/mdm2_results/(\w{3})/rank1_confidence(.+)\.sdf', file)
    if m:
        print(f'{m.group(1)},{m.group(2)}')
