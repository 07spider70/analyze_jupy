#!/usr/bin/python3

import argparse
from test import *

parser = argparse.ArgumentParser(description='This is test app of analyzator')

parser.add_argument('-x', action='store_true',default=False,dest='x_days',help='How many times was name login in last x days')
parser.add_argument('-li', action='store_true', default=False, dest='login_bool', help='Who was login in x date.')
parser.add_argument('-lo', action='store_true', default=False, dest='logout_bool', help='Who was loggout in x date')
#rozdiel
parser.add_argument('-ro', action='store_true', default=False, dest='rozdiel', help='Difference between login/logout')
#7 dni
parser.add_argument('-s',action='store_true', default=False, dest='sev_days', help='How many times was name login in last 7 days')
results = parser.parse_args()

def main():
		if results.x_days==True:
			print(last_x_days(get_data('jupyterhub.log'),str(input('Zadaj meno: ')),int(input('Pocet dni: '))))

		elif results.login_bool==True:
			print(login(str(input('Datum v en formate: ')),get_data('jupyterhub.log')))

		elif results.logout_bool==True:
			print(logout(str(input('Datum v en formate: ')),get_data('jupyterhub.log')))

		elif results.rozdiel==True:
			print(neuplne(str(input('Datum v en formate: ')),get_data('jupyterhub.log')))

		elif results.sev_days==True:
			print(last_seven_days(get_data('jupyterhub.log'),str(input('Zadaj meno: '))))
		else:
			return 'pass'

if __name__=='__main__':
	main()
