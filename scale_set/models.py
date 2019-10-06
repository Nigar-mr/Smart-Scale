from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User

# Create your models here.
class InfoFields(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    T_GENDER = (
        ("E", "Erkək"),
        ("D", "Dişi")
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

    number = models.CharField(max_length=50, null=True,blank=True)
    weight = models.FloatField(null=True,blank=True)
    gender = models.CharField(max_length=55, choices=T_GENDER,null=True,blank=True)
    breed = MultiSelectField(max_length=55, choices=nov, null=True,blank=True)
    feed = MultiSelectField(max_length=55, choices=qida, null=True,blank=True)
    special_case = models.CharField(max_length=100, null=True, blank=True)
    age = models.DateTimeField(null=True, blank=True)

    publish_date = models.DateField(auto_now_add=False, null=True)
    create_date = models.DateTimeField(auto_now_add=True, null=True)

