from django.db import models
from django.db.models import Sum, Count, F, Value
from django.contrib.auth.models import User


# class Department(models.Model):
#     name = models.CharField(max_length=100, null=True)
#     created_on = models.DateTimeField('created_on', auto_now_add=True)

#     def __str__(self):
#         return self.name

#     class Meta:
#         ordering = ['name']


# class Category(models.Model):
#     name = models.CharField(max_length=100, null=True)
#     created_on = models.DateTimeField('created_on', auto_now_add=True)

#     def __str__(self):
#         return self.name

#     class Meta:
#         ordering = ['name']


# class SocialInsurance(models.Model):
#     code = models.CharField(max_length=100, null=True)
#     name = models.CharField(max_length=100, null=True)
#     created_on = models.DateTimeField('created_on', auto_now_add=True)

#     def __str__(self):
#         return f"{self.code}, {self.name}"

#     class Meta:
#         ordering = ['name']

# class PrePaidMedicalOp(models.Model):
#     code = models.CharField(max_length=100, null=True)
#     name = models.CharField(max_length=100, null=True)
#     created_on = models.DateTimeField('created_on', auto_now_add=True)

#     def __str__(self):
#         return f"{self.code}, {self.name}"

#     class Meta:
#         ordering = ['name']

# class Company(models.Model):
#     date_started = models.DateTimeField(null=True)
#     company_name = models.CharField(max_length=100, null=True)
#     company_name_short = models.CharField(max_length=100, null=True)
#     email = models.EmailField(max_length=100, null=True)
#     phone = models.CharField(max_length=100, null=True)
#     address = models.CharField(max_length=50, null=True)
#     address1 = models.CharField(max_length=50, null=True)
#     country = models.CharField(max_length=50, null=True)
#     city = models.CharField(max_length=100, null=True)
#     state = models.CharField(max_length=100, null=True)
#     zip_code = models.CharField(max_length=100, null=True)
#     active = models.BooleanField(default=True, null=False)
#     tax_id = models.CharField(max_length=100, null=True)
#     created_on = models.DateTimeField('created_on', auto_now_add=True)
#     logo = models.ImageField(upload_to='cia_picts/')

#     def __str__(self):
#         return f"{self.name}, {self.lastname}"

#     class Meta:
#         ordering = ['name']


# class Employee(models.Model):
#     date_hiring = models.DateTimeField(null=True)
#     first_name = models.CharField(max_length=100, null=True)
#     last_name = models.CharField(max_length=100, null=True)
#     legal_id = models.CharField(max_length=50, null=True)
#     birth_date = models.DateTimeField(null=True)
#     gender = models.CharField(max_length=1, null=True)
#     email = models.EmailField(max_length=100, null=True)
#     phone = models.CharField(max_length=100, null=True)
#     address = models.CharField(max_length=50, null=True)
#     address1 = models.CharField(max_length=50, null=True)
#     country = models.CharField(max_length=50, null=True)
#     city = models.CharField(max_length=100, null=True)
#     state = models.CharField(max_length=100, null=True)
#     zip_code = models.CharField(max_length=20, null=True)
#     active = models.BooleanField(default=True, null=False)
#     position = models.CharField(max_length=100, null=True)
#     picture = models.ImageField(upload_to='employees_picts/')
#     category = models.ForeignKey(
#         Category, on_delete=models.PROTECT, related_name='category')
#     department = models.ForeignKey(
#         Department, on_delete=models.PROTECT, related_name='department')
#     company = models.ForeignKey(
#         Company, on_delete=models.PROTECT, related_name='company')
#     insurance= models.ForeignKey(
#         SocialInsurance, on_delete=models.PROTECT, related_name='insurance')
#     prepaid= models.ForeignKey(
#         PrePaidMedicalOp, on_delete=models.PROTECT, related_name='prepaid')
#     created_on = models.DateTimeField('created_on', auto_now_add=True)

#     def __str__(self):
#         return f"{self.name}, {self.lastname}"

#     class Meta:
#         ordering = ['name']


# class SalaryHistory(models.Model):
#     date = models.DateTimeField(null=False)
#     salary = models.DecimalField(max_digits=7, decimal_places=2)
#     created_on = models.DateTimeField('created_on', auto_now_add=True)
#     employee = models.ForeignKey(
#         Employee, on_delete=models.PROTECT, related_name='employee')

#     def __str__(self):
#         return f"{self.salary}"


# class PayrollConcept(models.Model):
#     code = models.CharField(max_length=50, null=True)
#     name = models.CharField(max_length=100, null=True)
#     # haberes con aporte, sin aporte y deducciones
#     type = models.CharField(max_length=10, null=True)
#     mandatory = models.BooleanField(default=True, null=False)
#     created_on = models.DateTimeField('created_on', auto_now_add=True)

#     def __str__(self):
#         return f"{self.code}, {self.type}"


# class Payroll(models.Model):
#     code = models.CharField(max_length=50, null=True)
#     name = models.CharField(max_length=100, null=True)
#     date = models.DateTimeField(null=False)
#     date_from = models.DateTimeField(null=False)
#     date_to = models.DateTimeField(null=False)
#     open = models.BooleanField(default=True, null=False)
#     created_on = models.DateTimeField('created_on', auto_now_add=True)

#     def __str__(self):
#         return f"{self.code} - {self.name} - {self.date}"


# class PayrollDetail(models.Model):
#     employee = models.ForeignKey(
#         Employee, on_delete=models.PROTECT, related_name='employee')
#     concept = models.ForeignKey(
#         PayrollConcept, on_delete=models.PROTECT, related_name='concept')
#     qtty = models.DecimalField(max_digits=7, decimal_places=2)
#     amount = models.DecimalField(max_digits=7, decimal_places=2)
#     # automatic(can be deleted on re tries) | manual (deleted manually)
#     # manual created have prority over automatic, this way
#     # can handle concept overriding for more flexybility
#     automatic = models.BooleanField(default=True, null=False)
#     payroll = models.ForeignKey(
#         Payroll, on_delete=models.PROTECT, related_name='payroll')
#     created_on = models.DateTimeField('created_on', auto_now_add=True)




# class Appointment(models.Model):
#     start = models.DateTimeField(null=True)
#     end =  models.DateTimeField(null=True)
#     profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
#     speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)
#     contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='client')
#     created_on = models.DateTimeField('created_on', auto_now_add=True)
#     def __str__(self):
#         return "{}".format(self.contact.name)

# class Product(models.Model):
#     name = models.CharField(max_length=100, null=True)
#     price = models.DecimalField(max_digits=7, decimal_places=2)
#     dct = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
#     tax = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
#     created_on = models.DateTimeField('created_on', auto_now_add=True)
#     def __str__(self):
#         return f"{self.name} - {self.price}"

# class Invoice(models.Model):
#     contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
#     date = models.DateTimeField(null=True)
#     invoice = models.CharField(max_length=20, null=True)
#     order = models.CharField(max_length=20, null=True)
#     payment_nro = models.CharField(max_length=20, null=True)
#     payment_method = models.CharField(max_length=20, null=True)
#     created_on = models.DateTimeField('created_on', auto_now_add=True)

#     @property
#     def total(self):
#         return InvoiceDetail.objects.filter(invoice=self).aggregate(total=Sum("price"))["total"]

#     class Meta:
#         ordering = ['-date']

# class InvoiceDetail(models.Model):
#     invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='invoice_detail')
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
#     qtty = models.IntegerField(null=True, default=1)
#     price = models.DecimalField(max_digits=7, decimal_places=2)

# #Susbsistema caja
# #--------

# class Caja(models.Model):
#     fecha = models.DateTimeField(null=True)
#     apertura = models.DateTimeField(null=True)
#     cierre = models.DateTimeField(null=True)
#     descripcion = models.CharField(max_length=200, null=True)
#     monto_apertura = models.DecimalField(max_digits=7, decimal_places=2)
#     monto_cierre = models.DecimalField(max_digits=7, decimal_places=2)
#     usuario = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
#     status = models.IntegerField(null=True, default=0)
#     created_on = models.DateTimeField('created_on', auto_now_add=True)

#     def __str__(self):
#         return f"{self.fecha} - {self.monto_apertura} - {self.monto_cierre}"

#     class Meta:
#         ordering = ['-fecha']

# class CajaDetalle(models.Model):
#     caja = models.ForeignKey(Caja, on_delete=models.CASCADE, related_name='caja_detail')
#     concepto = models.CharField(max_length=100, null=True)
#     monto = models.DecimalField(max_digits=7, decimal_places=2)

#     def __str__(self):
#         return f"{self.caja.fecha} - {self.concepto} - {self.monto}"

