from lib.class_TODO_list import *
import pytest

"""
Given the task is an empty string, return an exception error
"""

def test_todo_task_is_empty_string():
    with pytest.raises(Exception) as e:
        task_1 = ToDoList()
        task_1.add(" ")
    assert str(e.value) == "Task cannot be an empty task!"

"""
Given a task which is not a string, but an integer,
return exception message
"""

def test_input_is_int_not_string():
    with pytest.raises(Exception) as e:
        task_1 = ToDoList()
        task_1.add(15)
    assert str(e.value) == "Task input must be a string, not an integer!"
