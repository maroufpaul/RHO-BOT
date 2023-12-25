import re

def preprocess_text(text):
    # Remove unnecessary characters
    text = re.sub(r'Some regex for characters to remove', '', text)

    # Replace ligatures like 'ﬂ' with 'fl'
    text = text.replace('ﬂ', 'fl').replace('ﬁ', 'fi')  # Add other ligatures as needed

    # Normalize whitespace
    text = ' '.join(text.split())

    # Convert to lowercase
    text = text.lower()

    return text

# Load your extracted text
with open('F:/RHO-BOT/extracted_text.txt', 'r', encoding='utf-8') as file:
    extracted_text = file.read()

# Preprocess the text
preprocessed_text = preprocess_text(extracted_text)

# Optionally, save the preprocessed text to a new file
with open('F:/RHO-BOT/preprocessed_text.txt', 'w', encoding='utf-8') as file:
    file.write(preprocessed_text)

