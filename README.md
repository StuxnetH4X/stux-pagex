# STUX PAGEX

**STUX PAGEX** is a user-friendly desktop application built with Python's Tkinter library, designed to simplify PDF management tasks. Whether you need to extract specific pages, merge multiple PDFs, or secure your documents with encryption, STUX PAGEX provides an intuitive interface to handle these operations effortlessly.

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Contact](#contact)

## Features

- **Extract Pages**: Select a PDF and extract a range of pages to create a new PDF.
- **Merge PDFs**: Combine two PDF files by selecting specific page ranges or merging entire documents.
- **Encrypt PDFs**: Protect your PDFs with a password to ensure document security.

## Demo

- ![Extract Tab](https://drive.google.com/file/d/13aeDwGSGKK8GOTLtP05C0HyIvuGQZJ4q)
- ![Merge Tab](https://drive.google.com/file/d/18aWtBeYu2TbpZwKPJbwJW0VnDUerSEeR)
- ![Encrypt Tab](https://drive.google.com/file/d/1PAnbGiYBerJuEVEoga4yxEp4gDa2c0Qd)


## Installation

## Dependencies

- [Python](https://www.python.org/) 3.6+
- [Tkinter](https://docs.python.org/3/library/tkinter.html) (usually included with Python)
- [PyPDF2](https://pypi.org/project/PyPDF2/)

### Install Dependencies

It's recommended to use a virtual environment to manage dependencies.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS and Linux:
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install required packages
pip install -r requirements.txt
```

*If you don't want to use virtual environment, directly go to terminal and run the given command:*

```bash
pip install PyPDF2
```

## Usage

Run the application using Python:

```bash
python main.py
```
To directly run the application rename `main.py` to `main.pyw`. Then directly double click on the file to run the application.

### Extract Pages

1. Navigate to the **Extract** tab.
2. Click the **Browse** button to select the PDF file.
3. Enter the **Start Page** and **End Page** numbers.
4. Click **Browse** to choose the destination to save the extracted PDF.
5. Click **Extract Pages** to perform the operation.

### Merge PDFs

1. Navigate to the **Merge** tab.
2. Click **Browse** to select the first PDF file.
3. Choose whether to merge **All** pages or a specific **Range**.
4. If selecting **Range**, enter the **Start Page** and **End Page**.
5. Repeat the steps for the second PDF file.
6. Choose the destination to save the merged PDF.
7. Click **Merge Pages** to combine the documents.

### Encrypt PDFs

1. Navigate to the **Encrypt** tab.
2. Click **Browse** to select the PDF file you wish to protect.
3. Enter a password in the **Enter your password** field.
4. Choose the destination to save the encrypted PDF.
5. Click **Protect PDF** to apply encryption.

## Contact

For any inquiries or support, please open an issue on [GitHub Issues](https://github.com/StuxnetH4X/stux-pagex/issues).

---

**Thank you for using STUX PAGEX!** If you find this project helpful, please consider giving it a ⭐ on GitHub.
