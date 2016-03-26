@echo off

:: Reset global variables to avoid leaking
set "contMod1="
set "cont=
set "contMod=
set "target=

SetLocal EnableDelayedExpansion

if Not "%~1" == "" (
    if "%~1" == "-g" ( :: Generating documentation
        if Not "%~2" == "" ( :: The target is given
            set target= %2
            goto Docs
        ) else ( :: The target is not given
            set /p target= "What form of documentation do you want to generate: "
            goto Docs
        )
    ) else if "%~1" == "-m" ( :: Installing modules
        goto Modules
    ) else ( :: Something else
        echo "Unkown Command"
        goto Help
    )
) else (
    goto Help
)

:Docs
set /p contMod= "Install Modules?[y/n]: "
echo.

if "!contMod!" == "y" (
    goto Modules
) else if "!contMod!" == "n" (
    echo.
) else if "!contMod!" == "" (
    echo Unkown command, assuming yes
    goto Modules
)

cd docs
echo Generating docs
echo.
call make clean :: To avoid random errors
call make !target! && ( :: Executed on success
    echo.
    cd ..
) || ( :: Executed on failure
    cd ..
    echo Making documentation failed
    echo Could it be an unsupported form of documentation?
    echo Please assert that modules have been installed already
    echo.

    set /p contMod1= "Install Modules?[y/n]: "
    echo.

    if "!contMod1!" == "y" (
        goto Modules
    ) else if "!contMod1!" == "n" (
        echo.
    ) else (
        echo Unkown command, assuming yes
        goto Modules
    )
)

goto Done

:Modules
echo Installing modules
pip3 install -r requirements.txt && (
    echo.
) || (
    echo Installation of required modules failed
    echo Make sure Python 3 and pip3 are installed
)

goto Done

:Help
echo Proper Usage: ./setup [Flags]
echo [Flags]:
echo     -g [type]
echo        -- Generates documentation of type [type], if type is not provided, the program asks for type
echo     -m
echo        -- Installs pip modules
echo.
goto Exit

:Done
echo Setup Completed
echo.

:Exit


EndLocal
