from django import forms
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def validate_url(value):
    url_validator=URLValidator()
    try:
        url_validator(value)
    except:
        raise ValidationError("INVALID URL")
    return value       

class Submitform(forms.Form):
    url=forms.CharField(label='Submit url',validators=[validate_url])


    """def clean(self):
        cleaned_data=super(Submitform,self).clean()
        url=cleaned_data.get('url')
        url_validator=URLValidator()
        try:
            url_validator(url)
        except:
            raise forms.ValidationError("INVALID URL")
        return url        
"""