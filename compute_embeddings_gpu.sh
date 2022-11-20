#!/bin/bash
#SBATCH --partition=gpu-long        # partition you want to run job in
#SBATCH --gpus=3                    # Number of GPUs that you want to use (max is 3)
#SBATCH --time=7-00:00:00         # walltime for the job in format (days-)hours:minutes:seconds 
#SBATCH --mail-user=your-email   --mail-type=END,FAIL     # send email when job changes state to email address (Optional)

export LD_LIBRARY_PATH=/usr/local/cuda/lib64

srun ch-run biopython python /app/compute_protein_embeddings.py --bind /home/username/folder:/app/output 
