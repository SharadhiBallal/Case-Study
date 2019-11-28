from django.shortcuts import render
import logging
import datetime
from django.http import HttpResponse
import time
import json
from numpy.random import choice
from channels import Group
from django.utils import timezone
from server.models import logDetails
#Get instance of a logger
logger = logging.getLogger(__name__)
response_list = ['error','success','info','debug']
probability =[0.05,0.8,0.1,0.05]

# Create your views here.
def ping(request):
    try:
        time.sleep(2)
        
        result = choice(response_list,p=probability)
        if result == "success":
            response = "success:Fetching users list"
            logger.info(response)
            
        elif result == "info":
            response = "Info:User is trying to fetch past 1 year data."
            logger.info(response)
        elif result == "error":
            response = "error:Internal Server Error"
            logger.error(response)
        elif result == "debug":
            response = "degug:Infrastructure at peak load"
            logger.debug(response)
                
    except Exception as e:
        response = "Internal Server Error"
        logger.error(response)

    #Save in database for later refrence
    m = logDetails(msg_type=result,msg_content=response, msg_date=datetime.datetime.now())
    m.save()
   
    #Send response to monitor
    data = result+"|"+response+"|"+myconverter(m.msg_date)
    Group('users').send({'text':data})
    return HttpResponse(response)

def monitor(request):
   
    return render(request,'monitor.html')

def getdatatable(request):
    all_message = logDetails.objects.order_by('-msg_date')
    dataList=[]
    for each in all_message:
        dataList.append({'type':each.msg_type,'msg':each.msg_content,'date':each.msg_date})
    data = { "data": dataList}
    return  HttpResponse(json.dumps(data, default = myconverter), content_type="application/json")


def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()
    
    
