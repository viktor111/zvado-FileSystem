import os 
import subprocess

def launch_vim(file_name):
	command = ["vim", file_name]
	subprocess.call(command)

def launch_vscode():
	command = ["code", "."]
	subprocess.call(command)

def display_file_dat(filename):
	f = open(filename)
	print(f.read())
	f.close()

def list_files():
	array_of_items = os.listdir()
	result = ""
	for item in array_of_items:
		result += f"	{item}" 
	print(result)

def change_dir(new_dir):
	try:
		result = os.chdir(new_dir)
	except FileNotFoundError:
		print("[-] File not found")

def get_current_dir():
	print(os.getcwd())

def go_back(how_much_back):
	if how_much_back is None or 0: 
		print("[-] add correct number")
		return
	curren_working_dir = os.getcwd()
	array_of_dirs = curren_working_dir.split("/")
	for i in range(how_much_back):
		array_of_dirs.pop()

	new_dir = ""
	for i in array_of_dirs:
		dir_part = f"/{i}"
		new_dir += dir_part
	new_dir = new_dir[1 : : ]
	change_dir(new_dir)

def read_command():
	current_working_dir = os.getcwd()
	command = input(f"{current_working_dir} >")
	if "list" in command:
		list_files()
	
	if "go" in command:
		try:
			array_commands = command.split()
			new_dir = array_commands[1]
		except IndexError:
			read_command()
		change_dir(new_dir)

	if "cur" in command:
		get_current_dir()
	if "back" in command:
		try:
			array_commands = command.split()
			how_much_back = array_commands[1] 
		except IndexError:
			read_command()
		go_back(int(how_much_back))
	if "read" in command:
		try:
			array_commands = command.split()
			filename = array_commands[1]
		except IndexError:
			read_command()
		display_file_dat(filename)
	if "code ." in command:
		print("[+] Launching VSCode.....")
		launch_vscode()
	if "vim" in command:
		try:
			array_commands = command.split()
			file_name = array_commands[1]
		except IndexError:
			read_command()
		print("[+] Launching vim.....")
		launch_vim(file_name)
while True:
	read_command()
