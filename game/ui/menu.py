"""主菜单与游戏循环"""

import random
from game.cultivation import cultivate, closed_door_cultivate, breakthrough
from game.combat import battle
from game.events import trigger_random_event
from game.story import check_story
from game.save_manager import save_game
from game.config import SECTS, TECHNIQUES, ITEMS


def main_loop(player):
    """主游戏循环"""
    print(f"\n欢迎进入修仙世界，{player.name}。")
    print("输入数字选择行动。\n")

    while player.is_alive():
        # 检查剧情
        if player.story_stage <= 5:
            check_story(player)
        if player.story_stage >= 6:
            print("\n游戏结束。感谢游玩《长生劫》！")
            break

        # 显示状态栏
        print(f"\n  [{player.realm}] {player.name} | Lv.{player.level} | HP:{player.hp}/{player.max_hp} | MP:{player.mp}/{player.max_mp} | 年龄:{player.age}")
        print()

        print("  1. 修炼")
        print("  2. 探索")
        print("  3. 突破境界")
        print("  4. 查看状态")
        print("  5. 储物袋")
        print("  6. 商店")
        print("  7. 宗门")
        print("  8. 存档")
        print("  9. 退出游戏")

        choice = input("\n行动: ").strip()

        if choice == "1":
            sub_menu_cultivate(player)
        elif choice == "2":
            sub_menu_explore(player)
        elif choice == "3":
            breakthrough(player)
        elif choice == "4":
            player.status()
        elif choice == "5":
            sub_menu_inventory(player)
        elif choice == "6":
            sub_menu_shop(player)
        elif choice == "7":
            sub_menu_sect(player)
        elif choice == "8":
            save_game(player)
        elif choice == "9":
            confirm = input("确定退出？存档将丢失！(y/n): ").strip().lower()
            if confirm == "y":
                print("后会有期，道友。")
                break
        else:
            print("无效选择。")

    if not player.is_alive():
        print("\n  道 消 身 殇")
        print(f"  最终境界: {player.realm}")
        print(f"  存活年龄: {player.age}")
        print(f"  击杀数: {player.kill_count}")


def sub_menu_cultivate(player):
    """修炼子菜单"""
    print("\n  1. 吐纳修炼（快速）")
    print("  2. 闭关修炼（大量经验，消耗寿元）")
    choice = input("\n选择: ").strip()

    if choice == "1":
        cultivate(player)
    elif choice == "2":
        closed_door_cultivate(player)


def sub_menu_explore(player):
    """探索子菜单"""
    print("\n  1. 随机探索（可能遭遇战斗或奇遇）")
    print("  2. 历练闯关（连续战斗）")
    print("  3. 进入秘境（高风险高回报）")
    choice = input("\n选择: ").strip()

    if choice == "1":
        roll = random.randint(1, 100)
        if roll <= 40:
            print("\n你四处游历，没有发现异常。")
            player.gain_exp(10)
        elif roll <= 70:
            battle(player)
        else:
            trigger_random_event(player)

    elif choice == "2":
        print("\n你开始了历练之旅……")
        rounds = random.randint(2, 4)
        for i in range(rounds):
            print(f"\n--- 第{i+1}场 ---")
            result = battle(player)
            if not result:
                print("历练失败。")
                player.heal(20)  # 给一点恢复
                break
        else:
            print("\n历练完成！获得额外奖励。")
            player.gain_exp(100)
            player.spirit_stones += 10

    elif choice == "3":
        if player.level < 15:
            print("你的修为太低，秘境中极为危险。")
            confirm = input("仍然进入？(y/n): ").strip().lower()
            if confirm != "y":
                return
        print("\n你进入了上古秘境……")
        result = battle(player)
        if result:
            print("你在秘境中获得了丰厚的收获！")
            player.spirit_stones += random.randint(10, 30)
            if random.randint(1, 100) <= 30:
                player.add_item("洗髓丹", 1)


def sub_menu_inventory(player):
    """道具子菜单"""
    player.show_inventory()
    if not player.inventory:
        return

    print("\n  1. 使用道具")
    print("  2. 返回")
    choice = input("选择: ").strip()

    if choice == "1":
        item = input("输入道具名称: ").strip()
        player.use_item(item)


def sub_menu_shop(player):
    """商店"""
    print(f"\n{'='*30}")
    print(f"  商店 (灵石: {player.spirit_stones})")
    print(f"{'='*30}")

    shop_items = {
        "回气丹": 5,
        "疗伤丹": 8,
        "破境丹": 50,
        "延寿丹": 100,
    }

    for i, (name, price) in enumerate(shop_items.items(), 1):
        desc = ITEMS.get(name, {}).get("desc", "")
        print(f"  {i}. {name} - {price}灵石 ({desc})")

    print(f"  0. 离开")

    while True:
        try:
            idx = int(input("\n购买（0离开）: ").strip())
            if idx == 0:
                break
            if 1 <= idx <= len(shop_items):
                name = list(shop_items.keys())[idx - 1]
                price = shop_items[name]
                if player.spirit_stones >= price:
                    player.spirit_stones -= price
                    player.add_item(name)
                else:
                    print("灵石不足！")
            else:
                print("无效选择。")
        except ValueError:
            print("请输入数字。")


def sub_menu_sect(player):
    """宗门系统"""
    if player.sect is None:
        print("\n你尚未加入任何宗门。")
        print("可选宗门:")
        for i, (name, data) in enumerate(SECTS.items(), 1):
            print(f"  {i}. {name} ({data['type']})")

        print("  0. 不加入")
        try:
            idx = int(input("\n选择: ").strip())
            if idx == 0:
                return
            sect_name = list(SECTS.keys())[idx - 1]
            sect_data = SECTS[sect_name]
            player.sect = sect_name
            player.sect_rank = sect_data["ranks"][0]
            # 应用宗门加成
            for attr, bonus in sect_data["bonus"].items():
                if hasattr(player, attr):
                    setattr(player, attr, getattr(player, attr) + bonus)
            print(f"\n你加入了{sect_name}，成为{player.sect_rank}！")
        except (ValueError, IndexError):
            print("无效选择。")
    else:
        print(f"\n{'='*30}")
        print(f"  宗门: {player.sect}")
        print(f"  职位: {player.sect_rank}")
        print(f"{'='*30}")
        print("  1. 宗门任务（获取经验和灵石）")
        print("  2. 藏经阁（学习功法）")
        print("  3. 申请晋升")
        print("  0. 返回")

        choice = input("\n选择: ").strip()
        if choice == "1":
            print("\n你接取了宗门任务，外出执行……")
            result = battle(player)
            if result:
                reward_exp = 50 + player.level * 5
                reward_stones = random.randint(3, 8)
                player.gain_exp(reward_exp)
                player.spirit_stones += reward_stones
                print(f"任务完成！获得{reward_exp}修为，{reward_stones}灵石。")

        elif choice == "2":
            print("\n你在藏经阁中翻阅功法……")
            available = [name for name in TECHNIQUES if name not in player.skills]
            if available and random.randint(1, 100) <= 40:
                new_skill = random.choice(available)
                player.skills.append(new_skill)
                print(f"你领悟了「{new_skill}」！")
            else:
                print("今日有所收获，但未能领悟新功法。")
                player.gain_exp(30)

        elif choice == "3":
            sect = SECTS[player.sect]
            ranks = sect["ranks"]
            current_idx = ranks.index(player.sect_rank)
            if current_idx < len(ranks) - 1:
                cost = (current_idx + 1) * 20
                if player.spirit_stones >= cost:
                    player.spirit_stones -= cost
                    player.sect_rank = ranks[current_idx + 1]
                    print(f"恭喜晋升为{player.sect_rank}！")
                    player.attack += 5
                    player.defense += 3
                else:
                    print(f"晋升需要{cost}灵石。")
            else:
                print("你已是宗门最高职位。")
