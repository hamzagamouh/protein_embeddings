#!/bin/bash
#SBATCH --partition=debug-long        # partition you want to run job in
#SBATCH --time=7-00:00:00         # walltime for the job in format (days-)hours:minutes:seconds
#SBATCH --mail-user=hamza.gamouh@gmail.com --mail-type=END,FAIL     # send email when job changes state to email address 

srun ch-run biopython python /app/compute_protein_embeddings.py --bind /home/gamouhh/files/MIonSite_embeddings:/app/output

