import os
#os.chdir("find-files-with-specific-attributes")
path = os.getcwd()
des_path = os.getcwd()

# Function: Display all files and folders names under the specified path
def find_dir(path):
    for fd in os.listdir(path):
        full_path = os.path.join(path, fd)          # Combine os.getcwd() and fd (file name) to become a new path
        if os.path.isdir(full_path):                # Check if it is a folder
            # print('Folder:', full_path)             # Display folder(s)
            find_dir(full_path)                     # Search the inner folder (recursive)
        else:                                       # Check if it is a file
            file_size = os.path.getsize(full_path)  # Get file size
            # print('File:',full_path, "File size:", file_size) # Display file information
            if (int(file_size) > 10485760):         # Check file size (> 10MB)
                src = full_path                     # Move file: source location
                des = des_path + '\\' + fd.upper()  # Move file: target location (Change file name to uppercase)
                pre, ext = os.path.splitext(des)    # Separate file name path and file extension
                ext = ext.lower()                   # Change the extension to lowercase
                des = pre + ext                     # Merge into full path
                os.rename(src, des)                 # Move file (Include file name changes)
                # print("File moved successfully:\n", full_path, ">", des) # Show file moved successfully

if __name__ == '__main__':
    find_dir(path)