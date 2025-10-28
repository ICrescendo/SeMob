This repository provides the dataset for the EMNLP 2025 paper, "SeMob: Semantic Synthesis for Dynamic Urban Mobility Prediction".
# 🚀 Data Download
The complete `data` directory is hosted on Google Drive due to its size.

1.  **Download the data folder:** [Google Drive Link](https://drive.google.com/file/d/1ICfEvA0ZWHOetJEWwx-12chz6bpPRsxD/view?usp=sharing)
2.  **Unzip it:** Unzip the downloaded file.
3.  **Place it:** Place the resulting `data` folder in the root of this repository.

The final structure should look like this:

```bash
.
├── data/
│   ├── sensors.npz
│   ├── sensor_distances.csv
│   └── text_data/
│
└──  check_npz.py

```
# 📊 Dataset Description
### 1. `data/sensors.npz`

This file contains traffic data for sensors surrounding venues on their respective event days, organized by event and sensor.

**! ! ! IMPORTANT: How to Load ! ! !**
This file contains nested Python dictionaries and **requires `allow_pickle=True`** to be loaded correctly. You can use `check_npz.py` to check the structure of this file.

**Structure:**

* `venue_event_data` (dict): A Python dictionary where each key is an `event_day_id`.
* `event_day_id` (e.g., `'421'`): A unique ID representing a specific venue on a specific date. This ID maps to the `Event_id` in `sensor_distances.csv` and the corresponding multi-agent report in the `text_data/` directory.
    * **Inside each `event_day_id` dict:**
        * `sensor_id` (e.g., `'400372'`): The ID of an affected sensor.
        * `np.array(288,)`: A 1D NumPy array of the ground-truth traffic data. The data has a 5-minute resolution (288 samples per day).

### 2. `data/sensor_distances.csv`

A metadata file provides the distances between sensors and their influencing event venues.

### 3. `data/text_data/`

This directory contains the text outputs from our **SeMob** multi-agent framework. Each filename corresponds to an `event_day_id` from `sensors.npz`.
