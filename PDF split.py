import PyPDF2
from tkinter import Tk, filedialog
import os

def split_pdf(input_pdf, output_folder):
    pdf = PyPDF2.PdfReader(input_pdf)
    for i in range(len(pdf.pages)):
        pdf_writer = PyPDF2.PdfWriter()
        pdf_writer.add_page(pdf.pages[i])

        output_filename = os.path.join(output_folder, f'page_{i+1}.pdf')
        with open(output_filename, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

def get_file_and_folder():
    root = Tk()
    root.withdraw()  # Cache la fenêtre principale de Tkinter
    input_pdf = filedialog.askopenfilename(title="Sélectionnez le fichier PDF à diviser", filetypes=[("PDF Files", "*.pdf")])
    output_folder = filedialog.askdirectory(title="Sélectionnez le dossier de sortie")
    return input_pdf, output_folder

if __name__ == "__main__":
    input_pdf, output_folder = get_file_and_folder()
    if input_pdf and output_folder:
        split_pdf(input_pdf, output_folder)
        print("PDF divisé avec succès!")
    else:
        print("Sélection du fichier ou du dossier annulée.")