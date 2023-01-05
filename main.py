from draw import Draw
import time
from memory import PVZ

if __name__ == "__main__":
    keeping = True
    screen = Draw()
    game = PVZ()
    while keeping:
        if game.isFront() == False:
            screen.CleanScreen()
            screen.Update()
            time.sleep(1)
            continue

        quantity = game.GetZombieQuantity()
        limit = game.GetLimit()
        screen.CleanScreen()
        for zombie in range(limit):
            zombieHealth = game.GetZombieHealth(zombie)
            zombiePoint = game.GetZombiePoint(zombie)
            if (zombieHealth == 0) or (zombiePoint[0] < 1) or (zombiePoint[0] > 1300):
                continue
            healthText = screen.GetHealthText(zombieHealth)
            screenPoint = game.ClientToScreen(tuple(map(int, zombiePoint)))
            screen.DrawRect(*screenPoint)
            screen.DrawText(healthText, screenPoint)

        screen.Update()
        time.sleep(0.5)