import PyPDF2

def batch_pdf_to_text_files(pdf_filename, output_folder, pages_per_batch=10):
    with open(pdf_filename, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        total_pages = len(reader.pages)
        for start_page in range(0, total_pages, pages_per_batch):
            end_page = min(start_page + pages_per_batch, total_pages)
            batch_text = ""

            for page_num in range(start_page, end_page):
                page = reader.pages[page_num]
                batch_text += page.extract_text()

            batch_number = start_page // pages_per_batch + 1
            with open(f"{output_folder}/batch_{batch_number}.txt", "w", encoding="utf-8") as output_file:
                output_file.write(batch_text)

def pdf_to_text_files(pdf_filename, output_folder):
    with open(pdf_filename, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text = page.extract_text()
            with open(f"{output_folder}/page_{page_num + 1}.txt", "w", encoding="utf-8") as output_file:
                output_file.write(text)

# Usage
batch_pdf_to_text_files("Bravura-Security-Fabric-Documentation.pdf", ".")
