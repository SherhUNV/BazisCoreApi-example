@echo off
echo Hello, programmer
copy ".\bin\Debug\net8.0\TestLib.dll" ".\..\PythonAPI\src\BazisCoreAPI\libs\"
cd ".\..\PythonAPI"
echo "start build package"
start ".\..\TestLib\bats\BuildPythonPackage.bat"
cd ".\..\TestAPIConnection"
echo "start update deps"
start ".\..\TestLib\bats\UpdateDeps.bat"
