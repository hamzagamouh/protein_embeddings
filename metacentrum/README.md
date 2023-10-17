# Computing embeddings on the metacentrum
## Obtaining the Metacentrum account
To obtain the metacentrum account, visit [this page](https://metavo.metacentrum.cz/osobniv3/wayf/proxy.jsp?locale=en&target=https%3A%2F%2Fsignup.e-infra.cz%2Ffed%2Fregistrar%2F%3Fvo%3Dmeta%26locale%3Den).

## Computing Embeddings
### Login to the Metacentrum
Once your account is ready, login to the Metacentrum through ssh:
```
ssh skrhakv@skirit.ics.muni.cz
```
(use your username instead of `skrhakv`).

### Install the dependencies
To install the dependencies, request a job, you can use a similar command:
```
qsub -I -l select=1:ncpus=16:scratch_local=30gb:mem=64gb:ngpus=1 -l walltime=24:00:00
```
Then, proceed with the instructions from the `metacentrum-bio-embedding-installation.sh` file:
```
module add py-pip/21.3.1
export TMPDIR=$SCRATCHDIR
```
Install:
```
pip3 install bio-embeddings[all] --root /storage/plzen1/home/skrhakv/test_bio-embeddings
pip3 install tensorboard --root /storage/plzen1/home/skrhakv/test_bio-embeddings
pip3 install numpy==1.21.4 --root /storage/plzen1/home/skrhakv/test_bio-embeddings
```
(Use your path instead of `/storage/plzen1/home/skrhakv/test_bio-embeddings`!)

Add the dependencies to the path:
```
export PATH=/storage/plzen1/home/skrhakv/test_bio-embeddings/cvmfs/software.metacentrum.cz/spack18/software/linux-debian11-x86_64_v2/gcc-10.2.1/python-3.9.12-rg2lpmkxpcq423gx5gmedbyam7eibwtc/bin:$PATH
export PYTHONPATH=/storage/plzen1/home/skrhakv/test_bio-embeddings/cvmfs/software.metacentrum.cz/spack18/software/linux-debian11-x86_64_v2/gcc-10.2.1/python-3.9.12-rg2lpmkxpcq423gx5gmedbyam7eibwtc/lib/python3.9/site-packages:$PYTHONPATH
```
(Again, use the path where the dependencies got installed! Not the `/storage/plzen1/home/skrhakv/test_bio-embeddings/...` path)

### Run the embeddings
Now, everything should be ready to run the embeddings computation. Firstly, copy the respective script to your workspace. Secondly, run the script - for example:
```
python3 metacentrum-extract-embeddings-t5.py
```


### File overview
1. `metacentrum-bio-embedding-installation.sh`: Installation steps - use your own paths!
2. `metacentrum-embeddings-computation-steps.sh`: Steps for embedding computation - use your own paths!
3. `metacentrum-extract-embeddings-bert.py`: Python script for BERT embeddings
4. `metacentrum-extract-embeddings-esm.py`: Python script for ESM embeddings
5. `metacentrum-extract-embeddings-t5.py`: Python script for T5 embeddings