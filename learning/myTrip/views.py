from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
# Create your views here.


def index(request):

    # dest1 = Destination()
    # dest1.name='Goa'
    # dest1.desc=' Experience world-class music, dance, and sunset'
    # dest1.price= 900
    # dest1.img='destination_1.jpg'
    # dest1.offer=True

    # dest2 = Destination()
    # dest2.name='Assam'
    # dest2.desc=' Beautiful lush covers of greenery'
    # dest2.price= 700
    # dest2.img='destination_2.jpg'
    # dest2.offer=False

    # dest3 = Destination()
    # dest3.name='Kolkata'
    # dest3.desc='City of joy.'
    # dest3.price= 800
    # dest3.img='destination_3.jpg'
    # dest3.offer=False

    # dest4 = Destination()
    # dest4.name='Delhi'
    # dest4.desc='Delhi Dilwalon ki !!'
    # dest4.price= 650
    # dest4.img='destination_4.jpg'
    # dest4.offer=False

    # dest5 = Destination()
    # dest5.name='Andaman Island'
    # dest5.desc='Emerald, Blue and You'
    # dest5.price= 850
    # dest5.img='destination_5.jpg'
    # dest5.offer=False

    # dest6 = Destination()
    # dest6.name='Mykonos Blu'
    # dest6.desc='Best Holiday Destination'
    # dest6.price= 950
    # dest6.img='destination_6.jpg'
    # dest6.offer=False

    # dests = [dest1,dest2,dest3,dest4,dest5,dest6]

    dests = Destination.objects.all()
    return render(request,'index.html',{'dests':dests})

