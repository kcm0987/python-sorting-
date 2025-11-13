from tkinter import *
import tkinter as tk
import random
import time
import heapq
import csv
from tkinter import filedialog


# Function to swap two bars in animation
def swap(pos_0, pos_1):
    bar11, _, bar12, _ = canvas.coords(pos_0)
    bar21, _, bar22, _ = canvas.coords(pos_1)
    canvas.move(pos_0, bar21 - bar11, 0)
    canvas.move(pos_1, bar12 - bar22, 0)


def animate(generator):
    def step():
        try:
            next(generator)
            window.after(100, step)
        except StopIteration:
            return

    step()


worker = None


# Sorting Algorithms
def _insertion_sort():
    global barList, lengthList
    for i in range(len(lengthList)):
        cursor = lengthList[i]
        cursorBar = barList[i]
        pos = i
        while pos > 0 and lengthList[pos - 1] > cursor:
            lengthList[pos] = lengthList[pos - 1]
            barList[pos], barList[pos - 1] = barList[pos - 1], barList[pos]
            swap(barList[pos], barList[pos - 1])
            yield
            pos -= 1
        lengthList[pos] = cursor
        barList[pos] = cursorBar


def _bubble_sort():
    global barList, lengthList
    for i in range(len(lengthList) - 1):
        for j in range(len(lengthList) - i - 1):
            if lengthList[j] > lengthList[j + 1]:
                lengthList[j], lengthList[j + 1] = lengthList[j + 1], lengthList[j]
                barList[j], barList[j + 1] = barList[j + 1], barList[j]
                swap(barList[j + 1], barList[j])
                yield


def _selection_sort():
    global barList, lengthList
    for i in range(len(lengthList)):
        min_idx = i
        for j in range(i + 1, len(lengthList)):
            if lengthList[j] < lengthList[min_idx]:
                min_idx = j
        lengthList[i], lengthList[min_idx] = lengthList[min_idx], lengthList[i]
        barList[i], barList[min_idx] = barList[min_idx], barList[i]
        swap(barList[i], barList[min_idx])
        yield


def _merge_sort(start, end):
    global barList, lengthList
    if end - start > 1:
        mid = (start + end) // 2
        yield from _merge_sort(start, mid)
        yield from _merge_sort(mid, end)
        yield from _merge(start, mid, end)


def _merge(start, mid, end):
    global barList, lengthList
    # Create temporary arrays for the merge operation
    left = lengthList[start:mid]
    right = lengthList[mid:end]
    temp = []
    temp_bars = []

    # Save the original bar references
    left_bars = barList[start:mid].copy()
    right_bars = barList[mid:end].copy()

    # Merge the two sorted halves
    i, j, k = 0, 0, start
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            lengthList[k] = left[i]
            temp.append(left[i])
            temp_bars.append(left_bars[i])
            i += 1
        else:
            lengthList[k] = right[j]
            temp.append(right[j])
            temp_bars.append(right_bars[j])
            j += 1
        k += 1

    # If there are remaining elements in left array
    while i < len(left):
        lengthList[k] = left[i]
        temp.append(left[i])
        temp_bars.append(left_bars[i])
        i += 1
        k += 1

    # If there are remaining elements in right array
    while j < len(right):
        lengthList[k] = right[j]
        temp.append(right[j])
        temp_bars.append(right_bars[j])
        j += 1
        k += 1

    # Update the bar positions visually
    for i in range(start, end):
        # Calculate the coordinates for each bar
        x1, y1, x2, y2 = canvas.coords(barList[i])
        canvas.delete(barList[i])
        barList[i] = temp_bars[i - start]

        # Create new visual rectangle for each bar at correct position
        value = lengthList[i]
        new_bar = canvas.create_rectangle(x1, 365 - value, x2, 365, fill='yellow')
        barList[i] = new_bar
        yield


def _quick_sort(start, end):
    if start < end:
        pivot = lengthList[end]
        i = start - 1
        for j in range(start, end):
            if lengthList[j] < pivot:
                i += 1
                lengthList[i], lengthList[j] = lengthList[j], lengthList[i]
                barList[i], barList[j] = barList[j], barList[i]
                swap(barList[i], barList[j])
                yield
        lengthList[i + 1], lengthList[end] = lengthList[end], lengthList[i + 1]
        barList[i + 1], barList[end] = barList[end], barList[i + 1]
        swap(barList[i + 1], barList[end])
        yield from _quick_sort(start, i)
        yield from _quick_sort(i + 2, end)


def _heap_sort():
    global barList, lengthList
    n = len(lengthList)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        yield from _heapify(n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        # Swap the root (maximum value) with the last element
        lengthList[i], lengthList[0] = lengthList[0], lengthList[i]
        barList[i], barList[0] = barList[0], barList[i]
        swap(barList[i], barList[0])
        yield

        # Call heapify on the reduced heap
        yield from _heapify(i, 0)


def _heapify(n, i):
    global barList, lengthList
    largest = i  # Initialize largest as root
    left = 2 * i + 1
    right = 2 * i + 2

    # See if left child of root exists and is greater than root
    if left < n and lengthList[left] > lengthList[largest]:
        largest = left

    # See if right child of root exists and is greater than root
    if right < n and lengthList[right] > lengthList[largest]:
        largest = right

    # Change root if needed
    if largest != i:
        # Swap
        lengthList[i], lengthList[largest] = lengthList[largest], lengthList[i]
        barList[i], barList[largest] = barList[largest], barList[i]
        swap(barList[i], barList[largest])
        yield

        # Heapify the affected sub-tree
        yield from _heapify(n, largest)


def load_csv():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            data = [int(row[0]) for row in reader]
            print("CSV Data:", data)
            generate(data)


def load_from_text():
    input_text = input_box.get()
    try:
        # Parse the input text to a list of numbers
        # This handles comma-separated values and space-separated values
        if ',' in input_text:
            data = [int(x.strip()) for x in input_text.split(',') if x.strip()]
        else:
            data = [int(x.strip()) for x in input_text.split() if x.strip()]

        if not data:
            raise ValueError("No valid numbers found")

        print("Input Data:", data)
        generate(data)
    except ValueError as e:
        # Show error message if the input is invalid
        error_label.config(text=f"Error: {str(e)}")
        window.after(3000, lambda: error_label.config(text=""))
        return


def generate(user_data=None):
    global barList, lengthList
    canvas.delete('all')
    barstart = 5
    barend = 15
    barList = []
    lengthList = user_data if user_data else [random.randint(1, 360) for _ in range(20)]

    # Limit to reasonable number of bars to fit on screen
    if len(lengthList) > 45:
        lengthList = lengthList[:45]
        error_label.config(text="Warning: Limited to 45 values")
        window.after(3000, lambda: error_label.config(text=""))

    # Limit values to fit within canvas height
    lengthList = [min(value, 360) for value in lengthList]

    for value in lengthList:
        bar = canvas.create_rectangle(barstart, 365 - value, barend, 365, fill='yellow')
        barList.append(bar)
        barstart += 20
        barend += 20


window = tk.Tk()
window.title('Sorting Visualizer')
window.geometry('1000x500')

# Canvas for visualization
canvas = tk.Canvas(window, width='1000', height='400')
canvas.grid(column=0, row=0, columnspan=50)

# Input box frame
input_frame = tk.Frame(window)
input_frame.grid(column=0, row=2, columnspan=50, pady=10)

input_label = tk.Label(input_frame, text="Enter numbers (comma or space separated):")
input_label.grid(column=0, row=0, padx=5)

input_box = tk.Entry(input_frame, width=50)
input_box.grid(column=1, row=0, padx=5)

load_button = tk.Button(input_frame, text="Load List", command=load_from_text)
load_button.grid(column=2, row=0, padx=5)

# Error message label
error_label = tk.Label(window, text="", fg="red")
error_label.grid(column=0, row=3, columnspan=50)

# Sorting algorithm buttons
buttons = [
    ('Insertion Sort', lambda: animate(_insertion_sort())),
    ('Selection Sort', lambda: animate(_selection_sort())),
    ('Bubble Sort', lambda: animate(_bubble_sort())),
    ('Merge Sort', lambda: animate(_merge_sort(0, len(lengthList)))),
    ('Quick Sort', lambda: animate(_quick_sort(0, len(lengthList) - 1))),
    ('Heap Sort', lambda: animate(_heap_sort())),
    ('Shuffle', lambda: generate()),
    ('Load CSV', load_csv)
]

for i, (text, command) in enumerate(buttons):
    tk.Button(window, text=text, command=command).grid(column=i, row=1)

generate()
window.mainloop()