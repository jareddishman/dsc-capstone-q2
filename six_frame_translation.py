import skbio
import os

# replace with own filepath
# fasta_file = r"C:\Users\erik1\Downloads\GCF_003627195.1_ASM362719v1_protein.faa.gz"
fasta_file = '/home/mcdonadt/GCF_000007625.1_ASM762v1_genomic.fna.gz'

if not os.path.exists(fasta_file):
    raise ValueError()

fasta_data = skbio.DNA.read(fasta_file, format="fasta")

translation = fasta_data.translate_six_frames()

frames = [1,2,3,-1,-2,-3]
translation_by_frame = {}
for idx, reading_frame in enumerate(translation):
    translation_by_frame[frames[idx]] = str(reading_frame).split('*') # there is almost certainly a method in the protein class for this

# printing out the last protein sequence from the first reading frame
print(translation_by_frame[1][-1]) 

# printing out the first protein sequence from the first reverse reading frame
print(translation_by_frame[-1][0]) 