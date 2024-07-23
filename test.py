import glob

for file in (glob.glob(f"HML/rank*_confidence*.sdf")):
    with open(file, "r") as fhIn:
        content = fhIn.read()
        lines = content.split("\n")
        analysis_line = lines[4].lstrip()
        entries = analysis_line.split()
        if len(entries) < 16:
            continue
        
    
            
            
                