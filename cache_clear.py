#!/usr/bin/env python
# encoding: utf-8
import sys,os
import hashlib
import urlparse
from optparse import OptionParser



def clear_cache(path, cache_url):
    path = path
    #md5v = hashlib.md5(cache_url.encode(encoding='gb2312')).hexdigest()
    md5v = hashlib.md5(cache_url).hexdigest()
    onep=md5v[31:32]
    twop=md5v[29:31]
    filename=path+"/"+onep+"/"+twop+"/"+md5v
    if os.path.isfile(filename):
        print filename
        if os.remove(filename)==None:
            print(filename+" ==>清除成功")
        else:
            print("清除失败")
    else:
        print("没有这个缓存文件")
def func_jfnewclear(url,method,strategy):
    tuple_url = urlparse.urlparse(url)
    #tuple_url = urlparse.urlsplit(url)
    if tuple_url.query:
        cache_url = tuple_url.scheme + method + tuple_url.netloc + '/' + strategy + tuple_url.path + '?' + tuple_url.query
    else:
        cache_url = tuple_url.scheme + method + tuple_url.netloc + '/' + strategy + tuple_url.path
    return cache_url



if __name__ == '__main__':
    usage = "usage: %prog [options] args"
    parser = OptionParser(usage=usage)
    parser.add_option("-p", "--path", action="store", type="string", dest="path", help="for example: /data/www/cache")
    parser.add_option("-u", "--url", action="store", type="string", dest="url", help="for examle: http://www.test.com/test?a=1")
    parser.add_option("-m", "--method", action="store", type="string", dest="method", default= 'GET', help="for examle: GET")
    parser.add_option("-s", "--strategy", action="store", type="string", dest="strategy", default= 'jfnewclear', help="for example: jfnewclear")
    (options, args) = parser.parse_args()
    if options.strategy == 'jfnewclear':
        cache_url = func_jfnewclear(options.url, options.method, options.strategy)
        print cache_url
        clear_cache(options.path, cache_url)
