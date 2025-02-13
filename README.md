# 3D Surface Plotter

## Overview
This Python script reads a CSV file containing 3D data points and generates a surface plot using Matplotlib. It supports a descriptor column (e.g., well numbers or sample IDs) along with X, Y, and Z values.

## Features
- Reads CSV files with a descriptor column (optional, e.g., well numbers)
- Dynamically extracts X, Y, and Z values
- Creates 3D surface plots using Matplotlib
- Supports customizable color maps

## Installation
Ensure you have Python installed along with the necessary dependencies:

```bash
pip install numpy pandas matplotlib
```

## Usage
1. Prepare a CSV file with the following format:

```csv
Descriptor,X,Y,Z
A1,0,0,17520.5
A2,0,1,37289.5
...
H12,7,11,15256.5
```

2. Run the script and provide the CSV file path when prompted:

```bash
python plot_3d_surface.py
```

## Example Output
The script generates a 3D surface plot visualizing the data.

## License
This project is licensed under the MIT License.
