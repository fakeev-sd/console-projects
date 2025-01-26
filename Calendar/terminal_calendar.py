from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
import calendar
import datetime
from tabulate import tabulate

console = Console()
events = []


def show_calendar(year, month):
    """Функция для отображения календаря на выбранный месяц."""
    cal = calendar.TextCalendar(calendar.MONDAY)
    console.print(f"[bold cyan]{calendar.month_name[month]} {year}[/]\n")
    console.print(cal.formatmonth(year, month))


def add_event():
    """Добавление нового события."""
    year = Prompt.ask("Введите год события", default=str(datetime.datetime.now().year))
    month = Prompt.ask(
        "Введите месяц события", default=str(datetime.datetime.now().month)
    )
    day = Prompt.ask("Введите день события", default=str(datetime.datetime.now().day))
    event_name = input("Введите название события: ")

    # Проверка корректности даты
    try:
        event_date = datetime.date(int(year), int(month), int(day))
        events.append({"date": event_date, "name": event_name})
        console.print(
            f"[green]Событие '{event_name}' успешно добавлено на {event_date}.[/]"
        )
    except ValueError:
        console.print("[red]Некорректная дата. Попробуйте снова.[/]")


def view_events():
    """Просмотр всех событий в табличном формате."""
    if events:
        event_list = [[event["date"], event["name"]] for event in events]
        table = tabulate(event_list, headers=["Дата", "Событие"], tablefmt="grid")
        console.print(table)
    else:
        console.print("[yellow]Пока нет добавленных событий.[/]")


def delete_event():
    """Удаление события по индексу."""
    if events:
        view_events()
        event_index = Prompt.ask("Введите номер события для удаления", default="1")
        try:
            event_index = int(event_index) - 1
            removed_event = events.pop(event_index)
            console.print(f"[red]Событие '{removed_event['name']}' удалено.[/]")
        except (ValueError, IndexError):
            console.print("[red]Некорректный индекс. Попробуйте снова.[/]")
    else:
        console.print("[yellow]Нет событий для удаления.[/]")


def calendar_app():
    """Главное меню календаря."""
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month

    while True:
        console.print("[bold magenta]Интерактивный календарь событий[/]")
        console.print("[1] Показать календарь на текущий месяц")
        console.print("[2] Добавить событие")
        console.print("[3] Посмотреть список событий")
        console.print("[4] Удалить событие")
        console.print("[5] Выйти")

        choice = Prompt.ask(
            "Выберите действие", choices=["1", "2", "3", "4", "5"], default="1"
        )

        if choice == "1":
            show_calendar(current_year, current_month)
        elif choice == "2":
            add_event()
        elif choice == "3":
            view_events()
        elif choice == "4":
            delete_event()
        elif choice == "5":
            console.print("[bold cyan]Выход...[/]")
            break


if __name__ == "__main__":
    calendar_app()
