@echo off

set /p city="Enter the City Name: "

curl wttr.in/%city%

pause