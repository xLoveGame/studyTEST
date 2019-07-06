# 敌人类
import cocos


class enemy(cocos.layer.Layer):
    def __init__(self, x, y):
        super().__init__()
        self.diren = cocos.sprite.Sprite('source/image/敌人.png')
        self.diren.position = x, y
        self.add(self.diren)
        a = cocos.actions.Repeat(cocos.actions.MoveBy((-30, 0), duration=0.5))
        self.diren.do(a)
