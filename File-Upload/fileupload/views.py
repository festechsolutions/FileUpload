from django.shortcuts import render, HttpResponse
from .models import FilesUpload
# Create your views here.
def home(request):
	if request.method == "POST":
		fn = request.POST["na"]
		ln = request.POST["la"]
		p = request.POST["ph"]
		e = request.POST["em"]
		w = request.POST["we"]
		j = request.POST["jd"]
		file2 = request.FILES["file"]
		document = FilesUpload.objects.create(fname=fn,lname=ln,phonenumber=p,emai=e,workex=w,jobdes=j,file=file2)
		document.save()
		return HttpResponse("Your file was uploaded")
	return render(request, "careers.html")


