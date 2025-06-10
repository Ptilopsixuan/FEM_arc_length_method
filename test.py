from mylib import type, reader, writer
import numpy as np
import os
import matplotlib.pyplot as plt

model_names = ["0.1", "0.3", "0.5"]

for model_name in model_names:
    input_path = os.path.join(os.getcwd(), "input", f"{model_name}.txt")
    model = reader.readFile(input_path)
    # output = model.iterate()
    output, la, F, u = model.arc_length_method(steps=25000, s=0.0005, max_p_detect=False)

    output_path = os.path.join(os.getcwd(), "output", f"{model_name}", f"{model_name}.txt")
    if not os.path.exists(os.path.dirname(output_path)):
        os.makedirs(os.path.dirname(output_path))

    for i, o in enumerate(output):
        if i % 200 == 0:
            writer.writeFile(output_path.replace(".txt", f"_{i:05d}.txt"), o)
            print(i, o)

    plt.plot([-item[151][0] for item in u], la)
    plt.savefig(os.path.join(os.getcwd(), model_name + ".png"))

    curve_path = os.path.join(os.getcwd(), model_name)
    with open(curve_path, "w") as f:
        for i in range(len(u)):
            f.write(f"{-u[i][151][0]: 05f}, {la[i]*-25000000: 05f}\n")
