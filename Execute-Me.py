import subprocess
import os
import time
os.system("cls")
from CTN_HI import ForeGroundColor as fg,BackGroundColor as bg,Default as Dt, Style as St
print(f"{fg.get('Blue')};{St.get('Concealed_Style')};{bg.get('LightGreen')}m Comming Soon This Program Is In Development {Dt.get('Default_Color')}m {Dt.get('Riset')}\n")
time.sleep(3)
subprocess.run(["python", "main.py"])