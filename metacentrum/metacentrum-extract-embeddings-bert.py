import numpy as np
import os
from Bio import SeqIO
from bio_embeddings.embed.prottrans_bert_bfd_embedder import ProtTransBertBFDEmbedder
# import torch

def main(input_path):
    # print(torch.cuda.is_available())
    # print(torch.cuda.get_device_name(0))
    e = ProtTransBertBFDEmbedder()
    i = 0
    files_list = os.listdir(input_path)
    for filename in files_list:
        i = i + 1
        print(f"Processing {filename} ... {i}/{len(files_list)}")
        fasta = SeqIO.parse(f'{input_path}/' + filename, "fasta")
        for seq_record in fasta:    
            vectors = e.embed(str(seq_record.seq))
            num_arr = np.array(vectors)
            if not os.path.exists("embedding-files-bert/"): 
                os.makedirs("embedding-files-bert/") 
            np.save('embedding-files-bert/' + seq_record.id + '.npy', num_arr)



if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--input', metavar='path', required=True,
                        help='the path to the fasta files')
    args = parser.parse_args()
    main(args.input)