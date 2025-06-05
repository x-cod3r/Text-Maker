# 📄 File to Text Converter

<div align="center">

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![GUI](https://img.shields.io/badge/GUI-Tkinter-orange.svg)

*A simple, elegant GUI tool to convert multiple code files into a single text document*

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Supported Formats](#-supported-file-formats) • [Screenshots](#-screenshots)

</div>

---

## ✨ Features

- 🎯 **Simple & Intuitive**: Clean, user-friendly interface
- 📁 **Flexible Selection**: Browse individual files or entire folders
- 🔧 **Customizable Output**: Control headers, separators, and structure
- 🌐 **Smart Encoding**: Automatically handles different text encodings
- 📊 **Progress Tracking**: Real-time processing status
- 🛡️ **Error Handling**: Gracefully manages unreadable files
- 🚀 **Cross-Platform**: Works on Windows, macOS, and Linux

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher
- tkinter (usually included with Python)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/file-to-text-converter.git
   cd file-to-text-converter
   ```

2. **Run directly** (no additional dependencies needed!)
   ```bash
   python file_to_text_converter.py
   ```

### Alternative: Download Release
Download the latest release from the [Releases page](https://github.com/x-cod3r/Text-Maker/releases) and run the standalone executable.

## 🎮 Usage

### Basic Workflow
1. **Launch** the application
2. **Select Files**: 
   - Click "Browse Files" for individual selection
   - Click "Browse Folder" to scan entire directories
3. **Configure Options**:
   - ✅ Include filename headers
   - ✅ Add separators between files
   - ✅ Preserve folder structure
4. **Convert**: Click "Convert to Text File" and choose output location

### Command Line Alternative
For automation, you can also use the tool programmatically:

```python
from file_to_text_converter import FileToTextConverter
import tkinter as tk

# Create and run the GUI
root = tk.Tk()
app = FileToTextConverter(root)
root.mainloop()
```

## 📋 Supported File Formats

<table>
<tr>
<td>

**Programming Languages**
- C/C++ (`.cpp`, `.c`, `.cc`, `.cxx`)
- Headers (`.h`, `.hpp`, `.hh`, `.hxx`)
- Python (`.py`, `.pyw`)
- JavaScript (`.js`, `.jsx`)
- TypeScript (`.ts`, `.tsx`)
- Java (`.java`)
- C# (`.cs`)
- PHP (`.php`)

</td>
<td>

**Additional Formats**
- Ruby (`.rb`)
- Go (`.go`)
- Rust (`.rs`)
- Swift (`.swift`)
- Kotlin (`.kt`)
- Scala (`.scala`)
- Shell Scripts (`.sh`, `.bash`)
- SQL (`.sql`)
- And many more...

</td>
</tr>
</table>

## 📸 Screenshots

### Main Interface
```
┌─────────────────────────────────────────────┐
│           File to Text Converter            │
├─────────────────────────────────────────────┤
│ Select Files: [Browse Files] [Browse Folder] [Clear] │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ Selected Files:                         │ │
│ │ • project/main.cpp                      │ │
│ │ • project/utils.h                       │ │
│ │ • project/data.py                       │ │
│ │ • project/config.json                   │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ Options:                                    │
│ ☑ Include filename headers                  │
│ ☑ Add separators between files             │
│ ☐ Preserve folder structure in output      │
│                                             │
│           [Convert to Text File]            │
│                                             │
│ Status: 4 files selected                   │
└─────────────────────────────────────────────┘
```

## 🛠️ Configuration Options

| Option | Description | Default |
|--------|-------------|---------|
| **Include filename headers** | Adds `=== filename.ext ===` before each file | ✅ Enabled |
| **Add separators** | Inserts `========================================` between files | ✅ Enabled |
| **Preserve folder structure** | Shows full path instead of just filename | ❌ Disabled |

## 📝 Output Example

```text
=== main.cpp ===
#include <iostream>
#include "utils.h"

int main() {
    std::cout << "Hello World!" << std::endl;
    return 0;
}

==================================================

=== utils.h ===
#ifndef UTILS_H
#define UTILS_H

void printMessage();

#endif

==================================================

=== data.py ===
import json

def load_config():
    with open('config.json', 'r') as f:
        return json.load(f)
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Ideas for Contributions
- 🎨 UI/UX improvements
- 📝 Additional file format support
- 🔧 Command-line interface
- 🌍 Internationalization
- 📦 Package management integration

## 🐛 Bug Reports & Feature Requests

Found a bug or have a feature idea? Please open an issue on the [Issues page](https://github.com/x-cod3r/Text-Maker/issues).

**Bug Report Template:**
- Python version
- Operating system
- Steps to reproduce
- Expected vs actual behavior

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with Python's tkinter for maximum compatibility
- Inspired by the need for simple code consolidation tools
- Thanks to all contributors and users!

## 📊 Stats

<div align="center">

![GitHub stars](https://img.shields.io/github/stars/x-cod3r/Text-Maker?style=social)
![GitHub forks](https://img.shields.io/github/forks/x-cod3r/Text-Maker?style=social)
![GitHub issues](https://img.shields.io/github/issues/x-cod3r/Text-Maker)
![GitHub pull requests](https://img.shields.io/github/issues-pr/x-cod3r/Text-Maker)

</div>

---

<div align="center">
<strong>Made with ❤️ for developers who need to consolidate their code</strong>
</div>
