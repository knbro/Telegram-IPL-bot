import requests
import json
import configparser as cfg

import os
from os import environ

Telegram_Token = environ[2020490054:AAE34WE8QUEv3-cy_LqNj0w0S-Xznjxbeh8]

class telegram_chatbot():
	def __init__(self,config):
		self.token = Telegram_Token or self.read_token_from_config_file(config)
		self.base = "https://api.telegram.org/bot{}/".format(self.token)

	def get_updates(self, offset=None):
		url = self.base + "getUpdates?timeout=86400"
		if offset:
			url = url + "&offset={}".format(offset + 1)
		r = requests.get(url)	
		return json.loads(r.content)

	def send_message(self, msg, chat_id):
		url = self.base + "sendMessage?chat_id={}&text={}".format(chat_id, msg)
		if msg is not None:
			requests.get(url)

	def read_token_from_config_file(self,config):
		parser = cfg.ConfigParser()
		parser.read(config)
		return parser.get('credentials', 'token')		
