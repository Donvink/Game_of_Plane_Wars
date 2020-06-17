# -*- coding = utf-8 -*-
# @Time: 2020/6/16 16:36
# @Author: Yudong Zhong
# @File: planeIndex.py
# @Software: PyCharm

import random
import pygame
from pygame.locals import *


class HeroPlane(object):
    """
    1、实现飞机的显示，并控制飞机的移动（面向对象）
    """
    def __init__(self, screen):
        """
        初始化函数
        :param screen: 主窗体对象
        """
        # 飞机默认位置
        self.x = 150
        self.y = 450
        # 设置要显示内容的窗口
        self.screen = screen
        # 生成飞机的图片对象
        self.image_name = './img/hero.png'
        self.image = pygame.image.load(self.image_name)
        # 用来存放子弹的列表
        self.bullet_list = []
        pass

    def move_left(self):
        """
        左移动
        :return:
        """
        if self.x > 0:
            self.x -= 10
        pass

    def move_right(self):
        """
        右移动
        :return:
        """
        if self.x < 350 - 46:   # hero飞机像素为46x57
            self.x += 10
        pass

    def display(self):
        """
        在主窗口显示飞机、子弹
        :return:
        """
        self.screen.blit(self.image, (self.x, self.y))
        # 判断子弹的位置是否越界，如果是，那么就要删除这颗子弹
        # 用来存放需要删除的对象引用
        del_bullet_list = []
        # 保存需要删除的对象
        for item in self.bullet_list:
            if item.judge():
                del_bullet_list.append(item)
        # 删除self.del_bullet_list中需要删除的对象
        for i in del_bullet_list:
            self.bullet_list.remove(i)
        for bullet in self.bullet_list:
            bullet.display()    # 显示一个子弹的位置
            bullet.move()       # 让这个子弹进行移动，下次再显示时就会看到子弹在修改后的位置
        pass

    def fire(self):
        """
        发射子弹
        :return:
        """
        # 创建一个新的子弹对象
        new_bullet = HeroBullet(self.x, self.y, self.screen)
        self.bullet_list.append(new_bullet)
        pass


class HeroBullet(object):
    """
    创建子弹类
    """
    def __init__(self, x, y, screen):
        """
        初始化参数
        :param x:
        :param y:
        :param screen:
        """
        self.x = x + 21
        self.y = y - 20
        self.screen = screen
        self.image = pygame.image.load('./img/bullet1.png')
        pass

    def display(self):
        """
        显示子弹
        :return:
        """
        self.screen.blit(self.image, (self.x, self.y))
        pass

    def move(self):
        """
        子弹向上移动
        :return:
        """
        self.y -= 10
        pass

    def judge(self):
        """
        判断子弹是否越界
        :return:
        """
        if self.y < 0:
            return True
        else:
            return False
        pass


class EnemyPlane(object):
    """
    创建敌机类
    """
    def __init__(self, screen):
        """
        初始化函数
        :param screen: 主窗体对象
        """
        # 飞机默认位置
        self.x = random.randint(0, 350-57)  # 敌机像素为57x43
        self.y = 0
        # 设置要显示内容的窗口
        self.screen = screen
        # 生成飞机的图片对象
        self.image_name = './img/enemy0.png'
        self.image = pygame.image.load(self.image_name)
        # 用来存放子弹的列表
        self.bullet_list = []
        # 默认设置一个方向
        self.direction = 'right'
        pass

    def display(self):
        """
        在主窗口显示敌机、子弹
        :return:
        """
        self.screen.blit(self.image, (self.x, self.y))
        # 判断子弹的位置是否越界，如果是，那么就要删除这颗子弹
        # 用来存放需要删除的对象引用
        del_bullet_list = []
        # 保存需要删除的对象
        for item in self.bullet_list:
            if item.judge():
                del_bullet_list.append(item)
        # 删除self.del_bullet_list中需要删除的对象
        for i in del_bullet_list:
            self.bullet_list.remove(i)
        for bullet in self.bullet_list:
            bullet.display()  # 显示一个子弹的位置
            bullet.move()  # 让这个子弹进行移动，下次再显示时就会看到子弹在修改后的位置
        pass

    def fire(self):
        """
        敌机随机发射子弹
        :return:
        """
        num = random.randint(1, 5)
        if num == 3:
            # 创建一个新的子弹对象
            new_bullet = EnemyBullet(self.x, self.y, self.screen)
            self.bullet_list.append(new_bullet)
        pass

    def move(self):
        """
        敌机随机移动
        :return:
        """
        if self.direction == 'right':
            self.x += 10
        elif self.direction == 'left':
            self.x -= 10
        if self.x > 350-57:
            self.direction = 'left'
        elif self.x < 0:
            self.direction = 'right'
        pass


class EnemyBullet(object):
    """
    创建敌机子弹类
    """
    def __init__(self, x, y, screen):
        """
        初始化参数
        :param x:
        :param y:
        :param screen:
        """
        self.x = x + 28
        self.y = y + 50
        self.screen = screen
        self.image = pygame.image.load('./img/bullet0.png')
        pass

    def display(self):
        """
        显示子弹
        :return:
        """
        self.screen.blit(self.image, (self.x, self.y))
        pass

    def move(self):
        """
        子弹向下移动
        :return:
        """
        self.y += 10
        pass

    def judge(self):
        """
        判断子弹是否越界
        :return:
        """
        if self.y > 500:
            return True
        else:
            return False
        pass


def key_control(HeroObj):
    """
    键盘的检测
    :param HeroObj: 可控制检测的对象
    :return:
    """
    # 获取键盘事件
    event_list = pygame.event.get()
    # 获取事件，比如按键等
    for event in event_list:
        # 判断是否点击了退出按钮
        if event.type == QUIT:
            # print('exit')
            exit()
        # 判断是否按下了键
        elif event.type == KEYDOWN:
            # 检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                # print('left')
                HeroObj.move_left()     # 调用函数实现左移动
            # 检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                # print('right')
                HeroObj.move_right()     # 调用函数实现右移动
            # 检测按键是否是空格键
            elif event.key == K_SPACE:
                # print('space')
                HeroObj.fire()


def main():
    """
    一、搭建界面，主要完成窗口和背景图的显示
    :return:
    """
    # 1、创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((350, 500), 0, 32)
    # 2、加载一张照片，用来充当背景
    background = pygame.image.load('./img/background.png')
    # 3、设置title
    pygame.display.set_caption('Game of Plane War')

    # 添加背景音乐
    pygame.mixer.init()
    pygame.mixer.music.load('./music/background.mp3')
    pygame.mixer.music.set_volume(0.15)
    pygame.mixer.music.play(-1)  # 循环次数，-1表示无限循环

    # 创建一个飞机对象
    hero_plane = HeroPlane(screen)

    # 创建一个敌机对象
    enemy_plane = EnemyPlane(screen)

    # 4、把背景图片放到窗口中显示
    while True:
        # 设定需要显示的背景图
        screen.blit(background, (0, 0))
        # 显示玩家飞机的图片
        hero_plane.display()
        # 显示敌机的图片
        enemy_plane.display()
        # 敌机移动
        enemy_plane.move()
        # 敌机发射子弹
        enemy_plane.fire()
        # 获取键盘事件
        key_control(hero_plane)
        # 更新需要显示的内容
        pygame.display.update()
        pygame.time.Clock().tick(5)     # 1秒钟内循环5次


if __name__ == "__main__":
    main()
