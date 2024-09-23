#!/bin/bash

set -e

LAUNCH=${LAUNCH:-"act_pixel_rlbench"}
DS_ROOT=${DS_ROOT:-"/mnt/bn/robotics-data-mx/rlbench_datasets/all_variations/train"}

envs=( take_lid_off_saucepan open_drawer )

for env in ${envs[*]}
do
    echo rlbench/$env
    cp merlin/template.yaml merlin/submit.yaml
    sed -i "s#%DS_ROOT#${DS_ROOT}#g" "merlin/submit.yaml"
    sed -i "s#%LAUNCH#${LAUNCH}#g" "merlin/submit.yaml"
    sed -i "s#%ENV#rlbench\/${env}#g" "merlin/submit.yaml"
    mlx job submit --yaml=merlin/submit.yaml
    rm merlin/submit.yaml
done