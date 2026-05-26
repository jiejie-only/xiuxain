"""战斗系统"""

import random
from game.config import ENEMIES


def battle(player, enemy_name=None):
    """一场战斗，返回 True 胜利 False 失败"""
    if enemy_name is None:
        enemy_name = get_random_enemy(player.level)
    if enemy_name is None:
        print("此处并无危险。")
        return True

    enemy_data = ENEMIES[enemy_name]
    enemy = {
        "name": enemy_name,
        "hp": enemy_data["hp"],
        "max_hp": enemy_data["hp"],
        "attack": enemy_data["attack"],
        "exp": enemy_data["exp"],
        "drops": enemy_data.get("drops", {}),
    }

    print(f"\n{'!'*30}")
    print(f"  遭遇敌人: {enemy_name}！")
    print(f"  生命: {enemy['hp']}  攻击: {enemy['attack']}")
    print(f"{'!'*30}")

    turn = 0
    while player.is_alive() and enemy["hp"] > 0:
        turn += 1
        print(f"\n--- 第{turn}回合 ---")
        print(f"  你的生命: {player.hp}/{player.max_hp}  灵力: {player.mp}/{player.max_mp}")
        print(f"  {enemy_name}生命: {enemy['hp']}/{enemy['max_hp']}")
        print()
        print("  1. 攻击")
        print("  2. 使用功法（消耗20灵力）")
        print("  3. 使用道具")
        print("  4. 逃跑")

        choice = input("\n选择行动: ").strip()

        if choice == "1":
            # 普通攻击
            damage = max(1, player.attack + random.randint(-2, 5) - random.randint(0, 3))
            crit = random.randint(1, 100) <= 10
            if crit:
                damage = int(damage * 2)
                print(f"  暴击！你对{enemy_name}造成了{damage}点伤害！")
            else:
                print(f"  你对{enemy_name}造成了{damage}点伤害。")
            enemy["hp"] -= damage

        elif choice == "2":
            if player.mp < 20:
                print("  灵力不足！")
                continue
            player.mp -= 20
            damage = int(player.attack * 1.8) + random.randint(5, 15)
            skill_name = player.skills[-1] if player.skills else "基础拳法"
            print(f"  你使出「{skill_name}」，对{enemy_name}造成了{damage}点伤害！")
            enemy["hp"] -= damage

        elif choice == "3":
            player.show_inventory()
            if not player.inventory:
                print("  没有可用道具。")
                continue
            item = input("  使用什么道具（回车取消）: ").strip()
            if item:
                player.use_item(item)
            else:
                continue

        elif choice == "4":
            if random.randint(1, 100) <= 40 + player.luck // 2:
                print("  你成功逃离了战斗！")
                return False
            else:
                print("  逃跑失败！")
        else:
            print("  无效选择，你发呆了一回合。")

        # 敌人回合
        if enemy["hp"] > 0:
            enemy_dmg = max(1, enemy["attack"] + random.randint(-3, 3) - player.defense)
            player.hp -= enemy_dmg
            print(f"  {enemy_name}对你造成了{enemy_dmg}点伤害。")

    if not player.is_alive():
        print(f"\n你被{enemy_name}击败了……")
        print("道消身殒。")
        return False

    # 胜利
    print(f"\n{'='*30}")
    print(f"  击败了{enemy_name}！")
    print(f"{'='*30}")
    player.gain_exp(enemy["exp"])

    # 掉落
    for item, rate in enemy["drops"].items():
        if random.random() < rate:
            player.add_item(item)

    # 灵石掉落
    stones = random.randint(1, 5)
    player.spirit_stones += stones
    print(f"获得 {stones} 块灵石。")

    return True


def get_random_enemy(player_level):
    """根据玩家等级获取合适的敌人"""
    suitable = []
    for name, data in ENEMIES.items():
        if data["level"] <= player_level + 3:
            suitable.append(name)
    if not suitable:
        return None
    return random.choice(suitable)
