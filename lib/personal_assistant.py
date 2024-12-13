class Personal_assistant:
    def __init__(self):
        self.todo_list = []
        self.contact_list = {}
        self.diary_list = []
    
    def add_todo(self, todo):
        self.todo_list.append(todo)

    def add_contact(self, contact_name, phone_number):
        self.contact_list[contact_name] = phone_number
    
    def update_number(self, contact_name, new_number):
        self.contact_list[contact_name] = new_number
    
    def add_diary_entry(self, entry):
        self.diary_list.append(entry)

    def incomplete_todos(self):
        return [task for task in self.todo_list if not task.complete]
        # returns list of incomplete todos
        
    def complete_todos(self):
        # returns list of completed todos
        return [task for task in self.todo_list if task.complete]
    
    def read_entries(self, title):
        # returns a diary entry by title
        pass
    def reading_time(self, wpm, minutes):
        # returns a diary entry that can be read within given 
        # wpm&minutes
        pass
    def call_contact(self, contact_name):
        # returns the phone number for the given contact_name
        return (self.contact_list[contact_name])
    def get_all_contacts(self):
        # returns a list of all contacts and their phone numbers
        pass

