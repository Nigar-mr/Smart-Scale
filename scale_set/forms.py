from django import forms
from .models import *


class RegisterForm(forms.ModelForm):
    age = forms.DateTimeField(input_formats=["%m/%d/%Y"], widget=forms.DateTimeInput(attrs={
        'class': 'form-control datetimepicker-input',
        'data-target': '#datetimepicker1'
    }))

    class Meta:
        model = InfoFields
        fields = ['age', 'gender', 'breed', 'feed', 'special_case']
        widgets = {
            "gender": forms.Select(attrs={"class": "form-control"}),
            "breed": forms.TextInput(attrs={"class": "form-control"}),
            "feed": forms.TextInput(attrs={"class": "form-control"}),
            "special_case": forms.TextInput(attrs={"class": "form-control"})
        }
        labels = {
            'age': "Yası",
            'gender': 'Cinsiyyət',
            'breed': "Cins",
            'feed': "Yem",
        }


class LoginForm(forms.Form):
    username = forms.CharField(label='İstifadəçi Adı', widget=forms.TextInput(
        attrs={
            "class": "form-control"
        }
    ))
    password = forms.CharField(label='Şifrə', widget=forms.PasswordInput(
        attrs={
            "class": "form-control"
        }
    ))

class EditForm(forms.ModelForm):
    qida = (
        ("Saman", " Saman"),
        ("Senaj", "Senaj"),
        ("Quru ot", "Quru ot"),
        ("Ot unu", "Ot unu"),
        ("Çiyid qabigi", "Çiyid qabigi"),
        ("Buğda", "Buğda"),
        ("Çovdar", "Çovdar"),
        ("Arpa", "Arpa"),
        ("Vələmir", "Vələmir"),
        ("Darı", "Darı"),
        ("Düyü", "Düyü"),
        ("Qarğıdalı", "Qarğıdalı"),
        ("Yem noxudu", "Yem noxudu"),
        ("Soya", "Soya"),
        ("Günəbaxan jmıxı", "Günəbaxan jmıxı"),
        ("Pambıq çiyidi", "Pambıq çiyidi"),
        ("Jmıx", "Jmıx"),
        ("Kök yumruları", "Kök yumruları"),
        ("Şəkər çuğunduru", "Şəkər çuğunduru"),
        ('Yaşıl kütlə', "Yaşıl kütlə"),
        ("Yem balqabağı", "Yem balqabağı"),
        ("Qarpız", "Qarpız"),
        ("Silos", "Silos"),
        ("Ət unu", "Ət unu"),
        ("Sümük unu", "Sümük unu"),
        ("Ət-sümük unu", " Ət-sümük unu"),
        ("Balıq unu", " SaBalıq unuman"),
        ("Üzlü süd əvəzediciləri", " Üzlü süd əvəzediciləri"),
    )
    nov = (
        ("Y/Ətlik-südlük", "Yerli : Ətlik-Südlük -- Ağqulaq"),
        ("Y/Ətlik-südlük", "Yerli : Ətlik-Südlük -- Qafqaz qonuru"),
        ("X/Ətlik-südlük", "Xarici : Ətlik-Südlük -- Simmental"),
        ("X/Südlük", "Xarici : Südlük -- Holstein Friesian"),
        ("X/Südlük", "Xarici : Südlük -- Brown Swiss"),
        ("X/Südlük", "Xarici : Südlük -- Jersey"),
        ("X/Südlük", "Xarici : Südlük -- Hereford"),
        ("X/Ətlik", "Xarici : Ətlik -- Angus"),
        ("X/Ətlik", "Xarici : Ətlik -- Limousin"),
        ("X/Ətlik", "Xarici : Ətlik -- Sharole"),
        ("X/Ətlik", "Xarici : Ətlik -- Texas Longhorn"),
        ("X/Ətlik", "Xarici : Ətlik -- Shorthorn"),
        ("X/Ətlik", "Xarici : Ətlik -- Belgian Blue"),

    )
    age = forms.DateTimeField(label='Yaşı', input_formats=["%d/%m/%Y"])
    feed = forms.MultipleChoiceField(label='Yem', widget=forms.CheckboxSelectMultiple, choices=qida)
    breed = forms.MultipleChoiceField(label='Cins', widget=forms.CheckboxSelectMultiple, choices=nov)


    class Meta:
        model = InfoFields
        fields = ['weight', 'breed', 'feed', 'special_case','gender', 'age']
        widgets = {
            "gender": forms.Select(attrs={"class": "form-control"}),
            # "breed": forms.Select(attrs={"class": "form-control"}),
            "weight": forms.TextInput(attrs={"class": "form-control", 'readonly': 'asds'})
        }

        labels = {
            'gender': 'Cinsiyyət',
            'breed': "Cins",
            'feed': "Yem",
            'weight': 'Çəki',
            'special_case': 'Əlavələr'
        }


