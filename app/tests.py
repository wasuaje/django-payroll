from django.test import TestCase
from decimal import *
from datetime import datetime
# Create your tests here.
from django.test import TestCase
from app.models import Contact, Speciality, Profesional, Appointment, Product, Invoice, Caja
from django.contrib.auth.models import User
from app import views
from django.urls import reverse


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(email="wasuaje-test@gmail.com")        

    def test_user_are_correct(self):
        """User retrieve data"""
        gm = User.objects.get(email="wasuaje-test@gmail.com")        
        self.assertEqual(gm.email, 'wasuaje-test@gmail.com')        

class ContactTestCase(TestCase):
    def setUp(self):
        Contact.objects.create(name="wuelfhis", age=25, gender='T')        

    def test_contact_are_correct(self):
        """Contact retrieve data"""
        gm = Contact.objects.get(name="wuelfhis")        
        self.assertEqual(gm.name, 'wuelfhis')        
        self.assertEqual(gm.age, 25)        
        self.assertEqual(gm.gender, 'T')        

class SpecialityTestCase(TestCase):
    def setUp(self):
        Speciality.objects.create(name="Lavado y Planchado")        

    def test_speciality_are_correct(self):
        """Speciality retrieve data"""
        gm = Speciality.objects.get(name="Lavado y Planchado")        
        self.assertEqual(gm.name, 'Lavado y Planchado')        

class ProfesionalTestCase(TestCase):
    def setUp(self):
        Profesional.objects.create(name="Andres Galarraga",email='andres@gmail.com', gender='M', phone='5491123322332')        
     

    def test_profesional_are_correct(self):
        """Profesional retrieve data"""
        gm = Profesional.objects.get(name="Andres Galarraga")        
        self.assertEqual(gm.name, 'Andres Galarraga')   
        self.assertEqual(gm.email, 'andres@gmail.com')        
        self.assertEqual(gm.gender, 'M')
        self.assertEqual(gm.phone, '5491123322332')        
             
class AppointmentTestCase(TestCase):
    def setUp(self):
        pr = Profesional.objects.create(name="Andres Galarraga",email='andres@gmail.com', gender='M', phone='5491123322332')        
        sp = Speciality.objects.create(name="Lavado y Planchado")        
        ct = Contact.objects.create(name="wuelfhis", age=25, gender='T')   
        Appointment.objects.create(profesional=pr,
                                    speciality=sp, 
                                    contact=ct, 
                                    start='2020-01-01 12:00:00',
                                    end='2020-01-01 12:30:00')        

    def test_appointment_are_correct(self):
        """Appoinments retrieve data"""
        gm = Appointment.objects.get(profesional__name="Andres Galarraga")        
        self.assertEqual(datetime.strftime(gm.start, "%Y-%m-%d %H:%M:%S"), '2020-01-01 12:00:00')   
        self.assertEqual(datetime.strftime(gm.end, "%Y-%m-%d %H:%M:%S"), '2020-01-01 12:30:00')        


class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name=u"Lavado y Enjuage",price=102.34, dct=10.00, tax=5.00)        

    def test_product_are_correct(self):
        """Product retrieve data"""
        gm = Product.objects.get(name="Lavado y Enjuage")        
        self.assertEqual(gm.name, u'Lavado y Enjuage')   
        self.assertEqual(str(gm.price), '102.34')
        self.assertEqual(str(gm.dct), '10.00')
        self.assertEqual(str(gm.tax), '5.00')

class InvoiceTestCase(TestCase):
    def setUp(self):        
        ct = Contact.objects.create(name="wuelfhis", age=25, gender='T')   
        Invoice.objects.create(     contact=ct, 
                                    date='2020-01-01 12:00:00',
                                    invoice='FACT-001')        

    def test_invoice_are_correct(self):
        """Invoice retrieve data"""
        gm = Invoice.objects.get(invoice="FACT-001")        
        self.assertEqual(datetime.strftime(gm.date, "%Y-%m-%d %H:%M:%S"), '2020-01-01 12:00:00')   
        self.assertEqual(gm.invoice,  'FACT-001')
        self.assertEqual(gm.contact.name,  'wuelfhis')

class CajaTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(email="wasuaje-test@gmail.com")                
        Caja.objects.create(     usuario=user, 
                                 fecha='2020-01-01 12:00:00',
                                monto_apertura=1234.56,
                                monto_cierre=9807.54)        

    def test_caja_are_correct(self):
        """Caja retrieve data"""
        gm = Caja.objects.get(monto_apertura=1234.56)        
        self.assertEqual(datetime.strftime(gm.fecha, "%Y-%m-%d %H:%M:%S"), '2020-01-01 12:00:00')   
        self.assertEqual(str(gm.monto_apertura),  '1234.56')
        self.assertEqual(str(gm.monto_cierre),  '9807.54')
        self.assertEqual(gm.usuario.email,  'wasuaje-test@gmail.com')


### Test Views ###

# class CajaDetailViewTests(TestCase):
#     def test_caja_created(self):
#         """
#         The detail view of a question with a pub_date in the future
#         returns a 404 not found.
#         """
#         user = User.objects.create(email="wasuaje-test@gmail.com")                
#         caja = Caja.objects.create( usuario=user, 
#                                  fecha='2020-02-01 12:00:00',
#                                 monto_apertura=12.56,
#                                 monto_cierre=98.54) 
#         url = reverse('modificar-caja', args=(caja.id,))
#         response = self.client.get(url)
#         print(response)
#         self.assertIn(response.status_code, [200, 302])
#         self.assertEqual(response.content, '12.56')
    
#     def test_caja_list(self):
#         """
#         The detail view of a question with a pub_date in the future
#         returns a 404 not found.
#         """
#         user = User.objects.create(email="wasuaje-test@gmail.com")                
#         caja = Caja.objects.create( usuario=user, 
#                                  fecha='2020-02-01 12:00:00',
#                                 monto_apertura=12.56,
#                                 monto_cierre=98.54) 
#         url = reverse('caja')
#         response = self.client.get(url)
#         print(response)
#         self.assertIn(response.status_code, [200, 302])
#         self.assertEqual(response.context['cajas'], '12.56')