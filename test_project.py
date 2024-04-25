import pytest
from tkinter import *
from project import add_task, delete_task, view_task

@pytest.fixture
def tk_root():
    root = Tk()
    yield root
    root.destroy()

def test_add_task(tk_root):
  task_enter = Entry(tk_root)
  task_enter.insert(0, "Test Task")

  task_list = []
  listbox = Listbox(tk_root)

  add_task(task_enter, listbox, task_list)

  with open("tasklist.txt") as taskfile:
        lines = taskfile.readlines()
        last_task = lines[-1].strip() if lines else ""
        assert "Test Task" == last_task
  


def test_delete_task(tk_root):
    listbox = Listbox(tk_root)
    task_list = ["shreya"]
    listbox.insert(ANCHOR, "shreya")
    listbox.selection_set(0)

    delete_task(listbox, task_list)
    print("the task list is:",task_list)

    with open("tasklist.txt",'r') as taskfile:
        file_content=taskfile.read()
        assert "shreya" not in file_content

def test_view_task(tk_root):
    task_list = ["Task 1", "Task 2", "Task 3"]
    listbox = Listbox(tk_root)

    view_task(listbox, task_list)
    print("task list",task_list)

    assert all(task in task_list for task in ["Task 1", "Task 2", "Task 3"])


if __name__ == "__main__":
    pytest.main()
