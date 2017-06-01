
:: '@echo off' is so we dont see a cmd prompt printed out.
@echo off

:: get the filename
set /p converter_input_file_path="enter the filename (or path/filename): "

:: enter blank line
echo.

:: are we converting from MS/DOS line endings to UNIX, or vice versa?
echo enter 0 for converting DOS text file to UNIX,
set /p converter_direction="enter non-zero value to convert in the opposite direction: "

if "%converter_direction%"=="0" (
    set internal_converter_direction=0
) else (
    set internal_converter_direction=1
)

python line_ending_converter.py %converter_input_file_path% %internal_converter_direction%


pause
