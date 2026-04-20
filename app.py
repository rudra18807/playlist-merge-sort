import gradio as gr

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
        steps.append(f"Comparing {left[0][0]}({left[0][1]}) and {right[0][0]}({right[0][1]})")
        
        if left[0][1] <= right[0][1]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
        
        steps.append(f"Current merged list: {[(x[0], x[1]) for x in result]}")
    
    result.extend(left)
    result.extend(right)
    
    steps.append(f"Final merge result: {[(x[0], x[1]) for x in result]}")
    
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

def format_playlist(songs):
    output = ""
    for i, song in enumerate(songs, 1):
        output += f"{i}. {song[0]} (Energy: {song[1]})\n"
    return output

def format_steps():
    output = ""
    for i, step in enumerate(steps, 1):
        output += f"Step {i}: {step}\n"
    return output

def run_sort(input_text):
    global steps
    steps = []
    
    if not input_text.strip():
        return "Please enter at least one song.", ""
    
    songs = parse_input(input_text)
    if songs is None:
        return "Invalid format. Use: SongA:80, SongB:50", ""
    
    steps.append(f"Original list: {[(x[0], x[1]) for x in songs]}")
    
    sorted_songs = merge_sort(songs.copy())
    
    steps.append(f"Final sorted list: {[(x[0], x[1]) for x in sorted_songs]}")
    
    return format_playlist(sorted_songs), format_steps()

with gr.Blocks() as app:
    gr.Markdown("# 🎵 Playlist Vibe Builder (Merge Sort Visualizer)")
    gr.Markdown("Enter songs like: `SongA:80, SongB:50, SongC:90`")
    
    input_box = gr.Textbox(label="Songs Input")
    
    run_btn = gr.Button("Sort Playlist")
    
    output_playlist = gr.Textbox(label="Sorted Playlist")
    output_steps = gr.Textbox(label="Step-by-Step Visualization")
    
    run_btn.click(run_sort, inputs=input_box, outputs=[output_playlist, output_steps])

app.launch()