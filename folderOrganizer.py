from tkinter import filedialog
from tkinter import *
import os, threading
from pathlib import Path

class Folder_Organizer():
    def __init__(self):
        root.title("Folder Organizer | BETA")
        root.geometry('400x300')
        root.resizable(width=False, height=False)
        root.configure(bg='#fafafa')

        # frame
        self.formFrame = Frame(root, bg='#fafafa')
        self.startFrame = Frame(root, bg='#fafafa')
        
        # widgets
        self.label1 = Label(root, text="Folder Organizer", font=["Selena", "20"], pady=10, bg='#fafafa')
        self.label2 = Label(root, text="Organize files in a folder by putting them in their categories",font=["Selena", "12"], bg='#fafafa')
        self.label1.pack()
        self.label2.pack()

        self.formFrame.pack(pady=20)
        self.btnSelFolder = Button(self.formFrame, text="Select Folder", font=["Selena", "11"], padx=20, pady=5, fg='white', bg='#555555', command=lambda: self.Select_Folder(self.lblFolderSelected, self.btnSelFolder))
        self.lblFolderSelected = Label(self.formFrame, text="...", font=["Selena", "12"], pady=5, bg='#fafafa', width=20)
        self.btnSelFolder.grid(row=0)
        self.lblFolderSelected.grid(row=0, column=1, padx=10)

        self.startFrame.pack(pady=10)
        self.btnOrgFolder = Button(self.startFrame, text="Organize Files", font=["Selena", "12"], padx=20, pady=10, fg='white', bg='#159F5C', command=lambda:self.initOrgFolder())
        self.orgFolderStatus = Label(self.startFrame, text="Status: ", font=["Selena", "12"], pady=5, bg='#fafafa')
        self.btnOrgFolder.pack()
        self.orgFolderStatus.pack(pady=5)

        self.Categories = {
            "HTML-CSS-JS": [".html5", ".html", ".htm", ".xhtml", ".css", ".scss", ".less", ".js"],
            "Images": [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif",".raw", ".arw", ".cr2", ".nrw", ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz"],
            "Adobe Files": [".psd", ".ai", ".eps"],
            "Videos": [".avi", ".flv", ".wmv", ".mov", ".mkv", ".mp4", ".webm", ".vob", ".mng", ".qt", ".mpg", ".mpeg", ".3gp"],
            "Documents": [".doc", ".docx", ".odt", ".pdf", ".xls", ".xlsx", ".ods", ".ppt", ".pptx"],
            "Archives": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                        ".dmg", ".rar", ".xar", ".zip"],
            "Audio": [".aac", ".aa", ".aac", ".caf", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", ".msv", ".ogg", ".oga", ".pcm", ".vox", ".wav", ".wave", ".wma"],
            "Text": [".txt", ".in", ".out"],
            "Python": [".py", ".pyc"],
            "Applications": [".exe"],
            "Android Apps": [".apk"],
            "Shell": [".sh", ".bat"]
        }
        self.FILE_FORMATS = {
            file_format: directory
            for directory, file_formats in self.Categories.items()
            for file_format in file_formats
        }

    def Select_Folder(self, labelSrc, btn):
        folderSelected = filedialog.askdirectory()
        labelSrc.config(text=folderSelected)
        btn.config(text="Change Folder")

    def initOrgFolder(self):
        # use 
        t = threading.Thread(target=self.Organize_Folder, args=[self.lblFolderSelected.cget("text"), self.orgFolderStatus])
        t.daemon = True
        t.start()

    def Organize_Folder(self, bFolder, status):
        folderPath = os.path.normpath(bFolder)
        status.config(text="Initializing...", fg='orange')
        os.chdir(folderPath)

        for entry in os.scandir():
            if entry.is_dir():
                continue
            status.config(text="Organizing Files...", fg='blue')
            file_path = Path(entry)
            file_format = file_path.suffix.lower()
            if file_format in self.FILE_FORMATS:
                directory_path = Path(self.FILE_FORMATS[file_format])
                directory_path.mkdir(exist_ok=True)
                file_path.rename(directory_path.joinpath(file_path))

            for dir in os.scandir():
                try:
                    os.rmdir(dir)
                except:
                    pass
            # done
            status.config(text="DONE! Successfully Organized Files.", fg='green')



root = Tk()
proc = Folder_Organizer()
root.mainloop()