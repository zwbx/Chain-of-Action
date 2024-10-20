#!/bin/bash
#SBATCH --job-name=data_generator_${SLURM_ARRAY_TASK_ID} 
##SBATCH -p gpuext
#SBATCH -A OD-221915
#SBATCH --time=0-24:00:00 # time allocation, which has the format (D-HH:MM), here set to 1 hour
#SBATCH -N 1               	                                # number of nodes (use a single node)
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=32
#SBATCH --gres=gpu:1 # generic resource required (here requires 1 GPU)
#SBATCH --mem=192GB # specify memory required per node (here set to 8 GB)
#SBATCH --mail-type=ALL
#SBATCH --mail-user=wenbo.zhang01@adelaide.edu.au
#SBATCH --output=robobase20_%A_%a.out

source activate robobase_acc

Xvfb :98 -screen 0 1024x768x16 &
export DISPLAY=:98
export COPPELIASIM_ROOT=/home/zha414/.local/bin/CoppeliaSim
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$COPPELIASIM_ROOT 
export QT_QPA_PLATFORM_PLUGIN_PATH=$COPPELIASIM_ROOT
# module load cudnn
# module load cuda
export CUDA_VISIBLE_DEVICES=0
rlbench-generate-dataset --save_path=/home/zha414/fire/manipulation/robobase_accelerate/data_raw --tasks 'reach_target' 'open_box' 'take_lid_off_saucepan' --episodes_per_task=50 --variations=1 --processes=4