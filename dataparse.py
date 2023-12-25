import PyPDF2

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)  # Use PdfReader instead of PdfFileReader
        text = ''
        for page in reader.pages:
            text += page.extract_text() + '\n'  # Use extract_text() method
    return text

def save_text_to_file(text, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)

# Specify the path to your PDF file
pdf_path = 'F:/RHO-BOT/Rhode_College_Catalog_-_2023-24-compressed.pdf'

# Extract text from the PDF
pdf_text = extract_text_from_pdf(pdf_path)

# Save the extracted text to a file
output_file_path = 'F:/RHO-BOT/extracted_text.txt'
save_text_to_file(pdf_text, output_file_path)

print(f"Text extracted and saved to {output_file_path}")

