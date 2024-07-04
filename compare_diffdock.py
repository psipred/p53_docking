from itertools import islice
import subprocess
import glob

#Random peptides to test
pep_strs = ['AAA']

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
                            'inference',
                            '--protein_path',
                            '/home/aiman/DiffDock/1YCR.pdb',
                            '--ligand', 
                            f"{pep_str}.sdf",
                            '--out_dir',
                            '/home/aiman/DiffDock/results/',
                            '--complex_name',
                            pep_str,
                            '--inference_steps',
                            str(inference_step),
                            '--samples_per_complex',
                            str(sample_complex)]
        
            parameter_out = subprocess.check_output(parameter_args)

    #Print rank1 for every parameter pair tested
    for rank in glob.glob(f"/home/aiman/DiffDock/results/{pep_str}/rank1_confidence*.sdf"):
        print (rank)
    
