# setting界面
import cocos
from cocos.audio.pygame import music


class settingimage(cocos.layer.Layer):
    """setting 的背景图片"""

    def __init__(self):
        super().__init__()
        s_width, s_height = cocos.director.director.get_window_size()
        background = cocos.sprite.Sprite('source/image/setting.png')
        background.position = s_width // 2, s_height // 2
        self.add(background, -1)  # 将此场景加入


class setting_menu(cocos.menu.Menu):
    """setting的菜单"""

    def __init__(self):
        super().__init__()
        self.font_item['font_size'] = 40
        self.font_item['color'] = (0, 0, 0, 100)
        self.font_item_selected['color'] = (0, 0, 0, 200)
        music = cocos.menu.ToggleMenuItem('音效： ', self.callback_music, True)
        back = cocos.menu.MenuItem('返回', self.callback)
        self.create_menu([music, back],
                         selected_effect=cocos.menu.zoom_in(),
                         unselected_effect=cocos.menu.zoom_out(),
                         layout_strategy=cocos.menu.fixedPositionMenuLayout([(400, 400), (400, 200)]))

    # 邢云鹤 20177710638
    def callback_music(self, value):
        """音效处理,控制是否播放背景音乐"""
        if value:
            music.unpause()
        else:
            music.pause()

    def callback(self):
        """返回主界面"""
        cocos.director.director.pop()


def Create_setting():
    setting = settingimage()
    menu = setting_menu()
    background = cocos.scene.Scene(setting)
    background.add(menu)
    return background
