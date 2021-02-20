import requests
import codecs
import sqlite3
import datetime
moonlamp_db = '/moonlamp.db'

def request_handler(request):
	if request['method'] == 'GET':

		red_col, green_col, blue_col = (252, 252, 242)
		date_object = datetime.date.today()

		conn = sqlite3.connect(moonlamp_db)
		c = conn.cursor()
		c.execute('''CREATE TABLE IF NOT EXISTS moonlamp_table (red_val int, green_val int, blue_val int, timing timestamp);''')
		count = c.execute('''SELECT COUNT(*) FROM moonlamp_table;''').fetchone()[0]
		

		if count > 0:
			red_col, green_col, blue_col, moon_date = c.execute('''SELECT * FROM moonlamp_table ORDER BY timing DESC; ''').fetchone()
		else:
			c.execute('''INSERT into moonlamp_table VALUES(?,?,?,?);''', (red_col, green_col, blue_col, datetime.date.today()))
		
		if date_object != moon_date:
			date_string = date_object.strftime("%m-%d-%Y")
			if date in total:
				red_col, green_col, blue_col = (232, 16, 16)
			elif date in partial:
				red_col, green_col, blue_col = (255, 135, 141)
			else:
				URL = 'https://api.ipgeolocation.io/astronomy?apiKey=9ffd4af756ac449794129ce5903eff6a&lat=42.3657&long=71.0824'
				req = requests.get(url=URL)
				data = req.json()
				moonset = data['moonset']
				moonrise = data['moonrise']
				moondistance = data['moon_distance']
				response = requests.get(
				  'https://api.stormglass.io/v2/astronomy/point',
				  params={
				    'lat': 42.3657,
				    'lng': 71.0824,
				  },
				  headers={
				    'Authorization': 'c9bffa12-6d73-11eb-b399-0242ac130002-c9bffaa8-6d73-11eb-b399-0242ac130002'
				  }
				)
				more_data = response.json()['data'][0]
				moonvisibility = more_data['moonFraction']
				if moonvisibility >= 0.85 and moondistance <= 360000:
					red_col, green_col, blue_col = (162, 215, 252)
				elif moonvisibility >= 0.85:
					red_col, green_col, blue_col = (1, 76, 128)

			c.execute('''INSERT into smartlamp_table VALUES(?,?,?,?);''', (red_col, green_col, blue_col, datetime.date.today()))

					
		conn.commit()
		conn.close()
		response = "{}, {}, {}".format(red_col, green_col, blue_col)
		return response
					

partial = {'11-19-2021','10-28-2023','09-18-2024','08-28-2026','01-12-2028','07-06-2028','09-28-2034','08-18-2035','08-19-2035',
'06-15-2030','06-06-2039','11-30-2039','05-26-2040'}


total = {'05-26-2021','05-16-2022','11-08-2022','03-14-2025','09-07-2025','03-03-2026','12-31-2028','07-26-2029','12-20-2029',
'12-21-2029','04-25-2032','10-18-2032','04-14-2033','10-08-2033','02-11-2036','02-12-2036','08-06-2036','08-07-2036','01-31-2037',
'07-27-2037','11-18-2040'}









