from lib.contacts import *
from lib.diary import *
from lib.todo import *
from lib.personal_assistant import *

def test_adding_an_entry_to_diary():
    title = "December 2019"
    content = "Solo trip to Finland, Estonia, Lithuania, and Latvia"
    entry = Diary(title, content)
    diary = Personal_assistant()
    diary.add_diary_entry(entry)
    assert diary.diary_list == [entry]

def test_adding_a_contact():
    contact_name = "Rory"
    phone_number = "777-1234"
    contacts = Personal_assistant()
    contacts.add_contact(contact_name, phone_number)
    assert contacts.contact_list == {contact_name:phone_number}

def test_adding_a_task_to_a_list():
    title = "do daily meditation"
    task = Todo(title)
    todos = Personal_assistant()
    todos.add_todo(task)
    assert todos.todo_list == [task]

def test_two_incomplete_todos_ignore_one_complete_return_incomplete():
    task1 = Todo("think happy thoughts")
    task2 = Todo("practice self-care")
    task3 = Todo("reflect on successes")
    task1.mark_complete()
    task2.mark_complete()
    todos = Personal_assistant()
    todos.add_todo(task1)
    todos.add_todo(task2)
    todos.add_todo(task3)
    result = todos.incomplete_todos()
    assert result == [task3]

def test_two_complete_todos_ignore_one_incomplete_return_complete():
    task1 = Todo("think happy thoughts")
    task2 = Todo("practice self-care")
    task3 = Todo("reflect on successes")
    task1.mark_complete()
    task2.mark_complete()
    todos = Personal_assistant()
    todos.add_todo(task1)
    todos.add_todo(task2)
    todos.add_todo(task3)
    result = todos.complete_todos()
    assert result == [task1, task2]

def test_alternate_data_type_complete():
    todo = True
    task = Todo(todo)
    task.mark_complete()
    lst = Personal_assistant()
    lst.add_todo(task)
    result = lst.complete_todos()
    assert result == [task]

def test_change_phone_number():
    contact_name = "Phoebe"
    phone_number = "555-1234"
    new_number = "123-4567"
    pa = Personal_assistant()
    pa.add_contact(contact_name, phone_number)
    pa.update_number(contact_name, new_number)
    result = pa.contact_list
    assert result == {"Phoebe":"123-4567"}

def test_call_contact_retrieve_one_number():
    contact_name = "Rory"
    phone_number = "777-1234"
    contact_name_two = "Kirk"
    phone_number_two = "555-9876"
    contacts = Personal_assistant()
    contacts.add_contact(contact_name, phone_number)
    contacts.add_contact(contact_name_two, phone_number_two)
    result = contacts.call_contact(contact_name)
    assert result == phone_number