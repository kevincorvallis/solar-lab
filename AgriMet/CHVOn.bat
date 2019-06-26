:while1
	IF %TIME% LEQ %deadline% (
		Python C:\SRML\bin\AgriMet_prime.py -s CHVO -b 20%cy%/%cm%/01 -e 20%cy%/%cm%/%md% >C:\PC208w\AgriMet\CHRQ%cy%%cm%.txt
		IF errorlevel 1 set flag=99
		IF errorlevel 0 set flag=0
	)