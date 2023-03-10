base = 0x331C50 # 模块偏移
first = 0x868 # 一级偏移

# Zombie UseFirst
zombieLimit = 0xac # 僵尸上限
zombieQuantity = 0xb8 # 当前僵尸数量
zombie = 0xa8 # 僵尸地址
# Use Zombie
zombieIntX = 0x8 # 僵尸整数X坐标
zombieIntY = 0xc # 僵尸整数Y坐标
zombieX = 0x2c # 僵尸X坐标
zombieY = 0x30 # 僵尸Y坐标
zombieL = 0x1c # 僵尸行数
zombieHealth = 0xc8 # 僵尸生命值
zombieNext = 0x168 # 下一只僵尸

# Card UseFirst
cardFirst = 0x15c # 卡槽2级偏移
cardCD = 0x4c # 卡槽当前CD
cardRequireCD = 0x50 # 卡槽所需CD
cardNext = 0x50 # +50是下一个卡槽

# Sun UseFirst
sun = 0x5578 #阳光

# Item UseFirst
item = 0xfc
visible = 0x18
collect = 0x50
nextItem = 0xd8