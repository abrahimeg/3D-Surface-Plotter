import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.ticker as ticker

def plot_3d_surface(csv_file):
    # Load data
    df = pd.read_csv(csv_file)
    
    # Allow for a descriptor column but ensure proper column mapping
    df.columns = ['Descriptor', 'X', 'Y', 'Z']
    
    # Extract X, Y, Z
    x_values = df['X'].unique()  # Second column as X
    y_values = df['Y'].unique()  # Third column as Y
    
    # Pivot table to get Z values in matrix form
    Z = df.pivot(index='Y', columns='X', values='Z').values
    X, Y = np.meshgrid(x_values, y_values)
    
    # Plotting the 3D surface plot
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    surface = ax.plot_surface(X, Y, Z, cmap='viridis')
    
    # Labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Surface Plot')
    
    # Adding color bar
    cbar = fig.colorbar(surface, ax=ax, shrink=0.5, aspect=5)
    cbar.set_label('Z')
    
    plt.show()

if __name__ == "__main__":
    csv_file = input("Enter the path to the CSV file: ")
    plot_3d_surface(csv_file)
