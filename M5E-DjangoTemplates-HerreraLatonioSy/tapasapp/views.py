# , ; Zale Sebastian Latonio, ; Nathan Riley Sy, 244311
# March , 2026 

'''
We hereby attest to the truth of the following facts:

We have not discussed the Python language code in our program with anyone
other than my instructor or the teaching assistants assigned to this course.

We have not used Python language code obtained from another student, or
any other unauthorized source, either modified or unmodified.

If any Python language code or documentation used in our program was
obtained from another source, such as a textbook or course notes, that has been clearly noted with proper citation in the
comments of my program.
'''

from django.shortcuts import render
from .models import Dish

# Create your views here.

def view_basic_list(request):
    dish_objects = Dish.objects.all()
    return render(request, 'tapasapp/basic_list.html', {'dishes':dish_objects})


def view_menu(request):
    dish_objects = Dish.objects.all()
    return render(request, 'tapasapp/list.html', {'dishes':dish_objects})


def add_menu(request):
    return render(request, 'tapasapp/add_menu.html')
