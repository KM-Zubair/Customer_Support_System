from langchain.document_loaders import PDFLoader, YouTubeLoader, URLLLoader

def load_documents():
    # Load PDF document
    pdf_loader = PDFLoader("https://www.sfbu.edu/sites/default/files/Documents/sfbu-2024-2025-university-catalog-8-20-2024.pdf")
    pdf_documents = pdf_loader.load()

    # Load YouTube transcript
    youtube_loader = YouTubeLoader("https://www.youtube.com/watch?v=kuZNIvdwnMc")
    youtube_documents = youtube_loader.load()

    # Load URL
    url_loader = URLLLoader("https://www.sfbu.edu/student-health-insurance")
    url_documents = url_loader.load()

    # Combine all loaded documents
    return pdf_documents + youtube_documents + url_documents
