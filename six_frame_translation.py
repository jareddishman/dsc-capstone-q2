import skbio
import os

# replace with own filepath
# fasta_file = r"C:\Users\erik1\Downloads\GCF_003627195.1_ASM362719v1_protein.faa.gz"
fasta_file = '/home/mcdonadt/GCF_000007625.1_ASM762v1_genomic.fna.gz'

if not os.path.exists(fasta_file):
    raise ValueError()

fasta_data = skbio.DNA.read(fasta_file, format="fasta")

print(fasta_data[0])



# six_frame_translation = skbio.sequence.DNA.translate_six_frames(fasta_data)

# for seq in fasta_data:
#     six_frame_translation = skbio.sequence.DNA.translate_six_frames(seq)
#     # Now you have the six-frame translation for each sequence in fasta_data
#     print("Sequence ID:", seq.metadata['id'])
#     print("Six-frame translation:", six_frame_translation)