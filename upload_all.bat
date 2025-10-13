@echo off
REM ============================================================
REM  🚀  HSLU - Auto Git Uploader
REM  Projekt: DT_Programmieren
REM  Autor:   manuhslu
REM  Beschreibung:
REM     Lädt alle neuen/geänderten Dateien automatisch zu GitHub hoch.
REM ============================================================

echo.
echo ================================
echo   🚀  GITHUB AUTO-UPLOADER
echo ================================
echo.

REM Aktiviere dein virtuelles Environment (optional, falls nötig)
call myenv\Scripts\activate

REM Wechsle in das Projektverzeichnis (anpassen falls nötig)
cd /d C:\Users\manue\OneDrive\VS_Projects\DT_Programmieren

REM Zeige den aktuellen Git-Status
git status

echo.
echo 🔄  Füge alle Änderungen hinzu...
git add .

echo.
echo 💬  Committe Änderungen...
git commit -m "Auto-Upload"

echo.
echo ☁️  Lade alles zu GitHub hoch...
git push

echo.
echo ✅  Fertig! Alle Änderungen sind auf GitHub.
echo.
pause
