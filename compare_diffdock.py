from itertools import islice
import subprocess
import glob
import os
import re

#Random peptides to test
pep_strs = ['AAA', 'ADN', 'WPA', 'YYY']

def run_diff():
#Generate the range to test
    inference_steps = list(islice(range(105), 5, 100, 5))
    samples_complex = list(islice(range(105), 5, 100, 5))

    for pep_str in pep_strs:
            #Run loop for sample_per_complex 
            #while changing inference_steps
        for sample_complex in samples_complex:
            for inference_step in inference_steps:
                parameter_args = ['/home/aiman/virtualenvs/diffdock/bin/python',
                                '-m',
                                "inference",
                                '--protein_path',
                                "/home/aiman/DiffDock/1YCR.pdb",
                                '--ligand', 
                                f"/home/aiman/p53_docking/{pep_str}.sdf",
                                '--out_dir',
                                "/home/aiman/DiffDock/results/",
                                '--complex_name',
                                f'{inference_step}_{sample_complex}_{pep_str}',
                                '--inference_steps',
                                str(inference_step),
                                '--samples_per_complex',
                                str(sample_complex)]
                os.chdir("/home/aiman/DiffDock/")
                parameter_out = subprocess.check_output(parameter_args)
                break
            break
            
        #Print rank1 for every parameter pair tested


# run_diff()
print("peptide,inference,sample,conf")
for file in glob.glob(f"/home/aiman/DiffDock/results/*/rank1_confidence*.sdf"):
    # print(file)
    m = re.search('^/home/aiman/DiffDock/results/(\d+)_(\d+)_(\w{3})/rank1_confidence(.+)\.sdf', file)
    if m:
        print(f'{m.group(2)},{m.group(0)},{m.group(1)},{m.group(3)}')