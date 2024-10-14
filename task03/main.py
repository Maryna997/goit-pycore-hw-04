import sys
from pathlib import Path
from colorama import init, Fore

init(autoreset=True)

def show_directory_structure(directory_path, indent=0):
    path = Path(directory_path)

    if not path.exists() or not path.is_dir():
        print(Fore.RED + f"Шлях '{directory_path}' не існує або не є директорією.")
        return
    
    print(" " * indent + Fore.BLUE + f"📁 {path.name}/")

    for item in path.iterdir():
        if item.is_dir():
            print(" " * (indent + 2) + Fore.CYAN + f"📁 {item.name}/")
            show_directory_structure(item, indent + 4)
        elif item.is_file():
            print(" " * (indent + 2) + Fore.GREEN + f"📄 {item.name}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.RED + "Потрібно вказати шлях до директорії.")
        sys.exit(1)

    directory_path = sys.argv[1]

    show_directory_structure(directory_path)  
     