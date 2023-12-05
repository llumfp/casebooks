import subprocess
import sys
import re
from miniproto1 import *

def run_clips_with_commands(input_file,output_file):
    # Iniciar el proceso CLIPS.
    with subprocess.Popen(["C:\Program Files\CLIPS 6.4.1\CLIPSDOS.exe"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True) as proc:
        
        # Leer comandos adicionales desde otro archivo y ejecutarlos en CLIPS.
        print('Execucio clips...')
        with open(input_file, 'r') as f:
            additional_commands = f.read()
            proc.stdin.write(additional_commands)
        
        # Capturar la salida.
        print('Capturando salida...')
        out, err = proc.communicate()
        # Imprimir la salida.
        with open(output_file,'w') as f:
            f.write(out)
        if err:
            print("Error:", err)


# Function to parse the book entries and create instances of the Book class

def create_book_instances(file_path):
    # Read the file content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Pattern to capture book details
    pattern = r'--------------- LLIBRE ---------------\n(.*?)\n\n'
    book_entries = re.findall(pattern, content, re.DOTALL)

    # List to store Book instances
    books = []
    nivells = []


    # Iterate over each book entry and create Book instances
    for entry in book_entries:
        # Parsing the book details
        first = re.findall(r'Nivell: \w', entry)
        nivell = (eval(first[0][-1]))
        details = re.findall(r'(\w+) "(.*?)"', entry)
        details_dict = {key: value for key, value in details}


        # Creating the Book instance
        book = Book(
            title=details_dict.get('title', 'Unknown'),
            isactual=details_dict.get('actual', 'false') == 'true',
            length=details_dict.get('length', 'Unknown'),
            public=details_dict.get('public', 'Unknown') == 'adult',
            cover=details_dict.get('cover', 'Unknown'),
            genre=details_dict.get('main_genre', 'Unknown'),
            rating=float(details_dict.get('rating', 0)),
            subgenre=details_dict.get('has_subgenre', None),
            goal=details_dict.get('goal', ''),
            illustrated=details_dict.get('illustrated', 'FALSE') == 'true',
            theme=details_dict.get('theme', ''),
            bestseller=details_dict.get('bestseller', 'FALSE') == 'true',
            triggerw=details_dict.get('triggerw', None)
        )

        books.append(book)
        nivells.append(nivell)

    return books, np.mean(nivells)

# Note: The Author class is not defined here. I'm assuming it's a simple class with basic attributes like name, nationality, etc.
# If the Author class is more complex or requires specific handling, additional code would be needed.
