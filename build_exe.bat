
@echo off
echo Building photo_report.exe ...
python -m PyInstaller photo_report.spec --onefile --noconsole
pause
