# Computation of protein language model embeddings

This is a repository for computing protein language model embeddings using the bio-embeddings python library.


### Environment (KSI cluster)
The following environment setup instructions are for users that have an account in the following computational clusters of KSI MFF UK : <b>parlab</b> and <b>gpulab</b>. More information about the clusters can be found in https://gitlab.mff.cuni.cz/mff/hpc/clusters

1. Clone the repository ```git clone https://github.com/hamzagamouh/protein_embeddings.git``` 
2. Run ```cd protein_embeddings``` to go to the repo directory (where a dockerFile is stored)
3. Run ```salloc -C docker``` to switch to a node where docker is installed.
4. Run ```ch-image build -t biopython ./biopython``` to create a docker image (for example here the name of the image will be "biopython").
5. Run ```ch-convert biopython .``` to convert the docker image to a directory structure.
6. Import CUDA libaries by running ```srun -p gpu-short --gpus=1 ch-fromhost --nvidia .```
7. Create the output directory ```mkdir biopython/app/output```. This is the directory will be mounted to a local folder (of your choice), the python script expects inputs and outputs in ```/app/output``` inside the app.

If you want to run the docker image in interactive mode :

1. Run ```salloc -p debug-short``` for CPU mode, or ```salloc -p gpu-short``` for GPU mode.
2. Change directory to where your image folder is stored. (if you run ```ls``` you should see ```biopython``` folder !)
3. Then run your image by running ```ch-run --bind /src:/app/output biopython bash``` where `src` is the source folder.
4. For GPU mode, you need also to import the CUDA libraries by running ```export LD_LIBRARY_PATH=/usr/local/cuda/lib64```
5. You are now inside the image and you can make changes, test the code...


### Computing embeddings 
The current code supports the following embeddings from [bio-embeddings library](https://docs.bioembeddings.com/v0.2.3/api/bio_embeddings.embed.html) :

- ```OneHotEncodingEmbedder``` 
- ```ProtTransBertBFDEmbedder```
- ```ProtTransXLNetUniRef100Embedder```
- ```ProtTransT5XLU50Embedder```

There are two options to compute embeddings :

* Running the batch script ```compute_protein_embeddings_cpu.sh```. This script runs the computation on a CPU. It may be time consuming but it is most suitable for embeddings whose memory doesn't fit in the GPU RAM. This is the case for the <b>t5 embedding.</b>

* Running the batch script ```compute_protein_embeddings_gpu.sh```. This script runs the computation on GPUs. This is suitable for other embeddings like <b>bert and xlnet embeddings.</b>

You can provide one of the following inputs to the scripts :

- the path to a <b>.csv</b> file that has at least a column named "sequence" .
- the path to a folder that contains multiple <b>.pdb</b> files
- the path to a <b>.fa</b> FASTA file.

From now on, the root folder of the python script will be considered to be the one that you specify in the --bind argument inside the ```.sh``` script. This is where all of your datasets and outputs are expected to be.

### Running the bash scripts (example of a GPU script)

```sbatch --job-name job_name --output job_name.txt --emb_name bert --input_dataset datasets/dataset.csv --output_folder embeddings compute_embeddings_gpu.sh```

Where : 

- ```job_name``` : the name of your job
- ```output``` : the saved logs
- ```emb_name``` : the embedding name "onehot", "bert", "xlnet" or "t5"
- ```input_dataset``` : the input dataset
- ```output_folder``` : the output folder

### Expected output
The output will be a ```.zip``` file that contains the embeddings for each sequence in ```.npy``` format, as well as a ```.csv``` file that contains the mappings of the sequence IDs and sequences to the filenames of the embeddings in the ```.zip``` file.

