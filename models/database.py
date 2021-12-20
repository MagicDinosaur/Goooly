import inspect, os, csv
import logging
import mysql.connector

class database:

	def __init__(self, server_name, username, password, dbn):
		self.conn = mysql.connector.connect(user=username, password=password,
											host=server_name,
											database=dbn)
		self.database = dbn
		self.cursor = self.conn.cursor()

