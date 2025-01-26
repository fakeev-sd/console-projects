# импортируем нужные библиотеки
from art import tprint
from rich.console import Console
from tabulate import tabulate

console = Console()

# создаем список для хранения трат
expenses = []

# красивая надпись
tprint("Fin-tracker")


# функция для добавления траты
def add_expense():
    name = input("Введите название траты: ")
    amount = float(input("Введите сумму: "))
    expenses.append([name, amount])


# функция для отображения трат. задаём таблицу
def display_expenses():
    table = tabulate(expenses, headers=["Название", "Сумма"], tablefmt="grid")
    console.print(table)


# суммируем все траты
def show_total():
    total = sum([expense[1] for expense in expenses])
    console.print(f"[bold green]Общая сумма расходов: {total}[/]")


# основная функция
def fin_calculator():
    while True:
        console.print("[bold yellow]1. Добавить трату[/]")
        console.print("[bold yellow]2. Показать все траты[/]")
        console.print("[bold yellow]3. Показать общую сумму[/]")
        console.print("[bold yellow]4. Выйти[/]")

        choice = input("Выберите действие: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            display_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            console.print("[bold cyan]Выход из программы...[/]")
            break
        else:
            console.print("[red]Неверный выбор![/]")


fin_calculator()
