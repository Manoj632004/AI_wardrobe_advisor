from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
        path('',views.get_home,name = 'home') ,
        path('closet/',views.closet,name = 'closet')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

"""
dict:
>>>outfit for my date
>>>college wear
>>>for party
>>>for grandmas funeral
>>>outfit for my brithday

output: 
<art>
fixed measurements => like neck hole and shoulder lenth ..
hidden parts of our body

1.starter:
tokenize,
ignore certain words,
read the remaining words and find the fashion topic, i.e., casuals, formals
print(fashion topic)

2.data:
type of cloth
full sleeve, half..
buttons..
colours

3.designing outfit:
import data
rules for how each fashion topic should be,i.e., formals should have collar and buttons
returns an idea of different combinations of outfit

4.convert it into a image
apply the idea to paint(auto draw w colors)
returns bunch of fotos

new:
colors represented in the basic.json should be as same as colors defined in the art <software>, so that
itll be able to call from the the dict

art software:
turtle





main_logic:
2.if choice:casuals
3.retrieve all sorts of :
    upper:[shirt,tshirt] from their retreive each's description
    lower: llly
4.retrieve colors
5.make list of combiantion,all data is there now. draw using turtle for each combinations


now step:
#drawing using turtle 
"""class draw_upper:
    def __init__(self,waist,sleeve,collar):
        pass
    def shirt(self):
        pass
    def tshirt(self):#with collar, wo collar all types and return their names too(to search on amazon)
        pass"""
#lower all sorts1.turtle,2.php,3.js


django:
django-admin startproject AI_FD 
python manage.py runserver   
python manage.py startapp <appname diff name from project's>

workon <envname>
#https://www.youtube.com/watch?v=2w8XIskzdFw"""