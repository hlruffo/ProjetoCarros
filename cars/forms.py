from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    model = forms.CharField(max_length=200)
    class Meta:
        model = Car
        fields = '__all__'
        
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1990:
            self.add_error('factory_year', 'Ano de fabricação inválido')
        return factory_year
    