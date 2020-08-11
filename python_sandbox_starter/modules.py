# A module is basically a file containing a set of functions to include in your application. 
# There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules
#import datetime
#today = datetime.date.today()

# from datetime import date
# today =date.today()
# #print(today)
# import time
# timestamp = time.time()

# print(timestamp)

# import camelcase

# c =camelcase.CamelCase()

# print(c.hump('i love you, god'))

# import validator

# v= validator

# print (v.validate_email('c.gao@ecj.com.au'))

import classes

oUser = classes.clsUser("CG",40)

oUser.greeting()

oCustomer = classes.clsCustomer("Lynn",40)
oCustomer.greeting()
oCustomer.setBalance(1000000000)
oCustomer.showBalance()