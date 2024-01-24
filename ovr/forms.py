from django import forms
from .models import *
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
dd = Event_Category.objects.all().values('id')
class CONFIDENTIAL_OVR_tickitForm(forms.ModelForm):
   # favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS
    def __init__(self, *args, **kwargs):
        super(CONFIDENTIAL_OVR_tickitForm, self).__init__(*args, **kwargs)
        self.fields['Risk_Classification'].widget.attrs['readonly'] = True
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class': 'form-control',})
            self.fields[name].widget.attrs['required'] = 'required'
    class Meta:
        model = CONFIDENTIAL_OVR_tickit
        fields = [ 'Location' , 'Description','patient_type','Event_type', 'Injury_occurred' , 'Level_of_Harm','Likelihood_Category' ,  'Risk_Classification'  ,   'Event_Category' , 'Contributing_Factors']



class Replay_OvrForm(forms.ModelForm):
    
    class Meta:
        model = Replay_Ovr
        fields = ['comment' , 'Privet']





        


class Assign_To_SectionForm(forms.ModelForm):
   Assign_To_Section = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset=Quality_Departement_Service.objects.all())
   
   class Meta:
        model = CONFIDENTIAL_OVR_tickit
        fields = [
                'Assign_To_Section',
                
               ]


