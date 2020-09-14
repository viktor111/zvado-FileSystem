import os 
import threading
import sys
import subprocess
import socket

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

def list_info():
	info = os.uname()
	for i in info:
		print(i)

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

def create_dir(name):
	current_dir = get_current_dir()
	try:
		os.mkdir(name)
	except FileExistsError:
		print(f"[-] Dir with name - {name} - already exists")
	
def delete_dir(name):
	try:
		os.rmdir(name)	
	except (NotADirectoryError, FileNotFoundError):
		print("[-] Not a direcotry to remove")

def create_file(name):
	new_file = open(name, "w")
	new_file.close()

def delete_file(name):
	try:
		os.remove(name)
	except (PermissionError , FileNotFoundError):
		print("[-] Not a file to remove")

def threaded_port_scan(url):
	remote_server_ip = socket.gethostbyname(url)
	print(remote_server_ip)
	return
	

def read_command():
	current_working_dir = os.getcwd()
	current_logged_user = os.getlogin()
	try:
		command = input(f"{current_logged_user}@{current_working_dir} >")
	except KeyboardInterrupt:
		print("[+] Exiting....")
		sys.exit()
		
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
	if "newd" in command:
		try:
			array_commands = command.split()
			name = array_commands[1]
		except IndexError:
			print("[-] Please provide a name for new dir")
			read_command()
		create_dir(name)
	if "rmd" in command:
		try:
			array_commands = command.split()
			name = array_commands[1]
		except IndexError:
			print("[-] Provide name to delete dir")
		delete_dir(name)
	if "newf" in command:
		try:
			array_commands = command.split()
			name = array_commands[1]
		except IndexError:
			print("[-] Provide file name to create")
			read_command()
		create_file(name)
	if "rmf" in command:
		try:
			array_commands = command.split()
			name = array_commands[1]
		except IndexError:
			print("[-] Provide file name to delete")
			read_command()
		delete_file(name)
	if "usr" in command:
		print(os.getlogin())
	if "linfo" in command:
		list_info()
	if "portscan" in command:
		try:
			array_commands = command.split()
			url = array_commands[1]
		except IndexError:
			print("[-] Provide more arguments")	
			read_command()
		thread1 = threading.Thread(target=threaded_port_scan, args=[url])
		thread1.start()

def main_thread():
	while True:
		read_command()

main_program = threading.Thread(target=main_thread())
main_program.start()
