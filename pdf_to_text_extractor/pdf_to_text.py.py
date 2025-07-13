from PyPDF2 import PdfReader

try:
    reader = PdfReader("example.pdf") 
    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted

    with open("new_file.txt", "w", encoding="utf-8") as file:
        file.write(text)

    with open("new_file.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print("\nExtracted Content:\n")
        print(content)

except FileNotFoundError:
    print("Error: PDF file not found. Please check the file name or path.")
except PermissionError:
    print("Error: Permission denied while accessing file.")
except Exception as e:
    print(f"Unexpected error occurred: {e}")
