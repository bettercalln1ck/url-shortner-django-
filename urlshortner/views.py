from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View

from .models import shorturl
from .forms import Submitform

# Create your views here.




def sellyo_redirect_view(request,shortenurl=None,*args,**kwargs):     # redirect the shortened url to main url
    obj=get_object_or_404(shorturl,shortenurl=shortenurl) 
    return redirect(obj.url)


def home_view_fbv(request,*args,**kwargs):
    if request.method == "POST":
        print(request.POST)
    return render(request,"urlshortner/home.html",{})    

class Home(View):
    def get(self,request,*args,**kwargs):       # handles home page
        the_form=Submitform()
        context ={
            "title":"Submit your URL HERE",   
            "form":  the_form,
        }
        return render(request,"urlshortner/home.html",context)

    def post(self,request,*args,**kwargs):       # handles post request to server
        form=Submitform(request.POST)

        context={
            "title":"Your shortened URL",
            "form": form,
            }   
        template="urlshortner/home.html"    
        if form.is_valid():                           # Handles the validity of form
            new_url=form.cleaned_data.get("url")
            created=shorturl.objects.filter(url=new_url)
            t=0
            if not created:
                t=1
                new=shorturl(url=new_url)
                new.save()
                created=new
            else:
                created=created[0]
            obj=created
            context={
                "object":obj,
                "created":created,
            }
            
            if t==1:
                template="urlshortner/success.html"         # redirect to success page if url already does not exist
            else:
                template="urlshortner/alreadyexists.html"      #redirect to already visit page if url already exist
        
        return render(request,template,context)



'''class sellCBView(View):
    def get(self,request,shortenurl=None,*args,**kwargs):
        print(shortenurl)
        obj=get_object_or_404(shorturl,shortenurl=shortenurl)
        print(obj)
        return redirect(obj.url)
        #return HttpResponse("hello again {sc}".format(sc=shortcode))    
    ''''''
    def post(self,request,*args,**kwargs):
        return HttpResponse()

     '''
'''
   try:
        obj=shorturl.objects.get(shortenurl=shortenurl)
    except:
        obj=shorturl.objects.all().first()    

    return HttpResponse("hello {sc}".format(sc=obj.url))
'''