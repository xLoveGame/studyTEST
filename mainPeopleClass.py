# 主人物及控制
import cocos
import armClass
import pyglet
import TestClass
import enemyClass
import random


class mianPeople(cocos.layer.Layer):
    """主人物类"""
    is_event_handler = True  # 千万不能少了，否则无法执行键盘事件

    def __init__(self):
        super().__init__()
        self.i = 0  # 此处定义i的目的是为了键盘事件监听
        self.people = cocos.sprite.Sprite('source/image/主人物.png')
        self.d_weight, self.d_height = cocos.director.director.get_window_size()
        self.people.position = self.d_weight // 2, self.d_height // 2
        self.add(self.people)
        self.li = TestClass.armTest()
        self.st = TestClass.enemyTest()

    def on_key_press(self, key, modifiers):
        """处理键盘事件"""
        self.li.test()  # 测试武器是否需要删除
        self.i += 1  # 每次执行加一，说明此时在运行的事件数
        self.st.test()  # 测试敌人是否需要删除
        TestClass.people_enemy(self.people, self.st.st)  # 人物和敌人碰撞检测
        TestClass.enemy_arm(self.li.li, self.st.st)  # 敌人和武器碰撞检测
        if 30 <= self.people.x <= 650 and 80 <= self.people.y <= 720:
            if key == pyglet.window.key.W or key == pyglet.window.key.UP:
                a = cocos.actions.MoveBy((0, 30), duration=0.2)
                b = cocos.actions.Repeat(a)
                self.people.do(b)
            if key == pyglet.window.key.S or key == pyglet.window.key.DOWN:
                a = cocos.actions.MoveBy((0, -30), duration=0.2)
                b = cocos.actions.Repeat(a)
                self.people.do(b)
            if key == pyglet.window.key.D or key == pyglet.window.key.RIGHT:
                a = cocos.actions.MoveBy((30, 0), duration=0.2)
                b = cocos.actions.Repeat(a)
                self.people.do(b)
            if key == pyglet.window.key.A or key == pyglet.window.key.LEFT:
                a = cocos.actions.MoveBy((-30, 0), duration=0.2)
                b = cocos.actions.Repeat(a)
                self.people.do(b)
            if key == pyglet.window.key.SPACE:
                # 创建武器
                temp = armClass.arm(self.people.x + 30, self.people.y)
                self.add(temp)
                self.li.add(temp)
                # 创建敌人
                enemy = enemyClass.enemy(random.randrange(500, 600), random.randrange(100, 700))
                self.add(enemy)
                self.st.add(enemy)

        else:
            self.people.do(cocos.actions.MoveTo((300, 300), duration=0.1))

    def on_key_release(self, key, modifiers):
        self.i -= 1  # 每次执行，i-1
        if self.i == 0:  # 当i == 0， 说明此时没有事件，这时才停止
            self.people.stop()
