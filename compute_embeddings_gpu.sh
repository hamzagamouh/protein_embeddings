#!/bin/bash
#SBATCH --partition=gpu-long        # partition you want to run job in
#SBATCH --gpus=1
#SBATCH --time=7-00:00:00         # walltime for the job in format (days-)hours:minutes:seconds
#SBATCH --mail-user=youremail --mail-type=END,FAIL     # send email when job changes state to email address 


export LD_LIBRARY_PATH=/usr/local/lib

while [ $# -gt 0 ]; do
    if [[ $1 == "--"* ]]; then
        v="${1/--/}"
        declare "$v"="$2"
        shift
    fi
    shift
done


srun ch-run --bind /home:/home ~/prot_embs -- python /app/compute_protein_embeddings.py --emb_name $emb_name --input_dataset $input_dataset --output_folder $output_folder

