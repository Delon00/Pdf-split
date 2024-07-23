# PDF Splitter Script

Ce script Python permet de diviser un fichier PDF en plusieurs fichiers PDF, chacun contenant une page du document original.

## Prérequis

- Python 3.x
- Bibliothèque PyPDF2

## Installation

1. **Installer Python 3.x** : Vous pouvez télécharger Python à partir du site officiel : [Python.org](https://www.python.org/downloads/)

2. **Installer PyPDF2** : Exécutez la commande suivante pour installer la bibliothèque PyPDF2 :

    ```sh
    pip install PyPDF2
    ```

## Utilisation

### Script

Copiez le script suivant dans un fichier Python (par exemple, `split_pdf.py`) :

```python
import PyPDF2
import os

def split_pdf(input_pdf, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    pdf = PyPDF2.PdfReader(input_pdf)
    for i in range(len(pdf.pages)):
        pdf_writer = PyPDF2.PdfWriter()
        pdf_writer.add_page(pdf.pages[i])

        output_filename = os.path.join(output_folder, f'page_{i+1}.pdf')
        with open(output_filename, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

if __name__ == "__main__":
    input_pdf = input("Entrez le chemin du fichier PDF à diviser : ")
    output_folder = input("Entrez le dossier où les pages doivent être enregistrées : ")
    split_pdf(input_pdf, output_folder)
    print(f"Les pages du fichier PDF ont été enregistrées dans le dossier {output_folder}")
```

## Instructions
Exécuter le script :
```sh
python split_pdf.py
```
## Auteur
Ce script a été créé par Moi Delon.