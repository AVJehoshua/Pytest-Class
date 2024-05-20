from lib.class_TODO_list import *
from lib.class_TODO_tasks import *

"""
Given i add a task, it adds the task into
the TODO list

"""

def test_1_task_adds_to_list():
    todo_list = ToDoList()
    task_1 = ToDo("Walk my Cat")
    todo_list.add(task_1)
    assert todo_list.incomplete() == [task_1]

"""
Given i add multiple tasks, it adds the tasks into
the TODO list

"""

def test_adds_multiple_tasks_to_list():
    todo_list = ToDoList()
    task_1 = ToDo("Walk my Cat")
    task_2 = ToDo("Embrace the absurd")
    todo_list.add(task_1)
    todo_list.add(task_2)
    assert todo_list.incomplete() == [task_1, task_2]
    

"""
Given a list of Todo Instances, it returns
a list of todos which are complete
"""


def test_takes_2_tasks_returns_1_complete_in_list():
    todo_list = ToDoList()
    task_1 = ToDo("Walk my Cat")
    task_2 = ToDo("Embrace the Absurd")
    todo_list.add(task_1)
    todo_list.add(task_2)
    task_2.mark_complete()
    assert todo_list.complete() == [task_2]



"""
Given a list 3 of TODO instances, 
mark_complete, marks two tasks as complete,
and returns a list of complete tasks
"""
    
def test_3_tasks_marks_2_as_complete_returns_list_of_2():
    todo_list = ToDoList()
    task_1 = ToDo("Walk my Cat")
    task_2 = ToDo("Embrace the Absurd")
    task_3 = ToDo("Appreciate family and friends")
    todo_list.add(task_1)
    todo_list.add(task_2)
    todo_list.add(task_3)
    task_2.mark_complete()
    task_3.mark_complete()
    assert todo_list.complete() == [task_2, task_3]

"""
Given the user is giving up, give_up()
marks all todo tasks as complete.
"""

def test_user_has_given_up_mark_all_todo_as_complete():
    todo_list = ToDoList()
    task_1 = ToDo("Walk my Cat")
    task_2 = ToDo("Embrace the Absurd")
    task_3 = ToDo("Appreciate family and friends")
    todo_list.add(task_1)
    todo_list.add(task_2)
    todo_list.add(task_3)
    todo_list.give_up()
    assert todo_list.complete() == [task_1, task_2, task_3]







