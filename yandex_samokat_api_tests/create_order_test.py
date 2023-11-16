import data
import sender_stand_request
import json


#   Order creation
def test_create_order():
	post_order_response = sender_stand_request.post_new_order(data.order_body)
	track = str(json.loads(post_order_response.text)["track"])
	get_order_response = sender_stand_request.get_order(track)
	assert get_order_response.status_code == 200
