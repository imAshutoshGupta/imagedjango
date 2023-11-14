from django.shortcuts import render,HttpResponse
from django.views import View
from django.core.files.storage import FileSystemStorage
from .models import uploadFile
# Create your views here.

def image(request):
    pass

def upload(request):
    if request.method == 'POST':
        fileobj = request.FILES['myimage']
        print(fileobj) #fetched the object
        print(fileobj.name)     #it is the name attribute value
        fs=FileSystemStorage()  #this is an inbuilt class
        
        filename=fs.save(fileobj.name,fileobj)  #save
        print(filename)
        url=fs.url(filename) #this will fetch the url path of the file
        print(url)
        
        uobj=uploadFile.objects.create(path=url)
        uobj.save()
        return HttpResponse("File uploaded")
    else:
        return render(request,'upload.html')

def showimage(request):
    imgs=uploadFile.objects.all()
    context = {'images' : imgs}
    return render(request,'showimage.html',context)

class FormData(View):
    def get(self,request):
        return render(request,'form.html')
    
    def post(self, request):
        
            fn=request.POST['fname']
            ln=request.POST['lname']
            print(fn)
            print(ln)
            return HttpResponse("Data fetched")
        #return render(request,'form.html')