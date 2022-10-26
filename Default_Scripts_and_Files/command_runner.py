#########################################################################################################
# Developed by Raging Bits. (2022)																		#
# This code is provided free and to be used at users own responsability.								#
#########################################################################################################
import subprocess
import os
import re
import time
import queue 
import socket,os
from subprocess import PIPE, Popen
from threading  import Thread
import io
import os.path
from pathlib import Path
import sys
import platform 



def main():
	
	#Declaration of globals to use.
	print("Simple Command executer.")
	while(1):
	
		for file_name in os.listdir('.'):
			if re.match('simple_command', file_name):
				print("New file: ")
				f = open(file_name, "r")
				lines = f.readlines()
				f.close()
				os.remove(file_name)
				
				for command in lines:
					
					print(command)
					proc = subprocess.run([command],shell=True,stdout=subprocess.PIPE)
					f = open("simple.command.out.txt", "a")
					f.write(proc.stdout.decode('utf-8'))
					f.flush()
					f.close()
					subprocess.call(['chmod', '0777', 'simple.command.out.txt'])
			

	
		time.sleep(1)
	
	print("Exiting Simple Command executer.")
	
	
if __name__ == "__main__":
	main()
