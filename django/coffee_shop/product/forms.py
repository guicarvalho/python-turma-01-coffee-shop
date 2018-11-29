from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=30, required=True)
    email = forms.EmailField(label='E-mail', required=True)
    subject = forms.CharField(label='Assunto', widget=forms.Textarea())

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('name') and not cleaned_data.get('name').startswith('G'):
            self.add_error('name', 'O nome deve começar com a letra "G".')

    def clean_email(self):
        data = self.cleaned_data['email']

        if 'gmail' in data.split('@')[-1]:
            raise forms.ValidationError('O email não pode ser Gmail!')

