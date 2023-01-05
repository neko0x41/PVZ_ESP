import pymem
import win32
import win32gui

import offsets


class PVZ:
    def __init__(self) -> None:
        self.hwnd = win32gui.FindWindow(None, "Plants vs. Zombies")
        self.game = pymem.Pymem("popcapgame1.exe")
        self.baseAddress = self.game.read_int(self.game.base_address + offsets.off_base)
        self.firstAddress = self.game.read_int(self.baseAddress + offsets.off_first)
        self.zombieAddress = self.game.read_int(self.firstAddress + offsets.off_zombie)


    def isFront(self) -> bool:
        """判断窗口是否在最前方."""

        result = False
        if win32gui.GetForegroundWindow() == self.hwnd:
            result = True
        return result

    def GetZombiePoint(self, zombie: int) -> tuple:
        zombieX = self.game.read_float(self.zombieAddress + offsets.off_zombieX + (offsets.off_zombieNext * zombie))
        zombieY = self.game.read_float(self.zombieAddress + offsets.off_zombieY + (offsets.off_zombieNext * zombie))
        return (int(zombieX), int(zombieY))

    def GetZombieQuantity(self) -> int:
        return self.game.read_int(self.firstAddress + offsets.off_zombieQuantity)

    def ClientToScreen(self, point: tuple):
        return win32gui.ClientToScreen(self.hwnd, point)

    def GetZombieHealth(self, zombie: int) -> int:
        return self.game.read_int(self.zombieAddress + offsets.off_zombieHealth + (offsets.off_zombieNext * zombie))
    
    def GetLimit(self) -> int:
        return self.game.read_int(self.firstAddress + offsets.off_zombieLimit)

