from util import *
from emulator import Emulator
from test import *
import shutil
import os


class SkyEmu(Emulator):
    def __init__(self):
        super().__init__("SkyEmu", "https://skyemu.app/", startup_time=0.6)
        self.speed = 1.0

    def setup(self):
        download("https://nightly.link/skylersaleh/SkyEmu/workflows/deploy_win/dev/WindowsRelease.zip", "downloads/SkyEmu.zip")
        extract("downloads/SkyEmu.zip", "emu/SkyEmu")

        self.path = os.path.join("emu", "SkyEmu", os.listdir("emu/SkyEmu")[0])
        setDPIScaling("%s/SkyEmu.exe" % (self.path))
    
    def startProcess(self, rom, *, model, required_features):
        env = {}
        for k, v in os.environ.items():
            env[k] = v
        model = {DMG: "DMG", CGB: "CGB", SGB: "SGB"}.get(model)
        if model is None:
            return None
        return subprocess.Popen(["%s/SkyEmu.exe" % (self.path), "run_gb_test", os.path.abspath(rom)], cwd=self.path, env=env)

