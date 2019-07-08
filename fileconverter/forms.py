from django import forms
from .models import CSVUpload
import time

class CsvForm(forms.ModelForm):

    csv_file = forms.FileField(widget=forms.FileInput(
        attrs= {
            'class': 'form-group',
        }
    ))

    class Meta:
        model = CSVUpload
        fields = ('csv_file', )

    def save(self):
        csvfile = super(CsvForm, self).save()
        return csvfile


    def clean_csv_file(self):
       uploaded_csv_file = self.cleaned_data['csv_file']
       if uploaded_csv_file:
         filename = uploaded_csv_file.name
         if filename.endswith('.csv'):
             return uploaded_csv_file 
         else:
             raise forms.ValidationError("File must be csv")
       else:
        return uploaded_csv_file