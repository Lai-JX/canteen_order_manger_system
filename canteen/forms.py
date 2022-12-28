from django import forms


class RegisterForm(forms.Form):

    gender = (
        (1, "男"),
        (0, "女"),
    )
    sex = forms.ChoiceField(label='性别', choices=gender, )
