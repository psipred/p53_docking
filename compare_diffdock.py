from itertools import islice
import subprocess

inference_steps = list(islice(range(100), 10, 100, 5))
for inference_step in inference_steps:
    print (inference_step)