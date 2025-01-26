import os
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich import box
from art import tprint

console = Console()
tasks = []


# очистить экран
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# отобразить список
def display_tasks():
    clear_screen()
    tprint("To-Do List")

    table = Table(title="Список задач", box=box.ROUNDED)
    table.add_column("№", justify="center")
    table.add_column("Задача", justify="center")
    table.add_column("Статус", justify="center")

    for i, task in enumerate(tasks, 1):
        status = "Выполнено" if task["done"] else "Не выполнено"
        table.add_row(str(i), task["name"], status)

    console.print(table)


# добавить задачу
def add_task():
    task_name = Prompt.ask("Название задачи")
    tasks.append({"name": task_name, "done": False})
    display_tasks()


# отметить задачу выполненной
def task_done():
    task_num = Prompt.ask(
        "Номер задачи, которую хотите отметить как выполненную", default="1"
    )
    task_num = int(task_num) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]["done"] = True
    display_tasks()


# основная функция
def main():
    while True:
        display_tasks()
        console.print(
            "\n1. Добавить задачу\n2. Отметить как выполненную\n3. Выйти"
        )
        choice = Prompt.ask("Выберите действие", choices=["1", "2", "3"])

        if choice == "1":
            add_task()
        elif choice == "2":
            task_done()
        elif choice == "3":
            console.print("Программа завершена!")
            break


# добавить datetime для задач и их приоритетность, категории? добавить время и календарь.

main()
