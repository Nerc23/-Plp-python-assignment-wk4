def file_read_and_write(input_filename="input.txt", output_filename="output.txt"):
    """
    Reads a file, modifies its content, and writes it to a new file.

    Args:
        input_filename (str): The name of the input file.
        output_filename (str): The name of the output file.
    """
    try:
        with open(input_filename, 'r') as infile:
            lines = infile.readlines()

        modified_lines = [line.upper() for line in lines]  # Example modification: convert to uppercase

        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_lines)

        print(f"Successfully read '{input_filename}', modified it, and wrote to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: Input file '{input_filename}' not found.")
    except Exception as e:
        print(f"An error occurred during file processing: {e}")

def handle_file_errors():
    """
    Asks the user for a filename and handles potential file errors.
    """
    while True:
        filename = input("Enter the filename to read: ")
        try:
            with open(filename, 'r') as file:
                content = file.read()
                print(f"Successfully read the file '{filename}'. First 50 characters:\n{content[:50]}...") # Print a snippet
            break  # Exit the loop if the file is read successfully
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found. Please try again.")
        except PermissionError:
            print(f"Error: Permission denied to read file '{filename}'. Please check file permissions.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")

if __name__ == "__main__":
    # Create a sample input file for the first part
    with open("input.txt", "w") as f:
        f.write("This is the first line.\n")
        f.write("This is the second line with some text.\n")
        f.write("And this is the third line.\n")

    # Run the file read and write challenge
    file_read_and_write()

    print("\n--- Error Handling Lab ---")
    # Run the error handling lab
    handle_file_errors()
