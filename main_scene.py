# 进入界面
import cocos
import setting
import shuoming
import game
from cocos.scenes.transitions import *  # 包含场景切换动画


class main_background(cocos.layer.ColorLayer):
    """主界面背景层,设置为colorLayer层，防止图片设置成透明后显得黑"""

    def __init__(self):
        super().__init__(255, 255, 255, 10)
        d_weight, d_height = cocos.director.director.get_window_size()
        background = cocos.sprite.Sprite('source/image/main_background.png', opacity=255)  # 最后一栏是透明度
        background.position = d_weight // 2, d_height // 2
        self.add(background, -1)


"""
class title(cocos.menu.Menu):
    #标题

    def __init__(self):
        super().__init__()
        self.font_item['font_size'] = 65
        self.font_item_selected['font_size'] = 65
        self.font_item['font_name'] = 'Times New Roman'
        self.font_item['color'] = (0, 0, 0, 200)
        self.font_item_selected['color'] = (0, 0, 0, 200)
        menu_title = cocos.menu.ImageMenuItem('source/image/武侠大冒险.png', self.callback_title)
        # 实例化菜单
        self.create_menu([menu_title],
                         layout_strategy=cocos.menu.fixedPositionMenuLayout([(300, 650)]))

    def callback_title(self):
        print('彩蛋一枚')
"""


class main_menu(cocos.menu.Menu):
    """主菜单"""

    def __init__(self):
        super().__init__()
        self.font_item['font_size'] = 40
        self.font_item_selected['font_size'] = 60
        self.font_item['color'] = (0, 0, 0, 85)
        self.font_item_selected['color'] = (0, 0, 0, 170)
        menu_start = cocos.menu.MenuItem('开始', self.callback_start)
        menu_setting = cocos.menu.MenuItem('设置', self.callback_setting)
        menu_shuoming = cocos.menu.MenuItem('说明', self.callback_shuoming)

        # 创建菜单
        self.create_menu([menu_start, menu_setting, menu_shuoming],
                         selected_effect=cocos.menu.zoom_in(),
                         unselected_effect=cocos.menu.zoom_out(),
                         layout_strategy=cocos.menu.fixedPositionMenuLayout([(300, 500), (300, 400), (300, 300)]))

    # 游戏的所有控制由以下三个回调函数完成

    def callback_start(self):
        temp = game.create_game()
        mid = SlideInBTransition(temp, 1)
        cocos.director.director.push(mid)

    def callback_setting(self):
        temp = setting.Create_setting()
        mid = MoveInBTransition(temp, 2)  # 添加场景切换动画
        cocos.director.director.push(mid)

    def callback_shuoming(self):
        temp = shuoming.create_shuoming()
        mid = TurnOffTilesTransition(temp, 1)
        cocos.director.director.push(mid)


def create_mainScene():
    """创建主界面"""
    background = cocos.scene.Scene(main_background())  # 创建主背景
    background.add(main_menu())  # 创建主菜单
    # background.add(title())  # 创建标题
    return background
