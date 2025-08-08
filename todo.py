def add_todo(item):
    todos.append({"text": item, "completed": False})
    print(f"Added '{item}' to your to-do list.")

def complete_todo(index):
    if 0 <= index < len(todos):
        todos[index]["completed"] = True
        print(f"Completed: '{todos[index]['text']}'")
    else:
        print("Invalid index.")

def print_todos():
    print("--- TODOs ---")
    for index, todo in enumerate(todos):
        status = "✓" if todo["completed"] else " "
        print(f"{index + 1}. [{status}] {todo['text']}")
    print("---------------")


print("Welcome to your to-do list!")

add_todo("Learn Git")
add_todo("Buy groceries")
complete_todo(0) # Mark 'Learn Git' as complete
print_todos()