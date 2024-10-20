import pickle
import rlbench
# Specify the path to the pickle file
file_path = '/home/zha414/fire/manipulation/robobase_accelerate/data_raw/open_box/variation0/episodes/episode0/low_dim_obs.pkl'

# Open the pickle file in read mode
with open(file_path, 'rb') as file:
    # Load the contents of the pickle file
    data = pickle.load(file)

# Now you can use the 'data' variable to access the contents of the pickle file
# For example, you can print the contents
print(data)