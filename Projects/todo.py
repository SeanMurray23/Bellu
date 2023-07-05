import tkinker as tk


class TaskList(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()

        if not tasks:
            self.tasks = []
        else: 
            self.tasks = tasks

        self.title("Task List")


if __name__ == "__main__":
    task_list = TaskList()
    task_list.mainloop()