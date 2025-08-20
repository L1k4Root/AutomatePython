from pathlib import Path

basepath = Path("./03-WorkingWithFiles/files")
p1 = Path(basepath + "/content.txt")

with open(p1, "r") as file:
    p2 = file.read()
    
p2 = Path(p2)
print(p2)