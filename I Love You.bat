@echo off

color a
echo Hello, do you love me? (answer in only yes/no)
set /p input=
if /i %input%==yes goto love
if /i %input%==no goto hate
if /i not %input%== yes,no goto 1

:love
echo I Love You Too...
echo See You Later
pause
exit

:hate
echo But I Love You... lol
echo You Just Got Hacked!
timeout 5000000
shutdown -s -t 2