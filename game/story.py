"""主线剧情系统"""

import random
from game.combat import battle


def check_story(player):
    """检查并推进主线剧情"""
    if player.story_stage == 1 and player.level >= 3:
        chapter1(player)
    elif player.story_stage == 2 and player.level >= 10:
        chapter2(player)
    elif player.story_stage == 3 and player.level >= 25:
        chapter3(player)
    elif player.story_stage == 4 and player.level >= 40:
        chapter4(player)
    elif player.story_stage == 5 and player.level >= 60:
        chapter5(player)


def chapter1(player):
    """第一阶段：凡尘求生 - 黑山妖乱"""
    print(f"\n{'='*50}")
    print("  【主线剧情·第一章】黑山妖乱")
    print(f"{'='*50}")
    print()
    print("你在宗门中听闻，黑山深处有妖兽暴动，")
    print("已有数名外门弟子折损其中。")
    print("长老下令，召集弟子前往剿灭。")
    print()
    print("  1. 主动请缨（勇气+3）")
    print("  2. 随队出征（中规中矩）")
    print("  3. 推脱不去（安全第一）")

    while True:
        choice = input("\n你的选择: ").strip()
        if choice == "1":
            print("\n你挺身而出，长老赞许地点了点头。")
            player.luck += 3
            player.karma += 2
            break
        elif choice == "2":
            print("\n你随队出发，混在人群之中。")
            break
        elif choice == "3":
            print("\n你找了个借口推脱，留在宗门修炼。")
            player.gain_exp(30)
            player.story_stage = 2
            return
        else:
            print("无效选择。")

    print("\n黑山之中，妖气弥漫。")
    print("突然，一只巨大的妖狼扑了出来！")
    result = battle(player, "黑山妖兽")

    if result:
        print("\n你成功剿灭妖兽，回到宗门受到嘉奖。")
        player.spirit_stones += 10
        player.add_item("破境丹", 1)
    else:
        print("\n你勉强逃回宗门，虽败犹荣。")
        player.heal(30)

    player.story_stage = 2


def chapter2(player):
    """第二阶段：宗门争锋 - 外门大比"""
    print(f"\n{'='*50}")
    print("  【主线剧情·第二章】外门大比")
    print(f"{'='*50}")
    print()
    print("一年一度的外门大比开始了。")
    print("获胜者可晋升内门弟子，获得大量资源。")
    print()
    print("  1. 全力以赴")
    print("  2. 保存实力")
    print("  3. 暗中下毒（魔道手段）")

    while True:
        choice = input("\n你的选择: ").strip()
        if choice == "1":
            print("\n你全力以赴，连战连胜！")
            result = battle(player)
            if result:
                print("你夺得了外门大比第一，晋升内门！")
                player.attack += 15
                player.spirit_stones += 30
            break
        elif choice == "2":
            print("\n你保存实力，获得了不错的名次。")
            player.spirit_stones += 15
            break
        elif choice == "3":
            print("\n你暗中在对手的饮水里下了药……")
            print("对手纷纷落败，你轻松获胜。")
            print("但有人似乎注意到了你的小动作。")
            player.karma -= 5
            player.spirit_stones += 25
            break
        else:
            print("无效选择。")

    print("\n大比之后，你注意到宗门高层的秘密……")
    print("深夜，你看到长老将几名弟子带入禁地，再未出来。")
    print("丹阁飘出的烟气中，似乎夹杂着血腥味。")
    print()
    print("  1. 暗中调查")
    print("  2. 假装不知")
    print("  3. 直接告发")

    while True:
        choice = input("\n你的选择: ").strip()
        if choice == "1":
            print('\n你暗中调查，发现了"人丹"的秘密……')
            print("宗门高层在利用弟子炼制禁药！")
            player.luck += 3
            break
        elif choice == "2":
            print("\n你假装不知，继续修炼。")
            break
        elif choice == "3":
            print("\n你直接告发，但被长老反咬一口！")
            print("你被迫逃离宗门。")
            player.sect = None
            player.sect_rank = None
            break
        else:
            print("无效选择。")

    player.story_stage = 3


def chapter3(player):
    """第三阶段：九州大战"""
    print(f"\n{'='*50}")
    print("  【主线剧情·第三章】九州大战")
    print(f"{'='*50}")
    print()
    print("正魔大战爆发了。")
    print("九州大地战火纷飞，生灵涂炭。")
    print("你被卷入了这场浩劫之中。")
    print()
    print("  1. 投身正道阵营")
    print("  2. 加入魔道阵营")
    print("  3. 独善其身")

    while True:
        choice = input("\n你的选择: ").strip()
        if choice == "1":
            print("\n你加入了正道联军，浴血奋战。")
            player.alignment = "正道"
            player.karma += 5
            break
        elif choice == "2":
            print("\n你投入魔道，以杀证道。")
            player.alignment = "魔道"
            player.attack += 20
            player.karma -= 5
            break
        elif choice == "3":
            print("\n你远离战场，独自修炼。")
            player.gain_exp(300)
            break
        else:
            print("无效选择。")

    print("\n大战之中，你逐渐发现了一个惊天秘密：")
    print('所谓的"飞升"，不过是高阶修士对下界的收割。')
    print("仙路断绝，是因为上界不允许再有人飞升。")

    print("\n  1. 继续修炼，逆天而行")
    print("  2. 顺天而行，伺机飞升")
    print("  3. 寻找真相")

    while True:
        choice = input("\n你的选择: ").strip()
        if choice in ("1", "2", "3"):
            print("\n你做出了自己的选择。")
            player.luck += 3
            break
        else:
            print("无效选择。")

    player.story_stage = 4


def chapter4(player):
    """第四阶段：天道之争"""
    print(f"\n{'='*50}")
    print("  【主线剧情·第四章】天道之争")
    print(f"{'='*50}")
    print()
    print("天机子现出了真面目。")
    print("他布局千年，正是为了收割九州气运。")
    print("血河老祖、妖族大能纷纷现身。")
    print("最终之战，一触即发。")
    print()
    print("  1. 对抗天机子")
    print("  2. 与天机子合作")
    print("  3. 渔翁得利")

    while True:
        choice = input("\n你的选择: ").strip()
        if choice == "1":
            print("\n你挺身而出，与天机子决一死战！")
            result = battle(player, "血河老祖")
            if result:
                print("你击败了天机子的爪牙！")
            break
        elif choice == "2":
            print("\n你选择与天机子合作，获得强大力量。")
            player.attack += 50
            player.karma -= 10
            break
        elif choice == "3":
            print("\n你等待双方两败俱伤，坐收渔利。")
            player.luck += 5
            break
        else:
            print("无效选择。")

    player.story_stage = 5


def chapter5(player):
    """终章：抉择"""
    print(f"\n{'='*50}")
    print("  【终章】你的道")
    print(f"{'='*50}")
    print()
    print("一切尘埃落定。")
    print("你站在天道之门前，面前是无尽的选择。")
    print()
    print("  1. 飞升成仙 - 斩断七情六欲")
    print("  2. 成为魔尊 - 吞噬九州气运")
    print("  3. 重塑天道 - 建立新秩序")
    print("  4. 化凡归隐 - 放弃长生")
    print("  5. 轮回之主 - 掌控生死")

    endings = {
        "1": ("飞升成仙", "你斩断七情六欲，一步登天。\n仙光洒落，你成为此界最后一位飞升者。\n\n但你已不再是你。\n\n—— 飞升成仙 END"),
        "2": ("成为魔尊", "你吞噬九州气运，成为至高魔尊。\n万物在你脚下颤抖，你就是天道。\n\n但永恒的孤独，是永恒的诅咒。\n\n—— 魔尊 END"),
        "3": ("重塑天道", "你以无上神通重塑天道。\n仙路重开，万物复苏。\n\n你耗尽所有修为，化为天地法则的一部分。\n\n—— 重塑天道 END"),
        "4": ("化凡归隐", '你放弃了长生，选择了红尘。\n回到凡间，做一个普通人。\n\n日出而作，日落而息。\n或许这才是真正的"道"。\n\n—— 化凡 END'),
        "5": ("轮回之主", "你掌控了生死轮回。\n不死不灭，但也永远无法离开。\n\n你在无尽的轮回中，等待着下一个挑战者。\n\n—— 轮回之主 END"),
    }

    while True:
        choice = input("\n你的最终选择: ").strip()
        if choice in endings:
            name, text = endings[choice]
            print(f"\n{'*'*50}")
            print(text)
            print(f"{'*'*50}")
            print(f"\n你选择了「{name}」结局。")
            print(f"最终境界: {player.realm}")
            print(f"最终等级: Lv.{player.level}")
            print(f"存活年龄: {player.age}")
            print(f"击杀数: {player.kill_count}")
            print(f"因果值: {player.karma}")
            player.story_stage = 6  # 游戏结束标记
            return
        else:
            print("无效选择。")
