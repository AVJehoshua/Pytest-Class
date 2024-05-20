
class ToDoList():

    def __init__(self):
        self.list = []
        self.complete_list = []

    def add(self, todo):
        if todo == " ":
            raise Exception("Task cannot be an empty task!")
        elif type(todo) == int:
            raise Exception("Task input must be a string, not an integer!")
        else:
            self.list.append(todo)


    def incomplete(self):
        return self.list
    
    def complete(self):
        for task in self.list:
            if task.is_complete == True:
                # return [task]                     #for one task to be marked as true
                self.complete_list.append(task)        #for multiple tasks to be marked as true
        return self.complete_list

    def give_up(self):
        for task in self.list:
            task.is_complete == True
            self.complete_list.append(task)
        return self.complete_list
    


todo_list = ToDoList()

todo_list.add("Walk my cat")

