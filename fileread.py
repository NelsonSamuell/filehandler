def handle_file():
    filename = input("Enter the file to read: ")

    try:
        with open(filename, "r") as file1:
            content = file1.read()

        modified_content = content.upper()

        new_filename = "modified_" + filename
        with open(new_filename, "w") as file2:
            file2.write(modified_content)

        print(f"Success! Modified file is saved as '{new_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
   
handle_file()
