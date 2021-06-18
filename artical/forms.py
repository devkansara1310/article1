from django import forms
from .models import Artical,ArticalTag

class articalForm(forms.ModelForm):
    class Meta:
        model = Artical
        fields='__all__'
        widgets= {
            # 'User': forms.HiddenInput(),
            #  'status': forms.CharField(widget=forms.HiddenInput(), initial="published") 
        }  
        def save(self):
            pass

        
class tagForm(forms.ModelForm):
    class Meta:
        model = ArticalTag
        fields='__all__'




        
        
        