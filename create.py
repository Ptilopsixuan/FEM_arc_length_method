import os

def y(x, h):
    y = h/25*x*(10-x)
    return y

def create(path, p_num, h):
    p_num = int(p_num)
    u_num = p_num - 1
    load_index = int((p_num+1)/2)
    l = 10
    f_points = f"{p_num} #Points\n"
    for i in range(0, p_num):
        f_points += f"{i+1} {i*l/(p_num-1)} {y(i*l/(p_num-1), h)}\n"
    f_material = "1 #Material\n1 200000000000.0 0.3\n"
    f_plane = "1 #Plane\n1 1 0.2 0.3\n"
    f_unit = f"{u_num} #Unit\n"
    for i in range(0, u_num):
        f_unit += f"{i+1} {i+1} {i+2} 1 1\n"
    f_load = f"1 #Load\n{load_index} 0 -25000000 0\n"
    f_constraint = f"6 #Constraint\n1 1 0\n1 2 0\n1 3 0\n{p_num} 1 0\n{p_num} 2 0\n{p_num} 3 0\n"
    f_hitch = "0 #Hitch\n"
    with open(path, "w") as f:
        f.write(f_points)
        f.write(f_material)
        f.write(f_plane)
        f.write(f_unit)
        f.write(f_load)
        f.write(f_constraint)
        f.write(f_hitch)

if __name__ == "__main__":
    for name in ["0.1", "0.3", "0.5"]:
    # name = "0.3_200"
        path = os.path.join(os.getcwd(), "input", f"{name}.txt")
        create(path, 101, float(name)*10)
