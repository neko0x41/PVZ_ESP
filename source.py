import pygame
import pymem
import offsets
import time
import win32gui, win32con, win32api

# 创建透明绘制窗口
# 获取游戏数据
# 绘制图形



class Pvz:
    def __init__(self) -> None:

        pygame.init()
        pygame.display.init()
        pygame.font.init()
        self.fuchsia = (255,0,128)
        self.font = pygame.font.Font(pygame.font.match_font("cascadiamonoregular"), 16)
        self.screen = pygame.display.set_mode(flags=pygame.NOFRAME | pygame.DOUBLEBUF)
        self.SetScreen()
        self.ghwnd = win32gui.FindWindow(None, "Plants vs. Zombies")
        self.game = pymem.Pymem("popcapgame1.exe")

    def SetScreen(self) -> None:
        """设置绘画屏幕."""
        hwnd = pygame.display.get_wm_info()["window"]
        sizeX, sizeY = pygame.display.get_window_size()
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT | win32con.WS_EX_TOOLWINDOW)
        win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*self.fuchsia), 0, win32con.LWA_COLORKEY)
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, sizeX, sizeY, 0x0001)
        print("SetScreen Complete.")

    def isFront(self) -> bool:
        """判断游戏窗口是否最前."""
        result = False
        if win32gui.GetForegroundWindow() == self.ghwnd:
            result = True
        return result

    def GetZombies(self) -> list[tuple] | None:
        "获取僵尸坐标."
        zombies = []
        firstValue = self.game.read_int(self.game.read_int(self.game.base_address + offsets.base) + offsets.first)
        try:
            zombieLimit = self.game.read_int(firstValue + offsets.zombieLimit)
        except:
            return None
        zombieAddress = self.game.read_int(firstValue + offsets.zombie)
        for i in range(zombieLimit):
            zombieX = self.game.read_int(zombieAddress + offsets.zombieIntX + (offsets.zombieNext * i))
            zombieY = self.game.read_int(zombieAddress + offsets.zombieIntY + (offsets.zombieNext * i))
            zombieHeal = self.game.read_int(zombieAddress + offsets.zombieHealth + (offsets.zombieNext * i))
            zombieLine = self.game.read_int(zombieAddress + offsets.zombieL + (offsets.zombieNext * i))
            if zombieHeal:
                zombies.append((zombieX, zombieY, zombieHeal, (zombieLimit - i), zombieLine))
        return zombies
        
    def Draw(self, zombie: tuple[int]) -> None:
        "绘制."
        heal = zombie[2]
        number = zombie[3]
        line = zombie[4]
        x, y = win32gui.ClientToScreen(self.ghwnd, zombie[0:2])
        text_list = []
        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(x, y, 100, 100), 2)

        number_text = self.font.render(f"number:{number}", False, (255, 0, 0), None)
        number_width, number_height = number_text.get_size()
        
        text_list.append((number_text, ((x - number_width), y)))

        heal_text = self.font.render(f"health:{heal}", False, (255, 0, 0), None)
        heal_width, heal_height = heal_text.get_size()
        text_list.append((heal_text, ((x - heal_width), (y + number_height))))
        
        self.screen.blits(text_list)
        # print(f"X:{x}  Y:{y}  绘制.")
        return None

    def ClearScreen(self) -> None:
        self.screen.fill(self.fuchsia)
        pygame.display.update()
        return None

    def Update(self) -> None:
        """更新屏幕."""
        self.screen.fill(self.fuchsia)
        point = self.GetZombies()

        if point == None:
            pygame.display.update()
            return None

        for i in point:
            self.Draw(i)
        pygame.display.update()

        return None
    
    def quit(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


if __name__ == "__main__":
    test = Pvz()
    while True:
        if test.GameIsStarted() and test.isFront():
            test.Update()
            time.sleep(0.1)
        else:
            test.ClearScreen()
            time.sleep(0.1)
            
