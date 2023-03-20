from django.shortcuts import render
from .models import Balance
from django.db.models import F
from django import http
from django.http import request
from django.http.response import HttpResponse, HttpResponseRedirect
from django.http import HttpResponse
from django.db import connection

def index(request):

    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')


def transfer(request):
    if request.method == "GET":
        with connection.cursor() as cursor:
            cursor.execute('select name from setup1_balance')
            cus_name = []
            for i in cursor.fetchall():
                cus_name.append(i[0])
            return render(request, 'transfer.html', {'customer_name': cus_name})
    elif request.method == "POST":
        sender = request.POST['Sender1']
        receiver = request.POST['Receiver1']
        amount = int(request.POST['amount1'])
        with connection.cursor() as cursor:
            cursor.execute(
                "select balance from setup1_balance where name = '%s'" % (sender))
            sender_balance = int(cursor.fetchall()[0][0])

        if int(sender_balance) >= int(amount):
            sender_new_balance = int(sender_balance) - int(amount)
            with connection.cursor() as cursor:
                update_sender_balance = "update setup1_balance set BALANCE = %d where NAME = '%s'" % (
                    sender_new_balance, sender)
                cursor.execute(update_sender_balance)
                cursor.execute(
                    "select balance from setup1_balance where name = '%s'" % (receiver))
                receiver_balance = cursor.fetchall()[0][0]
            receiver_new_balance = int(receiver_balance) + int(amount)
            with connection.cursor() as cursor:
                update_receiver_balance = "update setup1_balance set Balance = %d where NAME = '%s'" % (
                    receiver_new_balance, receiver)
                cursor.execute(update_receiver_balance)
            
            return render(request, 'transfer.html')
        else:
            return HttpResponse('home.html')

def customer(request):
    with connection.cursor() as cursor:
        cursor.execute('select * from setup1_balance')
        detail_tuple = cursor.fetchall()
        return render(request, 'customers.html', {'Balance': detail_tuple})

