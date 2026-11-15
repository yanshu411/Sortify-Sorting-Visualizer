
import tkinter as tk
from tkinter import ttk
import random

# ---------------- CONFIGURATION ----------------

BG = "#0B1020"
PANEL = "#151D32"
ACCENT = "#7C5CFC"
TEXT = "#F1F5F9"
MUTED = "#94A3B8"
BAR = "#38BDF8"
COMPARE = "#FACC15"
SORTED = "#22C55E"

root = tk.Tk()
root.title("Sortify | Sorting Algorithm Visualizer")
root.geometry("1050x700")
root.minsize(850, 600)
root.configure(bg=BG)

numbers = []
sorting = False
after_id = None
speed = 60


# ---------------- NUMBER GENERATION ----------------

def generate_numbers():
    global numbers, sorting

    stop_sorting()
    sorting = False

    numbers = [random.randint(20, 300) for _ in range(35)]

    status_label.config(text="Ready to visualize")
    draw_bars()
    
def use_custom_array():
    global numbers

    stop_sorting()

    try:
        user_input = array_entry.get().strip()

        if not user_input:
            status_label.config(
                text="Please enter some numbers!",
                fg="#EF4444"
            )
            return

        # Convert comma-separated input into integers
        new_numbers = [
            int(x.strip()) for x in user_input.split(",")
        ]

        if len(new_numbers) < 2:
            raise ValueError("Enter at least two numbers")

        if len(new_numbers) > 100:
            raise ValueError("Maximum 100 numbers allowed")

        if any(x <= 0 for x in new_numbers):
            raise ValueError("Enter positive numbers only")

        numbers = new_numbers

        draw_bars()

        status_label.config(
            text="Your custom array is ready!",
            fg="#22C55E"
        )

    except ValueError:
        status_label.config(
            text="Invalid input! Enter numbers separated by commas.",
            fg="#EF4444"
        )



# ---------------- DRAWING BARS ----------------


def draw_bars(highlight=None, sorted_index=None):
    if not numbers:
        return

    highlight = highlight or []
    canvas.delete("all")

    width = max(canvas.winfo_width(), 600)
    height = max(canvas.winfo_height(), 300)

    bar_width = width / len(numbers)
    max_value = max(numbers)

    for i, value in enumerate(numbers):

        bar_height = (value / max_value) * (height - 55)

        x1 = i * bar_width + 2
        x2 = (i + 1) * bar_width - 2
        y1 = height - bar_height - 25
        y2 = height - 25

        if i in highlight:
            color = COMPARE
        elif sorted_index is not None and i >= sorted_index:
            color = SORTED
        else:
            color = BAR

        # Draw the bar
        canvas.create_rectangle(
            x1, y1, x2, y2,
            fill=color,
            outline=""
        )

        # Display number inside the bar
        canvas.create_text(
            (x1 + x2) / 2,
            y1 + 15,
            text=str(value),
            fill="white",
            font=("Segoe UI", 10, "bold")
        )



# ---------------- BUBBLE SORT ----------------

def bubble_sort():
    global numbers

    arr = numbers.copy()
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):

            # Compare two elements
            yield j, j + 1, n - i

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                numbers = arr.copy()

                # Show swapped elements
                yield j, j + 1, n - i

    yield None, None, 0


# ---------------- ANIMATION CONTROL ----------------

def start_sorting():
    global sorting, sort_generator

    if sorting:
        return

    if not numbers:
        return

    sorting = True
    sort_generator = bubble_sort()

    status_label.config(text="Sorting in progress...")
    next_step()


def next_step():
    global sorting, after_id

    if not sorting:
        return

    try:
        a, b, sorted_index = next(sort_generator)

        if a is None:
            draw_bars()
            status_label.config(text="Sorting completed!")
            sorting = False
            return

        draw_bars(
            highlight=[a, b],
            sorted_index=sorted_index
        )

        after_id = root.after(speed, next_step)

    except StopIteration:
        sorting = False
        status_label.config(text="Sorting completed!")


def stop_sorting():
    global sorting, after_id

    sorting = False

    if after_id is not None:
        root.after_cancel(after_id)
        after_id = None


def reset_visualizer():
    stop_sorting()
    generate_numbers()


def change_speed(value):
    global speed
    speed = int(value)


# ---------------- HEADER ----------------

header = tk.Frame(root, bg=BG)
header.pack(fill="x", padx=30, pady=(22, 12))

tk.Label(
    header,
    text="SORTIFY",
    font=("Segoe UI", 25, "bold"),
    fg=TEXT,
    bg=BG
).pack(side="left")

tk.Label(
    header,
    text="DSA VISUALIZATION LAB",
    font=("Segoe UI", 10, "bold"),
    fg=ACCENT,
    bg=BG
).pack(side="left", padx=15, pady=12)
 
# ---------------- CUSTOM ARRAY INPUT ----------------

input_frame = tk.Frame(root, bg=BG)
input_frame.pack(fill="x", padx=30, pady=5)

tk.Label(
    input_frame,
    text="Enter Your Array:",
    font=("Segoe UI", 11, "bold"),
    fg=TEXT,
    bg=BG
).pack(side="left", padx=(0, 10))

array_entry = tk.Entry(
    input_frame,
    font=("Segoe UI", 12),
    bg="#1E293B",
    fg="white",
    insertbackground="white",
    relief="flat",
    width=45
)

array_entry.pack(side="left", ipady=8, padx=5)

array_entry.insert(0, "50, 20, 80, 10, 40, 30")

tk.Button(
    input_frame,
    text="Use My Array",
    command=use_custom_array,
    bg="#7C5CFC",
    fg="white",
    relief="flat",
    padx=15,
    pady=9,
    cursor="hand2"
).pack(side="left", padx=10)


# ---------------- MAIN PANEL ----------------

panel = tk.Frame(root, bg=PANEL)
panel.pack(fill="both", expand=True, padx=30, pady=15)

tk.Label(
    panel,
    text="Sorting Algorithm Visualizer",
    font=("Segoe UI", 21, "bold"),
    fg=TEXT,
    bg=PANEL
).pack(anchor="w", padx=25, pady=(20, 5))

tk.Label(
    panel,
    text="Watch how sorting algorithms organize data step by step.",
    font=("Segoe UI", 10),
    fg=MUTED,
    bg=PANEL
).pack(anchor="w", padx=25)


# ---------------- CANVAS ----------------

canvas = tk.Canvas(
    panel,
    bg="#0F172A",
    highlightthickness=0
)
canvas.pack(fill="both", expand=True, padx=25, pady=25)


# ---------------- CONTROLS ----------------

controls = tk.Frame(panel, bg=PANEL)
controls.pack(fill="x", padx=25, pady=(0, 15))

tk.Label(
    controls,
    text="ALGORITHM: BUBBLE SORT",
    font=("Segoe UI", 10, "bold"),
    fg=TEXT,
    bg=PANEL
).pack(side="left", padx=(0, 20))

tk.Button(
    controls,
    text="Generate Array",
    command=generate_numbers,
    bg="#334155",
    fg=TEXT,
    activebackground="#475569",
    activeforeground=TEXT,
    relief="flat",
    padx=14,
    pady=9,
    cursor="hand2"
).pack(side="left", padx=5)

tk.Button(
    controls,
    text="Start Sorting",
    command=start_sorting,
    bg=ACCENT,
    fg="white",
    activebackground="#6845E8",
    activeforeground="white",
    relief="flat",
    padx=18,
    pady=9,
    cursor="hand2"
).pack(side="left", padx=5)

tk.Button(
    controls,
    text="Reset",
    command=reset_visualizer,
    bg="#334155",
    fg=TEXT,
    activebackground="#475569",
    activeforeground=TEXT,
    relief="flat",
    padx=18,
    pady=9,
    cursor="hand2"
).pack(side="left", padx=5)


# ---------------- SPEED CONTROL ----------------

speed_frame = tk.Frame(panel, bg=PANEL)
speed_frame.pack(fill="x", padx=25, pady=(0, 10))

tk.Label(
    speed_frame,
    text="Animation Speed",
    font=("Segoe UI", 10),
    fg=MUTED,
    bg=PANEL
).pack(side="left")

speed_scale = tk.Scale(
    speed_frame,
    from_=10,
    to=200,
    orient="horizontal",
    command=change_speed,
    bg=PANEL,
    fg=TEXT,
    troughcolor="#334155",
    highlightthickness=0,
    length=200
)
speed_scale.set(60)
speed_scale.pack(side="left", padx=10)


# ---------------- STATUS BAR ----------------

status_label = tk.Label(
    panel,
    text="Ready to visualize",
    font=("Segoe UI", 10, "bold"),
    fg=SORTED,
    bg=PANEL
)
status_label.pack(anchor="w", padx=25, pady=(5, 20))


# ---------------- START APPLICATION ----------------

root.bind("<Configure>", lambda event: draw_bars()
          if event.widget == root else None)

generate_numbers()

root.mainloop()
