import os
from tkinter import Tk, StringVar, Label, Button, Entry, filedialog, messagebox, PhotoImage, LEFT
from tkinter import ttk

from PyPDF2 import PdfReader, PdfWriter

# -----------------------Extract--------------------------#

def extract_pages(input_pdf, start_page, end_page, save_pdf):
    try:
        reader = PdfReader(input_pdf)
        writer = PdfWriter()

        for page_num in range(start_page - 1, end_page):
            writer.add_page(reader.pages[page_num])

        base_name = os.path.splitext(save_pdf)[0]
        output_pdf = f"{base_name}_v1.pdf"

        with open(output_pdf, "wb") as output_file:
            writer.write(output_file)

        messagebox.showinfo("Success", f"Pages {start_page}-{end_page} extracted successfully to {output_pdf}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def select_file(pdf_file):
    file_path = filedialog.askopenfilename(title="Select PDF file", filetypes=[("PDF files", "*.pdf")])
    if file_path:
        pdf_file.delete(0, "end")
        pdf_file.insert(0, file_path)

def save_file(output_pdf):
    file_path1 = filedialog.asksaveasfilename(title="Save PDF file", filetypes=[("PDF files", "*.pdf")])
    if file_path1:
        output_pdf.delete(0, "end")
        output_pdf.insert(0, file_path1)

def run_extraction():
    pdf_file = pdf_file_entry.get()
    pdf_file1 = pdf_file_entry1.get()

    try:
        start_page = int(start_page_entry.get())
        end_page = int(end_page_entry.get())

        if not pdf_file:
            messagebox.showwarning("Input Error", "Please select a PDF file.")
        elif start_page < 1 or end_page < start_page:
            messagebox.showwarning("Input Error", "Invalid page range.")
        else:
            save_pdf = pdf_file1 if pdf_file1 else pdf_file
            extract_pages(pdf_file, start_page, end_page, save_pdf)
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter valid page numbers.")

#--------------------------Merge----------------------------#

def toggle_entry(option, merge_start_range, merge_end_range):
    if option.get() == "Range":
        merge_start_range.config(state="normal", bg="#8a8a8a")
        merge_end_range.config(state="normal", bg="#8a8a8a")
    else:
        merge_start_range.config(state="disabled", bg="#000000")
        merge_end_range.config(state="disabled", bg="#000000")

def merge_pages(input_pdf, start_page, end_page, input_pdf1, start_page1, end_page1, save_pdf):
    try:
        reader = PdfReader(input_pdf)
        reader1 = PdfReader(input_pdf1)
        writer = PdfWriter()

        for page_num in range(start_page - 1, end_page):
            writer.add_page(reader.pages[page_num])
        
        for page_num in range(start_page1 - 1, end_page1):
            writer.add_page(reader1.pages[page_num])

        base_name = os.path.splitext(save_pdf)[0]
        output_pdf = f"{base_name}_v1.pdf"

        with open(output_pdf, "wb") as output_file:
            writer.write(output_file)

        messagebox.showinfo("Success", f"Merged PDF is saved at {output_pdf}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def run_merge():
    merge_pdf_file1 = merge_file_entry1.get()  
    merge_pdf_file2 = merge_file_entry2.get()  
    output_pdf_file = output_pdf_file_entry.get()  

    try:
        start_page = int(merge_start_range1.get())
        end_page = int(merge_end_range1.get())

        start_page1 = int(merge_start_range2.get())
        end_page1 = int(merge_end_range2.get())

        if not merge_pdf_file1 or not merge_pdf_file2:
            messagebox.showwarning("Input Error", "Please select 2 PDF files.")
        elif start_page < 1 or end_page < start_page or start_page1 < 1 or end_page1 < start_page1 :
            messagebox.showwarning("Input Error", "Invalid page range.")
        else:
            save_pdf = output_pdf_file 
            merge_pages(merge_pdf_file1, start_page, end_page,merge_pdf_file2, start_page1, end_page1, save_pdf)
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter valid page numbers.")

#-------------------------------Encrypt----------------------------#

def show():
    pass_entry.configure(show='')
    check.config(text='HIDE', command=hide)

def hide():
    pass_entry.configure(show='*')
    check.config(text='SHOW', command=show)

def encrypt(input_pdf, password, protected_pdf):
    try:
        reader = PdfReader(input_pdf)
        writer = PdfWriter()
        writer.append_pages_from_reader(reader)
        writer.encrypt(password)
        
        base_name = os.path.splitext(protected_pdf)[0]
        output_pdf = f"{base_name}.pdf"

        with open(output_pdf, "wb") as output_file:
            writer.write(output_file)

        messagebox.showinfo("Success", f"Successfully saved protected PDF to {output_pdf}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def run_encryption():
    unsafe_pdf_file = en_pdf_entry.get()
    safe_pdf_file1 = en_output_pdf_file_entry.get()

    try:
        encryptor = pass_entry.get()

        if not unsafe_pdf_file:
            messagebox.showwarning("Input Error", "Please select a PDF file.")
        else:
            save_pdf = safe_pdf_file1
            encrypt(unsafe_pdf_file, encryptor, save_pdf)
    except ValueError:
        messagebox.showwarning("Input Error", "Invalid input.")

#----------------------------Tkinter Code----------------------------#

root = Tk()
root.title("STUX PAGEX")

style = ttk.Style()
style.theme_use('default')  


style.configure("Custom.TFrame", background="#424242")  

style.configure("Custom.TLabel", background="#424242", foreground="#f2f2f2")

style.configure("Custom.TRadiobutton", background="#424242", foreground="#f2f2f2")
style.map("Custom.TRadiobutton",
          foreground=[('active', '#f2f2f2'), ('selected', '#f2f2f2')],
          background=[('active', '#424242'), ('selected', '#424242')])

style.configure("Custom.TCheckbutton", background="#424242", foreground="#f2f2f2")
style.map("Custom.TCheckbutton",
          foreground=[('active', '#f2f2f2'), ('selected', '#f2f2f2')],
          background=[('active', '#424242'), ('selected', '#424242')])

tabControl = ttk.Notebook(root, padding=0, width=700)

tab1 = ttk.Frame(tabControl, width=800, height=500, style="Custom.TFrame")
tab2 = ttk.Frame(tabControl, width=800, height=500, style="Custom.TFrame")
tab3 = ttk.Frame(tabControl, width=800, height=500, style="Custom.TFrame")

tabControl.add(tab1, text='Extract')
tabControl.add(tab2, text='Merge')
tabControl.add(tab3, text='Encrypt')

tabControl.pack(expand=1, fill="both")

def add_hover_effect(button, hover_background, normal_background):
    def on_enter(e):
        button['background'] = hover_background

    def on_leave(e):
        button['background'] = normal_background

    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

# ------------------- Extract Tab ------------------- #

file_label = ttk.Label(tab1, text="Select PDF File:", style="Custom.TLabel")
file_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')

pdf_file_entry = Entry(tab1, width=50, bg="#8a8a8a", fg="#ffffff", bd=2, relief="groove")
pdf_file_entry.grid(row=0, column=1, padx=10, pady=10, sticky='w')

browse_button = Button(tab1, text="Browse", command=lambda: select_file(pdf_file_entry),
                       bg="#5DADE2", fg="#ffffff", activebackground="#3498DB", activeforeground="#ffffff", bd=0, cursor="hand2")
browse_button.grid(row=0, column=2, padx=10, pady=10)
add_hover_effect(browse_button, "#3498DB", "#5DADE2")

start_page_label = ttk.Label(tab1, text="Start Page:", style="Custom.TLabel")
start_page_label.grid(row=1, column=0, padx=10, pady=10, sticky='e')

start_page_entry = Entry(tab1, width=10, bg="#8a8a8a", fg="#ffffff", bd=2, relief="groove")
start_page_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

end_page_label = ttk.Label(tab1, text="End Page:", style="Custom.TLabel")
end_page_label.grid(row=2, column=0, padx=10, pady=10, sticky='e')

end_page_entry = Entry(tab1, width=10, bg="#8a8a8a", fg="#ffffff", bd=2, relief="groove")
end_page_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

file_label1 = ttk.Label(tab1, text="Save PDF File:", style="Custom.TLabel")
file_label1.grid(row=3, column=0, padx=10, pady=10, sticky='e')

pdf_file_entry1 = Entry(tab1, width=50, bg="#8a8a8a", fg="#ffffff", bd=2, relief="groove")
pdf_file_entry1.grid(row=3, column=1, padx=10, pady=10, sticky='w')

browse_button1 = Button(tab1, text="Browse", command=lambda: save_file(pdf_file_entry1),
                        bg="#5DADE2", fg="#ffffff", activebackground="#3498DB", activeforeground="#ffffff", bd=0, cursor="hand2")
browse_button1.grid(row=3, column=2, padx=10, pady=10)
add_hover_effect(browse_button1, "#3498DB", "#5DADE2")

extract_button = Button(tab1, text="Extract Pages", command=run_extraction,
                        bg="#58D68D", fg="#ffffff", activebackground="#2ECC71", activeforeground="#ffffff", bd=0, cursor="hand2")
extract_button.grid(row=4, column=1, padx=10, pady=20)
add_hover_effect(extract_button, "#2ECC71", "#58D68D")

# ------------------- Merge Tab ------------------- #

file_label_merge1 = ttk.Label(tab2, text="Select PDF File 1:", style="Custom.TLabel")
file_label_merge1.grid(row=0, column=0, padx=10, pady=10, sticky='e')

merge_file_entry1 = Entry(tab2, width=35, bg="#8a8a8a", fg="#ffffff", bd=2, relief="groove")
merge_file_entry1.grid(row=0, column=1, padx=10, pady=10, sticky='w')

pdf1_browse_button = Button(tab2, text="Browse", command=lambda: select_file(merge_file_entry1),
                             bg="#5DADE2", fg="#ffffff", activebackground="#3498DB", activeforeground="#ffffff", bd=0, cursor="hand2")
pdf1_browse_button.grid(row=0, column=2, padx=10, pady=10)
add_hover_effect(pdf1_browse_button, "#3498DB", "#5DADE2")

option = StringVar(value="All")
radio_all = ttk.Radiobutton(tab2, text="All", variable=option, value="All",
                            command=lambda: toggle_entry(option, merge_start_range1, merge_end_range1), style="Custom.TRadiobutton")
radio_all.grid(row=1, column=0, padx=(10,0), pady=10, sticky='w')

radio_range = ttk.Radiobutton(tab2, text="Range", variable=option, value="Range",
                              command=lambda: toggle_entry(option, merge_start_range1, merge_end_range1), style="Custom.TRadiobutton")
radio_range.grid(row=1, column=1, padx=50, pady=10, sticky='w')

merge_start_range1 = Entry(tab2, state="disabled", bg="#000000", fg="#ffffff", bd=2, relief="groove")
merge_start_range1.grid(row=1, column=2, padx=10, pady=10, sticky='w')

to_label = ttk.Label(tab2, text="to", style="Custom.TLabel")
to_label.grid(row=1, column=3, padx=5, pady=10, sticky='w')

merge_end_range1 = Entry(tab2, state="disabled", bg="#000000", fg="#ffffff", bd=2, relief="groove")
merge_end_range1.grid(row=1, column=4, padx=10, pady=10, sticky='w')

file_label_merge2 = ttk.Label(tab2, text="Select PDF File 2:", style="Custom.TLabel")
file_label_merge2.grid(row=2, column=0, padx=10, pady=10, sticky='e')

merge_file_entry2 = Entry(tab2, width=35, bg="#8a8a8a", fg="#ffffff", bd=2, relief="groove")
merge_file_entry2.grid(row=2, column=1, padx=10, pady=10, sticky='w')

pdf2_browse_button2 = Button(tab2, text="Browse", command=lambda: select_file(merge_file_entry2),
                              bg="#5DADE2", fg="#ffffff", activebackground="#3498DB", activeforeground="#ffffff", bd=0, cursor="hand2")
pdf2_browse_button2.grid(row=2, column=2, padx=10, pady=10)
add_hover_effect(pdf2_browse_button2, "#3498DB", "#5DADE2")

option2 = StringVar(value="All")
radio_all2 = ttk.Radiobutton(tab2, text="All", variable=option2, value="All",
                             command=lambda: toggle_entry(option2, merge_start_range2, merge_end_range2), style="Custom.TRadiobutton")
radio_all2.grid(row=3, column=0, padx=(10,0), pady=10, sticky='w')

radio_range2 = ttk.Radiobutton(tab2, text="Range", variable=option2, value="Range",
                               command=lambda: toggle_entry(option2, merge_start_range2, merge_end_range2), style="Custom.TRadiobutton")
radio_range2.grid(row=3, column=1, padx=50, pady=10, sticky='w')

merge_start_range2 = Entry(tab2, state="disabled", bg="#000000", fg="#ffffff", bd=2, relief="groove")
merge_start_range2.grid(row=3, column=2, padx=10, pady=10, sticky='w')

to_label2 = ttk.Label(tab2, text="to", style="Custom.TLabel")
to_label2.grid(row=3, column=3, padx=5, pady=10, sticky='w')

merge_end_range2 = Entry(tab2, state="disabled", bg="#000000", fg="#ffffff", bd=2, relief="groove")
merge_end_range2.grid(row=3, column=4, padx=10, pady=10, sticky='w')

file_label_merge_save = ttk.Label(tab2, text="Save PDF File:", style="Custom.TLabel")
file_label_merge_save.grid(row=5, column=0, padx=10, pady=10, sticky='e')

output_pdf_file_entry = Entry(tab2, width=35, bg="#8a8a8a", fg="#ffffff", bd=2, relief="groove")
output_pdf_file_entry.grid(row=5, column=1, padx=10, pady=10, sticky='w')

merge_pdf_browse_button1 = Button(tab2, text="Browse", command=lambda: save_file(output_pdf_file_entry),
                                  bg="#5DADE2", fg="#ffffff", activebackground="#3498DB", activeforeground="#ffffff", bd=0, cursor="hand2")
merge_pdf_browse_button1.grid(row=5, column=2, padx=10, pady=10)
add_hover_effect(merge_pdf_browse_button1, "#3498DB", "#5DADE2")

merge_extract_button = Button(tab2, text="Merge Pages", command=run_merge,
                              bg="#58D68D", fg="#ffffff", activebackground="#2ECC71", activeforeground="#ffffff", bd=0, cursor="hand2")
merge_extract_button.grid(row=6, column=1, padx=10, pady=20)
add_hover_effect(merge_extract_button, "#2ECC71", "#58D68D")

# ------------------- Encrypt Tab ------------------- #

select_pdf_file = ttk.Label(tab3, text="Select PDF file:", style="Custom.TLabel")
select_pdf_file.grid(row=0, column=0, padx=10, pady=10, sticky='e')

en_pdf_entry = Entry(tab3, width=50, bg="#8a8a8a", fg="#ffffff", bd=2, relief="groove")
en_pdf_entry.grid(row=0, column=1, padx=10, pady=10, sticky='w')

en_browse_button2 = Button(tab3, text="Browse", command=lambda: select_file(en_pdf_entry),
                            bg="#5DADE2", fg="#ffffff", activebackground="#3498DB", activeforeground="#ffffff", bd=0, cursor="hand2")
en_browse_button2.grid(row=0, column=2, padx=10, pady=10)
add_hover_effect(en_browse_button2, "#3498DB", "#5DADE2")

pass_label = ttk.Label(tab3, text="Enter your password:", style="Custom.TLabel")
pass_label.grid(row=1, column=0, padx=10, pady=10, sticky='e')

pass_entry = Entry(tab3, width=40, show='*', bg="#8a8a8a", fg="#ffffff", bd=2, relief="groove")
pass_entry.grid(row=1, column=1, padx=10, pady=10, sticky='w')

check = ttk.Checkbutton(tab3, text='SHOW', command=show, style="Custom.TCheckbutton")
check.grid(row=1, column=2, padx=10, pady=10, sticky='w')

en_file_label = ttk.Label(tab3, text="Save PDF File:", style="Custom.TLabel")
en_file_label.grid(row=2, column=0, padx=10, pady=10, sticky='e')

en_output_pdf_file_entry = Entry(tab3, width=50, bg="#8a8a8a", fg="#ffffff", bd=2, relief="groove")
en_output_pdf_file_entry.grid(row=2, column=1, padx=10, pady=10, sticky='w')

en_pdf_browse_button1 = Button(tab3, text="Browse", command=lambda: save_file(en_output_pdf_file_entry),
                                bg="#5DADE2", fg="#ffffff", activebackground="#3498DB", activeforeground="#ffffff", bd=0, cursor="hand2")
en_pdf_browse_button1.grid(row=2, column=2, padx=10, pady=10)
add_hover_effect(en_pdf_browse_button1, "#3498DB", "#5DADE2")

encrypt_button = Button(tab3, text="Protect PDF", command=run_encryption,
                        bg="#58D68D", fg="#ffffff", activebackground="#2ECC71", activeforeground="#ffffff", bd=0, cursor="hand2")
encrypt_button.grid(row=3, column=1, padx=10, pady=20)
add_hover_effect(encrypt_button, "#2ECC71", "#58D68D")

root.mainloop()
