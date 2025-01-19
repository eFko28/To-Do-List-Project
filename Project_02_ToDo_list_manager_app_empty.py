# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram

import os
from datetime import datetime


# Cesta k souboru s úkoly
TASKS_FILE = "data/todo_tasks.txt"


def load_tasks():
    """Načte úkoly ze souboru do seznamu slovníků.
    Returns:
        list: seznam úkolů, kde každý úkol je slovník s vlastnostmi.
    """
    tasks = []

    path = "./data/todo_tasks.txt"
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()

        for line in lines:
            parts = line.strip().split(";")  # Rozdelit řádek na list

            task = {
                "id": int(parts[0]),
                "name": parts[1],
                "priority": parts[2],
                "deadline": parts[3],
                "completed": parts[4],
            }

            tasks.append(task)

    return tasks


def save_tasks(tasks):
    """Uloží úkoly do souboru.
    Args:
        tasks: list, seznam úkolů ve formě slovníků.
    """
    path = "./data/todo_tasks.txt"
    with open(path, "w", encoding="utf-8") as file:
        for task in tasks:
            line = f"{task['id']};{task['name']};{task['priority']};{task['deadline']};{task['completed']}"
            file.write(f"{line}\n")



def add_task(tasks):
    """Přidá nový úkol na seznam.

    Args:
        tasks (list): Aktuální seznam úkolů.

    Returns:
        list: Aktualizovaný seznam úkolů.
    """
    name = input("Zadejte název úkolu: ")

    while True:
        priority = input("Zadejte prioritu (Nízká, Střední, Vysoká): ").strip().capitalize()
        if priority == "":
            priority = "Střední"
            break
        if priority in ["Nízká", "Střední", "Vysoká", "Nizka", "Stredni", "Vysoka"]:
            if priority == "Nizka":
                priority = "Nízká"
            if priority == "Stredni":
                priority = "Střední"
            if priority == "Vysoka":
                priority = "Vysoká"
            break
        else:
            print("Chyba: Zadejte platnou prioritu (Nízká, Střední, Vysoká).")

    while True:
        deadline = input("Zadejte termín splnění (YYYY-MM-DD, volitelně): ").strip()
        current_time = datetime.now()
        current_day = current_time.strftime("%Y-%m-%d")    #získání dnešního data
        if deadline == "":
            deadline = "----------"
            break 
        try:
            datetime.strptime(deadline, "%Y-%m-%d")     #ověření nejen správnosti formátu, ale i existence daného data
            if deadline >= current_day:  #datum musi byt v budoucnosti
                break
            print("Datum musí být dněšní nebo budoucí.")
        except ValueError:
            print("Chyba: Termín musí být ve formátu YYYY-MM-DD (např. 2001-01-01) a platný.")

    highest_id = 0
    for task in tasks:
        if task["id"] > highest_id:
            highest_id = task["id"]
    new_id = highest_id + 1

    task = {
        "id": new_id,
        "name": name,
        "priority": priority,
        "deadline": deadline,
        "completed": "Ne",
    }

    tasks.append(task)
    return tasks



def list_tasks(tasks, filter_by=None):
    """Vypíše úkoly podle zadaného filtru.
    Args:
        tasks: list, seznam úkolů.
        filter_by: dict, filtr pro zobrazení úkolů (např. stav, priorita).
    """
    print("\nID | Úkol                | Priorita | Termín      | Stav")
    print("-----------------------------------------------------------")
    for task in tasks:
        if filter_by:
            if filter_by.get("priority") and task["priority"] != filter_by["priority"]:
                continue
            if (
                filter_by.get("completed")
                and task["completed"] != filter_by["completed"]
            ):
                continue
        print(
            f"{task['id']}  | {task['name'][:20]:<20} | {task['priority']:<7} | {task['deadline'] or '---':<10} | {task['completed']}"
        )
    print()


def remove_task(tasks):
    """Odstraní úkol na základě ID.
    Args:
        tasks: list, aktuální seznam úkolů.
    Returns:
        list, aktualizovaný seznam úkolů.
    """
    id = int(input("Zadejte ID úkolu, který chcete odstranit: "))

    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)
            return tasks

    print("Úkol nebyl nalezen.")
    return tasks


def complete_task(tasks):
    """Označí úkol jako dokončený.
    Args:
        tasks: list, aktuální seznam úkolů.
    """
    id = int(input("Zadejte ID úkolu, který chcete splnit: "))

    for task in tasks:
        if task["id"] == id:
            task["completed"] = "Ano"
            return tasks

    print("Úkol nebyl nalezen.")
    return tasks







def edit_task(tasks):
    """Umožní uživateli upravit název, prioritu nebo termín úkolu.
    Args:
        tasks: list, aktuální seznam úkolů.
    """
    id = int(input("Zadejte ID úkolu, který chcete upravit: "))

    for task in tasks:
        if task["id"] == id:
            name = input("Zadejte název úkolu: ")

            while True:
                priority = input("Zadejte prioritu (Nízká, Střední, Vysoká): ").strip().capitalize()
                if priority == "":
                    priority = "Střední"
                    break
            if priority in ["Nízká", "Střední", "Vysoká", "Nizka", "Stredni", "Vysoka"]:
                if priority == "Nizka":
                    priority = "Nízká"
                if priority == "Stredni":
                    priority = "Střední"
                if priority == "Vysoka":
                    priority = "Vysoká"
                break
            else:
                print("Chyba: Zadejte platnou prioritu (Nízká, Střední, Vysoká).")

            while True:
                deadline = input("Zadejte termín splnění (YYYY-MM-DD, volitelně): ").strip()
                current_time = datetime.now()
                current_day = current_time.strftime("%Y-%m-%d")    #získání dnešního data
                if deadline == "":
                    deadline = "----------"
                    break 
                try:
                    datetime.strptime(deadline, "%Y-%m-%d")     #ověření nejen správnosti formátu, ale i existence daného data
                    if deadline >= current_day:  #datum musi byt v budoucnosti
                        break
                    print("Datum musí být dněšní nebo budoucí.")
                except ValueError:
                    print("Chyba: Termín musí být ve formátu YYYY-MM-DD (např. 2001-01-01) a platný.")

            task["name"] = name
            task["priority"] = priority
            task["deadline"] = deadline
            task["completed"] = "Ne"

            print(f"Úkol '{task['name']}' byl upraven.")
            return tasks

    print("Úkol nebyl nalezen.")
    return tasks



def main(command, tasks):
    """Řídí zpracování jednotlivých příkazů.
    Args:
        command: str, zadaný příkaz od uživatele.
        tasks: list, seznam úkolů.
    Returns:
        list, aktualizovaný seznam úkolů.
    """
    if command == "add":
        tasks = add_task(tasks)
    elif command == "list":
        filter_choice = input("Chcete filtrovat? (priority/stav/ne): ").strip().lower()
        if filter_choice == "priority":
            priority = input("Zadejte prioritu (Nízká, Střední, Vysoká): ")
            list_tasks(tasks, filter_by={"priority": priority})
        elif filter_choice == "stav":
            status = input("Zadejte stav (Ano/Ne): ")
            list_tasks(tasks, filter_by={"completed": status})
        else:
            list_tasks(tasks)
    elif command == "remove":
        tasks = remove_task(tasks)
    elif command == "complete":
        tasks = complete_task(tasks)
    elif command == "edit":
        tasks = edit_task(tasks)
    elif command == "save":
        save_tasks(tasks)
        print("Úkoly byly uloženy.")
    else:
        print("Neznámý příkaz, prosím zkuste to znovu.")

    return tasks


### Spuštění programu - MAIN

if __name__ == "__main__":
    os.system("clear" if os.name == "posix" else "cls")

    # Načtení úkolů ze souboru
    tasks = load_tasks()

    print("\n=== ToDo List Manager - aktuální seznam úkolů ===")
    list_tasks(tasks)

    while True:
        # Základní menu
        print("\n=== ToDo List Manager ===")
        print("Příkazy: 'add', 'list', 'remove', 'complete', 'edit', 'save', 'exit'")
        command = input("Zadejte příkaz: ").strip().lower()

        if command == "exit":
            # Automatické uložení úkolů při ukončení
            save_tasks(tasks)
            print("Úkoly byly uloženy. Ukončuji aplikaci.")
            break
        else:
            tasks = main(command, tasks)


