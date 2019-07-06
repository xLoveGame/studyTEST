# 程序入口
import cocos
import main_scene
from cocos.audio.pygame import music  # 音乐相关

# 程序开始入口
if __name__ == '__main__':
    """程序开始入口"""
    # 创建整体背景
    cocos.director.director.init(width=700, height=750, caption="myGame", audio_backend='sdl')
    background = main_scene.create_mainScene()
    # 播放背景音乐(音乐为游戏古剑奇谭三背景音乐)
    music.load('source/sound/背景乐.mp3'.encode())
    music.play(loops=-1)  # 循环播放
    music.set_volume(0.3)  # 设置声音大小
    # 运行
    cocos.director.director.run(background)
