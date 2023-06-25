import math
from tqdm import tqdm
import matplotlib.pyplot as plt
import os
import pandas as pd
import colorsys

def equi(search_range):
    if os.path.exists("equiCheck\coords.csv"):
        with open("equiCheck\coords.csv", "r") as input:
            first_line = input.readline().strip()
            if first_line == "#"+str(search_range):
                return
            
        os.remove("equiCheck\coords.csv")
    

    with open("equiCheck\coords.csv", "a") as file:
        file.write(f"#{search_range}\n")

        results = []

        print("Checking coordinates...")
        for x2 in tqdm((n for n in range(1, search_range, 2))):
            tri = check_coordinates(x2)
            if tri == False:
                continue
            else: results.append(tri)

        for result in results:
            if check_distance(result):
                continue

            else: results.remove(result)
                
        print("Finished!\n")
        
        for i, coords in enumerate(results):
            for j, xy in enumerate(coords):
                for k, comp in enumerate(xy):
                    file.write(f"{comp}")
                    if k < len(xy) - 1:
                        file.write(",")
                if j < len(coords) - 1:
                    file.write(",")
            if i < len(results) - 1:
                file.write("\n")


            

def check_coordinates(x2):
    n = math.sqrt(0.75 * (x2 ** 2))
    if n == n // 1:
        x1, y1 = 0, 0
        y2 = 0                
        x3 = x2/2
        
        return ([x1, x2, x3], [y1, y2, n])
        
    else: return False

def check_distance(t):
    d1 = math.sqrt((t[0][2] - t[0][0]) ** 2 + (t[1][2] - t[1][0]) ** 2)
    d2 = math.sqrt((t[0][1] - t[0][0]) ** 2 + (t[1][1] - t[1][0]) ** 2)
    d3 = math.sqrt((t[0][2] - t[0][1]) ** 2 + (t[1][2] - t[1][1]) ** 2)
    return d1 == d2 == d3

def framing():
    columns = ["x1","x2","x3","y1","y2","y3"]
    df = pd.read_csv("equiCheck\coords.csv", sep=",", header=0, names=columns)
    num_colors = len(df)

    colors_hsv = [(i / num_colors, 1, 1) for i in range(num_colors)]
    colors_rgb = [colorsys.hsv_to_rgb(*color) for color in colors_hsv]
    colors = [f"#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}" for r, g, b in colors_rgb]

    fig, ax = plt.subplots(figsize=(10, 8))

    for i, (_, row) in enumerate(df.iterrows()):
        ax.plot([row['x1'], row['x2'], row['x3'], row['x1']], [row['y1'], row['y2'], row['y3'], row['y1']], color=colors[i])


    ax.set_title('Dreiecke')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_aspect('equal')
    axis_range = 10 ** 9  # Gewünschter Wertebereich
    ax.set_xlim(0, axis_range)
    ax.set_ylim(0, axis_range)

    plt.show()



search_range = 1000000000
equi(search_range)
framing()
