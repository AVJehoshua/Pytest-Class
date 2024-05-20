from lib.class_TODO_tasks import *
import pytest

"""
Given the task is an empty string, return an exception error
"""

def test_todo_task_is_empty_string():
    with pytest.raises(Exception) as e:
        task_1 = ToDo(" ")
    assert str(e.value) == "Task cannot be an empty task!"

"""
Given a task which is not a string, but an integer,
return exception message

"""

def test_input_is_int_not_string():
    with pytest.raises(Exception) as e:
        task_1 = ToDo(15)
    assert str(e.value) == "Task input must be a string, not an integer!"


"""
Given a task has been completed, set the property to True
"""

def test_complete_tasks_are_set_to_true():
    todo_1 = ToDo("Walk my Cat")
    todo_2 = ToDo("Embrace the Absurd")
    todo_1.mark_complete() == False
    todo_2.mark_complete() == True
    


