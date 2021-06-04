# How to run - By Julian

Als erstes musst du python3, und pip installiert haben. Unter Windows Installierst du dir einfach die *.exe, oder mit folgendem Command  in PowerShell:  
``PS C:\Users\@User> winget install python`` oder mit ``python3``    
Unter Linux musst du folgendes tun:

``~$ sudo apt install python3 python python3-pip``

Für das Installieren des Frameworks gehst du folgendermaßen vor:

**Linux:**  
``~$ python3 -m pip install -U discord.py``  
``~$ python3 -m pip install psutil``  
``~$ python3 -m pip install asyncio``  
``~$ python3 -m pip install datetime``


**Windows:**  
``~$ py -3 -m pip install -U discord.py``  
``~$ py -3 -m pip install psutil``  
``~$ py -3 -m pip install asyncio``  
``~$ py -3 -m pip install datetime``   

**Info**  
Wenn du ein PS Skript (Windows PowerShell) erstellen willst, dann musst du folgendes tun:  
Führe PowerShell als Administrator aus und gebe folgendes ein:

``PS C:\WINDOWS\system32> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned``

``Ausführungsrichtlinie ändern``  
``Die Ausführungsrichtlinie trägt zum Schutz vor nicht vertrauenswürdigen Skripts bei. Wenn Sie die Ausführungsrichtlinie                                                   ändern, sind Sie möglicherweise den im Hilfethema "about_Execution_Policies" unter                                                                                      "https:/go.microsoft.com/fwlink/?LinkID=135170" beschriebenen Sicherheitsrisiken ausgesetzt. Möchten Sie die                                                             Ausführungsrichtlinie ändern?                                                                                                                                            [J] Ja  [A] Ja, alle  [N] Nein  [K] Nein, keine  [H] Anhalten  [?] Hilfe (Standard ist "N"): A
``  
``PS C:\WINDOWS\system32>  ``

Nun kannst du PowerShell Skripte erstellen!
Ein PS-Skript könnte bspw so aussehen:

``cd <Pfad-zum-Projekt>``  
``<Installationsort-von-python.exe> main.py``

Bei mir sieht der PS-Skript so aus:  
``cd D:\Projekte\dfbPy\``  
``py main.py``

discord.py - HowTo Run - made by Julian (DC: Julius#1755)