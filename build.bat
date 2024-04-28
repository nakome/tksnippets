pyinstaller main.py ^
    --onefile ^
    --clean ^
    --windowed --noconsole ^
    --hidden-import "clr" --name "Snippets" ^
    --icon "icon.ico" 
