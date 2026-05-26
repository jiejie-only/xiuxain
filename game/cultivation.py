"""修炼与突破系统"""

import random
from game.config import REALMS, TECHNIQUES, SPIRIT_ROOTS


def cultivate(player):
    """修炼 - 获得经验"""
    spirit_mult = SPIRIT_ROOTS.get(player.spirit_root, {}).get("exp_mult", 1.0)
    base_exp = 15 + player.level * 2
    gain = int(base_exp * spirit_mult)

    print("\n你盘膝而坐，吐纳天地灵气……")
    print("灵气缓缓涌入丹田。")

    # 随机事件
    roll = random.randint(1, 100)
    if roll <= 5:
        print("你忽感灵台清明，有所顿悟！")
        gain = int(gain * 3)
    elif roll <= 15:
        print("你心有所感，修炼效率大增！")
        gain = int(gain * 2)
    elif roll >= 95:
        print("你心绪不宁，差点走火入魔！")
        player.hp -= 10
        gain = int(gain * 0.3)
        if not player.is_alive():
            print("走火入魔，经脉尽断……")
            return

    player.gain_exp(gain)


def closed_door_cultivate(player):
    """闭关修炼 - 消耗时间但获得更多经验"""
    years = random.randint(1, 5)
    spirit_mult = SPIRIT_ROOTS.get(player.spirit_root, {}).get("exp_mult", 1.0)
    base_exp = 50 + player.level * 5
    gain = int(base_exp * years * spirit_mult)

    player.age += years
    print(f"\n你闭关修炼了{years}年……")

    if player.age >= player.lifespan:
        print(f"闭关之中，寿元耗尽，坐化而去。")
        player.hp = 0
        return

    # 闭关可能获得功法
    if random.randint(1, 100) <= 15:
        available_techniques = [
            name for name, data in TECHNIQUES.items()
            if name not in player.skills
        ]
        if available_techniques:
            new_skill = random.choice(available_techniques)
            player.skills.append(new_skill)
            print(f"闭关之中，你领悟了新功法「{new_skill}」！")

    player.gain_exp(gain)
    print(f"修为大增，但也过去了{years}年。当前年龄: {player.age}")


def breakthrough(player):
    """境界突破"""
    if player.realm_idx >= len(REALMS) - 1:
        print("你已是此界巅峰，需渡劫飞升。")
        return False

    next_realm = REALMS[player.realm_idx + 1]
    next_name = next_realm["name"]
    min_level = next_realm["min_level"]

    print(f"\n{'='*40}")
    print(f"  当前境界: {player.realm}")
    print(f"  目标境界: {next_name}")
    print(f"  最低等级: {min_level} (当前: Lv.{player.level})")
    print(f"{'='*40}")

    if player.level < min_level:
        print(f"你的修为不足，需达到 Lv.{min_level} 才能尝试突破。")
        return False

    # 计算成功率
    success_rate = 50 + player.luck + (player.level - min_level) * 2
    success_rate = min(success_rate, 95)

    # 检查破境丹
    has_pill = "破境丹" in player.inventory
    if has_pill:
        print(f"你拥有破境丹，使用后成功率+20%。")
        use = input("是否使用？(y/n): ").strip().lower()
        if use == "y":
            player.use_item("破境丹")
            success_rate += 20
            success_rate = min(success_rate, 98)

    print(f"\n突破成功率: {success_rate}%")
    confirm = input("是否尝试突破？(y/n): ").strip().lower()

    if confirm != "y":
        print("你暂且压下突破的念头，继续积累修为。")
        return False

    print("\n你运转功法，引动天地灵气……")
    print("丹田之中，灵气翻涌！")

    # 渡劫动画
    if player.realm_idx >= 5:  # 化神以上有雷劫
        print("天空乌云密布，雷劫降临！")
        print("轰！轰！轰！")
        tribulation_dmg = random.randint(20, 50) * (player.realm_idx - 4)
        player.hp -= tribulation_dmg
        print(f"雷劫造成{tribulation_dmg}点伤害！")
        if not player.is_alive():
            print("你未能渡过雷劫，身死道消……")
            return False

    roll = random.randint(1, 100)
    if roll <= success_rate:
        # 突破成功
        player.realm_idx += 1
        player.realm = next_name
        player.max_hp += next_realm["hp_bonus"]
        player.max_mp += next_realm["hp_bonus"] // 2
        player.attack += next_realm["atk_bonus"]
        player.hp = player.max_hp
        player.mp = player.max_mp
        player.lifespan += 50
        player.tribulation_count += 1

        print(f"\n{'*'*40}")
        print(f"  突破成功！")
        print(f"  你已踏入{next_name}境！")
        print(f"  寿元增加50年！")
        print(f"{'*'*40}")
        return True
    else:
        # 突破失败
        dmg = int(player.max_hp * 0.3)
        player.hp -= dmg
        player.mp = max(0, player.mp - 20)
        print(f"\n突破失败！灵气反噬，损失{dmg}点生命。")
        if not player.is_alive():
            print("灵气暴走，经脉尽断，身死道消……")
        return False
