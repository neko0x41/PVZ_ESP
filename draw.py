import pygame
import win32api, win32gui, win32con

class Draw:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.init()
        pygame.font.init()
        self.font = pygame.font.Font(pygame.font.match_font("cascadiamonoregular"), 16)
        self.fuchsia = (255,0,128)
        self.screen = pygame.display.set_mode(flags=pygame.NOFRAME | pygame.DOUBLEBUF)
        sizeX, sizeY = pygame.display.get_window_size()
        self.hwnd = pygame.display.get_wm_info()["window"]
        win32gui.SetWindowLong(self.hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(self.hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED |win32con.WS_EX_TRANSPARENT)
        win32gui.SetLayeredWindowAttributes(self.hwnd, win32api.RGB(*self.fuchsia), 0, win32con.LWA_COLORKEY)
        win32gui.SetWindowPos(self.hwnd, win32con.HWND_TOPMOST, 0, 0, sizeX, sizeY, 0x0001)

    def CleanScreen(self) -> None:
        self.screen.fill(self.fuchsia)
        return None

    def Update(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()
        return None
    
    def GetHealthText(self, health: int) -> pygame.Surface:
        return self.font.render(f"health:{health}", False, (255, 0, 0), None)
    
    def DrawText(self, surface: pygame.Surface, rectPoint: tuple) -> None:
        width, height = surface.get_size()
        rectX, rectY = rectPoint
        self.screen.blit(surface, (rectX - width, rectY))
        return None

    def DrawRect(self, x, y) -> None:
        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(x, y, 100, 100), 2)
        return None

if __name__ == "__main__":
    Draw()