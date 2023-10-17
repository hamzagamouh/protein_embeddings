#!/bin/bash

module add py-pip/21.3.1
export TMPDIR=$SCRATCHDIR

export PATH=/storage/plzen1/home/skrhakv/test_bio-embeddings/cvmfs/software.metacentrum.cz/spack18/software/linux-debian11-x86_64_v2/gcc-10.2.1/python-3.9.12-rg2lpmkxpcq423gx5gmedbyam7eibwtc/bin:$PATH
export PYTHONPATH=/storage/plzen1/home/skrhakv/test_bio-embeddings/cvmfs/software.metacentrum.cz/spack18/software/linux-debian11-x86_64_v2/gcc-10.2.1/python-3.9.12-rg2lpmkxpcq423gx5gmedbyam7eibwtc/lib/python3.9/site-packages:$PYTHONPATH

cp /storage/brno2/home/skrhakv/protein-embeddings/metacentrum-extract-embeddings.py .
python3 metacentrum-extract-embeddings-t5.py # change to -esm or -bert if needed