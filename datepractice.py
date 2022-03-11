from calendar import weekday
import random
import time

codes=[6,2,2,5,0,3,5,1,4,6,2,4]
week=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    
def str_time_prop(start, end, time_format, prop):
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))

def random_date(start, end, prop):
    return str_time_prop(start, end, '%m/%d/%Y %I:%M %p', prop)

def checkanswer(question):
    month=int(question[0:2])
    date=int(question[3:5])
    year=int(question[8:10])
    index=month-1
    monthcode=codes[index]
    if((year%4)==0)and(index<=1):
        monthcode -= 1
    weekday=(date+monthcode+year+year//4)%7
    correct=week[weekday]
    return correct

answer = "start"
while(answer != "Exit"):
    newdate = random_date("1/1/2000 1:30 PM", "12/31/2099 4:50 AM", random.random())
    question = newdate[0:11]
    print(question)
    answer = input("What day of the week does this date fall on?")
    answer=answer.capitalize()
    correct = checkanswer(question)
    if(answer==correct):
        print("Correct")
    else:
        print("Incorrect: The answer is "+correct)
        print(answer)
        print(correct)
    print("")