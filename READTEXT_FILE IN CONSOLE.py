#TAKES THE TEXT FILE AND DISPLAY THE CONTENT OF THE FILE IN CONSOLE
def read_text_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
read_text_file('SYED.txt')