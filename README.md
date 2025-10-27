# ToDo App

A simple command-line todo application built with Python.

## Description

This is a basic todo list application that allows users to manage their tasks through a simple menu-driven interface. The app runs in the terminal and provides essential todo functionality without any external dependencies.

## Features

- **Add Tasks**: Create new tasks and add them to your todo list
- **View Tasks**: Display all current tasks with numbered indexes
- **Delete Tasks**: Remove completed or unwanted tasks from the list
- **User-friendly Menu**: Simple numbered menu system for easy navigation
- **Input Validation**: Handles invalid menu choices and task numbers gracefully

## How to Run

1. Make sure you have Python installed on your system
2. Navigate to the project directory
3. Run the application:
   ```
   python todoapp.py
   ```

## Usage

When you run the app, you'll see a menu with 4 options:

1. **Add Task** - Enter a new task to add to your list
2. **View Tasks** - See all your current tasks numbered from 1
3. **Delete Task** - Select a task number to remove from your list
4. **Quit** - Exit the application

## Technical Details

- **Language**: Python
- **Dependencies**: None (uses only built-in Python libraries)
- **Storage**: Tasks are stored in memory during runtime (not persistent between sessions)
- **Interface**: Command-line interface with text-based menu system

## Limitations

- Tasks are not saved to disk - they will be lost when the program exits
- No task editing functionality - tasks must be deleted and re-added to modify
  
  
## Future Enhancements

Potential improvements could include:
- File-based persistence to save tasks between sessions
- Task editing capabilities
