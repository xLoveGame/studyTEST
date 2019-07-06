# 测试类
import cocos
import game_over


class armTest():  # 用于管理武器删除
    def __init__(self):
        self.li = list()
        print('创建成功')

    def add(self, a):
        self.li.append(a)
        print('添加成功')

    def test(self):
        # 注意传参为对象，而要操作的数据在对象里面
        for i in range(len(self.li) - 1, -1, -1):
            if self.li[i].my.x >= 650:
                self.li[i].my.kill()
                self.li.pop(i)
                print('删除武器')


class enemyTest():  # 用于管理武器的删除
    def __init__(self):
        self.st = list()

    def add(self, a):
        self.st.append(a)

    def test(self):
        for i in range(len(self.st) - 1, -1, -1):
            if self.st[i].diren.x <= 20:
                self.st[i].diren.kill()
                self.st.pop(i)
                print('删除敌人')


def enemy_arm(arms, enemys):
    print('检测中')
    for i in range(len(arms) - 1, -1, -1):
        for j in range(len(enemys) - 1, -1, -1):
            if int(enemys[j].diren.y) in range(int(arms[i].my.y) - 30, int(arms[i].my.y) + 30) \
                    and int(enemys[j].diren.x) in range(int(arms[i].my.x) - 30, int(arms[i].my.x + 30)):
                arms[i].my.kill()
                arms.pop(i)
                enemys[j].diren.kill()
                enemys.pop(j)

                print('碰撞删除')


# 邢云鹤 20177710638

class xianshi(cocos.layer.Layer):
    def __init__(self):
        super().__init__()
        self.ly = cocos.text.Label('',
                                   font_name='123',
                                   font_size=50,
                                   anchor_x='center', anchor_y='center')
        self.ly.position = 300, 500
        self.add(self.ly)


def people_enemy(people, enemys):
    for i in range(len(enemys) - 1, -1, -1):
        if int(people.x) in range(int(enemys[i].diren.x) - 30, int(enemys[i].diren.x) + 30) and \
                int(people.y) in range(int(enemys[i].diren.y) - 30, int(enemys[i].diren.y) + 30):
            cocos.director.director.push(game_over.GameOver())
