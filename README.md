# TaskTracker



#### Description:

TaskTracker is a Python program designed to help users manage their tasks . This task manager allows users to create, view, and delete tasks conveniently within a graphical user interface (GUI) built using the Tkinter library.

## Project Structure

### project.py

The `project.py` file contains the main implementation of the task manager program. It consists of the following functions:

- `main()`: The main function that serves as the entry point of the program.
- `view_task()`: A function to display tasks from a file in a Listbox widget.
- `add_task()`: A function to add a new task to the task list.
- `delete_task()`: A function to delete a task from the task list.

### test_project.py

The `test_project.py` file contains unit tests for the functions implemented in `project.py`. Each test function in this file corresponds to a function in `project.py` and ensures that the functions work as expected.

## Design Choices

- **Tkinter GUI**: Tkinter was chosen as the GUI toolkit for its simplicity and ease of use. It provides a straightforward way to create a graphical interface for the task manager.

- **Separation of Concerns**: Functions in `project.py` are designed to perform specific tasks such as adding or deleting tasks. This separation of concerns makes the code modular and easier to maintain.

- **Error Handling**: Error handling is implemented to handle file related errors, such as file not found errors when reading task data from a file.

