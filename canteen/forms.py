from django import forms


class storeForm(forms.Form):
    state = (
        (1, '营业中'),
        (0, '休息中')
    )
    store_name = forms.CharField(label="商铺名称", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': "商铺名称",'autofocus': ''}))
    store_des = forms.CharField(label="商铺描述", widget=forms.TextInput(attrs={'class': 'form-control','placeholder': "商铺描述"}))
    store_state = forms.ChoiceField(label='商铺状态', choices=state, )
    store_image = forms.ImageField(label='商铺照片')
    manager_name = forms.CharField(label="所属商家名称", max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "商家名称", 'autofocus': ''}))

class dishForm(forms.Form):
    state = (
        (0, '售罄'),
        (1, '销售中')
    )
    dish_name = forms.CharField(label="菜品名称", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': "菜品名称",'autofocus': ''}))
    dish_des = forms.CharField(label="菜品描述", widget=forms.TextInput(attrs={'class': 'form-control','placeholder': "菜品描述"}))
    dish_state = forms.ChoiceField(label='菜品状态', choices=state, )
    dish_image = forms.ImageField(label='菜品照片')
    dish_price = forms.DecimalField(label="菜品价格", max_digits=5, decimal_places=2,)

