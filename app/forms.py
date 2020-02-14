from django import forms

class DirectMessageForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Enter username"}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'md-textarea form-control', 'rows': 5, 'placeholder':"Enter Message"}))