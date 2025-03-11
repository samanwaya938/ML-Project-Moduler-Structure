import os
from pathlib import Path

project_name = "MLModuler"
list_of_files = [

f"src/{project_name}/__init__.py",
f"src/{project_name}/components/__init__.py",
f"src/{project_name}/utils/__init__.py",
f"src/{project_name}/logger/__init__.py",
f"src/{project_name}/exception/__init__.py",
f"src/{project_name}/entity/__init__.py",
f"src/{project_name}/config/__init__.py",
f"src/{project_name}/pipeline/__init__.py",
f"src/{project_name}/config/__init__.py",
f"experiment/testing.ipynb",
f"main.py",
f"app.py"
f"requirements.txt",
f"setup.py",



]

for filepath in list_of_files:
  filepath = Path(filepath)
  filedir, filename = os.path.split(filepath)

  if filedir != "":
    os.makedirs(filedir, exist_ok=True)
    print(f"Creating directory; {filedir} for the file {filename}")

  if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
    with open(filepath, "w") as f:
      pass
      print(f"Creating empty file: {filepath}")
      