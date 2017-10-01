import subprocess as sub
import time


def get_proc_usr(name): #not reliable
	bash= 'ps aux | grep %s | wc' % name
	command = sub.Popen(bash, stdout=sub.PIPE,shell=True)
	output, error = command.communicate()
	return (output,error)

#not reliable too
def if_left_on(name): #return true if name left server in running state else return false

	output, error = get_proc_usr(name)
	print(output)
	print( int((output).split()[0]))
	if int((output).split()[0]) > 2:
		return True
	else:
		return False

def get_data(log='/var/log/jupyterhub.log'):
	with open(log,'r') as file:
		data = file.readlines()
	return (data)

def login(date,data):
	#logi = []
	#for i in data:
		#if 'logged in' in i and date in i:
			#logi.append(i.split(':')[-1])

	return sorted(list(i.split(':')[-1] for i in data if 'logged in' in i and date in i ))

#logo = []
def logout(date,data): #date must be in english format = year-month-day
	#for i in data:
		#if 'logged out' in i and date in i:
			#logo.append(i.split(':')[-1])
	return sorted(list(i.split(':')[-1] for i in data if 'logged out' in i and date in i))


#test
def neuplne(date,data): #difference between login & logout
    logi = login(date,data)
    logo = logout(date,data)
    #out = []
    #for i in logi:
     #   if i in logo:
      #      pass
       # else:
        #    out.append(i)
    return sorted(i for i in logi if i not in logo )

import datetime

def last_seven_days(data,name): #return number of logins in last 7 days
	days, x=7,7
	pocet=0
	w_name='{:1}{}{}'.format(' ',name,'\n')
	while days!=0:
		that_date = str((datetime.datetime.now() - datetime.timedelta(days)).date())
		arr = login(that_date,data)
		if w_name in arr:
			while w_name in arr:
				pocet+=1
				arr.remove(w_name)
		days-=1
	return name,'bol prihlaseny %d krat za poslednych %d dni' % (pocet,x)

def last_x_days(data,name,x):
	days = x
	pocet=0
	w_name='{:1}{}{}'.format(' ',name,'\n')
	while days!=0:
		that_date = str((datetime.datetime.now() - datetime.timedelta(days)).date())
		arr = login(that_date,data)
		if w_name in arr:
			while w_name in arr:
				pocet+=1
				arr.remove(w_name)
		days-=1
	return name,'bol prihlaseny %d krat za poslednych %d dni' % (pocet,x)
