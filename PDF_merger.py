# Import the tkinter library for creating the GUI
# Import the filedialog module for opening/saving files
# Import the PyPDF2 library for working with PDF files
import tkinter as tk
from tkinter import filedialog
import PyPDF2



# Create the main application window
app = tk.Tk()
app.title("PDF-Merger")
app.configure(bg='#FFFFFF')  
app.geometry("400x200")

print("PDF-Merger window opened!")
print("Please select several PDF files [Windows: leftMouseClick + CTRL / Mac: leftMouseClick + command]")

# Function to merge PDF files
def merge_pdfs():
    file_paths = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
     # Check if PDF files were selected
    if file_paths:
         # Create a PdfMerger object to merge the selected PDF files
        merged_pdf = PyPDF2.PdfMerger()
         # Loop through the selected PDF files and append them to the merger
        for file_path in file_paths:
            merged_pdf.append(file_path)

        # Open a file dialog to select the location and name for the merged PDF
        output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])

        # Check if an output file was chosen
        if output_path:
            merged_pdf.write(output_path)
            merged_pdf.close()
            status_label.config(text=f"Merged {len(file_paths)} PDFs into {output_path}")
        else:
            status_label.config(text="Merge canceled.")
    else:
        status_label.config(text="No PDF files selected for merging.")



# Create a "Merge PDFs" button and associate it with the merge_pdfs function
merge_button = tk.Button(app, text="Merge PDFs", command=merge_pdfs, bg="#FF5733")
merge_button.pack(pady=10) 

# Create a status label to display messages to the user
status_label = tk.Label(app, text="", wraplength=300)
status_label.pack(side="bottom")


app.mainloop()



