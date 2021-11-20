from django.shortcuts import render, get_object_or_404
from .models import iedcinfo,milestone,events,all_photos
from .forms import form_msg
# Create your views here.
def home(request):
    return render(request, 'landing/home.html', )

def iedc(request):
    info=iedcinfo.objects
    print('type',type(info))
    print('info',info)
    data1=milestone.objects
    
    data=events.objects.all().order_by('-id')
    count1=data.count()
    count=count1-3
    
    

    
    # if request.method =='POST':
    #     filled_form= form_msg(request.POST)
    #     if filled_form.is_valid():
    #         note='Thanks for your message %s'%(filled_form.cleaned_data['name'])
    #     new_form=form_msg()
    #     return render(request, 'main/iedc.html',{'iedcinfo':info,'milestone':data1,'events':data2,'form':new_form,'note':note})

    # else:
    #     form=form_msg()
    return render(request, 'main/iedc.html',{'iedcinfo':info,'milestone':data1,'events':data,'count':count})

def detail(request):
    
    info=get_object_or_404(iedcinfo,pk=1)
    
    return render(request, 'main/detail.html',{'iedcinfo':info})

def event(request,id):
    event=get_object_or_404(events,pk=id)
    return render(request,'main/event.html',{'events':event})

def all_events(request):
    event=events.objects.all().order_by('-id')
    return render(request,'main/events.html',{'allevents':event})

def image(request, id):
    info=get_object_or_404(iedcinfo,pk=1)
    image=get_object_or_404(all_photos, pk=id)
    return render(request,'main/image.html',{'image':image,'iedcinfo':info})

def event_image(request, id):
    data=events.objects
    image=get_object_or_404(all_photos, pk=id)
    return render(request,'main/event_image.html',{'image':image,'photo': data})

def gallery(request):
    info=get_object_or_404(iedcinfo,pk=1)
    
    return render(request,'main/Gallery.html',{'iedcinfo':info})
