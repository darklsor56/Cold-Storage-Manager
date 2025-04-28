"""CLI for Cold Storage Manager."""
import sys
from cold_storage_manager import scanner

def main():
    """The CLI startup."""
    print("Cold Storage Manager CLI Starting...")
    # Ensure there is more than 2 args entered
    if len(sys.argv) < 2:
        print("Usage: coldstore scan <directory> <days>")
        sys.exit(1)
    command = sys.argv[1]
    if comand == "scan":
        #Ensure the command is ran as coldstore scan <directory> <days>.
        if len(sys.argv) != 4:
            print("Usage: coldstore scan <directory> <days>")
            sys.exit(1)
        path = sys.argv[2]
        #Make sure days is an integer
        try:
            days = init(sys.argv[3])
        except:
            print("Error: <days> must be an integer.")
            sys.exit(1)
        # Call the scanner function and print results
        unused_files = scanner.get_unused_files(path, days)
        for file in unused_files:
            print(file)
    else:
        print(f"Unkown command: {command}")
        print("Available commands: scan")
        sys.exit(1)
if __name__ == "__main__":
    main()
