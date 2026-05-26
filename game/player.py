"""玩家角色系统"""

import random
from game.config import REALMS, SPIRIT_ROOTS


class Player:
    def __init__(self):
        self.name = "无名"
        self.realm = "淬体"       # 当前境界
        self.realm_idx = 0        # 境界索引
        self.level = 1
        self.exp = 0
        self.exp_to_next = 100
        self.hp = 100
        self.max_hp = 100
        self.mp = 50
        self.max_mp = 50
        self.attack = 10
        self.defense = 5
        self.spirit_root = "下品火灵根"
        self.skills = ["基础拳法"]
        self.inventory = {"回气丹": 3, "疗伤丹": 2}
        self.alignment = "中立"
        self.lifespan = 100
        self.age = 16
        self.luck = 10
        self.karma = 0
        self.sect = None
        self.sect_rank = None
        self.silver = 50
        self.spirit_stones = 0
        self.kill_count = 0
        self.quests_done = []
        self.story_stage = 1
        self.tribulation_count = 0

    def status(self):
        print(f"\n{'='*40}")
        print(f"  道号: {self.name}")
        print(f"  境界: {self.realm} (Lv.{self.level})")
        print(f"  灵根: {self.spirit_root}")
        print(f"  年龄: {self.age} / 寿元: {self.lifespan}")
        print(f"  生命: {self.hp}/{self.max_hp}  灵力: {self.mp}/{self.max_mp}")
        print(f"  攻击: {self.attack}  防御: {self.defense}")
        print(f"  经验: {self.exp}/{self.exp_to_next}")
        print(f"  气运: {self.luck}  因果: {self.karma}")
        print(f"  灵石: {self.spirit_stones}  银两: {self.silver}")
        print(f"  阵营: {self.alignment}")
        if self.sect:
            print(f"  宗门: {self.sect} [{self.sect_rank}]")
        print(f"  功法: {', '.join(self.skills)}")
        print(f"{'='*40}")

    def gain_exp(self, amount):
        self.exp += amount
        print(f"获得 {amount} 点修为。")
        while self.exp >= self.exp_to_next:
            self.level_up()

    def level_up(self):
        self.exp -= self.exp_to_next
        self.level += 1
        self.exp_to_next = int(self.exp_to_next * 1.3)
        self.max_hp += 15
        self.max_mp += 8
        self.attack += 3
        self.defense += 2
        self.hp = self.max_hp
        self.mp = self.max_mp
        print(f"\n修为精进！等级提升至 Lv.{self.level}")

    def is_alive(self):
        return self.hp > 0

    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)
        print(f"恢复了 {amount} 点生命。当前: {self.hp}/{self.max_hp}")

    def restore_mp(self, amount):
        self.mp = min(self.max_mp, self.mp + amount)
        print(f"恢复了 {amount} 点灵力。当前: {self.mp}/{self.max_mp}")

    def show_inventory(self):
        print(f"\n{'='*30}")
        print("  储物袋")
        print(f"{'='*30}")
        if not self.inventory:
            print("  空空如也。")
        else:
            for item, count in self.inventory.items():
                print(f"  {item} x{count}")
        print(f"{'='*30}")

    def use_item(self, item_name):
        if item_name not in self.inventory or self.inventory[item_name] <= 0:
            print(f"你没有{item_name}。")
            return False
        self.inventory[item_name] -= 1
        if self.inventory[item_name] <= 0:
            del self.inventory[item_name]

        if item_name == "回气丹":
            self.restore_mp(30)
        elif item_name == "疗伤丹":
            self.heal(50)
        elif item_name == "破境丹":
            print("破境丹已准备，突破时使用。")
            return True
        elif item_name == "延寿丹":
            self.lifespan += 20
            print(f"寿元增加20年。当前寿元: {self.lifespan}")
        else:
            print(f"使用了{item_name}。")
        return True

    def add_item(self, item_name, count=1):
        self.inventory[item_name] = self.inventory.get(item_name, 0) + count
        print(f"获得 {item_name} x{count}")

    def to_dict(self):
        return vars(self).copy()

    @classmethod
    def from_dict(cls, data):
        p = cls()
        for k, v in data.items():
            setattr(p, k, v)
        return p


def create_player():
    player = Player()

    print("\n请输入你的道号（直接回车随机生成）:")
    name = input("> ").strip()
    if name:
        player.name = name
    else:
        names = ["李逍遥", "叶凡", "林动", "萧炎", "韩立", "石昊", "孟浩", "王林"]
        player.name = random.choice(names)
        print(f"仙人赐你道号：{player.name}")

    print("\n你曾是何人？")
    print("1. 猎户 - 根骨+3")
    print("2. 书生 - 悟性+3")
    print("3. 乞丐 - 气运+3")
    print("4. 药童 - 寿元+10")
    print("5. 死囚 - 杀意+5，攻击+5")

    while True:
        origin = input("\n选择出身: ").strip()
        if origin == "1":
            print("你曾是深山猎户，与虎狼为伴。")
            break
        elif origin == "2":
            print("你曾是赶考书生，满腹经纶。")
            break
        elif origin == "3":
            print("你曾是街边乞丐，命如草芥。")
            break
        elif origin == "4":
            print("你曾是药铺童子，识得百草。")
            player.lifespan += 10
            player.add_item("疗伤丹", 2)
            break
        elif origin == "5":
            print("你曾是死囚，刀口舔血。")
            player.attack += 5
            break
        else:
            print("无效选择。")

    # 随机灵根
    roll = random.randint(1, 100)
    if roll <= 5:
        player.spirit_root = "天灵根"
        print(f"\n仙人检测灵根，金光大放！你是{player.spirit_root}！")
    elif roll <= 20:
        player.spirit_root = "上品灵根"
        print(f"\n仙人检测灵根，灵光闪动。你是{player.spirit_root}。")
    elif roll <= 50:
        player.spirit_root = "中品灵根"
        print(f"\n仙人检测灵根，略有灵光。你是{player.spirit_root}。")
    else:
        player.spirit_root = "下品灵根"
        print(f"\n仙人检测灵根，光芒微弱。你是{player.spirit_root}。")

    print('\n仙人道："' + player.name + '，你既有仙缘，便入我门下。"')
    print("自此，你踏入修仙之路。\n")

    return player
