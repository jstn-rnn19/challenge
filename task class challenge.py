class Task:
    def __init__(self, title, descript):
        self.title = title
        self.descript = descript
        self.is_done = False

    def mark_done(self):
        self.is_done = True

    def mark_undone(self):
        self.is_done = False

    def summary(self):
        print(self.title)
        print(self.descript)
        print(self.is_done)



class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def show_all(self):
        for task in self.tasks:
            task.summary()

    def show_done(self):
        for task in self.tasks:
            if task.is_done:
                task.summary()

    def show_pending(self):
        for task in self.tasks:
            if not task.is_done:
                task.summary()



t1 = Task("Clean desk", "Organize books and wires")
t2 = Task("Submit assignment", "Upload to LMS")

todo = TodoList()
todo.add_task(t1)
todo.add_task(t2)

t1.mark_done()

todo.show_all()
todo.show_done()
todo.show_pending()