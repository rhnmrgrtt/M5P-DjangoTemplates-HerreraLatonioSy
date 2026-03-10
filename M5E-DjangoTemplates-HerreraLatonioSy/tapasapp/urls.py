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

from django.urls import path
from . import views


urlpatterns = [
    path('basic_list', views.view_basic_list, name='view_basic_list'),
    path('', views.view_menu, name='view_menu'),
    path('add_menu', views.add_menu, name='add_menu'),
]