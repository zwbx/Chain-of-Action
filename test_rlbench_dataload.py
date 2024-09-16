from rlbench.utils import get_stored_demos
from rlbench.observation_config import ObservationConfig, CameraConfig

import os
import pickle
import argparse

def cam_config():
    return CameraConfig()


def get_demo(dataset_root, task_name, variation_number):
    obs_config = ObservationConfig(
        left_shoulder_camera=cam_config(),
        right_shoulder_camera=cam_config(),
        overhead_camera=cam_config(),
        wrist_camera=cam_config(),
        front_camera=cam_config(),
        gripper_matrix=True,
        gripper_joint_positions=True,
        gripper_touch_forces=True,
        wrist_camera_matrix=True,
        task_low_dim_state=True,
    )
    return get_stored_demos(
        -1,
        False,
        dataset_root=dataset_root,
        variation_number=variation_number,
        task_name=task_name,
        obs_config=obs_config,
    )

def save_as_pickles(root, target_root, task_name):
    dataset_types = ["train", "eval"]

    for dt in dataset_types:
        cur_root, save_root = os.path.join(root, dt), os.path.join(target_root, dt)
        task_data_root = os.path.join(cur_root, task_name)
        variations = os.listdir(task_data_root)
        variations = [
            int(f.strip("variation")) for f in variations
        ]

        for v in variations:
            demos = get_demo(cur_root, task_name, v)
            variation_id = demos[0][0].misc["variation_index"]
            os.makedirs(os.path.join(save_root, task_name, f"variation_{variation_id}"), exist_ok=True)
            for i, demo in enumerate(demos):
                _path = os.path.join(
                    save_root, task_name, f"variation_{variation_id}", f"episode_{i}.pkl"
                )
                with open(_path, "wb") as fout:
                    pickle.dump(demo, fout, pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=str, help="dataset root")
    parser.add_argument("--target", type=str, help="target dataset root")
    parser.add_argument("--task_name", type=str, help="task name")
    args = parser.parse_args()

    save_as_pickles(args.root, args.target, args.task_name)
