#print("Hello, To-Do App!")
#a list to store our todo. each task is a dictionary.
tasks = [
    {"task" : "read a book", "completed":False},
    {"task" : "do some code", "completed":True},
    {"task" : "lets check how git tracks me", "completed":False},
    {"task" : "another check", "completed":False}
        ]
def display_tasks():
    print("---your todo list---")
    if not tasks:
        print("you have no tasks")
    else:
        for index, task in enumerate(tasks, start=1):
            status_icon = "|/" if task["completed"] else "||"
            print(f"{index},{status_icon}){task['task']}")
    print(".................................................")

if __name__ == "__main__":
    display_tasks()
            