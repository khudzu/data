from django import forms
class ssim_input(forms.Form):
    image_original = forms.ImageField(
            label='Masukkan Citra Digital Original ',
            required=True,
        )
    image_result = forms.ImageField(
            label='Masukkan Citra Digital Hasil Proses Enkripsi/Dekripsi ',
            required=True,
        )