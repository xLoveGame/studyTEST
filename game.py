# 游戏界面
import cocos
import mainPeopleClass
import TestClass


class gameBG(cocos.layer.Layer):
    """
    背景
    """

    def __init__(self):
        super().__init__()
        d_weight, d_height = cocos.director.director.get_window_size()
        background = cocos.sprite.Sprite('source/image/游戏界面.png')
        background.position = d_weight // 2, d_height // 2
        self.add(background, -1)


def create_game():
    background = cocos.scene.Scene(gameBG())
    a = mainPeopleClass.mianPeople()
    background.add(a)
    b = TestClass.xianshi()
    background.add(b)
    return background
