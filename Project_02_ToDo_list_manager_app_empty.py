# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
Project_02_ToDo_list_manager_app_empty.py

Vytvořte terminálovou aplikaci, která bude sloužit jako ToDo list. 
Aplikace umožní uživateli spravovat úkoly, ukládat je do souboru a načítat při startu aplikace. 

## Funkcionalita aplikace
* Přidání úkolu - aplikace umožní uživateli přidat nový úkol. 
  Každý úkol bude obsahovat následující vlastnosti:
        Název úkolu (povinný)
        Priorita úkolu (nízká, střední, vysoká), výchozí je střední.
        Termín splnění úkolu ve formátu YYYY-MM-DD (volitelné, může být prázdné).
        Status úkolu (hotovo/nehotovo), který se bude standardně nastavovat na "nehotovo" při vytvoření nového úkolu.
* Zobrazení seznamu úkolů - uživatel může zobrazit seznam všech úkolů. 
  Seznam bude obsahovat všechny úkoly s jejich vlastnostmi. Uživatel může také filtrovat úkoly podle:
        Priorit (zobrazí jen úkoly s konkrétní prioritou)
        Stavu úkolu (hotovo/nehotovo)
        Termínu splnění (úkoly s blížícím se termínem)
* Odstranění úkolu - aplikace umožní odstranit úkol ze seznamu podle ID nebo názvu.
* Označení úkolu jako dokončeného - uživatel může označit libovolný úkol jako "hotovo". 
  Tento úkol bude v seznamu označen jako dokončený, ale zůstane uložený pro případné další zobrazení.
* Editace úkolu - uživatel může změnit vlastnosti již existujícího úkolu. 
  Bude možné upravit název, prioritu, termín nebo status úkolu.
* Uložení a načtení úkolů ze souboru - při ukončení aplikace se všechny úkoly uloží do souboru 
  ve formátu CSV nebo JSON. Aplikace při spuštění tento soubor načte a pokračuje v práci s dříve uloženými úkoly.

## Formát souboru s úkoly
Seznam úkolů bude uložen v textovém souboru ve složce data, který bude mít následující strukturu:
    Každý úkol bude na jednom řádku a jednotlivé vlastnosti budou odděleny středníkem.
    Pokud nebude zadán termín, zůstane pole prázdné.

## Ukázkový soubor todo_tasks.txt:
        1;Nakoupit potraviny;Vysoká;2024-10-15;Ne
        2;Dokončit projekt;Střední;;Ne
        3;Udělat domácí úkol;Nízká;2024-10-20;Ne
        4;Zavolat babičce;Střední;;Ano

## Příkazy aplikace:
* add
  Přidání nového úkolu. Aplikace požádá uživatele o název úkolu, prioritu a termín. 
  Pokud uživatel nezadá prioritu, nastaví se střední. Termín je volitelný.
* list
  Zobrazení seznamu úkolů. Uživatel může zadat parametr pro filtrování podle priority, stavu nebo termínu.
* remove
  Odstranění úkolu. Uživatel zadá ID nebo název úkolu, který chce odstranit.
* complete
  Označení úkolu jako hotového. Uživatel zadá ID nebo název úkolu, který chce označit jako hotový.
* edit
  Umožní uživateli upravit název, prioritu, termín nebo status existujícího úkolu.
* save
  Ruční uložení změn do souboru todo_tasks.txt.
* exit
  Automatické uložení všech změn do souboru a ukončení programu.

## Struktura souborů:
* main.py
  Hlavní soubor aplikace, který bude obsahovat logiku pro zpracování příkazů.
* data/todo_tasks.txt
  Soubor s úkoly, který se bude načítat při startu aplikace a ukládat při ukončení.

## Ukázkový výpis aplikace:
        === ToDo List Manager ===
        Nápověda: použijte příkazy 'add', 'list', 'remove', 'complete', 'edit', 'save', 'exit' pro práci s úkoly.

        > add
        Zadejte název úkolu: Nakoupit potraviny
        Zadejte prioritu (Nízká, Střední, Vysoká): Vysoká
        Zadejte termín splnění (YYYY-MM-DD, volitelně): 2024-10-15
        Úkol byl přidán!

        > list
        ID | Úkol                | Priorita | Termín      | Stav
        -----------------------------------------------------------
        1  | Nakoupit potraviny   | Vysoká   | 2024-10-15  | Ne
        2  | Dokončit projekt     | Střední  |             | Ne

        > complete 1
        Úkol "Nakoupit potraviny" byl označen jako dokončený.

        > list
        ID | Úkol                | Priorita | Termín      | Stav
        -----------------------------------------------------------
        1  | Nakoupit potraviny   | Vysoká   | 2024-10-15  | Ano
        2  | Dokončit projekt     | Střední  |             | Ne

        > remove 2
        Úkol "Dokončit projekt" byl odstraněn.

        > save
        Úkoly byly uloženy do souboru.

        > exit
        Úkoly byly uloženy. Ukončuji aplikaci.

## Detailní popis jednotlivých funkcí:
* load_tasks()
  Funkce pro načtení všech úkolů z textového souboru při spuštění aplikace. 
  Pokud soubor neexistuje, vytvoří se prázdná seznamová struktura.
* save_tasks()
  Uloží aktuální stav seznamu úkolů do souboru. Při ukončení aplikace dojde k automatickému uložení, 
  ale uživatel může zadat příkaz save pro ruční uložení kdykoliv.
* add_task()
  Přidá nový úkol. Uživatel zadá název, prioritu a termín. Pokud není zadaný termín, pole termínu 
  zůstane prázdné. Každý úkol je přiřazen ID, které je automaticky generováno.
* list_tasks()
  Zobrazí všechny úkoly ve formě tabulky. Uživatel může filtrovat úkoly podle priority, 
  termínu nebo statusu (hotovo/nehotovo).
* remove_task()
  Umožňuje odstranit úkol podle ID nebo názvu.
* complete_task()
  Označí úkol jako dokončený. Uživatel zadá ID nebo název úkolu.
* edit_task()
  Umožňuje uživateli upravit název, prioritu, termín nebo status existujícího úkolu.

## Závěrečné poznámky:
Všechny změny se ukládají do souboru todo_tasks.txt, který je přístupný v podadresáři data.
Po spuštění aplikace se úkoly automaticky načtou, takže uživatel může pokračovat tam, kde skončil.
Data jsou ukládána ve formátu, který umožňuje jednoduchou editaci i mimo aplikaci (např. v textovém editoru).

"""


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
            break
        if priority in ["Nízká", "Střední", "Vysoká", "Nizka", "Stredni", "Vysoka"]:
            break
        else:
            print("Chyba: Zadejte platnou prioritu (Nízká, Střední, Vysoká).")

    while True:
        deadline = input("Zadejte termín splnění (YYYY-MM-DD, volitelně): ").strip()
        if deadline == "":
            break 
        try:
            datetime.strptime(deadline, "%Y-%m-%d")
            break
        except ValueError:
            print("Chyba: Termín musí být ve formátu YYYY-MM-DD (např. 2001-01-01).")

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
            priority = input("Zadejte prioritu (Nízká, Střední, Vysoká): ")
            deadline = input("Zadejte termín splnění (YYYY-MM-DD, volitelně): ")

            task["name"] = name
            task["priority"] = priority if deadline != "" else "Střední"
            task["deadline"] = deadline if deadline else ""
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


