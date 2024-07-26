## generate_peptides.py

1. makes sdf files of all combinations of n aminoacids (n=3)

``` bash
python3 generate_peptides.py
```
##compare_diffdock.py

2. compares rank1_confidence scores for inference_steps and samples_per_complex

``` bash
python3 compare_diffdock.py
```
5. runs diffdock for all n peptides (n=8000)

``` bash
python3 diffdock_final.py
```

6. Calculates the minimum distance between the heavy atoms of p53 and the peptide. Specify the peptide as the input. (Input: peptide directory, output: dd_distance.csv)
``` bash
python3 dd_distance.py
```

4. Generates a 3D scatter plot for confidence_score vs samples_per_complex vs inference_number
``` bash
python3 plot_3d.py
```

8. Calculates the mean and standard deviation for the distance between the ranks
``` bash
python3 dd_rank.py
```

7. calculates the maximum length of the peptides
```bash
python3 pep_length.py
```
3. Plots a graph of samples_per_complex vs confidence score. Can be used for inference_steps by changing the y-axis. (Input: dd_test2.csv, Output: graph)
```bash
python3 plot_surface.py
``` 

9. Generates a list of all the peptides with a mean distance less than the length of the peptide (good peptides).Can be used to generate the list of bad peptides by changing the angle bracket. (Takes dd_stats2.csv as the input file, can output good_pep.csv)
```bash
python3 compare_stats.py
```

10. Plots a histogram for the mean distance of the 20 ranks of a specific peptide. Specify the peptide name and path to the directory in the input. (Input: peptide directory, output: graph)
```bash
python3 plot_mean.py
```

11. Plots a histogram of the mean distance for all the 'bad peptides'. Change the input csv file to plot for the 'good peptides'. (Input:bad_pep.csv/good_pep.csv, Output:graph)(histogram generated is messy and random)
```bash
python3 plot_all_means.py
``` 

