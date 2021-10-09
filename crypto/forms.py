from django import forms
class CryptInput(forms.Form):
    image = forms.ImageField(
            label='Citra Digital',
            required=True,            
        )
    ACTION_CHOICES=(
    ('ENKRIPSI', 'Enkripsi'),
    ('DEKRIPSI', 'Dekripsi'),
    )
    fungsi = forms.ChoiceField(choices=ACTION_CHOICES)

    Kunci_A = forms.IntegerField(
        label='Kunci A',
        required=True,
        min_value=1,     
    )
    Kunci_B = forms.IntegerField(
        label='Kunci B',
        required=True,
        min_value=1, 
        )
    Kunci_D = forms.IntegerField(
        label='Kunci D',
        required=True,
        min_value=1, 
    )