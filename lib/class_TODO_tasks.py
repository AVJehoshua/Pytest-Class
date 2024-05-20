class ToDo():
    
    def __init__(self, task, is_complete=False):
        if task == " ":
            raise Exception("Task cannot be an empty task!")
        elif type(task) == int:
            raise Exception("Task input must be a string, not an integer!")
        else:
            self.task = task                # task is a public property
            self.is_complete = is_complete  # This must be initiated so that it can be used within multiple classes!

    def mark_complete(self):
        self.is_complete = True



    

