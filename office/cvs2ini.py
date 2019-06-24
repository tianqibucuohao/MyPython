# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 11:05:29 2019

@author: Administrator

操作cvs
"""

import csv
import configparser

g_dicts = {}

"""
重载configparser：区分节点大小写
"""
class myconf(configparser.ConfigParser):
    def __init__(self,defaults=None, delimiters='='):
        configparser.ConfigParser.__init__(self,defaults=None, delimiters='=')
    def optionxform(self, optionstr):
        return optionstr

def Save2Ini(filepath,dicts):
    config=myconf(defaults=None,delimiters=':')
   #config.read(file, encoding='utf-8-sig')
    config.add_section('Mac')
    for i in dicts.keys():
        config.set('Mac', i, dicts[i])
    
    with open(filepath, "w+",encoding='UTF-8') as file:
        config.write(file)

def LoadIni(file):
    g_dicts['XiaoMi'] = "小米"
    g_dicts['HUAWEI'] = "华为"
    g_dicts['Cisco'] = 'Cisco'
    g_dicts['Samsung'] = '三星'
    g_dicts['HTC'] = 'HTC'
    g_dicts['Sony'] = 'Sony'
    g_dicts['TP-LINK'] = 'TP-LINK'
    g_dicts['Dell '] = 'Dell'
    g_dicts['Hangzhou H3C'] = '华三'
    g_dicts['Lenovo Mobile'] = '联想'
    g_dicts['zte '] = '中兴'
    g_dicts['Yulong '] = '酷派'
    g_dicts['LG Electronics'] = 'LG'
    g_dicts['Wingtech'] = '魅族1'
    g_dicts['Datang'] = '大唐'
    g_dicts['SHENZHEN FAST'] = '迅捷'
    g_dicts['Shenzhen TINNO'] = '天珑'
    g_dicts['Amazon'] = 'Amazon'
    g_dicts['China Mobile'] = '中移动'
    g_dicts['vivo Mobile'] = 'vivo'
    g_dicts['GUANGDONG OPPO'] = 'oppo'
    g_dicts['Gionee Communication'] = '金立'
    g_dicts['Microsoft Mobile'] = 'Microsoft'
    g_dicts['MEIZU'] = '魅族' 
    g_dicts['Panasonic Mobile'] = 'Panasonic'
    g_dicts['SHENZHEN ZHIBOTONG'] = '智博通'
    g_dicts['Smartisan Technology'] = '锤子'
    g_dicts['Nokia Corporation'] = 'Nokia'
    g_dicts['VMware, Inc'] = 'VMware'
    g_dicts['Google, Inc'] = 'Google'
    g_dicts['D-Link Corporation'] = '友讯'
    g_dicts['Hewlett Packard'] = '惠普'
    g_dicts['Shanghai Feixun'] = '斐讯'
    g_dicts['ASUSTek COMPUTER'] = '华硕'
    g_dicts['SHENZHEN CHUANGWEI'] = '创维'
    g_dicts['OnePlus Technology'] = '1+'
    g_dicts['Tenda Technology'] = '腾达'
    g_dicts['Apple, Inc'] = '苹果'
    g_dicts['Motorola Mobility'] = '摩托罗拉'
    g_dicts['Nubia Technology'] = 'Nubia' 
    g_dicts['Shenzhen Forcelink'] = '神舟' 
    g_dicts['Acer Inc'] = 'acer'
    
    
"""    
    dicts =[]
    try:
        config = myconf()#configparser.ConfigParser(defaults=None, delimiters='=')
        config.read(file, encoding='utf-8-sig')
        key = config.options('Replace')
       # help()
        print(key)
        for i in key:
            dicts[i] = config.get(i)
    except TypeError:
        print('type input error')
    except configparser.NoSectionError:
        print("read file error.Cannot read Replace section")
    return dicts
"""


"""
替换公司名称：只查子串->替换新名称
"""
def ReplaceCompanyName(src):
    newname=src
    for i in g_dicts.keys():
        #print(i)
        if (src.find(i) != -1):
            newname = g_dicts[i]
            break
    #print(newname)
    return newname

def sortedDictValues3(adict):
    keys = adict.keys()
    keys.sort()
    return map(adict.get, keys)

def OpenCSVfile(filepath):
    with open(filepath, 'r',encoding='UTF-8') as csvfile:
        reader = csv.DictReader(csvfile)
        #i = 0
        dicts ={}
        dicts_unknown={}
#        try:#不捕捉异常，保留异常输出信息
        for row in reader:
            #print(row)
            mac = row['Assignment']
            name = row['Organization Name']
           #print('mac=',mac,',company=',name)
            if (len(mac) == 6):
                #print(row['Organization Name'])
                newname = ReplaceCompanyName(name)
                if (newname == name):
                    dicts_unknown[mac] = newname
                else:
                    dicts[mac] = newname
        #print('rows = ',i)
        dicts2 = sorted(dicts)
        Save2Ini("f:\\mac.ini", dicts)
        #Save2Ini("f:\\sort.ini", dicts2)
        Save2Ini("f:\\mac_unkown.ini", dicts_unknown)
#        except UnicodeDecodeError:
#            print("ut8-decode error")
        
def main():
    filepath="f:\\oui.csv"
    dicts = LoadIni(".\\replace.ini")
    #ReplaceCompanyName('jojojxiaoMi')
    #OpenCSVfile(filepath)
    for i in g_dicts.keys():
        print(i)
    
if (__name__ == "__main__"):
    main()