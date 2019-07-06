import cocos


class gameover(cocos.layer.Layer):
    """发生碰撞结束界面"""
    is_event_handler = True

    def __init__(self):
        super().__init__()
        d_weight, d_height = cocos.director.director.get_window_size()
        background = cocos.sprite.Sprite('source/image/游戏界面.png')
        background.position = d_weight // 2, d_height // 2
        self.add(background, -1)


class game_over_menu(cocos.menu.Menu):
    is_event_handler = True

    def __init__(self):
        super().__init__()
        self.font_item['font_size'] = 90
        self.font_item['color'] = (255, 0, 0, 100)
        self.font_item_selected['color'] = (255, 0, 0, 200)
        dead = cocos.menu.MenuItem('YOU DEAD', self.callback_over)
        back = cocos.menu.MenuItem('退出', self.callback)
        self.create_menu([dead, back],
                         selected_effect=cocos.menu.zoom_out(),
                         unselected_effect=cocos.menu.zoom_out(),
                         layout_strategy=cocos.menu.fixedPositionMenuLayout([(350, 400), (500, 200)]))

    def callback_over(self):
        print('魂三不完美的彩蛋')

    def callback(self):
        exit()


# 邢云鹤 20177710638

def GameOver():
    background = gameover()
    temp = cocos.scene.Scene(background)
    menu = game_over_menu()
    temp.add(menu)
    return temp
