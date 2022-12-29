from django import forms


class storeForm(forms.Form):
    state = (
        (0, '营业中'),
        (1, '休息中')
    )
    store_name = forms.CharField(label="商铺名称", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': "商铺名称",'autofocus': ''}))
    store_des = forms.CharField(label="商铺描述", widget=forms.TextInput(attrs={'class': 'form-control','placeholder': "商铺描述"}))
    store_state = forms.ChoiceField(label='商铺状态', choices=state, )
    store_image = forms.ImageField(label='商铺照片')
    manager_name = forms.CharField(label="所属商家名称", max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "商家名称", 'autofocus': ''}))

