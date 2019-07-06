# 武器类
import cocos


class arm(cocos.layer.Layer, ):
    """武器类"""

    def __init__(self, x, y):
        super().__init__()
        self.my = cocos.sprite.Sprite('source/image/武器.png')
        self.my.position = x, y
        self.add(self.my)
        a = cocos.actions.MoveBy((10, 0), duration=0.1)
        b = cocos.actions.Repeat(a)
        self.my.do(b)
# 邢云鹤 20177710638
