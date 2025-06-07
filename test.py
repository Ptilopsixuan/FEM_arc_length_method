from mylib import type, reader, writer
import numpy as np
import os
import matplotlib.pyplot as plt

model_name = "arch"
input_path = os.path.join(os.getcwd(), "input", f"{model_name}.txt")
model = reader.readFile(input_path)
# output = model.iterate()
output, la, F, u = model.arc_length_method(steps=10000, s=0.0005, max_p_detect=False)


output_path = os.path.join(os.getcwd(), "output", f"{model_name}.txt")
if not os.path.exists(os.path.dirname(output_path)):
    os.makedirs(os.path.dirname(output_path))

# for i, o in enumerate(output):
#     if i % 200 == 0:
#         writer.writeFile(output_path.replace(".txt", f"_{i:05d}.txt"), o)
#         print(i, o)


plt.plot([-item[16][0] for item in u], la)
plt.show()


curve_path = os.path.join(os.getcwd(), "la-u_curve.txt")
with open(curve_path, "w") as f:
    for i in range(len(u)):
        f.write(f"{u[i][16][0]: 05f}, {la[i]*-25000000: 05f}\n")
