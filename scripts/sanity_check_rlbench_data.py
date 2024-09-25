from pathlib import Path
from rlbench.backend.const import *
import pickle
import tqdm
import multiprocessing as mp


def check_ep(ep):
    low_dim_obs = ep / LOW_DIM_PICKLE
    if not low_dim_obs.exists():
        return False

    with (ep / LOW_DIM_PICKLE).open("rb") as fin:
        obs = pickle.load(fin)

    dirs = [
        LEFT_SHOULDER_RGB_FOLDER,
        LEFT_SHOULDER_DEPTH_FOLDER,
        LEFT_SHOULDER_MASK_FOLDER,
        RIGHT_SHOULDER_RGB_FOLDER,
        RIGHT_SHOULDER_DEPTH_FOLDER,
        RIGHT_SHOULDER_MASK_FOLDER,
        OVERHEAD_RGB_FOLDER,
        OVERHEAD_DEPTH_FOLDER,
        OVERHEAD_MASK_FOLDER,
        WRIST_RGB_FOLDER,
        WRIST_DEPTH_FOLDER,
        WRIST_MASK_FOLDER,
        FRONT_RGB_FOLDER,
        FRONT_DEPTH_FOLDER,
        FRONT_MASK_FOLDER,
    ]
    dirs = [ep / d for d in dirs]
    len_dirs = [len(list(d.iterdir())) for d in dirs]
    clean = [len(obs) == l for l in len_dirs]
    return all(clean), len(obs)

def check_task(root, tag, task_name, ret):
    root = Path(root) / tag / task_name
    wrong_eps = []
    ep_lengths = []
    for variation in root.iterdir():
        if variation.is_dir():
            desc = variation / "variation_descriptions.pkl"
            if not desc.exists():
                for ep in (variation / "episodes").iterdir():
                    wrong_eps.append(ep)
                continue
            
            ep_dir = variation / "episodes"
            for ep in ep_dir.iterdir():
                if ep.is_dir():
                    correct_ep, ep_len = check_ep(ep)
                    if not correct_ep:
                        print(ep)
                        wrong_eps.append(ep)
                    else:
                        ep_lengths.append(ep_len)
    
    ret.append(
        {task_name: (wrong_eps, max(ep_lengths))}
    )

rlbench_tasks = [
    "basketball_in_hoop",
    "beat_the_buzz",
    "block_pyramid",
    "change_channel",
    "change_clock",
    "close_box",
    "close_door",
    "close_drawer",
    "close_fridge",
    "close_grill",
    "close_jar",
    "close_laptop_lid",
    "close_microwave",
    "empty_container",
    "empty_dishwasher",
    "get_ice_from_fridge",
    "hang_frame_on_hanger",
    "hit_ball_with_queue",
    "hockey",
    "insert_onto_square_peg",
    "insert_usb_in_computer",
    "lamp_off",
    "lamp_on",
    "lift_numbered_block",
    "light_bulb_in",
    "light_bulb_out",
    "meat_off_grill",
    "meat_on_grill",
    "move_hanger",
    "open_box",
    "open_door",
    "open_drawer",
    "open_fridge",
    "open_grill",
    "open_jar",
    "open_microwave",
    "open_oven",
    "open_washing_machine",
    "open_window",
    "open_wine_bottle",
    "phone_on_base",
    "pick_and_lift",
    "pick_and_lift_small",
    "pick_up_cup",
    "place_cups",
    "place_hanger_on_rack",
    "place_shape_in_shape_sorter",
    "play_jenga",
    "plug_charger_in_power_supply",
    "pour_from_cup_to_cup",
    "press_switch",
    "push_button",
    "push_buttons",
    "put_all_groceries_in_cupboard",
    "put_books_on_bookshelf",
    "put_bottle_in_fridge",
    "put_groceries_in_cupboard",
    "put_item_in_drawer",
    "put_knife_in_knife_block", "put_knife_on_chopping_board",
    "put_money_in_safe",
    "put_plate_in_colored_dish_rack",
    "put_rubbish_in_bin",
    "put_shoes_in_box",
    "put_toilet_roll_on_stand",
    "put_tray_in_oven",
    "put_umbrella_in_umbrella_stand",
    "reach_and_drag",
    "reach_target",
    "remove_cups",
    "scoop_with_spatula",
    "screw_nail",
    "set_the_table",
    "setup_checkers",
    "setup_chess",
    "slide_block_to_target",
    "slide_cabinet_open_and_place_cups",
    "slide_cabinet_open",
    "solve_puzzle",
    "stack_blocks",
    "stack_chairs",
    "stack_cups",
    "stack_wine",
    "straighten_rope",
    "sweep_to_dustpan",
    "take_cup_out_from_cabinet",
    "take_frame_off_hanger",
    "take_item_out_of_drawer",
    "take_lid_off_saucepan",
    "take_money_out_safe",
    "take_off_weighing_scales",
    "take_plate_off_colored_dish_rack",
    "take_shoes_out_of_box",
    "take_toilet_roll_off_stand",
    "take_tray_out_of_oven",
    "take_umbrella_out_of_umbrella_stand",
    "take_usb_out_of_computer",
    "toilet_seat_down",
    "toilet_seat_up",
    "turn_oven_on",
    "turn_tap",
    "tv_on",
    "unplug_charger",
    "water_plants",
    "weighing_scales",
    "wipe_desk",
]

wrong_eps = []
procs = []
manager = mp.Manager()
wrong_eps = manager.list()

for task in tqdm.tqdm(rlbench_tasks):
    for mode in ["train", "eval"]:
        procs.append(
            mp.Process(target=check_task, args=("/mnt/bn/robotics-data-mx/rlbench_datasets/all_variations/", mode, task, wrong_eps))
        )

[p.start() for p in procs]
[p.join() for p in procs]

output = []
for eps in list(wrong_eps):
    output += eps

# output_file = Path('paths.txt')

# # Open the file and write the paths
# with output_file.open(mode='w') as file:
#     for path in output:
#         file.write(f"{path}\n")

print("test")