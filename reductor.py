import pickle
import pandas as pd

# Load the pickle file
with open("data/pickles/SAMATE_PHP_SQLi_transform.pkl", "rb") as f:
    data = pickle.load(f)

# Function to extract only the first 5 rows from each DataFrame in the nested structure
def reduce_entries(nested_dict, num_entries=5):
    return {
        outer_key: {
            inner_key: {
                sub_key: sub_value.head(num_entries) if isinstance(sub_value, pd.DataFrame) else sub_value
                for sub_key, sub_value in inner_value.items()
            }
            for inner_key, inner_value in outer_value.items()
        }
        for outer_key, outer_value in nested_dict.items()
    }

# Reduce the data to only 5 rows per DataFrame
reduced_data = reduce_entries(data, num_entries=5)

# Save the reduced version back to a pickle file
with open("data/pickles/SAMATE_PHP_SQLi_transform_small.pkl", "wb") as f:
    pickle.dump(reduced_data, f)

print("✅ Reduced pickle file saved as 'SAMATE_PHP_SQLi_transform_small.pkl'")
