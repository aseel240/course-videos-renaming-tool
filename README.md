# course-videos-renaming-tool

A Python script to rename video files in a directory based on a course content text file. The script prompts the user for input paths and handles renaming with proper error handling and sorting.

## Features

- Prompts for directory and content file paths via command line
- Reads and validates course content text file
- Sorts video files by numeric order in filenames
- Renames video files with corresponding lecture names
- Provides detailed output and error handling

## Usage

1. Clone the repository:
   ```sh
   git clone https://github.com/aseel240/course-videos-renaming-tool.git
   cd course-videos-renaming-tool
   ```


2. Prepare your directory with video files and a course content text file. For example:

   ```sh
   D:/Education/course01
   ```
   ```sh
   ├── lesson1.mp4
   ├── lesson2.mp4
   ├── ...
   ├── lesson100.mp4
   ├── lessons.txt
   └── Readme.txt
   ```
The lessons.txt file should contain the names of the lectures, one per line.

Run the script:

   ```sh
   python renamer.py
   ```
Follow the prompts to enter the directory and content file paths.
