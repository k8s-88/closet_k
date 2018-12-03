from django import forms


class SizeForm(forms.Form):

    SHOE_SIZE_CHOICES = [(i, i,) for i in range(3, 14)]
  
    quantity = forms.IntegerField(label='quantity', required=True)
    shoe_sizes = forms.ChoiceField(label="Select Size", choices=SHOE_SIZE_CHOICES, required=True)
   