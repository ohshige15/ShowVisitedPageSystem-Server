#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import cgi
import cgitb; cgitb.enable()

import json

import search


form = cgi.FieldStorage()

output = {'mode':'', 'status':'NG'}


#---------------------------------------------
# クエリ検索
#---------------------------------------------
# クエリを入力して検索したとき
# mode = search_query
def search_query():
    global output
    try:
        query = form['query'].value.decode('utf-8')
        output['results'] = search.search_query(query)
        output['status'] = 'OK'
    except KeyError, e:
        output['reason'] = 'nothing-%s' % e


#---------------------------------------------
# クエリ推薦
#---------------------------------------------
# 推薦クエリを取得するとき
# mode = get_suggestions
def get_suggestions():
    global output
    try:
        query = form['query'].value.decode('utf-8')
        output['results'] = search.get_suggestions(query)
        output['status'] = 'OK'
    except KeyError, e:
        output['reason'] = 'nothing-%s' % e


# mode によって実行内容が変わる
try:
    mode = form['mode'].value
    func = {"search_query": search_query,
    		"get_suggestions": get_suggestions}
    if func.has_key(mode):
        output['mode'] = mode
        func[mode]()
    else:
        output['mode'] = 'branch'
        output['reason'] = 'unavailable-mode:%s' % mode
except KeyError:
    output['mode'] = 'start'
    output['reason'] = 'nothing-mode'

print "Content-type: text/javascript; charset=utf-8"
print
print json.dumps(output)
