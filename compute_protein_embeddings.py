import os
import time
import numpy as np
import pandas as pd
from Bio import SeqIO
import pickle
import shutil
import zipfile

import warnings
warnings.filterwarnings("ignore")
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--emb_name", default=None, type=str, help="Embedding name : onehot, bert, xlnet, t5")
parser.add_argument("--input_csv", default=None, type=str, help="Input file path in .csv format which contains at least a column named 'sequence'")
parser.add_argument("--input_fasta", default=None, type=str, help="Input file path in .fasta format")
parser.add_argument("--input_pdb", default=None, type=str, help="The dataset folder if it is in .pdb format")
parser.add_argument("--output_folder", default=None, type=str, help="Output folder")


def process_record(rec):
    chain_id=rec.id[-1]
    return chain_id,str(rec.seq)


# # Embedders
def get_embedder(emb_name):
    # XLNET 
    if emb_name=="xlnet":
        from bio_embeddings.embed.prottrans_xlnet_uniref100_embedder import ProtTransXLNetUniRef100Embedder
        return ProtTransXLNetUniRef100Embedder()
    # BERT 
    if emb_name=="bert":
        from bio_embeddings.embed.prottrans_bert_bfd_embedder import ProtTransBertBFDEmbedder
        return ProtTransBertBFDEmbedder()
    # ALBERT
    if emb_name=="albert":
        from bio_embeddings.embed.prottrans_albert_bfd_embedder import ProtTransAlbertBFDEmbedder
        return ProtTransAlbertBFDEmbedder()
    # ALBERT
    if emb_name=="onehot":
        from bio_embeddings.embed.one_hot_encoding_embedder import OneHotEncodingEmbedder
        return OneHotEncodingEmbedder()
    
    # T5
    if emb_name=="t5":
        from bio_embeddings.embed.prottrans_t5_embedder import ProtTransT5XLU50Embedder
        return ProtTransT5XLU50Embedder(half_model=True)
    

args = parser.parse_args([] if "__file__" not in globals() else None)


output_folder=args.output_folder
emb_name=args.emb_name

# Create embedder
print("Import embedder...")

EMBEDDER=get_embedder(emb_name)



# Process pdb dataset
if args.input_pdb is not None:
    dataset=os.path.basename(args.input_pdb)
    DF={"pdb_id":[],"chain_id":[],"sequence":[],emb_name+"_emb_path":[]}

    print(f"Getting sequences from dataset ...")

    missing=[]
    for n,file in enumerate(os.listdir(args.input_pdb)):
        if n%500==0:
            print(f"{n} files processed")
        prot_file=os.path.join(args.input_pdb,file)
        # Get sequences embeddings with chain IDs
        with open(prot_file) as handle:
            for rec in SeqIO.parse(handle, "pdb-atom"):
                chain_id,seq=process_record(rec)
                DF["pdb_id"]+=[file.replace(".pdb","")]
                DF["chain_id"]+=[chain_id]
                DF["sequence"]+=[seq]

# Process csv dataset
elif args.input_csv is not None:
    if ".csv" in args.input_csv:
        print(f"Getting sequences from dataset ...")
        DF=pd.read_csv(args.input_csv)
        dataset=os.path.basename(args.input_csv.replace(".csv",""))


# Process fasta file
elif args.input_fasta is not None:
    if ".fa" in args.input_fasta:
        DF={"ID":[],"sequence":[],emb_name+"_emb_path":[]}
        print(f"Getting sequences from dataset ...")
        with open(args.input_fasta) as handle:
            for rec in SeqIO.parse(handle, "fasta"):
                id,seq=process_record(rec)
                DF["ID"]+=[id]
                DF["sequence"]+=[seq]
        dataset=os.path.basename(args.input_fasta.replace(".fa",""))
        print(len(DF["sequence"]),'sequences found')





# Compute embeddings and store them in zip file. 
# A .csv file is also created to store to map sequences and IDs to the embedding filenames in the zip file 
print(f"Getting embeddings from {emb_name}")

with zipfile.ZipFile(f"{output_folder}/{dataset}_{emb_name}.zip","w") as thezip:
    for n,seq in enumerate(DF["sequence"]):
        emb=EMBEDDER.embed(seq)
        filename=f"{emb_name}_{n}.npy"
        filepath=os.path.join(output_folder,filename)
        np.save(filepath,emb)
        thezip.write(filepath,filename,compress_type=zipfile.ZIP_BZIP2)
        os.remove(filepath)
        DF[emb_name+"_emb_path"]+=[filename]


pd.DataFrame(DF).to_csv(os.path.join(output_folder,f"{dataset}_{emb_name}.csv"))






