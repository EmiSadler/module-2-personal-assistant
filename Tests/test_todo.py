from lib.todo import *

def test_initialize_a_todo():
    todo = Todo("buy carrots")
    assert todo.title == ("buy carrots")

    
def test_complete_a_todo():
    task = Todo("buy maple syrup")
    task.mark_complete()
    assert task.complete == True