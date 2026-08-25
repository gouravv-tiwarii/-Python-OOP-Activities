def run_command(command):
    match command.split():
        case ["go", direction]:
            print(f"Walking {direction}")
        case ["take", item]:
            print(f"Picking up {item}")
        case ["quit" | "exit"]:
            print("Goodbye!")
        case _:
            print("Unknown command")


if __name__ == "__main__":
    run_command("go north")
    run_command("take sword")
    run_command("exit")