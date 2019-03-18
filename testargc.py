# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 17:08:51 2019

@author: Administrator
"""

import argparse

parser = argparse.ArgumentParser(description='User-defined Translation Services')
#parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                    help='an integer for the accumulator')
parser.add_argument('-i'
                    , metavar='IP ADDRESS'
                    ,type=str,default='0.0.0.0'
                    ,required=False
                    ,help='bind address')
parser.add_argument('-p'
                    , metavar='POET'
                    , type=int
                    ,default='8088'
                    ,required=False
                    , help='port')
#parser.add_argument('--sum', dest='accumulate', action='store_const',
#                    const=sum, default=max,
#                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.i)

#print(args.accumulate(args.integers))