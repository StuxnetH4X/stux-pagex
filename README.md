# STUX PAGEX

**STUX PAGEX** is a user-friendly desktop application built with Python's Tkinter library, designed to simplify PDF management tasks. Whether you need to extract specific pages, merge multiple PDFs, or secure your documents with encryption, STUX PAGEX provides an intuitive interface to handle these operations effortlessly.

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Extract Pages**: Select a PDF and extract a range of pages to create a new PDF.
- **Merge PDFs**: Combine two PDF files by selecting specific page ranges or merging entire documents.
- **Encrypt PDFs**: Protect your PDFs with a password to ensure document security.
- **Intuitive GUI**: Easy-to-navigate interface with hover effects and clear instructions.
- **Cross-Platform**: Compatible with Windows, macOS, and Linux.

## Demo

![STUX PAGEX Screenshot](https://github.com/yourusername/STUX-PAGEX/blob/main/screenshots/demo.png)

*Note: Replace the image link with your actual screenshot URL.*

## Installation

### Prerequisites

- **Python 3.6 or higher**: Ensure you have Python installed on your system. You can download it from [Python's official website](https://www.python.org/downloads/).

### Clone the Repository

```bash
git clone https://github.com/yourusername/STUX-PAGEX.git
cd STUX-PAGEX
```

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

*If a `requirements.txt` file is not provided, install the necessary packages manually:*

```bash
pip install PyPDF2
```

## Usage

Run the application using Python:

```bash
python stux_pagex.py
```

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

## Dependencies

- [Python](https://www.python.org/) 3.6+
- [Tkinter](https://docs.python.org/3/library/tkinter.html) (usually included with Python)
- [PyPDF2](https://pypi.org/project/PyPDF2/)

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/YourFeature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/YourFeature`.
5. Open a pull request.

Please ensure your code adheres to the project's coding standards and includes appropriate documentation.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any inquiries or support, please open an issue on [GitHub Issues](https://github.com/yourusername/STUX-PAGEX/issues) or contact [youremail@example.com](mailto:youremail@example.com).

---

**Thank you for using STUX PAGEX!** If you find this project helpful, please consider giving it a ⭐ on GitHub.
