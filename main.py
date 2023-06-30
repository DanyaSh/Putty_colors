import winreg

print ("")
print ("This is awesome Putty settings update script!")
print ("---------------------------------------------")

i = 0
with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\SimonTatham\PuTTY\Sessions", 0, 15) as key:
  while 1:
    try:
      subkey = winreg.EnumKey(key, i ) 
      print ("Processing " + subkey + "...")
      with winreg.OpenKey(key, subkey, 0, 15) as session:
        winreg.SetValueEx(session, "Colour14", 0, winreg.REG_SZ, "96,96,255")
        winreg.SetValueEx(session, "Colour15", 0, winreg.REG_SZ, "150,150,255")
        winreg.SetValueEx(session, "ScrollbackLines", 0, winreg.REG_DWORD, 20000)

        winreg.SetValueEx(session, "TermHeight", 0, winreg.REG_DWORD, 40)
        winreg.SetValueEx(session, "TermWidth", 0, winreg.REG_DWORD, 150)

        winreg.SetValueEx(session, "WarnOnClose", 0, winreg.REG_DWORD, 0)
        winreg.SetValueEx(session, "Compression", 0, winreg.REG_DWORD, 1)
        winreg.SetValueEx(session, "FullScreenOnAltEnter", 0, winreg.REG_DWORD, 1)

      i+=1
    except WindowsError:
      break
  
print ("---------------------------------------------")
print ("We are done!")