#  -----  #
# neko0x41
# 2023年1月11日17:56:22
#  -----  #

import source
import time

if __name__ == "__main__":
    pvz = source.Pvz()
    while True:
        pvz.quit()
        if pvz.isFront():
            pvz.Update()
        else:
            pvz.ClearScreen()
            time.sleep(0.1)