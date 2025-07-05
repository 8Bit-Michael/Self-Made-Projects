from colorama import init, Fore
init(autoreset=True)

class TaskManager:
    def __init__(self):
        self.tasks = ['Walk the dog.', 'Finish your homework.', 'Do the dishes.']
        self.task_count = 3
        self.max_capacity = 5

    def add_task(self, task_title):
        if self.task_count < self.max_capacity:
            if self.task_count < len(self.tasks):
                self.tasks[self.task_count] = task_title
            else:
                self.tasks.append(task_title)
        else:
            self.max_capacity *= 2
            new_tasks = [None] * self.max_capacity
            for i in range(self.task_count):
                new_tasks[i] = self.tasks[i]
            new_tasks[self.task_count] = task_title
            self.tasks = new_tasks
        self.task_count += 1
        print(Fore.GREEN + f"{task_title} has been added to your list.")

    def remove_task(self, index):
        if 0 <= index < self.task_count:
            for i in range(index, self.task_count - 1):
                self.tasks[i] = self.tasks[i + 1]
            self.tasks[self.task_count - 1] = None
            self.task_count -= 1
            print(Fore.GREEN + f"The task, '{self.tasks[index]}' has been removed.")

    def list_tasks(self):
        for i in range(self.task_count):
            print(f"{i + 1}. {self.tasks[i]}")

    def mark_task(self, index):
        if 0 <= index < self.task_count:
            print(Fore.GREEN + f"The task, '{self.tasks[index]}' has been marked as done and removed.")
            self.remove_task(index)
        else:
            print(Fore.RED + "Invalid task index.")

tasks = TaskManager()
tasks.add_task('Wash the dog.')
tasks.mark_task(1)
tasks.list_tasks()