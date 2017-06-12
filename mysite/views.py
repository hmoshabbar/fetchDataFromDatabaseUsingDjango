from django.http import HttpResponse
import calendar

def myweb(request):
    return HttpResponse("Moshabbar Hussain Page")

def calendarWeb(request):
    x=calendar.calendar(2018,2,1,5,6)
    return HttpResponse(x)
def monthcal(request):
    x=calendar.month(2018,3)
    return HttpResponse(x)
#...............................................................
# GETTING DATA PURPOSE AND DISPLAY DATA FROM MY LOCAL SEVER

import MySQLdb
def database(request):
    SQL="select * from User"
    Con = MySQLdb.Connect(host="127.0.0.1",
                          port=3306,
                          user="root",
                          passwd="hussain",
                          db="user")
    cursor=Con.cursor()
    cursor.execute(SQL)
    x=cursor.fetchall()
    return HttpResponse(x)
    

#............................................................

def add(request):
    
    x=int(input("Enter Your x:"))
    y=int(input("Enter your y:"))
    c=x+y
    return HttpResponse(c)

    




                          
                          
                         
