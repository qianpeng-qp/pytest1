'''
Created on 2019年7月13日

@author: asus
'''
def make_car(business,type,**info):
    """函数调用，被调用方"""
    build = {}
    build['bus']=business
    build['type']=type
    for key,value in info.items():
        build[key]=value
    return build