# Sortify — Bubble Sort Visualizer

An animated Bubble Sort visualizer with a Tkinter desktop interface, random and custom arrays, adjustable speed, start and reset controls.

**Original source:** [`sorting_algoridhm_visualiser.py`](sorting_algoridhm_visualiser.py) (preserved exactly from the uploaded file).

## Technologies

- Python 3.10+
- Tkinter (included in standard Windows Python installs)

## Features verified from the source

- Animated Bubble Sort using color-coded bars and comparison highlights
- Accept comma-separated positive integers (2 to 100 values)
- Generate random numbers, set animation speed and reset

## Run on Windows

1. Download/clone the project and open its folder in File Explorer.
2. Click the File Explorer address bar, type `cmd`, and press Enter.
3. Run:

   ```cmd
   python sorting_algoridhm_visualiser.py
   ```

You can also open the script in **Python IDLE**, then select **Run → Run Module (F5)**.

No third-party packages are required for this project. Keep the Python window open while using the application.

## Limitations

The original code implements **Bubble Sort only**. Merge, Quick, Insertion and Selection Sort are not included.

This is a learning/portfolio project. The original script has been checked with Python syntax parsing, and selected non-GUI logic has been smoke-tested. **Its complete Tkinter interface was not tested in an actual Windows desktop session.**

## GitHub

Commit the Python file, this README and `.gitignore`. Generated `.db` files and personal records are ignored by Git. Store real data outside public GitHub repositories.
