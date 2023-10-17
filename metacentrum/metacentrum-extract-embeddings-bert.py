import numpy as np
import os
from Bio import SeqIO
from bio_embeddings.embed.prottrans_bert_bfd_embedder import ProtTransBertBFDEmbedder
# import torch

def main():
    # print(torch.cuda.is_available())
    # print(torch.cuda.get_device_name(0))
    e = ProtTransBertBFDEmbedder()
    i = 0
    files_list = os.listdir('/storage/brno2/home/skrhakv/protein-embeddings/fasta-files-mmcif-apo')
    for filename in files_list:
        i = i + 1
        name, ext = os.path.splitext(filename)
        print(f"Processing {filename} ... {i}/{len(files_list)}")
        fasta = SeqIO.parse('/storage/brno2/home/skrhakv/protein-embeddings/fasta-files-mmcif-apo/' + filename, "fasta")
        for seq_record in fasta:    
            vectors = e.embed(str(seq_record.seq))
            num_arr = np.array(vectors)
            np.save('embedding-files-mmcif-apo-bert/' + name + '.npy', num_arr)
            break


if __name__ == "__main__":
    main()