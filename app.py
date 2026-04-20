print("App is starting...")

import gradio as gr

# Global list to store steps
steps = []

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    
    while left and right:
        # Record step for visualization
        steps.append(f"Comparing {left[0]} and {right[0]}")
        
        if left[0][1] < right[0][1]:  # compare energy
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    
    result.extend(left)
    result.extend(right)
    
    steps.append(f"Merged into {result}")
    
    return result

def parse_input(input_text):
    songs = []
    
    try:
        items = input_text.split(",")
        for item in items:
            title, energy = item.split(":")
            songs.append((title.strip(), int(energy.strip())))
        return songs
    except:
        return None

def run_sort(input_text):
    global steps
    steps = []
    
    songs = parse_input(input_text)
    
    if songs is None:
        return "Invalid input format. Use: SongA:80, SongB:50"
    
    sorted_songs = merge_sort(songs.copy())
    
    result = "Sorted Playlist:\n"
    for song in sorted_songs:
        result += f"{song[0]} (Energy: {song[1]})\n"
    
    result += "\n--- Steps ---\n"
    for step in steps:
        result += step + "\n"
    
    return result

# Gradio UI
interface = gr.Interface(
    fn=run_sort,
    inputs=gr.Textbox(label="Enter songs (Song:Energy)"),
    outputs=gr.Textbox(label="Output"),
    title="Playlist Vibe Builder (Merge Sort Visualizer)",
    description="Enter songs like: SongA:80, SongB:50, SongC:90"
)

interface.launch()