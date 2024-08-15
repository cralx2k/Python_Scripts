@echo off
cls
:main_menu
cls
COLOR 0A
echo =====================================
echo Main Menu
echo =====================================
echo 1. Option 1
echo 2. Option 2
echo 3. Option 3
echo 4. Go to Sub Menu
echo 5. Exit
echo =====================================
set /p choice="Enter your choice: "

if "%choice%"=="1" goto option1
if "%choice%"=="2" goto option2
if "%choice%"=="3" goto option3
if "%choice%"=="4" goto sub_menu
if "%choice%"=="5" exit

echo Invalid choice, please select again.
pause
goto main_menu

:option1
cls
echo You selected Option 1
pause
goto main_menu

:option2
cls
echo You selected Option 2
pause
goto main_menu

:option3
cls
echo You selected Option 3
pause
goto main_menu

:sub_menu
COLOR 0B
cls
echo =====================================
echo Sub Menu
echo =====================================
echo 1. Sub Option 1
echo 2. Sub Option 2
echo 3. Back to Main Menu
echo =====================================
set /p sub_choice="Enter your choice: "

if "%sub_choice%"=="1" goto sub_option1
if "%sub_choice%"=="2" goto sub_option2
if "%sub_choice%"=="3" goto main_menu

echo Invalid choice, please select again.
pause
goto sub_menu

:sub_option1
cls
echo You selected Sub Option 1
pause
goto sub_menu

:sub_option2
cls
echo You selected Sub Option 2
pause
goto sub_menu
