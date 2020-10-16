import compiler.cstar_compiler as compiler
import ide.window.gamecode_window as ide


class GameCodeContext:

    version = '1.0.0'

    def __init__(self):
        self.cstar_compiler = compiler.CStarCompiler()
        self.gamecode_ide_window = ide.GameCodeWindow(self)

    def launch(self):
        self.gamecode_ide_window.launch()