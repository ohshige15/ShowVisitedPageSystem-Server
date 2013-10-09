# -*- coding: utf-8 -*-

from bing_api import Bing

from setting import api_key


def search_query(query):
	bing = Bing(api_key)
	results = bing.web_search(query, 100, ["Url", "Title", "Description"])
	return results


def get_suggestions(query):
	bing = Bing(api_key)
	results = bing.related_search(query)
	return results	
