from django import forms

from gamesplay_app.gamesplay.models import Profile, Game


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    class Meta:
        model = Profile
        fields = '__all__'

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        if commit:
            self.instance.delete()
            Game.objects.all().delete()

        return self.instance


class CreateGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'


class DeleteGameForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    class Meta:
        model = Game
        fields = '__all__'

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance


class EditGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'
