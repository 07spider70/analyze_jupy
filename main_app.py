#!/usr/bin/python3

import argparse
from lib import *

parser = argparse.ArgumentParser(description='Jupy log server analyzator')

parser.add_argument('-x', action='store_true',default=False,dest='x_days',help='How many times was name login in last x days')
parser.add_argument('-li', action='store_true', default=False, dest='login_bool', help='Who was login in x date.')
parser.add_argument('-lo', action='store_true', default=False, dest='logout_bool', help='Who was loggout in x date')
#rozdiel
parser.add_argument('-ro', action='store_true', default=False, dest='rozdiel', help='Difference between login/logout')
#7 dni
parser.add_argument('-s',action='store_true', default=False, dest='sev_days', help='How many times was name login in last 7 days')
parser.add_argument('-l',action='store_true',default=False, dest='lang',help='Changes lang of output between slovak/english')

results = parser.parse_args()

if open_json()["lang"]==0: #set lang according to config file
			from lang_set_sk import *
else:
			from lang_set_en import *


def main():

		if results.x_days==True:
			print(last_x_days(get_data(),str(input(name_l)),int(input(days_l)))) #!!!!!!!!!!!!!!!!!!!!!

		elif results.login_bool==True:
			print(login(str(input(input_l)),get_data()))

		elif results.logout_bool==True:
			print(logout(str(input(input_l)),get_data()))

		elif results.rozdiel==True:
			print(neuplne(str(input(input_l)),get_data()))

		elif results.lang==True:
			data = open_json()
			if data["lang"]==0:
				zapis_config("lang",1)
			else:
				zapis_config("lang",0)

		elif results.sev_days==True:
			print(last_seven_days(get_data(),str(input(name_l))))
		else:
			return 'pass'

if __name__=='__main__':
	main()
