import os
import webbrowser as wb

def workstation():
	workebchPath = "/usr/bin/mysql-workbench"
	nppPath = "/snap/bin/notepad-plus-plus"
	pycharPath = "/snap/bin/pycharm-community"
	os.popen(workebchPath)
	os.popen(nppPath)
	os.popen(pycharPath)
	chrome_path = '/usr/bin/google-chrome'#ADD THE PATH OF CHROME HERE
	URLS = (
	        "https://teams.microsoft.com/go#",
	        "https://github.com/",
	        "https://outlook.office.com/mail/inbox",
	        "https://diwo.atlassian.net/wiki/spaces/CPDT/pages/240943293/TEMP+table+design+version+2.0"
	        )#ADD THE WEBSITES YOU USE WHIE WORKING
	for url in URLS:
		wb.get(chrome_path).open(url)
workstation()