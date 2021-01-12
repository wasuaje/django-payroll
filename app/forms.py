from django import forms

# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Div, Submit, Row, Column, Field

from .models import Profesional, Speciality, Invoice, InvoiceDetail, Contact, Caja, CajaDetalle
from phonenumber_field.formfields import PhoneNumberField
from django.forms.models import inlineformset_factory

MESES = (
    (1,'Enero' ),
    (2,'Febrero' ),
    (3,'Marzo' ),
    (4,'Abril' ),
    (5,'Mayo' ),
    (6,'Junio' ),
    (7,'Julio' ),
    (8,'Agosto' ),
    (9,'Septiembre' ),
    (10,'Octubre' ),
    (11,'Noviembre' ),
    (12,'Diciembre' ),

)
STATES = (
    ('', 'STATE...'),
    ('Alabama','Alabama'),
    ('Alaska','Alaska'),
    ('Arizona','Arizona'),
    ('Arkansas','Arkansas'),
    ('California','California'),
    ('Colorado','Colorado'),
    ('Connecticut','Connecticut'),
    ('Delaware','Delaware'),
    ('Florida','Florida'),
    ('Georgia','Georgia'),
    ('Hawaii','Hawaii'),
    ('Idaho','Idaho'),
    ('Illinois','Illinois'),
    ('Indiana','Indiana'),
    ('Iowa','Iowa'),
    ('Kansas','Kansas'),
    ('Kentucky','Kentucky'),
    ('Louisiana','Louisiana'),
    ('Maine','Maine'),
    ('Maryland','Maryland'),
    ('Massachusetts','Massachusetts'),
    ('Michigan','Michigan'),
    ('Minnesota','Minnesota'),
    ('Mississippi','Mississippi'),
    ('Missouri','Missouri'),
    ('Montana','Montana'),
    ('Nebraska','Nebraska'),
    ('Nevada','Nevada'),
    ('New Hampshire','New Hampshire'),
    ('New Jersey','New Jersey'),
    ('New Mexico','New Mexico'),
    ('New York','New York'),
    ('North Carolina','North Carolina'),
    ('North Dakota','North Dakota'),
    ('Ohio','Ohio'),
    ('Oklahoma','Oklahoma'),
    ('Oregon','Oregon'),
    ('Pennsylvania','Pennsylvania'),
    ('Rhode Island','Rhode Island'),
    ('South Carolina','South Carolina'),
    ('South Dakota','South Dakota'),
    ('Tennessee','Tennessee'),
    ('Texas','Texas'),
    ('Utah','Utah'),
    ('Vermont','Vermont'),
    ('Virginia','Virginia'),
    ('Washington','Washington'),
    ('West Virginia','West Virginia'),
    ('Wisconsin','Wisconsin'),
    ('Wyoming','Wyoming')
)

GENDERS = (
    ('', 'GENDER...'),
    ('M', 'Male'),
    ('F', 'Female'),
    ('N', 'Prefer not to tell')
)
PAYMENT_METHODS = (
    ('', 'Methods...'),
    ('Efectivo', 'Efectivo'),
    ('Debito', 'Debito'),
    ('Credito', 'Credito'),
    ('M.Pago', 'M.Pago')

)
class ContactForm(forms.Form):
    date = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Date', 'class':'form-control'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'class':'form-control'}))
    age = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'Age', 'class':'form-control'}))
    gender = forms.ChoiceField(choices=GENDERS,widget=forms.Select(attrs={'placeholder': 'Gender', 'class':'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'class':'form-control'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone', 'class':'form-control'}))
    address = forms.CharField(label='Address', widget=forms.TextInput(attrs={'placeholder': 'Address', 'class':'form-control'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'City', 'class':'form-control'}))
    state = forms.ChoiceField(choices=STATES,widget=forms.Select(attrs={'placeholder': 'State', 'class':'form-control'}))
    zip_code = forms.CharField(label='Zip', widget=forms.TextInput(attrs={'placeholder': 'Zip code', 'class':'form-control'}))
    dob = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Dob', 'class':'form-control'}))
    driver_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Driver License Id', 'class':'form-control'}))
    auth_area = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Authorized Area', 'class':'form-control'}))
    auth_color = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Authorized Colors', 'class':'form-control'}))
    acceptance = forms.BooleanField(required=True, widget=forms.CheckboxInput(attrs={'placeholder': 'Acceptance', 'class':'form-control'}))

class ContactFormShort(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'class':'form-control'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone', 'class':'form-control'}))
    class Meta:
        model = Contact
        fields = ['name', 'phone']
class AppointmentForm(forms.Form):
    # client_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Client Name', 'class':'form-control'}))
    client_name = forms.ModelChoiceField(queryset=Contact.objects.all(),widget=forms.Select(attrs={'placeholder': 'Cliente', 'class':'form-control'}))
    # client_name = forms.ModelChoiceField(
    #     queryset=Contact.objects.all(),
    #     widget=autocomplete.ModelSelect2(url='client-autocomplete', attrs={'placeholder':'', 'class':'form-control',  'data-minimum-input-length': 3})
    # )
    # client_phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'', 'class':'form-control', 'type': 'tel'}))
    profesional = forms.ModelChoiceField(queryset=Profesional.objects.all(),widget=forms.Select(attrs={'placeholder': 'Profesional', 'class':'form-control'}))
    speciality = forms.ModelChoiceField(queryset=Speciality.objects.all(),widget=forms.Select(attrs={'placeholder': 'Speciality', 'class':'form-control'}))
    start = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Start Time', 'class':'form-control'}))
    end = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'End Time', 'class':'form-control'}))

class AppointmentFormDelete(forms.Form):
    client_name = forms.CharField(disabled=True, widget=forms.TextInput(attrs={'placeholder': 'Client Name', 'class':'form-control'}))
    client_phone = forms.CharField(disabled=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    profesional = forms.CharField(disabled=True, widget=forms.TextInput(attrs={'placeholder': 'Profesional', 'class':'form-control'}))
    speciality = forms.CharField(disabled=True, widget=forms.TextInput(attrs={'placeholder': 'Speciality', 'class':'form-control'}))
    start = forms.CharField(disabled=True, widget=forms.TextInput(attrs={'placeholder': 'Start Time', 'class':'form-control'}))
    end = forms.CharField(disabled=True, widget=forms.TextInput(attrs={'placeholder': 'End Time', 'class':'form-control'}))

class CrispyContactForm(ContactForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('email', css_class='form-group col-md-6 mb-0'),
                Column('password', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'address_1',
            'address_2',
            Row(
                Column('city', css_class='form-group col-md-6 mb-0'),
                Column('state', css_class='form-group col-md-4 mb-0'),
                Column('zip_code', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            'check_me_out',
            Submit('submit', 'Sign in')
        )


# class CustomCheckbox(Field):
#     template = 'app/custom_checkbox.html'


class CustomFieldForm(ContactForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('email', css_class='form-group col-md-6 mb-0'),
                Column('password', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'address_1',
            'address_2',
            Row(
                Column('city', css_class='form-group col-md-6 mb-0'),
                Column('state', css_class='form-group col-md-4 mb-0'),
                Column('zip_code', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            CustomCheckbox('check_me_out'),
            Submit('submit', 'Sign in')
        )

class VentasMonthForm(forms.Form):
    month = forms.ChoiceField(choices=MESES,widget=forms.Select(attrs={'placeholder': 'Mes', 'class':'form-control'}))
class InvoiceForm(forms.ModelForm):
    payment_method = forms.ChoiceField(choices=PAYMENT_METHODS,widget=forms.Select(attrs={'placeholder': 'Forma Pago', 'class':'form-control'}))
    class Meta:
        model = Invoice
        fields = ['contact', 'date', 'invoice', 'payment_method']

class DetalleInvoiceForm(forms.ModelForm):
    price = forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-control', 'step': '0.1'}))
    class Meta:
        model = InvoiceDetail
        fields = ['product','price', 'profesional']

    def __init__(self, *args, **kwargs):
        super(DetalleInvoiceForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'input-group'
            })

    def clean_cantidad(self):
        cantidad = self.cleaned_data['qtty']
        if cantidad == '':
            raise forms.ValidationError("Debe ingresar una cantidad valida")
        return cantidad

    def clean_price_Invoice(self):
        price = self.cleaned_data['price']
        if price == '':
            raise forms.ValidationError("Debe ingresar un precio valido")
        return price

DetalleInvoiceFormSet = inlineformset_factory(Invoice, InvoiceDetail, form=DetalleInvoiceForm, extra=6)

class CajaForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Descripcion', 'class':'form-control', "rows":20, "cols":150}))
    monto_apertura = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'Monto Apertura', 'class':'form-control', 'step': '0.1'}))
    monto_cierre = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'Monto Cierre', 'class':'form-control', 'step': '0.1'}))
    fecha = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Fecha', 'class':'form-control'}))
    class Meta:
        model = Caja
        fields = ['fecha', 'descripcion', 'monto_apertura', 'monto_cierre']

class DetalleCajaForm(forms.ModelForm):
    concepto = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Concepto', 'class':'form-control'}))
    monto = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'Monto (DblCLick=Ventas)','class':'form-control', 'step': '0.1'}))
    class Meta:
        model = CajaDetalle
        fields = ['concepto','monto']

    def __init__(self, *args, **kwargs):
        super(DetalleCajaForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'input-group'
            })

    def clean_monto(self):
        monto = self.cleaned_data['monto']
        if monto == '':
            raise forms.ValidationError("Debe ingresar una monto valido")
        return monto

    def clean_concepto(self):
        concepto = self.cleaned_data['concepto']
        if concepto == '':
            raise forms.ValidationError("Debe ingresar un concepto valido")
        return concepto

DetalleCajaFormSet = inlineformset_factory(Caja, CajaDetalle, form=DetalleCajaForm, extra=10)

class CierreCajaForm(forms.ModelForm):
    fecha = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Fecha', 'class':'form-control'}))
    class Meta:
        model = Caja
        fields = ['fecha']