import os
def rename(directory):
    os.chdir(r'C:\Users\rjvan\fix\screenshots')
    num = 1
    for file in [file for file in sorted(os.listdir(), key=os.path.getctime) if os.path.splitext(file)[1] == ".txt"]:
        if os.path.splitext(file)[1] == ".txt":
            os.rename(file, f"{num}_screenshot.txt")
            num += 1