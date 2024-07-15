import os
import re
import sys

def get_directory_path():
    """Prompt the user for the directory path and validate it."""
    while True:
        directory = input("Enter the path to the directory containing the videos: ").strip()
        if os.path.isdir(directory):
            return directory
        else:
            print("Invalid directory path. Please try again.")

def get_content_file_path(directory):
    """Prompt the user for the course content file path and validate it."""
    while True:
        content_file = input(f"Enter the path to the course content text file (default: {os.path.join(directory, 'lessons.txt')}): ").strip()
        if not content_file:
            content_file = os.path.join(directory, 'lessons.txt')
        if os.path.isfile(content_file):
            return content_file
        else:
            print("Invalid file path. Please try again.")

def read_course_content(content_file):
    """Read and return the course content from the provided text file."""
    try:
        with open(content_file, 'r', encoding='utf-8') as f:
            return f.readlines()
    except Exception as e:
        print(f"Error reading the content file: {e}")
        sys.exit(1)

def extract_number(f):
    """Extract and return the numeric part of the filename."""
    match = re.search(r'(\d+)', f)
    return int(match.group(1)) if match else 0

def main():
    # Get the directory and content file paths
    directory = get_directory_path()
    content_file = get_content_file_path(directory)
    
    # Read the course content
    lines = read_course_content(content_file)

    # Get and filter the list of video files
    video_files = [f for f in os.listdir(directory) if f.endswith(('.mp4', '.ts'))]
    
    if not video_files:
        print("No video files found in the directory.")
        sys.exit(1)
    
    # Sort video files by the extracted number
    video_files.sort(key=extract_number)

    # Ensure the number of lecture names matches the number of video files
    if len(lines) < len(video_files):
        print("Warning: The number of video files exceeds the number of lecture names provided.")
        print("Renaming will proceed with available lecture names.")

    # Rename the video files
    for i, video_file in enumerate(video_files):
        # Get the corresponding lecture name
        if i < len(lines):
            lecture_name = lines[i].strip()
        else:
            lecture_name = f'Unknown Lecture {i+1}'

        # Construct the new name
        extension = os.path.splitext(video_file)[1]
        new_name = f'{i+1:03d}_{lecture_name}{extension}'
        
        # Rename the file
        old_path = os.path.join(directory, video_file)
        new_path = os.path.join(directory, new_name)
        try:
            os.rename(old_path, new_path)
            print(f'Renamed: {video_file} -> {new_name}')
        except Exception as e:
            print(f"Error renaming {video_file} to {new_name}: {e}")

    print("Renaming completed.")

if __name__ == "__main__":
    main()
