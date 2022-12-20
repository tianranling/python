from random import randint
import time, sys

a = input("请输入玩家名字：")

# 玩家
class Player:
    @classmethod
    def __init__(self):
        self.stoneNumber = 1000 # 灵石数量
        self.warriors = {}  # 拥有的战士，包括弓箭兵和斧头兵

# 战士
class Warrior:

    # 初始化参数是生命值
    def __init__(self, strength):
        self.strength = strength

    # 用灵石疗伤
    def healing(self, stoneCount):
        # 如果已经到达最大生命值，灵石不起作用，浪费了
        if self.strength == self.maxStrength:
            return

        self.strength += stoneCount

        # 不能超过最大生命值
        if self.strength > self.maxStrength:
            self.strength = self.maxStrength


# 弓箭兵 是 战士的子类
class Archer(Warrior):
    # 种类名称
    typeName = '弓箭兵'

    # 雇佣价 100灵石，属于静态属性
    price = 100

    # 最大生命值 ，属于静态属性
    maxStrength = 100

    # 初始化参数是生命值, 名字
    def __init__(self, name, strength=maxStrength):
        Warrior.__init__(self, strength)
        self.name = name

    # 和妖怪战斗
    def fightWithMonster(self, monster):
        if monster.typeName == '鹰妖':
            self.strength -= 20
        elif monster.typeName == '狼妖':
            self.strength -= 80
        else:
            print('未知类型的妖怪！！！')


# 斧头兵 是 战士的子类
class Axeman(Warrior):
    # 种类名称
    typeName = '斧头兵'

    # 雇佣价 120灵石
    price = 120

    # 最大生命值
    maxStrength = 120

    # 初始化参数是生命值, 名字
    def __init__(self, name, strength=maxStrength):
        Warrior.__init__(self, strength)
        self.name = name

    # 和妖怪战斗
    def fightWithMonster(self, monster):
        if monster.typeName == '鹰妖':
            self.strength -= 80
        elif monster.typeName == '狼妖':
            self.strength -= 20
        else:
            print('未知类型的妖怪！！！')


# 鹰妖
class Eagle():
    typeName = '鹰妖'

# 狼妖
class Wolf():
    typeName = '狼妖'


# 森林
class Forest():
    def __init__(self, monster):
        # 该森林里面的妖怪
        self.monster = monster


print('''
***************************************
****           游戏开始             ****
***************************************

'''
      )

# 森林数量
forest_num = 7

# 森林 列表
forestList = []

# 为每座森林随机产生 鹰妖或者 狼妖
notification = '前方森林里的妖怪是：'  # 显示在屏幕上的内容
for i in range(forest_num):
    typeName = randint(0, 1)
    if typeName == 0:
        forestList.append(Forest(Eagle()))
    else:
        forestList.append(Forest(Wolf()))

    notification += \
        f'第{i + 1}座森林里面是 {forestList[i].monster.typeName}  '

# 显示 妖怪信息
print(notification, end='')
#时间延迟10秒
print("你有10秒钟记忆时间")
time.sleep(10)
print("\n\n\n\n\n\n\n\n\n\n")
player = Player()
print("你所拥有的灵石是：",player.stoneNumber)
gong = int(input("请输入想要雇佣弓箭手的数目："))
a = int(Player.stoneNumber)-int(gong)*int(Archer(Warrior).price)
if a > 0:
    print("你所还剩灵石数目：",a)
    name1 = input("请为你的弓箭手命名：")
    Player.warriors[name1] = Archer(name1)
    Archer(name1)
else:
    print("你所还剩灵石数目：", a)
    print('你的灵石不够')
fu = int(input("请输入想要雇佣斧头兵的数目："))

b = a-int(fu)*int(Axeman(Warrior).price)
if b > 0:
    print("你所还剩灵石数目：", b)
    name2 = input("请为你的斧头兵命名：")
    Player.warriors[name2] = Axeman(name2)
    Axeman(name2)
else:
    print("你所还剩灵石数目：", a)
    print('你的灵石不够')

print(Player.warriors)
List=list(player.warriors.keys())
print("您的战士有：")
print(List)

def ifkey(key):
	if key in player.warriors:
		return key
	else:
		rekey=input("您没有该战士，请重新输入")
		ifkey(rekey)
#每个森林战斗过程
for x in range(1,forest_num):
	fightwarrior=input("这是第"+str(x)+"个森林,请输入你要派出士兵的名字：")
	fightwarrior=ifkey(fightwarrior)
	player.warriors[fightwarrior].fightWithMonster(forestList[x].monster)
	print("该士兵剩余生命值为：")
	print(player.warriors[fightwarrior].strength)

