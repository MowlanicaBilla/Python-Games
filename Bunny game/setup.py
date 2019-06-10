import cx_Freeze
from cx_Freeze import setup, Executable
import sys,os

PYTHON_INSTALL_DIR = os.path.dirname(sys.executable)
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')


buildOptions = dict(packages = ["pygame","math","random"],excludes = [],includes = [],include_files=[(os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),os.path.join('lib', 'tk86t.dll')),(os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),os.path.join('lib', 'tcl86t.dll')),"resources/images/dude.png","resources/images/grass.png","resources/images/castle.png","resources/images/bullet.png","resources/images/badguy.png","resources/images/healthbar.png","resources/images/health.png","resources/images/gameover.png","resources/images/youwin.png","resources/audio/explode.wav","resources/audio/enemy.wav","resources/audio/shoot.wav","resources/audio/moonlight.wav"])

executables = [
    Executable('HelloBunny.py') 
] 
cx_Freeze.setup(
    name = "Hello Bunny",
    description='A game with a cute little bunny as a hero where it protects its castle from badgers and built using Python',options = dict(build_exe = buildOptions),
    executables = executables
)

