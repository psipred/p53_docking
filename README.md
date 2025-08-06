# Generate the data needed

## generate_peptides.py

1. makes sdf files of all combinations of n aminoacids (n=3)

``` bash
python3 generate_peptides.py
```

# Make a small benchmark of 20 and plot the outputs

## compare_diffdock.py

1. compares rank1_confidence scores for pairs of inference_steps and samples_per_complex (Output:test2.csv)
This, was a small benchmarking script to explore these two parameters

``` bash
python3 compare_diffdock.py
```

2. Generates a 3D scatter plot for confidence_score vs samples_per_complex vs inference_steps (Input:dd_test2.csv, output:graph)
``` bash
python3 plot_3d.py
```

3. Plots a graph of samples_per_complex vs confidence score. Can be used for inference_steps by changing the y-axis. (Input: dd_test2.csv, Output: graph)
```bash
python3 plot_surface.py
```

# DiffDock analysis

1. runs diffdock for all n peptides (n=8000)(Output: mdm2_results, dd_fin.csv)
This is the main script that does that stuff
``` bash
python3 diffdock_final.py > dd_fin.csv
```

2. UNUSED Calculates the minimum distance between the heavy atoms of p53 and the peptide. Specify the peptide as the input. (Input: peptide directory, output: dd_distance.csv)
``` bash
python3 dd_distance.py > dd_distance.csv
```

3. Calculates the mean and standard deviation for the distance between the ranks (Input: peptides from fin_results, output:dd_stats2.csv)
``` bash
python3 dd_rank.py > dd_stats2.csv
```

4. calculates the maximum length of the peptides (Input: rank1_confidence of peptides, Output: pep_length.csv)
```bash
python3 pep_length.py > pep_length.csv
```

5. Fuse all the things we've calculated in to one file for analysis
``` bash
python combine_data.py > dd_stats_complete.csv
```

6. Generates a list of all the peptides with a mean distance less than the length of the peptide (good peptides).Can be used to generate the list of bad peptides by changing the angle bracket. (Takes dd_stats_complete.csv as the input file, can output good_pep.csv)

```bash
python3 compare_stats.py > good_pep.csv
python3 compare_stats.py > bad_pep.csv
```

7. Plots a histogram for the mean distance of the 20 ranks of a specific peptide. Specify the peptide name and path to the directory in the input. (Input: peptide directory, output: graph)
```bash
python3 plot_mean.py
```

8. Plots a histogram of the mean distance for all the 'bad peptides'. Change the input csv file to plot for the 'good peptides'. (Input:bad_pep.csv/good_pep.csv, Output:graph)(histogram generated is messy and random)
```bash
python3 plot_all_means.py
``` 

# Results as stored in group project space

Project space directory guide -:

peptides:sdf files of the 8000 peptides

fin_results: results output of the final diffdock run for the 8000 peptides

csvs: *dd_fin- list of confidence scores for 8000 peptides,  
dd_test,dd_test2- inference_steps and samples_per_complex pairs along with confidence score of 3,20 peptides (grid search),  
dd_stats2- Mean distance, standard deviation and confidence scores of 8000 peptides  
pep_length- Maximum length of the 8000 peptides  
bad_pep- list of 'bad' peptides with mean dist and confidence score, good_pep- list of 'good' peptides with mean dist and confidence score*  

pep_graphs: svg files of histograms of the mean distance for GAA, GSN, LMC and GWC + word file for the histograms of all peptides, bad peptides and good peptides  
pep_pymol: pymol files for GAA, GSN, LMC and GWC  
(GAA- mean distance lower than the peptide length (good peptide) and narrow standard deviation.   
GSN- mean distance shorter than the peptide length (good peptide) but broad standard deviation.  
LMC- mean distance longer than the peptide length (bad peptide) and broad standard deviation.  
GWC- mean distance longer than the peptide length (bad peptide) but narrow standard deviation.)  
