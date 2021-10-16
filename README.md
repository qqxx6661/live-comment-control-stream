# live_comment_control_stream

接收弹幕指令并控制电脑操作 Python3+Redis+PyAutoGUI

## 实现原理

通过Github作者的项目

https://github.com/wbt5/real-url

获取直播实施弹幕

将弹幕写入消息队列

消费者接受消息，将弹幕内容转为键盘指令，最终通过PyAutoGUI操作电脑

## 代码结构

- control
    - consumer.py
    - display_redis.py
    - pyautogui_test.py
- danmu: 此文件夹代码取自https://github.com/wbt5/real-url
    - danmaku:各平台弹幕获取
    - main.py