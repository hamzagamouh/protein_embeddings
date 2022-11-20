# Computation of protein language model embeddings

This is a repository for computing protein language model embeddings using the bio-embeddings python library.


### Environment (KSI cluster)
The following environment setup instructions are for users that have an account in the following computational clusters of KSI MFF UK : <b>parlab</b> and <b>gpulab</b>. More information about the clusters can be found in https://gitlab.mff.cuni.cz/mff/hpc/clusters

1. Clone the repository ```git clone https://github.com/hamzagamouh/protein_embeddings.git``` 
2. Run ```cd protein_embeddings``` to go to the repo directory (where a dockerFile is stored)
3. Run ```salloc -C docker``` to switch to a node where docker is installed.
4. Run ```ch-image build -t biopython .``` to create a docker image (for example here the name of the image will be "biopython").
5. Run ```ch-convert -i docker biopython .``` to convert the docker image to a directory structure.
6. Import CUDA libaries by running ```srun -p gpu-short --gpus=1 ch-fromhost --nvidia .```

If you want to run the docker image in interactive mode :
a. Run ```salloc -p debug-short``` for CPU mode, or ```salloc -p gpu-short``` for GPU mode.
b. Change directory to where your image folder is stored. (if you run ```ls``` you should see ```biopython``` folder !)
c. Then run your image by running ```ch-run biopython bash``` 
d. You are now inside the image and you can make changes, test the code...


### Computing embeddings 
For embedding computation 



