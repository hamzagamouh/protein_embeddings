import numpy as np
import os
from Bio import SeqIO
from bio_embeddings.embed.esm_embedder import ESM1bEmbedder
# import torch

def main():
    # print(torch.cuda.is_available())
    # print(torch.cuda.get_device_name(0))
    e = ESM1bEmbedder()
    i = 0
    files_list = os.listdir('/storage/brno2/home/skrhakv/protein-embeddings/fasta-files-mmcif-apo')
    for filename in files_list:
        i = i + 1
        name, ext = os.path.splitext(filename)
        print(f"Processing {filename} ... {i}/{len(files_list)}")
        fasta = SeqIO.parse('/storage/brno2/home/skrhakv/protein-embeddings/fasta-files-mmcif-apo/' + filename, "fasta")

        for seq_record in fasta:   
            s = str(seq_record.seq) 
            treshold = 1022
            vectors = []
            while len(s) > 0:
                s1 = s[:treshold]
                s = s[treshold:]
                vectors1 = np.array(e.embed(s1))
                if len(vectors) > 0:
                    vectors = np.concatenate((vectors, vectors1))
                else:
                    vectors = vectors1
            np.save('embedding-files-mmcif-apo-esm/' + name + '.npy', vectors)
            break


if __name__ == "__main__":
    main()