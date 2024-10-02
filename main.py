from pypdf import PdfWriter

from sys import exit

from tkinter import Tk
from tkinter.filedialog import askopenfilenames, asksaveasfile

Tk().withdraw()
filepaths = askopenfilenames(
    title='Choose pdf files to Combine',
    filetypes=[('PDF File', '*.pdf')],
    initialdir='/Users/vova' # replace with users wanted default initial directory, or keep empty (initialdir=None)
)

if (len(filepaths) == 0): exit(1) # guard clause if closed

pdf_writer = PdfWriter()

for path in filepaths:
    with open(path, 'rb') as file_data:
        pdf_writer.append(file_data)

path_to_save_pdf = asksaveasfile(
    title='Save combined PDF to location',
    initialfile = 'combined_files.pdf', 
    defaultextension='.pdf', 
    filetypes=[('PDF File', '*.pdf')], 
    initialdir='/Users/vova/Downloads' # replace with users wanted default initial directory, or keep empty (initialdir=None)
)

if (path_to_save_pdf == None): exit(1) # guard clause if closed

path_to_save_pdf = path_to_save_pdf.name
with open(path_to_save_pdf, 'wb') as combined_file:
    pdf_writer.write(combined_file)

# for system output of success
print(f"\033[32m\u001b[1m-----MERGE SUCCESS-----\033[0m\n"
      f"\u001b[1mFiles merged (order): \033[0m{str([file.split('/')[-1] for file in filepaths])[1:-1]}\n"
      f"\u001b[1mMerged file name: \033[0m{path_to_save_pdf.split('/')[-1]}\n"
      f"\u001b[1mLocation: \033[0m{path_to_save_pdf}\n"
      f"\033[32m\u001b[1m-----------------------")