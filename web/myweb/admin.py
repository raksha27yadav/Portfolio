from django.contrib import admin
from .models import Contact,UpdateAbout,UpdateCertifications,UpdateCertiPhoto,UpdateSkills,UpdateHomePhoto,iam,UpdateAboutPhoto,UpdateProgressBar,UpdateColor
from django import forms
class UpdateAboutModelForm(forms.ModelForm):
    description=forms.CharField(widget=forms.Textarea)
    class Meta:
        model=UpdateAbout
        fields='__all__'
class UpdateAboutAdmin(admin.ModelAdmin):
    form=UpdateAboutModelForm
    
    

class UpdateSkillsModelForm(forms.ModelForm):
    desc3=forms.CharField(widget=forms.Textarea)
    class Meta:
        model=UpdateAbout
        fields='__all__'
class UpdateSkillsAdmin(admin.ModelAdmin):
    form=UpdateSkillsModelForm
    





class ContactModelForm(forms.ModelForm):
    message=forms.CharField(widget=forms.Textarea)
    class Meta:
        model=Contact
        fields='__all__'
class ContactAdmin(admin.ModelAdmin):
    form=ContactModelForm
    
    
    
class UpdateCertificationsModelForm(forms.ModelForm):
    desc2=forms.CharField(widget=forms.Textarea)
    class Meta:
        model=UpdateCertifications
        fields='__all__'
class UpdateCertificationsAdmin(admin.ModelAdmin):
    form=UpdateCertificationsModelForm
    
    
    
admin.site.register(Contact,ContactAdmin)
admin.site.register(UpdateAbout,UpdateAboutAdmin)
admin.site.register(UpdateCertifications,UpdateCertificationsAdmin)
admin.site.register(UpdateCertiPhoto)
admin.site.register(UpdateSkills,UpdateSkillsAdmin)
admin.site.register(UpdateAboutPhoto)
admin.site.register(UpdateHomePhoto)
admin.site.register(iam)
admin.site.register(UpdateProgressBar)
admin.site.register(UpdateColor)

# Register your models here.
