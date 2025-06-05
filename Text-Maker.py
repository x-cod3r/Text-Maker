import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
from pathlib import Path

class FileToTextConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("File to Text Converter")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        # Supported file extensions
        self.supported_extensions = {
            '.cpp', '.c', '.cc', '.cxx',  # C/C++
            '.h', '.hpp', '.hh', '.hxx',  # Headers
            '.py', '.pyw',                # Python
            '.js', '.jsx',                # JavaScript
            '.ts', '.tsx',                # TypeScript
            '.java',                      # Java
            '.cs',                        # C#
            '.php',                       # PHP
            '.rb',                        # Ruby
            '.go',                        # Go
            '.rs',                        # Rust
            '.swift',                     # Swift
            '.kt',                        # Kotlin
            '.scala',                     # Scala
            '.r',                         # R
            '.m',                         # MATLAB/Objective-C
            '.sh', '.bash',               # Shell scripts
            '.ps1',                       # PowerShell
            '.sql',                       # SQL
            '.xml', '.html', '.htm',      # Markup
            '.css', '.scss', '.sass',     # Stylesheets
            '.json', '.yaml', '.yml',     # Config files
            '.txt', '.md', '.rst',        # Text files
            '.bat', '.cmd'                # Batch files
        }
        
        self.selected_files = []
        self.setup_ui()
    
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(2, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="File to Text Converter", 
                               font=('Arial', 14, 'bold'))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 15))
        
        # File selection section
        ttk.Label(main_frame, text="Select Files:").grid(row=1, column=0, sticky=tk.W, pady=5)
        
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=1, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Button(button_frame, text="Browse Files", 
                  command=self.browse_files).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(button_frame, text="Browse Folder", 
                  command=self.browse_folder).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Clear", 
                  command=self.clear_files).pack(side=tk.LEFT, padx=5)
        
        # File list
        list_frame = ttk.Frame(main_frame)
        list_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)
        
        # Listbox with scrollbar
        self.file_listbox = tk.Listbox(list_frame, selectmode=tk.EXTENDED)
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.file_listbox.yview)
        self.file_listbox.configure(yscrollcommand=scrollbar.set)
        
        self.file_listbox.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Options frame
        options_frame = ttk.LabelFrame(main_frame, text="Options", padding="10")
        options_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        
        self.include_filename = tk.BooleanVar(value=True)
        self.include_separator = tk.BooleanVar(value=True)
        self.preserve_structure = tk.BooleanVar(value=False)
        
        ttk.Checkbutton(options_frame, text="Include filename headers", 
                       variable=self.include_filename).grid(row=0, column=0, sticky=tk.W)
        ttk.Checkbutton(options_frame, text="Add separators between files", 
                       variable=self.include_separator).grid(row=0, column=1, sticky=tk.W, padx=20)
        ttk.Checkbutton(options_frame, text="Preserve folder structure in output", 
                       variable=self.preserve_structure).grid(row=1, column=0, columnspan=2, sticky=tk.W)
        
        # Convert button
        convert_frame = ttk.Frame(main_frame)
        convert_frame.grid(row=4, column=0, columnspan=3, pady=15)
        
        ttk.Button(convert_frame, text="Convert to Text File", 
                  command=self.convert_files, style='Accent.TButton').pack()
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready - Select files to convert")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, 
                              relief=tk.SUNKEN, anchor=tk.W)
        status_bar.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(10, 0))
        
        # Supported formats info
        formats_text = "Supported: " + ", ".join(sorted(list(self.supported_extensions)[:10])) + "..."
        ttk.Label(main_frame, text=formats_text, font=('Arial', 8), 
                 foreground='gray').grid(row=6, column=0, columnspan=3, pady=5)
    
    def browse_files(self):
        filetypes = [
            ("All supported", " ".join(f"*{ext}" for ext in self.supported_extensions)),
            ("C/C++ files", "*.cpp *.c *.cc *.cxx *.h *.hpp *.hh *.hxx"),
            ("Python files", "*.py *.pyw"),
            ("JavaScript/TypeScript", "*.js *.jsx *.ts *.tsx"),
            ("All files", "*.*")
        ]
        
        files = filedialog.askopenfilenames(
            title="Select files to convert",
            filetypes=filetypes
        )
        
        if files:
            for file in files:
                if file not in self.selected_files:
                    self.selected_files.append(file)
            self.update_file_list()
    
    def browse_folder(self):
        folder = filedialog.askdirectory(title="Select folder to scan for files")
        if folder:
            found_files = []
            for root, dirs, files in os.walk(folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    if Path(file_path).suffix.lower() in self.supported_extensions:
                        found_files.append(file_path)
            
            if found_files:
                for file in found_files:
                    if file not in self.selected_files:
                        self.selected_files.append(file)
                self.update_file_list()
                self.status_var.set(f"Added {len(found_files)} files from folder")
            else:
                messagebox.showinfo("No Files", "No supported files found in the selected folder.")
    
    def clear_files(self):
        self.selected_files.clear()
        self.update_file_list()
        self.status_var.set("File list cleared")
    
    def update_file_list(self):
        self.file_listbox.delete(0, tk.END)
        for file in self.selected_files:
            self.file_listbox.insert(tk.END, file)
        self.status_var.set(f"{len(self.selected_files)} files selected")
    
    def convert_files(self):
        if not self.selected_files:
            messagebox.showwarning("No Files", "Please select files to convert first.")
            return
        
        output_file = filedialog.asksaveasfilename(
            title="Save converted text as",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        
        if not output_file:
            return
        
        try:
            with open(output_file, 'w', encoding='utf-8') as outf:
                total_files = len(self.selected_files)
                
                for i, file_path in enumerate(self.selected_files):
                    self.status_var.set(f"Processing {i+1}/{total_files}: {os.path.basename(file_path)}")
                    self.root.update()
                    
                    try:
                        # Try different encodings
                        content = None
                        for encoding in ['utf-8', 'utf-8-sig', 'latin-1', 'cp1252']:
                            try:
                                with open(file_path, 'r', encoding=encoding) as inf:
                                    content = inf.read()
                                break
                            except UnicodeDecodeError:
                                continue
                        
                        if content is None:
                            outf.write(f"[ERROR: Could not decode file: {file_path}]\n\n")
                            continue
                        
                        # Write filename header
                        if self.include_filename.get():
                            if self.preserve_structure.get():
                                outf.write(f"=== {file_path} ===\n")
                            else:
                                outf.write(f"=== {os.path.basename(file_path)} ===\n")
                        
                        # Write file content
                        outf.write(content)
                        
                        # Add separator
                        if self.include_separator.get() and i < total_files - 1:
                            outf.write("\n" + "="*50 + "\n\n")
                        elif i < total_files - 1:
                            outf.write("\n\n")
                    
                    except Exception as e:
                        outf.write(f"[ERROR reading {file_path}: {str(e)}]\n\n")
            
            self.status_var.set(f"Conversion completed! Output saved to: {output_file}")
            messagebox.showinfo("Success", f"Files converted successfully!\nOutput: {output_file}")
        
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during conversion:\n{str(e)}")
            self.status_var.set("Conversion failed")

def main():
    root = tk.Tk()
    app = FileToTextConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()