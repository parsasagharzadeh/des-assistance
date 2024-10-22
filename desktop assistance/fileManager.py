
import os
import glob

class fileManager:
    @staticmethod
    def create_file(file_name, file_extension, directory=None):
        if directory is None:
            directory = os.getcwd()
        else:
            os.makedirs(directory, exist_ok=True)
        
        file_path = os.path.join(directory, f"{file_name}.{file_extension}")
        with open(file_path, 'w') as f:
            pass
        return True

    @staticmethod
    def update_file(file_path, content):
        with open(file_path, 'a') as f:
            f.write(content + '\n')
    
    @staticmethod
    def create_folder(folder_name, directory=None):
        if directory is None:
            directory = os.getcwd()
        folder_path = os.path.join(directory, folder_name)
        os.makedirs(folder_path, exist_ok=True)

    @staticmethod
    def delete_file(file_path):
        if os.path.exists(file_path):
            os.remove(file_path)

    @staticmethod
    def delete_folder(folder_path):
        if os.path.exists(folder_path):
            os.rmdir(folder_path)

    @staticmethod
    def update_csv(file_path, content):
        with open(file_path, 'a') as f:
            f.write(content + '\n')

    @staticmethod
    def update_word(self,file_path, content):
        # اینجا می‌توانید از کتابخانه python-docx برای مدیریت فایل‌های Word استفاده کنید.
        from docx import Document
        doc = Document(file_path)
        doc.add_paragraph(content)
        doc.save(file_path)

    @staticmethod
    def update_py(file_path, content):
        with open(file_path, 'a') as f:
            f.write(content + '\n')

 
    @staticmethod
    def find_drives():
        """برای ویندوز: لیست درایوها را برمی‌گرداند."""
        drives = []
        for drive in range(65, 91):  # ASCII A-Z
            drive_letter = f"{chr(drive)}:"
            if os.path.exists(drive_letter):
                drives.append(drive_letter)
        return drives

    @staticmethod
    def find_files_by_name(name):
        results = []
        drives = fileManager.find_drives()
        for drive in drives:
            for root, dirs, files in os.walk(drive):
                for file in files:
                    if name in file:
                        results.append(os.path.join(root, file))
        return results

    @staticmethod
    def find_folders_by_name(name):
        results = []
        drives = fileManager.find_drives()
        for drive in drives:
            for root, dirs, files in os.walk(drive):
                for dir in dirs:
                    if name in dir:
                        results.append(os.path.join(root, dir))
      
name ="__main__"
# مثال استفاده از کتابخانه
if name == "__main__":
    fm = fileManager()
    
    # ایجاد فایل
    # fm.create_file("test", "txt")
    
    # # به‌روزرسانی فایل
    # fm.update_file("test.txt", "This is a test content.")
    
    # # ایجاد پوشه
    # fm.create_folder("test_folder")
    
    # حذف فایل
    # fm.delete_file("test.txt")
    
    # # حذف پوشه
    # fm.delete_folder("test_folder")
    
    # پیدا کردن فایل‌ها با نام مشخص
    # print(fm.find_files_by_name("example"))
    
    # پیدا کردن پوشه‌ها با نام مشخص
    # print(fm.find_folders_by_name("parsa sagharzadeh resume file"))
#  پیدا کردن فایل‌ها با نام مشخص
    # print(fm.find_files_by_name("example"))
    
    # پیدا کردن پوشه‌ها با نام مشخص
    # print(fm.find_folders_by_name("parsa sagharzadeh resume file"))