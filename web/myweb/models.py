from django.db import models
class UpdateHomePhoto(models.Model):
    img1=models.ImageField(upload_to='myweb/images',default="")
    imgmob=models.ImageField(upload_to='myweb/images',default="")

class iam(models.Model):
    im=models.CharField(max_length=120)
    def __str__(self):
        return self.im
class UpdateAboutPhoto(models.Model):
    img3=models.ImageField(upload_to='myweb/images',default="")
    
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.CharField(max_length=1000)
    def __str__(self):
        return self.name
class UpdateAbout(models.Model):
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.description[:100]+"...."
class UpdateProgressBar(models.Model):
    name=models.CharField(max_length=120)
    progress=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class UpdateCertifications(models.Model):
    desc2=models.TextField(blank=True,null=True)
    def __str__(self):
        return self.desc2[:100]+"...."
class UpdateCertiPhoto(models.Model):
    image=models.ImageField(upload_to='myweb/images',default="")
    desc=models.CharField(max_length=500,blank=True)
    def __str__(self):
        return self.desc
class UpdateSkills(models.Model):
    desc3 = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.desc3[:100]+"...."

class UpdateColor(models.Model):
    col=models.CharField(max_length=50)
    NavCont=models.CharField(max_length=50,blank=True)
    iamtext=models.CharField(max_length=50,blank=True)
    svg=models.CharField(max_length=50,blank=True)
    footersvg=models.CharField(max_length=50,blank=True)
    footertext=models.CharField(max_length=50,blank=True)
    footerbg=models.CharField(max_length=50,blank=True)
    bodybg=models.CharField(max_length=50,blank=True)
    bodytxt=models.CharField(max_length=50,blank=True)
    next=models.CharField(max_length=50,blank=True)
    nextbg=models.CharField(max_length=50,blank=True)
    nexthov=models.CharField(max_length=50,blank=True)


