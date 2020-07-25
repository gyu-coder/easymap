from django.shortcuts import render, redirect
from .models import Theme

# Create your views here.


def index(request):
    return render(request, 'selections/index.html')
    
# def select(request, select_id):
#     theme = Theme.objects.get(id=post_id)
#     context = { 'theme' : theme }
#     return render(request, 'sele')
    
def create(request):
    print(request.POST)
    bft = request.POST['bft']
    
    if "luxurious" in bft:
        context = {"bft":"luxurious"}
    elif "reasonable" in bft:
        context = {"bft":"reasonable"}
    elif "cheap" in bft:
        context = {"bft":"cheap"}
    
    
    # if "luxurious" in bft:
    #   theme = Theme(act1 = "luxurious",
    #   act2 = "luxurious",
    #   lun = "luxurious",
    #   act3 = "luxurious",
    #   act4 = "luxurious",
    #   din = "luxurious")
    # elif bft in "reasonable":
    #     theme = Theme(act1 = "reasonable",
    #     act2 = "reasonable",
    #     lun = "reasonable",
    #     act3 = "reasonable",
    #     act4 = "reasonable",
    #     din = "reasonable")
    # elif bft in "cheap":
    #     theme = Theme(act1 = "cheap",
    #     act2 = "cheap",
    #     lun = "cheap",
    #     act3 = "cheap",
    #     act4 = "cheap",
    #     din = "cheap")
    # theme.save()
    
    # context = {'theme': theme }
    
    return render(request, 'selections/select.html', context)
    
def update(request):
    
    bft = request.POST['bft']
    act1 = request.POST['act1']
    act2 = request.POST['act2']
    lun = request.POST['lun']
    act3 = request.POST['act3']
    act4 = request.POST['act4']
    din = request.POST['din']
    theme = Theme(bft=bft, act1=act1, act2=act2, lun=lun, act3=act3, act4=act4, din=din)
    theme.save()
    
    print(theme)
    
    return redirect('selections:index')
    
#def confirm(request):
    
    #theme = Theme.objects.get(user=request.user)
    
def 