import os
import sys
from termcolor import colored



def gl():
	g = 'git clone https://github.com/'
	i = 0
	update = 'sudo apt-get update'
	upgrade = 'sudo apt-get upgrade -y'
	os.system(update)
	os.system(upgrade)
	while i != 18:
		i += 1
		if i == 1:
			l = 'tegal1337/CiLocks'
			gl = g + l
			os.system(gl)
			print(colored('[+] CiLocks Is Downloaded For "bruteforce" Catagory', 'green'))

		if i == 2:
			l = 'yaron4u/EnigmaCracker'
			gl = g + l
			os.system(gl)
			print(colored('[+] EnigmaCracker Is Downloaded For "bruteforce" Catagory', 'green'))

		if i == 3:
			l = 'Ultrasecurity/DarkSide'
			gl = g + l
			os.system(gl)
			print(colored('[+] DarkSide Is Downloaded For "framework" Catagory', 'green'))

		if i == 4:
			l = 'hestihesti/HackingComm'
			gl = g + l
			os.system(gl)
			print(colored('[+] HackingComm Is Downloaded For "hestihesti" Catagory', 'green'))

		if i == 5:
			l = 'BullsEye0/dorks-eye'
			gl = g + l
			os.system(gl)
			print(colored('[+] dorks-eye Is Downloaded For "InfoGather" Catagory', 'green'))

		if i == 6:
			l = 'megadose/holehe'
			gl = g + l
			os.system(gl)
			print(colored('[+] holehe Is Downloaded For "InfoGather" Catagory', 'green'))

		if i == 7:
			pre = '--depth 1 '
			l = 'radenvodka/Recsech.git Recsech'
			gl = g + pre + l
			os.system(gl)
			print(colored('[+] Recsech Is Downloaded For "InfoGather" Catagory', 'green'))

		if i == 8:
			cmd = 'curl https://raw.githubusercontent.com/d4rckh/vaf/main/install.sh | sudo bash'
			gl = cmd
			os.system(gl)
			print(colored('[+] vaf Is Downloaded For "vuln-analysis" Catagory', 'green'))

		if i == 9:
			l = 'Moham3dRiahi/XAttacker'
			gl = g + l
			os.system(gl)
			print(colored('[+] XAttacker Is Downloaded For "vuln-analysis" Catagory', 'green'))

		if i == 10:
			l = 'indiancybertroops/click-sec'
			gl = g + l
			os.system(gl)
			print(colored('[+] click-sec Is Downloaded For "web-app" Catagory', 'green'))

		if i == 11:
			l = 'MrH0wl/Cloudmare'
			gl = g + l
			os.system(gl)
			print(colored('[+] Cloudmare Is Downloaded For "web-app" Catagory', 'green'))

		if i == 12:
			l = 'elceef/dnstwist'
			gl = g + l
			os.system(gl)
			print(colored('[+] dnstwist Is Downloaded For "web-app" Catagory', 'green'))

		if i == 13:
			l = 'zidansec/subscan'
			gl = g + l
			os.system(gl)
			print(colored('[+] subscan Is Downloaded For "web-app" Catagory', 'green'))

		if i == 14:
			l = 's0lst1c3/eaphammer'
			gl = g + l
			os.system(gl)
			print(colored('[+] eaphammer Is Downloaded For "wifi" Catagory', 'green'))


		if i == 15:
			l = 'ZerBea/hcxdumptool'
			gl = g + l
			os.system(gl)
			print(colored('[+] hcxdumptool Is Downloaded For "wifi" Catagory', 'green'))


		if i == 16:
			l = 'ZerBea/hcxtools'
			gl = g + l
			os.system(gl)
			print(colored('[+] hcxtool Is Downloaded For "wifi" Catagory', 'green'))


		if i == 17:
			l = 'hestihesti/bad-news'
			gl = g + l
			os.system(gl)
			print(colored('[+] bad-news Is Downloaded For "hestihesti" Catagory', 'green'))

		if i == 18:
			l = 'chorankates/Blunder'
			gl = g + l
			os.system(gl)
			print(colored('[+] Blunder Is Downloaded For "framework" Catagory', 'green'))

		if i == 18:
			print('Goodbye')


gl()
