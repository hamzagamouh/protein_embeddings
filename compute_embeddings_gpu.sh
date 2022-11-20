#!/bin/bash
#SBATCH --partition=gpu-long        # partition you want to run job in
#SBATCH --gpus=3
#SBATCH --time=7-00:00:00         # walltime for the job in format (days-)hours:minutes:seconds
#SBATCH --mail-user=hamza.gamouh@gmail.com --mail-type=END,FAIL     # send email when job changes state to email address 

export LD_LIBRARY_PATH=/usr/local/cuda/lib64

srun ch-run --bind /home/gamouhh/files:/app/output biopython -- python /app/compute_protein_embeddings.py --emb_name "emb_name" --input_fasta "filename" --output_folder "output_folder"


