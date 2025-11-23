notes = []

try:
    with open("notes.txt", "r", encoding="utf-8") as f:
        notes = f.read().splitlines()
except FileNotFoundError:
    notes = []

def show_menu():
    print("\n--- Personal Notes Saver ---")
    print("1. Add note")
    print("2. View notes")
    print("3. Delete note")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Choose (1-4): ").strip()

    if choice == "1":
        note = input("Type note: ").strip()
        if note:
            notes.append(note)
            print("Note saved.")
        else:
            print("Empty note not saved.")

    elif choice == "2":
        if not notes:
            print("No notes found.")
        else:
            print("\nSaved notes:")
            for i, n in enumerate(notes, start=1):
                print(f"{i}. {n}")

    elif choice == "3":
        try:
            idx = int(input("Enter note number to delete: ").strip())
            if 1 <= idx <= len(notes):
                removed = notes.pop(idx-1)
                print("Deleted:", removed)
            else:
                print("Invalid number.")
        except ValueError:
            print("Enter a valid number.")

    elif choice == "4":
        break
    else:
        print("Choose a valid option (1-4).")

with open("notes.txt", "w", encoding="utf-8") as f:
    for n in notes:
        f.write(n + "\n")

print("Goodbye!")