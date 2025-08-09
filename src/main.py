
import os
import sys
import subprocess

if __name__ == "__main__":
	# Ejecutar la interfaz principal
	base_path = os.path.dirname(os.path.abspath(__file__))
	ui_path = os.path.join(base_path, "ui", "gui_interface_main.py")
	subprocess.run([sys.executable, ui_path])