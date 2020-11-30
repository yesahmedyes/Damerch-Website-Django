# import json
# import requests
# from django.conf import settings
#
# Key1 = settings.MAILCHIMP_API_KEY
# Key2 = settings.MAILCHIMP_DATA_CENTER
# Key3 = settings.MAILCHIMP_AUDIENCE_ID
#
# api_url = "https://{dc}.api.mailchimp.com/3.0/lists/{list_id}".format(dc=Key2, list_id=Key3)
#
#
# def signup(email):
#     data = {
#         "email_address": email,
#         "status": "subscribed"
#     }
#     r = requests.post(
#         api_url+"/members",
#         myauth=("", Key1),
#         data=json.dumps(data)
#     )
#     return r.status_code, r.json()
