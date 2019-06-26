
::============================================
::GET THE CURRENT HOUR AND MINUTE + 1 MINUTES
::============================================
SET CURRENTTIME=%TIME%
for /F "tokens=1 delims=:" %%h in ('echo %CURRENTTIME%') do (set /a HR=%%h)
for /F "tokens=2 delims=:" %%m in ('echo %CURRENTTIME%') do (set /a MIN=%%m + 1)


::=======================================================
::IF THE MINUTE IS >= 60, ROLL IT OVER BY SUBSTRACTING 60
::FROM MINUTES AND ADDING 1 TO HOURS
::=======================================================
IF %MIN% GEQ 60 (
	SET /a MIN=%MIN%-60 
	SET /a HR=%HR%+1
)

::===========================================================================
::IF THE HOUR IS > 24, THEN IT IS BECAUSE WE ADDED 1 TO 24 ABOVE. SET IT TO 0
::===========================================================================
IF %HR% GTR 24 SET HR=00


::============================================
::PAD SINGLE DIGIT MINUTES WITH A LEADING ZERO
::============================================
IF %MIN% LEQ 9 (
	SET MIN=0%MIN%
)

::==========================================
::PAD SINGLE DIGIT HOURS WITH A LEADING ZERO
::==========================================
IF %HR% LEQ 9 (
	SET HR=0%HR%
)

::========================================================================
::USE THE NEW HOUR AND MINUTE (AND EXISTING SECONDS) TO CREATE THE NEW TIME
::========================================================================
SET NEWTIME=%HR%:%MIN%:%CURRENTTIME:~6,10%

SET deadline=%NEWTIME%
