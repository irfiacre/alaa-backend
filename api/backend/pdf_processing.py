from io import BytesIO
import pypdf
import requests

# To try to improve it using docling - https://www.docling.ai/
def extract_pdf_text(file_url: str):
    """
    Reads the content of a document, and returns the text. 

    Args:
        file_url: The URL to the file.
    """
    try:
        url_response = requests.get(file_url)        
        pdf_file = BytesIO(url_response.content)
        reader = pypdf.PdfReader(pdf_file)
        full_text = ""
        for page in reader.pages:
            full_text += page.extract_text() + ", "
        return full_text
    except Exception as e:
        print("---- Error Parsing PDF file:", e)
        return ""
