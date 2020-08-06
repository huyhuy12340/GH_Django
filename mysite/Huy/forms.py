from django import forms

getchoice = (('1', 'đồ ăn'), ('2', 'thức uống'))

class FormName(forms.Form):
    topic = forms.CharField()
    name = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)
    file = forms.FileField()
    abc = forms.ChoiceField(choices=getchoice)


