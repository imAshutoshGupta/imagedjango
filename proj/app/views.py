from django.shortcuts import render,HttpResponse
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