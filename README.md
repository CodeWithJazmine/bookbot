# BookBot

BookBot - Python command-line application that analyzes text files to generate statistical reports on word and character usage. Built as part of [Boot.dev](https://www.boot.dev) curriculum using Python, Git, and GitHub.

## Project Overview

BookBot analyzes text files to provide:
- Total word count
- Character frequency analysis
- Sorted character count statistics

This project was built as part of my learning journey with Boot.dev to practice Python programming, command-line application development, and setting up a professional development environment.

## Features

- Read and process text files (works with novels like "Frankenstein", "Moby Dick", or any plain text file)
- Count the total number of words in a text
- Track character frequency and display sorted results
- Command-line interface for easy use with any text file

## How to Use

1. Clone this repository
2. Create a `books` directory and download text files you want to analyze (Project Gutenberg is a great source for free e-books)
3. Run the application by providing a path to a text file:
python main.py path_to_book.txt

For example:
python main.py books/frankenstein.txt

## Sample Output
========== BOOKBOT ==========
Analyzing book found at [book_file]
---------- Word Count ----------
Found [num_words] total words
---------- Character Count ----------
[char]: [count]
...
========== END ==========

## Project Structure

- `main.py`: Entry point of the application
- `stats.py`: Contains functions for text analysis
- `books/`: Directory for text files (not included in repository to keep it clean)

## Technologies Used

- Python
- Git & GitHub
- VS Code

## Learning Outcomes

Through building this project, I:
- Set up a local Python development environment
- Practiced building a complete project from scratch
- Implemented file I/O operations in Python
- Created text processing and analysis functions
- Used Git for version control and GitHub for project hosting

## Acknowledgements

This project was built as part of the [Boot.dev](https://boot.dev) curriculum.