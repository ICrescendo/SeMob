import numpy as np
import sys

new_file = 'data/sensors.npz'

print(f"--- Check the npz file: {new_file} ---")

try:
    with np.load(new_file, allow_pickle=True) as data:
        
        file_keys = data.files
        print(f"\nThe top-level arrays in the file ({len(file_keys)} arrays):")
        print(file_keys)

        if '__readme__' in file_keys:
            print("\n" + "="*40)
            print("  File description ('__readme__'):\n")
            print(data['__readme__'].item())
            print("="*40)
        
        venue_data_array = data['venue_event_data']
        print(f"\n--- Check the structure of 'venue_event_data' ---")
        print(f"   Shape: {venue_data_array.shape}")
        print(f"   Dtype: {venue_data_array.dtype}")

        event_dict = venue_data_array.item()

        event_keys = list(event_dict.keys())
        first_event_key = event_keys[0]
        print(f"\n   -'venue_event_data' contains {len(event_keys)} event days.")
        print(f"   -The first event day (example): '{first_event_key}'")

        sensor_data_dict = event_dict[first_event_key]
        sensor_keys = list(sensor_data_dict.keys())
        
        first_sensor_id = None
        for key in sensor_keys:
            if isinstance(sensor_data_dict[key], np.ndarray):
                first_sensor_id = key
                break
        
        print(f"   -The event '{first_event_key}' contains {len(sensor_keys)} keys (sensors + metadata).")
        print(f"   -The first sensor (example): '{first_sensor_id}'")

        sensor_array_1d = sensor_data_dict[first_sensor_id]
        
        print(f"   -Key '{first_sensor_id}' corresponds to the content:")
        print(f"   --> Type: {type(sensor_array_1d)}")
        
        if isinstance(sensor_array_1d, np.ndarray):
            print(f"   --> Shape: {sensor_array_1d.shape}")
            print(f"   --> Dtype: {sensor_array_1d.dtype}")
            
except FileNotFoundError:
    print(f"\n[FATAL ERROR] File not found at path: {new_file}")
except KeyError as e:
    print(f"\n[FATAL ERROR] A key was not found. The file structure might be wrong.")
    print(f"Details: {e}")
except Exception as e:
    print(f"\n[FATAL ERROR] An unexpected error occurred: {e}")