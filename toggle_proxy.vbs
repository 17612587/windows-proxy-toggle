Set WshShell = CreateObject("WScript.Shell")
Set FSO = CreateObject("Scripting.FileSystemObject")

scriptDir = FSO.GetParentFolderName(WScript.ScriptFullName)
pyPath = scriptDir & "\toggle_proxy.py"

WshShell.Run "pyw """ & pyPath & """", 0, True

Set WshShell = Nothing
Set FSO = Nothing
