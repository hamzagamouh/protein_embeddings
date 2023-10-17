import numpy as np
import os
from Bio import SeqIO
from bio_embeddings.embed.esm_embedder import ESM1bEmbedder
# import torch

def main(input_path):
    # print(torch.cuda.is_available())
    # print(torch.cuda.get_device_name(0))
    e = ESM1bEmbedder()
    i = 0

    files_list = os.listdir(input_path)
    for filename in files_list:
        i = i + 1
        print(f"Processing {filename} ... {i}/{len(files_list)}")
        fasta = SeqIO.parse(f'{input_path}/' + filename, "fasta")

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

            if not os.path.exists("embedding-files-esm/"): 
                os.makedirs("embedding-files-esm/") 
            np.save('embedding-files-esm/' + seq_record.id + '.npy', vectors)
            


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--input', metavar='path', required=True,
                        help='the path to the fasta files')
    args = parser.parse_args()
    main(args.input)