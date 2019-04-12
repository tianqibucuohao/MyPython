# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 14:42:13 2019

@author: Administrator
"""

#Python-ConfigParser获取配置项名称大小写问题
import ConfigParser

def optionxform(self, optionstr):
    return optionstr.lower()
#会将配置文件中的选项名改为小写
#
#为了保持配置项名称的大小写格式，重写：

class myconf(ConfigParser.ConfigParser):
    def __init__(self, defaults=None):
        ConfigParser.ConfigParser.__init__(self, defaults=defaults)

    # 这里重写了optionxform方法，直接返回选项名
    def optionxform(self, optionstr):
        return optionstr


# 获取test.cfg
def get_config(self, cfg_file):
    cfg_dict = {}
    config = myconf()
    config.read(cfg_file)

    for sec in config.sections():
        cfg_dict[sec] = {}
        for op in config.items(sec):
            cfg_dict[sec][op[0]] = op[1]
    return cfg_dict