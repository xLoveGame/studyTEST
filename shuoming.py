# 说明界面
import cocos


class shuoming(cocos.layer.Layer):
    """setting 的背景图片"""

    def __init__(self):
        super().__init__()
        s_width, s_height = cocos.director.director.get_window_size()
        background = cocos.sprite.Sprite('source/image/setting.png')
        background.position = s_width // 2, s_height // 2
        self.add(background, -1)  # 将此场景加入


class shuomingMenu(cocos.menu.Menu):
    """说明的返回菜单"""

    def __init__(self):
        super().__init__()
        self.font_item['font_size'] = 35
        self.font_item['color'] = (0, 0, 0, 100)
        self.font_item_selected['color'] = (0, 0, 0, 200)
        back = cocos.menu.MenuItem('返回', self.callback)
        a = cocos.menu.MenuItem('此游戏为邢云鹤所做', self.calla)
        self.create_menu([a, back],
                         selected_effect=cocos.menu.zoom_out(),
                         unselected_effect=cocos.menu.zoom_in(),
                         layout_strategy=cocos.menu.fixedPositionMenuLayout([(350, 600), (400, 200)]))

    def callback(self):
        """返回主界面"""
        cocos.director.director.pop()

    def calla(self):
        print('本版本为:   1.0,\n已经经过0次修改\n邢云鹤 20177710638')


def create_shuoming():
    shuoming1 = shuoming()
    menu = shuomingMenu()
    background = cocos.scene.Scene(shuoming1)
    background.add(menu)
    return background
