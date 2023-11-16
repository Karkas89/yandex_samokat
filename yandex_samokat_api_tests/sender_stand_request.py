import requests

import configuration
import data


#   Creating an order
def post_new_order(order_body):
	return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
	                     json = order_body,
	                     headers = data.headers)

def get_order(track):
	return  requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + track,
						  headers = data.headers)
