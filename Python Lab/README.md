# Python Lab

This folder contains the 20 Python lab programs arranged unit-wise.

## Folder structure

- Unit 1 — Programs 1.a.py to 1.d.py
- Unit 2 — Programs 2.a.py to 2.d.py
- Unit 3 — Programs 3.a.py to 3.d.py
- Unit 4 — Programs 4.a.py to 4.d.py
- Unit 5 — Programs 5.a.py to 5.d.py

## Run in Visual Studio Code

1. Extract this folder from the ZIP file.
2. Open **Python Lab** in VS Code (`File > Open Folder`).
3. Open the required `.py` file.
4. Select **Run Python File** or open the VS Code terminal and run:
   `python "Unit 1/1.a.py"`

For another program, replace the path with its unit and filename.

## Install required libraries

Most programs use Python's standard library. Programs 5.c and 5.d require NumPy; Program 5.d also requires Matplotlib.

Run this in the VS Code terminal:

```bash
python -m pip install -r requirements.txt
```

Some programs create sample `.txt`, `.csv`, `.json`, `.log`, or `.png` files when they run. These are generated as part of the exercises.
