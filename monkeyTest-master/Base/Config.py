# /usr/bin/env python
# -*- encoding: utf-8 -*-
import random
import re


class Config:
    # apk包名
    package_name = "com.dc.hwsj"
    # 默认设备列表
    device_dict = {}
    # 网络
    net = "wifi"
    # monkey seed值，随机产生
    monkey_seed = str(random.randrange(1, 1000))
    # monkey 参数
    monkey_parameters = "--throttle 300 --ignore-crashes --ignore-timeouts --pct-touch 80 --pct-trackball 5 --pct-appswitch 5 --pct-syskeys 5 --pct-motion 5 -v -v 500"
    # log保存地址
    log_location = "E:\\Test_py\\monkeyTest-master\\log\\"
    # 性能数据存储目录
    info_path = "E:\\Test_py\monkeyTest-master\\info\\"


# "adb shell monkey -p com.quvideo.xiaoying --throttle 300 --ignore-crashes --ignore-timeouts --pct-touch 80 --pct-trackball 5 --pct-appswitch 5 --pct-syskeys 5 --pct-motion 5 -v -v 30000"


def filter(data):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_dev = re.sub(rstr, "_", data)  #
    return new_dev
