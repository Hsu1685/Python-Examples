# xml-parse-copy-file
XML Parse and File Copy GUI Tool</br>
Parse the project XML file from CodeWarrior 5.2 to find the name of the file contained in a specific Target, and then copy the file with the same name from the Sources folder to the specific folder.</br>
從CodeWarrior 5.2的專案XML檔案進行分析，找出特定Target包含的檔案名稱，再從Sources資料夾中複製相同名稱的檔案至特定資料夾。</br>

# 指令
## PySide6
### DNTW Desktop PySide6 轉換*.ui指令
```
conda activate ENVNAME
pyside6-uic main-window_2021-11-10.ui -o window.pyE
```

### DNTW Desktop PySide6 路徑
```
C:\Users\tw019032\Anaconda3\envs\myenv1\Lib\site-packages\PySide6
```

## 打包指令
### pyinstaller
```
conda activate ENVNAME
pyinstaller -F -w my-xml-parse.py (沒有終端機)
pyinstaller -F my-xml-parse.py (有終端機)
```

### nuitka
```
nuitka --onefile --windows-disable-console --show-progress --enable-plugin=pyside6 --follow-import-to=need --output-dir=output my-xml-parse.py
```
---