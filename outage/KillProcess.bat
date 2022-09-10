FOR /F "tokens=5 delims= " %%P IN ('netstat -a -n -o ^| findstr :5000') DO TaskKill.exe /F /PID %%P

pause
