from util import *
from emulator import Emulator
from test import *
import shutil
import os


class SkyEmu1(Emulator):
    def __init__(self):
        super().__init__("SkyEmu v1", "https://skyemu.app/", startup_time=0.6)
        self.speed = 1.0
        self.title_check = lambda title: title.startswith("SkyEmu")

    def setup(self):
        download("https://nightly.link/skylersaleh/SkyEmu/actions/runs/2660043561/WindowsRelease.zip", "downloads/SkyEmuv1.zip")
        extract("downloads/SkyEmuv1.zip", "emu/SkyEmuv1")

        self.path = os.path.join("emu", "SkyEmuv1", os.listdir("emu/SkyEmuv1")[0])
        setDPIScaling("%s/SkyEmu.exe" % (self.path))
    
    def startProcess(self, rom, *, model, required_features):
        env = {}
        for k, v in os.environ.items():
            env[k] = v
        model = {DMG: "DMG", CGB: "CGB", SGB: "SGB"}.get(model)
        if model is None:
            return None
        return subprocess.Popen(["%s/SkyEmu.exe" % (self.path), "run_gb_test", os.path.abspath(rom)], cwd=self.path, env=env)

