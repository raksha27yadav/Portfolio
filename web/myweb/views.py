from django.shortcuts import render
from .models import Contact,UpdateCertiPhoto,UpdateAbout,UpdateSkills,UpdateCertifications,UpdateAboutPhoto,UpdateHomePhoto,iam,UpdateProgressBar,UpdateColor
def index(request):
    bg=UpdateColor.objects.all()[0]
    ph=UpdateCertiPhoto.objects.all()
    m=iam.objects.all()
    
    am=[]
    for i in m:
        am.append(i.im)
    print(am)
    n=len(ph)
    k=[]
    for i in range(1,n+1):
        k.append(i)
    ab=UpdateAbout.objects.all()
    about=ab[0].description
    sk=UpdateSkills.objects.all()
    skill=sk[0].desc3
    cer=UpdateCertifications.objects.all()
    certi=cer[0].desc2
    pr=UpdateProgressBar.objects.all()
    
    hm=UpdateHomePhoto.objects.all()[0]
    abim=UpdateAboutPhoto.objects.all()
    abimg=abim[0].img3


    return render(request, 'index.html',{'ph':ph,'k':k,'about':about,'skill':skill,'certi':certi,'hm':hm,'am':am,'abimg':abimg,'pr':pr,'bg':bg})
def thanks(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        msg=request.POST.get("msg")

        index=Contact(name=name,email=email,message=msg)
        index.save()
    return render(request,'thanks.html')
