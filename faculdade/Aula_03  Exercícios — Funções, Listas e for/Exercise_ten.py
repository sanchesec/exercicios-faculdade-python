# Use enumerate(start=1) para listar uma lista de tarefas numerada a partir do 1.
c = "y"
tasks = []

while c in ("y","yes"):
    newtask = input("Insert task: ")
    tasks.append(newtask)
    c = input("you want insert other?: ").strip().lower()

print("Ok, your task list are: ")
for index, task in enumerate(tasks,1):
    print(f"°{index} Task  - {task}")