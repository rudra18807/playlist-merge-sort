---
title: Playlist Merge Sort Visualizer
emoji: 🎵
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: "4.0.0"
app_file: app.py
pinned: false
---

# Playlist Vibe Builder

## Chosen Problem:
The app helps the user organize a playlist by sorting songs based on their energy level. Allowing the user to build a playlist that gradually increases in intensity.

## Chosen Algorithm:
Merge Sort was chosen because:
- It is efficient with a time complexity of O(n log n)
- It uses a O(n log n)
- It solves the problem by dividing the list into small parts, then solving each small part, then combining and merging them back together
- Clear on showing how lists are split and merged

## Demo:
Screenshot:

## Problem Breakdown
- Decomposition: The problem is broken into smaller steps
    - Takes user input
    - Paste input to a structured list
    - Recursively split the list into small lists
    - Merges the small lists into a sorted order
    - Displays final list and the steps taken

- Pattern Recognition: The algorithm constantly:
    - Divides the list by half
    - Compares the smallest element
    - Merges sorted list

- Abstraction: The app shows:
    - Comparisons between song
    - Merging steps

- Algorithm Design:
    - Inputs -> Processes -> Output
        Process:
            - Input
            - Merge Sort
            - Steps Taken
        
        Output:
            - Sorted Playlist
            - Explaination of steps

## Flowchart

Start -> User Input -> Apply Merge Sort -> Steps Taken -> Display Sorted playlist with the steps -> End

## Steps to run Local

1. Install dependencies:
    - requirements.txt

2. Run the app:
    - python3 app.py (python3 because I'm on mac)

3. Open the link that shows up in the terminal in your browser

## Hugging Face Link:

## Testing
    - Normal Input (SongA:80,SongB:50) - Sorted Ascending
    - Already Sorted (SongA:20,SongB40) - No Change
    - Reverse Order (SongA:90,SongB:10) - Corrected sorting
    - Same Value (SongA:50,SongB:50) - No Change
    - Empty () - Error Message
    - Invalid Format (SongA-80) - Error Message

## Author & Acknowledgement
Created by Rudra Patel

AI was used for:
    - Fixing of many code
    - Assist with errors
    - Improve code structure
    - Help explain concepts
    - Idea with planning

Everything put together was by me.