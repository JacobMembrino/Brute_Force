import PyPDF2
import string

characters = list(string.ascii_letters)
passwords = []
for char1 in characters:
    for char2 in characters:
        for char3 in characters:
            for char4 in characters:
                for char5 in characters:
                    passwords.append(char1 + char2 + char3 + char4 + char5)

FILE_PATH = 'secret.pdf'
for PASSWORD in passwords:
    try:
        with open(FILE_PATH, mode='rb') as f:        
            reader = PyPDF2.PdfFileReader(f)
            reader.decrypt(PASSWORD)
            print(f"Number of page: {reader.getNumPages()}")
            print(PASSWORD)
    except:
        continue
