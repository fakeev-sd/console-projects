from art import tprint
from rich.console import Console
from rich.table import Table

console = Console()

board = [" " for _ in range(9)]

tprint("TIC-TAC-TOE")


# создаём поле для игры
def print_board():
    table = Table(show_header=False, show_lines=True)
    for i in range(0, 9, 3):
        table.add_row(
            f"[green]{board[i]}[/]" if board[i] != " " else "[yellow]_[/]",
            f"[green]{board[i+1]}[/]" if board[i + 1] != " " else "[yellow]_[/]",
            f"[green]{board[i+2]}[/]" if board[i + 2] != " " else "[yellow]_[/]",
        )
    console.print(table)


# всего существует 8 расположений, при которых объявляется победа
def check_winner():
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return board[combo[0]]
    return None


# основная функция
def game():
    current_player = "X"
    for _ in range(9):
        print_board()
        move = int(input(f"Игрок {current_player}, выберите клетку (1-9): ")) - 1
        if board[move] == " ":
            board[move] = current_player
            winner = check_winner()
            if winner:
                print_board()
                console.print(f"[bold green]Игрок {winner} победил![/]")
                return
            current_player = "O" if current_player == "X" else "X"
        else:
            console.print("[bold red]Клетка занята, выберите другую![/]")
    console.print("[bold yellow]Ничья![/]")


game()
