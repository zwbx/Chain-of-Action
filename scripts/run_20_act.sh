#!/bin/bash
#SBATCH --job-name=robobase20_${SLURM_ARRAY_TASK_ID} 
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
export CUDA_VISIBLE_DEVICES=0
# python3 train.py method=diffusion pixels=true env=rlbench/take_lid_off_saucepan demos=50 eval_every_steps=3000 num_pretrain_steps=3000  replay.nstep=1
# python3 train.py method=diffusion pixels=true env=rlbench/stack_wine demos=50 eval_every_steps=3000 num_pretrain_steps=3000  replay.nstep=1
# python3 train.py method=diffusion pixels=true env=rlbench/sweep_to_dustpan demos=50 eval_every_steps=3000 num_pretrain_steps=3000  replay.nstep=1
# python3 train.py method=diffusion pixels=true env=rlbench/turn_tap demos=50 eval_every_steps=3000 num_pretrain_steps=3000  replay.nstep=1
# python3 train.py method=diffusion pixels=true env=rlbench/push_button demos=50 eval_every_steps=3000 num_pretrain_steps=3000  replay.nstep=1
# python3 train.py method=diffusion pixels=true env=rlbench/open_box demos=50 eval_every_steps=3000 num_pretrain_steps=3000  replay.nstep=1
# python3 train.py method=diffusion pixels=true env=rlbench/open_drawer demos=50 eval_every_steps=3000 num_pretrain_steps=3000  replay.nstep=1
# python3 train.py method=diffusion pixels=true env=rlbench/pick_up_cup demos=50 eval_every_steps=3000 num_pretrain_steps=3000  replay.nstep=1
# python3 train.py method=diffusion pixels=true env=rlbench/press_switch demos=50 eval_every_steps=3000 num_pretrain_steps=3000  replay.nstep=1
# python3 train.py method=diffusion pixels=true env=rlbench/reach_target demos=50 eval_every_steps=3000 num_pretrain_steps=3000  replay.nstep=1

python3 train.py  launch=act_pixel_rlbench  env=rlbench/take_lid_off_saucepan demos=50 eval_every_steps=30000 num_pretrain_steps=30000 # 
# python3 train.py  launch=act_pixel_rlbench  env=rlbench/stack_wine  demos=50 eval_every_steps=3000 num_pretrain_steps=3000 
# python3 train.py  launch=act_pixel_rlbench  env=rlbench/sweep_to_dustpan  demos=50 eval_every_steps=3000 num_pretrain_steps=3000 
# python3 train.py  launch=act_pixel_rlbench  env=rlbench/turn_tap  demos=50 eval_every_steps=3000 num_pretrain_steps=3000 
# python3 train.py  launch=act_pixel_rlbench  env=rlbench/push_button  demos=50 eval_every_steps=3000 num_pretrain_steps=3000 
python3 train.py  launch=act_pixel_rlbench  env=rlbench/open_box  demos=50 eval_every_steps=3000 num_pretrain_steps=3000 
# python3 train.py  launch=act_pixel_rlbench  env=rlbench/open_drawer  demos=50 eval_every_steps=3000 num_pretrain_steps=3000 
# python3 train.py  launch=act_pixel_rlbench  env=rlbench/pick_up_cup  demos=50 eval_every_steps=3000 num_pretrain_steps=3000 
# python3 train.py  launch=act_pixel_rlbench  env=rlbench/press_switch  demos=50 eval_every_steps=3000 num_pretrain_steps=3000 
python3 train.py  launch=act_pixel_rlbench  env=rlbench/reach_target  demos=50 eval_every_steps=3000 num_pretrain_steps=3000 
# Collecting additional 181 random samples even though there are 1819 demo samples inside the buffer. Please make sure that this is an intended behavior