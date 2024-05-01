import pygame, sys

file_name = "data/scripts/main.en"
f = open(file_name, "r", encoding='utf-8')

widgets = []
complected_command = []
inputs = {}

RED = (255, 0, 0)
WHILE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

fps = 60
file_font = ""
wait_action = ""
wait_command = {}

data = {}
vars = []

def process_1(input1):
	list = vars[:]
	list.sort(key=len, reverse=True)
	input1 = input1.replace("+", " + ").replace("-", " - ").replace("*", " * ").replace("/", " / ")
	input1 = input1.split(" ")
	for i in range(len(input1)):
		if input1[i] in list:
			input1[i] = f'data["{input1[i]}"]'
	input2 = ""
	for string in input1:
		input2 += string
	print(input2)
	return input2

def read(file):
	global widgets
	loop = True
	while loop:
		string = ""
		loop2 = True
		while loop2:
			a = file.read(1)
			if a == " " or a == "\n" or a == "" or a == ":" or a == ";":
				loop2 = False
			else:
				string += a

		#print("'"+string+"'")

		if string == "init":
			global w, h
			string = ""
			loop2 = True
			while loop2:
				a = file.read(1)
				if a == ",":
					loop2 = False
				else:
					string += a
			w = int(string.replace(" ", ""))
			string = ""
			loop2 = True
			while loop2:
				a = file.read(1)
				if a == ";":
					loop2 = False
					file.read(1)
				else:
					string += a
			h = int(string.replace(" ", ""))

		if string == "font":
			global file_font
			string = ""
			loop2 = True
			while loop2:
				a = file.read(1)
				if a == ";":
					loop2 = False
					file.read(1)
				else:
					string += a
			file_font = string

		if string == "fps":
			global fps
			string = ""
			loop2 = True
			while loop2:
				a = file.read(1)
				if a == ";":
					loop2 = False
					file.read(1)
				else:
					string += a
			fps = int(string.replace(" ", ""))

		if string == "input":
			string = ""
			loop2 = True
			while loop2:
				a = file.read(1)
				if a == ":":
					loop2 = False
				else:
					string += a
			letter = string.replace(" ", "")
			string = ""
			loop2 = True
			while loop2:
				a = file.read(1)
				if a == ";":
					loop2 = False
					file.read(1)
				else:
					string += a
			command = string.replace(" ", "")
			inputs[letter] = command

		if string == "int":
			string = ""
			loop2 = True
			while loop2:
				a = file.read(1)
				if a == "=":
					loop2 = False
				else:
					string += a
			var = string.replace(" ", "")
			string = ""
			loop2 = True
			while loop2:
				a = file.read(1)
				if a == ";":
					file.read(1)
					loop2 = False
				else:
					string += a
			value = string.replace(" ", "")
			data[var] = int(eval(process_1(value)))
			if var not in vars:
				vars.append(var)

		if string == "spr":
			string = ""
			loop2 = True
			while loop2:
				a = file.read(1)
				if a == ",":
					loop2 = False
				else:
					string += a
			x = int(string.replace(" ", ""))
			string = ""
			loop2 = True
			while loop2:
				a = file.read(1)
				if a == ":":
					loop2 = False
				else:
					string += a
			y = int(string.replace(" ", ""))
			string = ""
			loop2 = True
			while loop2:
				a = file.read(1)
				if a == ";":
					loop2 = False
					file.read(1)
				else:
					string += a
			file_name = string.replace(" ", "")
			widgets.append({"type":"sprite", "x":x, "y":y, "file_name":file_name})

		if string == "txt":
			string = ""
			loop2 = True
			while loop2:
				a = file.read(1)
				if a == ":":
					loop2 = False
				else:
					string += a
			id = string.replace(" ", "")
			string = ""
			loop2 = True
			while loop2:
				a = file.read(1)
				if a == ",":
					loop2 = False
				else:
					string += a
			x = int(string.replace(" ", ""))
			string = ""
			loop2 = True
			while loop2:
				a = file.read(1)
				if a == ":":
					loop2 = False
				else:
					string += a
			y = int(string.replace(" ", ""))
			string = ""
			loop2 = True
			while loop2:
				a = file.read(1)
				if a == ":":
					loop2 = False
				else:
					string += a
			font_size = int(string.replace(" ", ""))
			string = ""
			loop2 = True
			while loop2:
				a = file.read(1)
				if a == ";":
					loop2 = False
					file.read(1)
				else:
					string += a
			no_id = True
			for i in range(len(widgets)):
				if widgets[i]["type"] == "text":
					if widgets[i]["id"] == id:
						no_id = False
						if string in vars:
							widgets[i] = {"type":"text", "id":id, "x":x, "y":y, "font_size":font_size, "text":str(eval(process_1(string)))}
						else:
							text = string
							widgets[i] = {"type":"text", "id":id, "x":x, "y":y, "font_size":font_size, "text":text}
			if no_id:
				if string in vars:
					widgets.append({"type":"text", "id":id, "x":x, "y":y, "font_size":font_size, "text":str(eval(process_1(string)))})
				else:
					text = string
					widgets.append({"type":"text", "id":id, "x":x, "y":y, "font_size":font_size, "text":text})

		if string == "bttn":
			string = ""
			loop2 = True
			while loop2:
				a = file.read(1)
				if a == ",":
					loop2 = False
				else:
					string += a
			x = int(string.replace(" ", ""))
			string = ""
			loop2 = True
			while loop2:
				a = file.read(1)
				if a == ",":
					loop2 = False
				else:
					string += a
			y = int(string.replace(" ", ""))
			string = ""
			loop2 = True
			while loop2:
				a = file.read(1)
				if a == ",":
					loop2 = False
				else:
					string += a
			dx = int(string.replace(" ", ""))
			string = ""
			loop2 = True
			while loop2:
				a = file.read(1)
				if a == ":":
					loop2 = False
				else:
					string += a
			dy = int(string.replace(" ", ""))
			string = ""
			loop2 = True
			while loop2:
				a = file.read(1)
				if a == ";":
					loop2 = False
					file.read(1)
				else:
					string += a
			command = string.replace(" ", "")
			widgets.append({"type":"button", "x":x, "y":y, "dx":dx, "dy":dy, "command":command})

		if string == "clear":
			widgets = []
			file.read(1)
			sc.fill(BLACK)

		if string == "wait":
			string = ""
			loop2 = True
			while loop2:
				a = file.read(1)
				if a == ";":
					loop2 = False
					file.read(1)
				else:
					string += a
			time = int(string.replace(" ", ""))
			a=0
			while True:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						sys.exit()
				if a==time*fps:
					break
				a+=1
				for widget in widgets:
					if widget["type"] == "sprite":
						sc.blit(pygame.image.load(widget["file_name"]), (widget["x"], widget["y"]))
					if widget["type"] == "text":
						sc.blit(pygame.font.Font(file_font, widget["font_size"]).render(widget["text"], True, WHILE), (widget["x"], widget["y"]))
				clock.tick(fps)
				pygame.display.update()

		if string == "ldfile":
			global f
			string = ""
			loop2 = True
			while loop2:
				a = file.read(1)
				if a == ";":
					loop2 = False
					file.read(1)
				else:
					string += a
			file_name = string.replace(" ", "")
			f = open(file_name, "r", encoding="utf-8")
			read(f)
			return None

		if string == "//":
			loop2 = True
			while loop2:
				a = file.read(1)
				if a == "\n" or a == "":
					loop2 = False

		if string == "if":
			string = ""
			loop2 = True
			while loop2:
				a = file.read(1)
				if a == "\n":
					loop2 = False
					file.read(2)
				else:
					string += a
			command = string
			actions = []
			com = ""
			while com != "};":
				string = ""
				loop2 = True
				while loop2:
					a = file.read(1)
					if a == " " or a == "\n" or a == "" or a == ":":
						loop2 = False
					else:
						string += a
				com = string
				if string == "spr":
					string = ""
					loop2 = True
					while loop2:
						a = file.read(1)
						if a == ",":
							loop2 = False
						else:
							string += a
					x = int(string.replace(" ", ""))
					string = ""
					loop2 = True
					while loop2:
						a = file.read(1)
						if a == ":":
							loop2 = False
						else:
							string += a
					y = int(string.replace(" ", ""))
					string = ""
					loop2 = True
					while loop2:
						a = file.read(1)
						if a == ";":
							loop2 = False
							file.read(1)
						else:
							string += a
					file_name = string.replace(" ", "")
					actions.append(["spr", {"type":"sprite", "x":x, "y":y, "file_name":file_name}])
		
				if string == "txt":
					string = ""
					loop2 = True
					while loop2:
						a = file.read(1)
						if a == ":":
							loop2 = False
						else:
							string += a
					id = string.replace(" ", "")
					string = ""
					loop2 = True
					while loop2:
						a = file.read(1)
						if a == ",":
							loop2 = False
						else:
							string += a
					x = int(string.replace(" ", ""))
					string = ""
					loop2 = True
					while loop2:
						a = file.read(1)
						if a == ":":
							loop2 = False
						else:
							string += a
					y = int(string.replace(" ", ""))
					string = ""
					loop2 = True
					while loop2:
						a = file.read(1)
						if a == ":":
							loop2 = False
						else:
							string += a
					font_size = int(string.replace(" ", ""))
					string = ""
					loop2 = True
					while loop2:
						a = file.read(1)
						if a == ";":
							loop2 = False
							file.read(1)
						else:
							string += a
					#if string in vars:
					#	widgets.append()
					#	actions.append(["txt", {"type":"text", "id":id, "x":x, "y":y, "font_size":font_size, "text":str(eval(process_1(string)))}])
					#else:
					actions.append(["txt", {"type":"text", "id":id, "x":x, "y":y, "font_size":font_size, "text":string}])
		
				if string == "bttn":
					string = ""
					loop2 = True
					while loop2:
						a = file.read(1)
						if a == ",":
							loop2 = False
						else:
							string += a
					x = int(string.replace(" ", ""))
					string = ""
					loop2 = True
					while loop2:
						a = file.read(1)
						if a == ",":
							loop2 = False
						else:
							string += a
					y = int(string.replace(" ", ""))
					string = ""
					loop2 = True
					while loop2:
						a = file.read(1)
						if a == ",":
							loop2 = False
						else:
							string += a
					dx = int(string.replace(" ", ""))
					string = ""
					loop2 = True
					while loop2:
						a = file.read(1)
						if a == ":":
							loop2 = False
						else:
							string += a
					dy = int(string.replace(" ", ""))
					string = ""
					loop2 = True
					while loop2:
						a = file.read(1)
						if a == ";":
							loop2 = False
							file.read(1)
						else:
							string += a
					command = string.replace(" ", "")
					actions.append(["bttn", {"type":"button", "x":x, "y":y, "dx":dx, "dy":dy, "command":command}])

				if string == "int":
					string = ""
					loop2 = True
					while loop2:
						a = file.read(1)
						if a == "=":
							loop2 = False
						else:
							string += a
					var = string.replace(" ", "")
					string = ""
					loop2 = True
					while loop2:
						a = file.read(1)
						if a == ";":
							file.read(1)
							loop2 = False
						else:
							string += a
					value = string.replace(" ", "")
					#data[var] = int(eval(process_1(value)))
					#if var not in vars:
					#	vars.append(var)
					actions.append(["var", var, value])
		
				if string == "clear;":
					actions.append(["clear"])

			wait_command[command] = actions

		if string == "waitif":
			global wait_action
			string = ""
			loop2 = True
			while loop2:
				a = file.read(1)
				if a == ";":
					loop2 = False
					file.read(1)
				else:
					string += a
			command = string.replace(" ", "")
			wait_action = command
			return None

		if string == "":
			loop = False

read(f)

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
sc = pygame.display.set_mode((w, h))
pygame.display.set_caption('Engine "D"')

game = True

while game:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			pos = event.pos[:]
			for widget in widgets:
				if widget["type"] == "button":
					if widget["x"] <=pos[0]<= widget["dx"] and widget["y"] <=pos[1]<= widget["dy"]:
						complected_command.append(widget["command"])
		elif event.type == pygame.KEYDOWN:
			if event.unicode in inputs:
				complected_command.append(inputs[event.unicode])

	#print(wait_command)

	if wait_action in complected_command:
		for i in range(len(complected_command)):
			if complected_command[i] == wait_action:
				del complected_command[i]
				wait_action = ''
		read(f)
	
	for command in complected_command:
		if command in wait_command:
			for action in wait_command[command]:
				if action[0] != "clear" and action[0] != "txt" and action[0] != "var":
					widgets.append(action[1])
				elif action[0] == "txt":
					no_id = True
					for i in range(len(widgets)):
						if widgets[i]["type"] == "text":
							if widgets[i]["id"] == action[1]["id"]:
								no_id = False
								first_text = action[1]["text"]
								try:
									action[1]["text"] = str(eval(process_1(action[1]["text"])))
								except Exception:
									pass
								widgets[i] = action[1].copy()
								action[1]["text"] = first_text
					if no_id:
						widgets.append(action[1])

				elif action[0] == "var":
					var = action[1]
					value = action[2]
					data[var] = int(eval(process_1(value)))
					if var not in vars:
						vars.append(var)
				else:
					widgets = []
					sc.fill(BLACK)
			for i in range(len(complected_command)):
				try:
					if complected_command[i] == command:
						del complected_command[i]
				except Exception as e:
					error_file = open("log.txt", "a")
					error_file.write("!multitach error"+"\n")
					error_file.close()

	for widget in widgets:
		if widget["type"] == "sprite":
			sc.blit(pygame.image.load(widget["file_name"]), (widget["x"], widget["y"]))
		if widget["type"] == "text":
			sc.blit(pygame.font.Font(file_font, widget["font_size"]).render(widget["text"], True, WHILE), (widget["x"], widget["y"]))

	clock.tick(fps)
	pygame.display.update()