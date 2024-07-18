## generate_peptides.py

makes sdf files of all combinations of n aminoacids (n=3)

``` bash
python3 generate_peptides.py
```
##compare_diffdock.py

compares rank1_confidence scores for inference_steps and samples_per_complex

``` bash
python3 compare_diffdock.py
```
runs diffdock for all n peptides (n=8000)

``` bash
python3 diffdock_final.py
```

Calculates the minimum distance between the heavy atoms of p53 and the peptide
``` bash
python3 dd_distance.py
```

Generates a 3D scatter plot for confidence_score vs samples_per_complex vs inference_number
``` bash
python3 plot_3d.py
```

Calculates the mean and standard deviation for the distance between the ranks
``` bash
python3 dd_rank.py
```

