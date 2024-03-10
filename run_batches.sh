#!/bin/bash

# Load the conda environment
source /home/jdishman/miniconda3/etc/profile.d/conda.sh
conda activate capstone

# Read file paths
readarray -t file_paths < paths/refseq_paths_only.txt

# Calculate the number of chunks and paths per chunk
num_chunks=200  # Also number of nodes as each chunk is sent to a separate node
num_paths=${#file_paths[@]}
paths_per_chunk=$((num_paths / num_chunks))
remainder=$((num_paths % num_chunks))

# Split paths into chunks
start=0
for ((i=0; i<num_chunks; i++)); do
    end=$((start + paths_per_chunk + (i < remainder ? 1 : 0)))
    chunk_paths=("${file_paths[@]:start:end-start}")
    start=$end

    # Create a job script for this chunk
    job_script="scripts/jobs/job_$i.sh"
    echo "#!/bin/bash" > "$job_script"
    echo "python run.py ${chunk_paths[*]}" >> "$job_script"
    chmod +x "$job_script"

    # Submit the job script to the cluster
    sbatch --mem=8g -N 1 -c 1 --partition=gpu --gres=gpu:1 --time=96:00:00 \
           --output="scripts/outputs/job_%j.out" \
           "$job_script"
done