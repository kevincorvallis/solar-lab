rem	AgriMet17.bat	03/16/2017 fev & riley
rem	Checks, formats, and distributes agrimet data.


rem	Cleanup from other runs, etc.
set ctrl_flag=
set cy=
set cm=
Set md=
set ch=
set cmin=
set py=
set pm=
set bat_step=0

rem	for testing:
rem     set date=mon 01/01/2018
rem	set time=00:03:00.00

rem	Some useful vars
set bat_name=AgriMet17.bat
set bat_log=C:\SRML\log\AgriMet17.log
set problem_log=C:\SRML\log\AgriMetPROBLEMS.log
set bin=C:\SRML\bin
set etc=C:\SRML\etc

rem	Go to where (some of) the data files live
C:
cd \SRML\bin

rem	Handle parms if used
if not "%1" == "" set ctrl_flag=%1%
if not "%2" == "" set cy=%2%
if not "%3" == "" set cm=%3%
if not "%4" == "" set py=%4%
if not "%5" == "" set pm=%5%
if "%ctrl_flag%" == NORMAL goto NORMAL
if "%ctrl_flag%" == NEWMONTH goto NEW_MTH
if "%ctrl_flag%" == NEWYEAR goto NEW_YEAR

rem	Otherwise set some vars depending on current date:
rem	Set current year (00-99)
set cy=%date:~12,2%
rem	Set current month (01-12)
set cm=%date:~4,2%
rem	Set current day of the month (01-31)
set md=%date:~7,2%
Rem	Set current hour
set ch=%time:~0,2%
Rem	Set current minute
Set cmin=%time:~3,2%

rem	Branch to set more vars
if %md% neq 01 goto PRE_NORM
if %cm% neq 01 goto PRE_MTH

rem	Otherwise, it's January 1st
rem	Set previous year
if %cy% geq 11 (set /a py=%cy%-1)
if %cy% == 10 set py=09
if %cy% == 09 set py=08
if %cy% == 08 set py=07
if %cy% == 07 set py=06
if %cy% == 06 set py=05
if %cy% == 05 set py=04
if %cy% == 04 set py=03
if %cy% == 03 set py=02
if %cy% == 02 set py=01
if %cy% == 01 set py=00
if %cy% == 00 set py=99
rem	Set previous month
set pm=12
goto NEW_YEAR

:PRE_MTH
rem	It's February 1st, or March 1st, etc.
rem	Set year it was yesterday
set py=%cy%
rem	Set previous month
if %cm% == 02 set pm=01
if %cm% == 03 set pm=02
if %cm% == 04 set pm=03
if %cm% == 05 set pm=04
if %cm% == 06 set pm=05
if %cm% == 07 set pm=06
if %cm% == 08 set pm=07
if %cm% == 09 set pm=08
if %cm% == 10 set pm=09
if %cm% == 11 set pm=10
if %cm% == 12 set pm=11
goto NEW_MTH

:PRE_NORM
rem	It's not the 1st of any month
rem	Set year it was yesterday
set py=%cy%
rem	Set month it was yesterday
set pm=%cm%



rem	***** NORMAL *****

Set Bat_Step=1
rem 	**ORIG**
rem	Python C:\SRML\bin\AgriMet_prime.py -s CHVO -b 20%cy%/%cm%/01 -e 20%cy%/%cm%/%md% >C:\PC208w\AgriMet\CHRQ%cy%%cm%.txt
rem	if errorlevel 1 goto HNDL_ERR
call timer.bat
call CHVOn.bat
if %flag% EQU 99 goto HNDL_RR
Set Bat_Step=2
rem 	**ORIG**
rem	Python C:\SRML\bin\AgriMet_prime.py -s FOGO -b 20%cy%/%cm%/01 -e 20%cy%/%cm%/%md% >C:\PC208w\AgriMet\FGRQ%cy%%cm%.txt
rem	if errorlevel 1 goto HNDL_ERR
call timer.bat
call FOGOn.bat
if %flag% EQU 99 goto HNDL_RR
Set Bat_Step=3
rem	**ORIG**
rem	Python C:\SRML\bin\AgriMet_prime.py -s MRSO -b 20%cy%/%cm%/01 -e 20%cy%/%cm%/%md% >C:\PC208w\AgriMet\MARQ%cy%%cm%.txt
rem	if errorlevel 1 goto HNDL_ERR
call timer.bat
call MRSOn.bat
if %flag% EQU 99 goto HNDL_RR
Set Bat_Step=4
rem	**ORIG**
rem	Python C:\SRML\bin\AgriMet_prime.py -s PICI -b 20%cy%/%cm%/01 -e 20%cy%/%cm%/%md% >C:\PC208w\AgriMet\PIRQ%cy%%cm%.txt
rem	if errorlevel 1 goto HNDL_ERR
call timer.bat
call PICIn.bat
if %flag% EQU 99 goto HNDL_RR
Set Bat_Step=5
rem	**ORIG**
rem	Python C:\SRML\bin\AgriMet_prime.py -s PMAI -b 20%cy%/%cm%/01 -e 20%cy%/%cm%/%md% >C:\PC208w\AgriMet\PARQ%cy%%cm%.txt
rem	if errorlevel 1 goto HNDL_ERR
call timer.bat
call PMAIn.bat
if %flag% EQU 99 goto HNDL_RR
Set Bat_Step=6
rem	**ORIG**
rem	Python C:\SRML\bin\AgriMet_prime.py -s TWFI -b 20%cy%/%cm%/01 -e 20%cy%/%cm%/%md% >C:\PC208w\AgriMet\TWRQ%cy%%cm%.txt
rem	if errorlevel 1 goto HNDL_ERR
call timer.bat
call TWFIn.bat
if %flag% EQU 99 goto HNDL_RR
Set Bat_Step=7
rem	**ORIG**
rem	Python C:\SRML\bin\AgriMet_prime.py -s ABEI -b 20%cy%/%cm%/01 -e 20%cy%/%cm%/%md% >C:\PC208w\AgriMet\ABRF%cy%%cm%.txt
rem	if errorlevel 1 goto HNDL_ERR
call timer.bat
call ABEIn.bat
if %flag% EQU 99 goto HNDL_RR
Set Bat_Step=8
rem	**ORIG**
rem	Python C:\SRML\bin\AgriMet_prime.py -s HRMO -b 20%cy%/%cm%/01 -e 20%cy%/%cm%/%md% >C:\PC208w\AgriMet\HNRQ%cy%%cm%.txt
rem	if errorlevel 1 goto HNDL_ERR
call timer.bat
call HRMOn.bat
if %flag% EQU 99 goto HNDL_RR
Set Bat_Step=9
goto Archive

rem	***** NEW YEAR *****
:NEW_YEAR

set bat_step=10
rem	**ORIG**
rem	Python C:\SRML\bin\AgriMet_prime.py -s CHVO -b 20%py%/%pm%/01 -e 20%cy%/%cm%/%md% >C:\PC208w\AgriMet\CHRQ%py%%pm%.txt
rem	if errorlevel 1 goto HNDL_ERR
call timer.bat
call CHVOny1.bat
if %flag% EQU 99 goto HNDL_RR
Set Bat_Step=11
rem	**ORIG**
rem	Python C:\SRML\bin\AgriMet_prime.py -s FOGO -b 20%py%/%pm%/01 -e 20%cy%/%cm%/%md% >C:\PC208w\AgriMet\FGRQ%py%%pm%.txt
rem	if errorlevel 1 goto HNDL_ERR
call timer.bat
call FOGOny1.bat
if %flag% EQU 99 goto HNDL_RR
Set Bat_Step=12
rem	**ORIG**
rem	Python C:\SRML\bin\AgriMet_prime.py -s MRSO -b 20%py%/%pm%/01 -e 20%cy%/%cm%/%md% >C:\PC208w\AgriMet\MARQ%py%%pm%.txt
rem	if errorlevel 1 goto HNDL_ERR
call timer.bat
call MRSOny1.bat
if %flag% EQU 99 goto HNDL_RR
Set Bat_Step=13
rem	**ORIG**
rem	Python C:\SRML\bin\AgriMet_prime.py -s PICI -b 20%py%/%pm%/01 -e 20%cy%/%cm%/%md% >C:\PC208w\AgriMet\PIRQ%py%%pm%.txt
rem	if errorlevel 1 goto HNDL_ERR
call timer.bat
call PICIny1.bat
if %flag% EQU 99 goto HNDL_RR
Set Bat_Step=14
rem	**ORIG**
rem	Python C:\SRML\bin\AgriMet_prime.py -s PMAI -b 20%py%/%pm%/01 -e 20%cy%/%cm%/%md% >C:\PC208w\AgriMet\PARQ%py%%pm%.txt
rem	if errorlevel 1 goto HNDL_ERR
call timer.bat
call PMAIny1.bat
if %flag% EQU 99 goto HNDL_RR
Set Bat_Step=15
rem	**ORIG**
rem	Python C:\SRML\bin\AgriMet_prime.py -s TWFI -b 20%py%/%pm%/01 -e 20%cy%/%cm%/%md% >C:\PC208w\AgriMet\TWRQ%py%%pm%.txt
rem	if errorlevel 1 goto HNDL_ERR
call timer.bat
call TWFIny1.bat
if %flag% EQU 99 goto HNDL_RR
Set Bat_Step=16
rem	**ORIG**
rem	Python C:\SRML\bin\AgriMet_prime.py -s ABEI -b 20%py%/%pm%/01 -e 20%cy%/%cm%/%md% >C:\PC208w\AgriMet\ABRF%py%%pm%.txt
rem	if errorlevel 1 goto HNDL_ERR
call timer.bat
call ABEIny1.bat
if %flag% EQU 99 goto HNDL_RR
Set Bat_Step=17
rem	**ORIG**
rem	Python C:\SRML\bin\AgriMet_prime.py -s HRMO -b 20%py%/%pm%/01 -e 20%cy%/%cm%/%md% >C:\PC208w\AgriMet\HNRQ%py%%pm%.txt
rem	if errorlevel 1 goto HNDL_ERR
call timer.bat
call HRMOny1.bat
if %flag% EQU 99 goto HNDL_RR
Set Bat_Step=18
rem	**ORIG**
rem	Python C:\SRML\bin\AgriMet_prime.py -s CHVO -b 20%cy%/%cm%/01 -e 20%cy%/%cm%/%md% >C:\PC208w\AgriMet\CHRQ%cy%%cm%.txt
rem	if errorlevel 1 goto HNDL_ERR
call timer.bat
call CHVOny2.bat
if %flag% EQU 99 goto HNDL_RR
Set Bat_Step=19
rem	**ORIG**
rem	Python C:\SRML\bin\AgriMet_prime.py -s FOGO -b 20%cy%/%cm%/01 -e 20%cy%/%cm%/%md% >C:\PC208w\AgriMet\FGRQ%cy%%cm%.txt
rem	if errorlevel 1 goto HNDL_ERR
call timer.bat
call FOGOny2.bat
if %flag% EQU 99 goto HNDL_RR
Set Bat_Step=20
rem	**ORIG**
rem	Python C:\SRML\bin\AgriMet_prime.py -s MRSO -b 20%cy%/%cm%/01 -e 20%cy%/%cm%/%md% >C:\PC208w\AgriMet\MARQ%cy%%cm%.txt
rem	if errorlevel 1 goto HNDL_ERR
call timer.bat
call MRSOny2.bat
if %flag% EQU 99 goto HNDL_RR
Set Bat_Step=21
rem	**ORIG**
rem	Python C:\SRML\bin\AgriMet_prime.py -s PICI -b 20%cy%/%cm%/01 -e 20%cy%/%cm%/%md% >C:\PC208w\AgriMet\PIRQ%cy%%cm%.txt
rem	if errorlevel 1 goto HNDL_ERR
call timer.bat
call PICIny2.bat
if %flag% EQU 99 goto HNDL_RR
Set Bat_Step=22
rem	**ORIG**
rem	Python C:\SRML\bin\AgriMet_prime.py -s PMAI -b 20%cy%/%cm%/01 -e 20%cy%/%cm%/%md% >C:\PC208w\AgriMet\PARQ%cy%%cm%.txt
rem	if errorlevel 1 goto HNDL_ERR
call timer.bat
call PMAIny2.bat
if %flag% EQU 99 goto HNDL_RR
Set Bat_Step=23
rem	**ORIG**
rem	Python C:\SRML\bin\AgriMet_prime.py -s TWFI -b 20%cy%/%cm%/01 -e 20%cy%/%cm%/%md% >C:\PC208w\AgriMet\TWRQ%cy%%cm%.txt
rem	if errorlevel 1 goto HNDL_ERR
call timer.bat
call TWFIny2.bat
if %flag% EQU 99 goto HNDL_RR
Set Bat_Step=24
rem	**ORIG**
rem	Python C:\SRML\bin\AgriMet_prime.py -s ABEI -b 20%cy%/%cm%/01 -e 20%cy%/%cm%/%md% >C:\PC208w\AgriMet\ABRF%cy%%cm%.txt
rem	if errorlevel 1 goto HNDL_ERR
call timer.bat
call ABEIny2.bat
if %flag% EQU 99 goto HNDL_RR
Set Bat_Step=25
rem	**ORIG**
rem	Python C:\SRML\bin\AgriMet_prime.py -s HRMO -b 20%cy%/%cm%/01 -e 20%cy%/%cm%/%md% >C:\PC208w\AgriMet\HNRQ%cy%%cm%.txt
rem	if errorlevel 1 goto HNDL_ERR
call timer.bat
call HRMOny2.bat
if %flag% EQU 99 goto HNDL_RR
Set Bat_Step=26
perl %bin%\FtpPutFiles.pl download/Archive C:\PC208w\AgriMet\CHRQ%py%%pm%.txt C:\PC208w\AgriMet\FGRQ%py%%pm%.txt C:\PC208w\AgriMet\MARQ%py%%pm%.txt C:\PC208w\AgriMet\PARQ%py%%pm%.txt C:\PC208w\AgriMet\PIRQ%py%%pm%.txt C:\PC208w\AgriMet\TWRQ%py%%pm%.txt C:\PC208w\AgriMet\HNRQ%py%%pm%.txt C:\PC208w\AgriMet\ABRF%py%%pm%.txt

Set Bat_Step=27
GoTo Archive

rem	***** NEW MONTH *****
:NEW_MTH

set Bat_step=28
rem	**ORIG**
rem	Python C:\SRML\bin\AgriMet_prime.py -s CHVO -b 20%cy%/%pm%/01 -e 20%cy%/%cm%/%md% >C:\PC208w\AgriMet\CHRQ%cy%%pm%.txt
rem	if errorlevel 1 goto HNDL_ERR
call timer.bat
call CHVOnm1.bat
if %flag% EQU 99 goto HNDL_RR
Set Bat_Step=29
rem	**ORIG**
rem	Python C:\SRML\bin\AgriMet_prime.py -s FOGO -b 20%cy%/%pm%/01 -e 20%cy%/%cm%/%md% >C:\PC208w\AgriMet\FGRQ%cy%%pm%.txt
rem	if errorlevel 1 goto HNDL_ERR
call timer.bat
call FOGOnm1.bat
if %flag% EQU 99 goto HNDL_RR
Set Bat_Step=30
rem	**ORIG**
rem	Python C:\SRML\bin\AgriMet_prime.py -s MRSO -b 20%cy%/%pm%/01 -e 20%cy%/%cm%/%md% >C:\PC208w\AgriMet\MARQ%cy%%pm%.txt
rem	if errorlevel 1 goto HNDL_ERR
call timer.bat
call MRSOnm1.bat
if %flag% EQU 99 goto HNDL_RR
Set Bat_Step=31
rem	**ORIG**
rem	Python C:\SRML\bin\AgriMet_prime.py -s PICI -b 20%cy%/%pm%/01 -e 20%cy%/%cm%/%md% >C:\PC208w\AgriMet\PIRQ%cy%%pm%.txt
rem	if errorlevel 1 goto HNDL_ERR
call timer.bat
call PICInm1.bat
if %flag% EQU 99 goto HNDL_RR
Set Bat_Step=32
rem	**ORIG**
rem	Python C:\SRML\bin\AgriMet_prime.py -s PMAI -b 20%cy%/%pm%/01 -e 20%cy%/%cm%/%md% >C:\PC208w\AgriMet\PARQ%cy%%pm%.txt
rem	if errorlevel 1 goto HNDL_ERR
call timer.bat
call PMAInm1.bat
if %flag% EQU 99 goto HNDL_RR
Set Bat_Step=33
rem	**ORIG**
rem	Python C:\SRML\bin\AgriMet_prime.py -s TWFI -b 20%cy%/%pm%/01 -e 20%cy%/%cm%/%md% >C:\PC208w\AgriMet\TWRQ%cy%%pm%.txt
rem	if errorlevel 1 goto HNDL_ERR
call timer.bat
call TWFInm1.bat
if %flag% EQU 99 goto HNDL_RR
Set Bat_Step=34
rem	**ORIG**
rem	Python C:\SRML\bin\AgriMet_prime.py -s ABEI -b 20%cy%/%pm%/01 -e 20%cy%/%cm%/%md% >C:\PC208w\AgriMet\ABRF%cy%%pm%.txt
rem	if errorlevel 1 goto HNDL_ERR
call timer.bat
call ABEInm1.bat
if %flag% EQU 99 goto HNDL_RR
Set Bat_Step=35
rem	**ORIG**
rem	Python C:\SRML\bin\AgriMet_prime.py -s HRMO -b 20%cy%/%pm%/01 -e 20%cy%/%cm%/%md% >C:\PC208w\AgriMet\HNRQ%cy%%pm%.txt
rem	if errorlevel 1 goto HNDL_ERR
call timer.bat
call HRMOnm1.bat
if %flag% EQU 99 goto HNDL_RR
Set Bat_Step=36
rem	**ORIG**
rem	Python C:\SRML\bin\AgriMet_prime.py -s CHVO -b 20%cy%/%cm%/01 -e 20%cy%/%cm%/%md% >C:\PC208w\AgriMet\CHRQ%cy%%cm%.txt
rem	if errorlevel 1 goto HNDL_ERR
call timer.bat
call CHVOnm2.bat
if %flag% EQU 99 goto HNDL_RR
Set Bat_Step=37
rem	**ORIG**
rem	Python C:\SRML\bin\AgriMet_prime.py -s FOGO -b 20%cy%/%cm%/01 -e 20%cy%/%cm%/%md% >C:\PC208w\AgriMet\FGRQ%cy%%cm%.txt
rem	if errorlevel 1 goto HNDL_ERR
call timer.bat
call FOGOnm2.bat
if %flag% EQU 99 goto HNDL_RR
Set Bat_Step=38
rem	**ORIG**
rem	Python C:\SRML\bin\AgriMet_prime.py -s MRSO -b 20%cy%/%cm%/01 -e 20%cy%/%cm%/%md% >C:\PC208w\AgriMet\MARQ%cy%%cm%.txt
rem	if errorlevel 1 goto HNDL_ERR
call timer.bat
call MRSOnm2.bat
if %flag% EQU 99 goto HNDL_RR
Set Bat_Step=39
rem	**ORIG**
rem	Python C:\SRML\bin\AgriMet_prime.py -s PICI -b 20%cy%/%cm%/01 -e 20%cy%/%cm%/%md% >C:\PC208w\AgriMet\PIRQ%cy%%cm%.txt
rem	if errorlevel 1 goto HNDL_ERR
call timer.bat
call PICInm2.bat
if %flag% EQU 99 goto HNDL_RR
Set Bat_Step=40
rem	**ORIG**
rem	Python C:\SRML\bin\AgriMet_prime.py -s PMAI -b 20%cy%/%cm%/01 -e 20%cy%/%cm%/%md% >C:\PC208w\AgriMet\PARQ%cy%%cm%.txt
rem	if errorlevel 1 goto HNDL_ERR
call timer.bat
call PMAInm2.bat
if %flag% EQU 99 goto HNDL_RR
Set Bat_Step=41
rem	**ORIG**
rem	Python C:\SRML\bin\AgriMet_prime.py -s TWFI -b 20%cy%/%cm%/01 -e 20%cy%/%cm%/%md% >C:\PC208w\AgriMet\TWRQ%cy%%cm%.txt
rem	if errorlevel 1 goto HNDL_ERR
call timer.bat
call TWFInm2.bat
if %flag% EQU 99 goto HNDL_RR
Set Bat_Step=42
rem	**ORIG**
rem	Python C:\SRML\bin\AgriMet_prime.py -s ABEI -b 20%cy%/%cm%/01 -e 20%cy%/%cm%/%md% >C:\PC208w\AgriMet\ABRF%cy%%cm%.txt
rem	if errorlevel 1 goto HNDL_ERR
call timer.bat
call ABEInm2.bat
if %flag% EQU 99 goto HNDL_RR
Set Bat_Step=43
rem	**ORIG**
rem	Python C:\SRML\bin\AgriMet_prime.py -s HRMO -b 20%cy%/%cm%/01 -e 20%cy%/%cm%/%md% >C:\PC208w\AgriMet\HNRQ%cy%%cm%.txt
rem	if errorlevel 1 goto HNDL_ERR
call timer.bat
call HRMOnm2.bat
if %flag% EQU 99 goto HNDL_RR
Set Bat_Step=44
perl %bin%\FtpPutFiles.pl download/Archive C:\PC208w\AgriMet\CHRQ%cy%%pm%.txt C:\PC208w\AgriMet\FGRQ%cy%%pm%.txt C:\PC208w\AgriMet\MARQ%cy%%pm%.txt C:\PC208w\AgriMet\ABRF%cy%%pm%.txt
perl %bin%\FtpPutFiles.pl download/Archive C:\PC208w\AgriMet\PARQ%cy%%pm%.txt C:\PC208w\AgriMet\PIRQ%cy%%pm%.txt C:\PC208w\AgriMet\TWRQ%cy%%pm%.txt C:\PC208w\AgriMet\HNRQ%cy%%pm%.txt
GoTo Archive

:Archive

Set Bat_Step=45
perl %bin%\FtpPutFiles.pl download/Archive C:\PC208w\AgriMet\CHRQ%cy%%cm%.txt C:\PC208w\AgriMet\FGRQ%cy%%cm%.txt C:\PC208w\AgriMet\MARQ%cy%%cm%.txt C:\PC208w\AgriMet\ABRF%cy%%cm%.txt
perl %bin%\FtpPutFiles.pl download/Archive C:\PC208w\AgriMet\PARQ%cy%%cm%.txt C:\PC208w\AgriMet\PIRQ%cy%%cm%.txt C:\PC208w\AgriMet\TWRQ%cy%%cm%.txt C:\PC208w\AgriMet\HNRQ%cy%%cm%.txt
if errorlevel 1 goto HNDL_ERR

Set Bat_Step=46

rem	***** END OF PROGRAM *****
:END_PGM

echo %date:~4,10% %time% SUCCESS after step %bat_step% in %bat_name% (cy: %cy%, cm: %cm%, py: %py%, pm: %pm%, md: %md%) >> %bat_log%
exit

rem	***** HANDLE ERROR *****
:HNDL_ERR

echo %date:~4,10% %time% ERROR at step %bat_step% in %bat_name% (cy: %cy%, cm: %cm%, py: %py%, pm: %pm%) >> %bat_log%
echo %date:~4,10% %time% ERROR at step %bat_step% in %bat_name% (cy: %cy%, cm: %cm%, ch: %ch%, cmin: %cmin%, py: %py%, pm: %pm%, md: %md%) >> %problem_log%

perl %bin%\FtpPutFiles.pl download/misc %problem_log%
exit
