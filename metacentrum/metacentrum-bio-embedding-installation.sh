#!/bin/bash

module add py-pip/21.3.1
export TMPDIR=$SCRATCHDIR

pip3 install bio-embeddings[all] --root /storage/plzen1/home/skrhakv/test_bio-embeddings
pip3 install tensorboard --root /storage/plzen1/home/skrhakv/test_bio-embeddings
pip3 install numpy==1.21.4 --root /storage/plzen1/home/skrhakv/test_bio-embeddings

export PATH=/storage/plzen1/home/skrhakv/test_bio-embeddings/cvmfs/software.metacentrum.cz/spack18/software/linux-debian11-x86_64_v2/gcc-10.2.1/python-3.9.12-rg2lpmkxpcq423gx5gmedbyam7eibwtc/bin:$PATH
export PYTHONPATH=/storage/plzen1/home/skrhakv/test_bio-embeddings/cvmfs/software.metacentrum.cz/spack18/software/linux-debian11-x86_64_v2/gcc-10.2.1/python-3.9.12-rg2lpmkxpcq423gx5gmedbyam7eibwtc/lib/python3.9/site-packages:$PYTHONPATH