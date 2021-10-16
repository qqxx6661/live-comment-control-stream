# 部分弹幕功能代码来自项目：https://github.com/IsoaSFlus/danmaku，感谢大佬
# 快手弹幕代码来源及思路：https://github.com/py-wuhao/ks_barrage，感谢大佬
# 仅抓取用户弹幕，不包括入场提醒、礼物赠送等。

import asyncio
import danmaku
import redis

list_name = 'bilibili'
key_list = ('w', 's', 'a', 'd', 'j', 'k', 'u', 'i', 'z', 'x', 'f', 'enter', 'shift', 'backspace')


def init_redis():
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    return r


async def printer(q, redis):
    while True:
        m = await q.get()
        if m['msg_type'] == 'danmaku':
            print(f'{m["name"]}：{m["content"]}')


            list_str = list(m["content"])
            print("弹幕拆分:", list_str)
            for char in list_str:
                if char.lower() in key_list:
                    print('推送队列：', char.lower())
                    redis.rpush(list_name, char.lower())


async def main(url):
    redis = init_redis()
    q = asyncio.Queue()
    dmc = danmaku.DanmakuClient(url, q)
    asyncio.create_task(printer(q, redis))
    await dmc.start()


a = input('请输入直播间地址：\n')
asyncio.run(main(a))

# 虎牙直播：https://www.huya.com/11352915
# 斗鱼直播：https://www.douyu.com/85894
# B站直播：https://live.bilibili.com/4249429
# 快手直播：https://live.kuaishou.com/u/jjworld126
# 火猫直播：
# 企鹅电竞：https://egame.qq.com/383204988
# 花椒直播：https://www.huajiao.com/l/303344861?qd=hu
# 映客直播：https://www.inke.cn/liveroom/index.html?uid=87493223&id=1593906372018299
# CC直播：https://cc.163.com/363936598/
# 酷狗直播：https://fanxing.kugou.com/1676290
# 战旗直播：
# 龙珠直播：http://star.longzhu.com/wsde135864219
# PPS奇秀直播：https://x.pps.tv/room/208337
# 搜狐千帆直播：https://qf.56.com/520208a
# 来疯直播：https://v.laifeng.com/656428
# LOOK直播：https://look.163.com/live?id=196257915
# AcFun直播：https://live.acfun.cn/live/23682490
# 艺气山直播：http://www.173.com/96
