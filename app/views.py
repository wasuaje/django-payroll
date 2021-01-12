# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.files.storage import default_storage

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.fields.files import FieldFile
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse

#from .forms import ContactForm, FilesForm, ContactFormSet
from django.shortcuts import render, get_object_or_404
# from app.models import Contact, Appointment, Speciality, Profesional, Invoice, InvoiceDetail, Caja, CajaDetalle
from django.contrib.auth.models import User
from django.views.generic import FormView, TemplateView, ListView, CreateView, UpdateView
from django.urls import reverse_lazy, reverse

# from .forms import ContactForm, CustomFieldForm, AppointmentForm
# from .forms import AppointmentFormDelete, DetalleInvoiceFormSet, InvoiceForm, VentasMonthForm
# from .forms import ContactFormShort, CajaForm, DetalleCajaFormSet, CierreCajaForm

from datetime import datetime, date, timedelta

from django.conf import settings

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import json

from django.db.models import Sum

# Create your views here.

# @login_required
def index(request):
    request.session['django_language'] = 'en'
    template_name = 'app/index.html'

    return render(request, template_name, {'form': 'prueba'})

# @login_required
# def step1(request):
#     template_name = 'app/step1.html'
#     form = ContactForm()
#     return render(request, template_name, {'form': form})

# @login_required
# def step2(request):
#     form = ContactForm(request.POST or None)
#     if request.method == 'POST':
#         request.session['date'] = request.POST['date']
#         request.session['name'] = request.POST['name']
#         request.session['age'] = request.POST['age']
#         request.session['gender'] = request.POST['gender']
#         #if form2.is_valid():
#             # pet = form.save(commit=False)
#             # person = Person.objects.create(fn=request.session['fn'])
#             # pet.owner = person
#             # pet.save()
#         #return HttpResponseRedirect(reverse('step2'))
#         return render(request, 'app/step2.html', {'form': form})

# @login_required
# def step3(request):
#     form = ContactForm(request.POST or None)
#     if request.method == 'POST':
#         request.session['email'] = request.POST['email']
#         request.session['phone'] = request.POST['phone']
#         request.session['address'] = request.POST['address']
#         request.session['city'] = request.POST['city']
#         request.session['state'] = request.POST['state']
#         request.session['zip_code'] = request.POST['zip_code']
#         #return HttpResponseRedirect(reverse('step3'))
#     return render(request, 'app/step3.html', {'form': form})

# @login_required
# def step4(request):
#     form = ContactForm(request.POST or None)
#     if request.method == 'POST':
#         request.session['dob'] = request.POST['dob']
#         request.session['driver_id'] = request.POST['driver_id']
#         request.session['auth_area'] = request.POST['auth_area']
#         request.session['auth_color'] = request.POST['auth_color']

#     return render(request, 'app/step4.html', {'form': form})

# @login_required
# def finish(request):
#     form = ContactForm(request.POST or None)
#     if request.method == 'POST':
#         # print(request.POST['acceptance'])
#         request.session['acceptance'] = request.POST['acceptance']
#         # print(request.POST['acceptance'])
#         contact = Contact.objects.create(
#             date = datetime.strptime(request.session['date'], '%m/%d/%Y'),
#             name = request.session['name'],
#             age = request.session['age'],
#             gender = request.session['gender'],
#             email = request.session['email'],
#             phone = request.session['phone'],
#             address = request.session['address'],
#             city = request.session['city'],
#             state = request.session['state'],
#             zip_code = request.session['zip_code'],
#             dob = request.session['dob'],
#             driver_id = request.session['driver_id'],
#             auth_area = request.session['auth_area'],
#             auth_color =request.session['auth_color'],
#             acceptance = 1 if request.session['acceptance']=='on' else 0
#             )
#         if contact:
#             return render(request, 'app/finish.html')
#     return render(request, 'app/step4.html')

# @login_required
# def success(request):

#     return render(request, 'app/finish.html')

# @login_required
# def agenda(request):

#     return render(request, 'app/agenda.html')


# def get_events(request):
#     import calendar
#     try:
#         # print(request.GET['start'],request.GET['end'])
#         _start = datetime.strptime(request.GET['start'][:-6], "%Y-%m-%dT%H:%M:%S")
#         _end = datetime.strptime(request.GET['end'][:-6], "%Y-%m-%dT%H:%M:%S")
#     except ValueError as e:
#         print(f"Warning: {e}")
#         today = datetime.today()
#         date_range = calendar.monthrange(today.year, today.month)
#         _start = datetime(today.year, today.month, date_range[0])
#         _end = datetime(today.year, today.month, date_range[1])

#     records = Appointment.objects.filter(start__gte=_start, end__lt=_end)
#     #print(_start,_end,records)
#     data = []
#     for rec in records:
#         data.append({'title': rec.__str__(),
#                      'start': rec.start.isoformat(' ')[:-6],
#                      'end': rec.end.isoformat(' ')[:-6],
#                      'resourceId': rec.profesional.pk,
#                      'url':  F"appointment-delete/{rec.pk}"
#                      })
#     #print(data)
#     return JsonResponse(data, safe=False)

# def get_profesionals(request):
#     records = Profesional.objects.all()
#     data = []
#     for rec in records:
#         data.append({'id': rec.pk,
#                      'title': rec.name[:3]
#                      })
#     #print(data)
#     return JsonResponse(data, safe=False)


# def arqueo_modal(request):
#     monto_apertura = 0.00
#     # _profId = request.GET['profId']
#     # initial = {'start': _start,
#     #             'end': _end,
#     #             'profesional': _profId}
#     # form = AppointmentForm(initial=initial)

#     return render(request, 'app/arqueo_modal.html', {'monto_apertura': monto_apertura})


# def appointment_modal(request):
#     _start = datetime.strptime(request.GET['start'][:-6], "%Y-%m-%dT%H:%M:%S")
#     _end = datetime.strptime(request.GET['end'][:-6], "%Y-%m-%dT%H:%M:%S")
#     _profId = request.GET['profId']
#     initial = {'start': _start,
#                 'end': _end,
#                 'profesional': _profId}
#     form = AppointmentForm(initial=initial)

#     return render(request, 'app/appointment_modal.html', {'form': form})


# def appointment_delete(request, pk):
#     record = Appointment.objects.filter(pk=pk)
#     initial = {'start': record[0].start,
#                'end': record[0].end,
#                'profesional': record[0].profesional.name,
#                'speciality': record[0].speciality.name

#                }
#     form = AppointmentFormDelete(initial=initial)
#     if request.method == 'POST':
#         con = Appointment.objects.filter(pk=pk).delete()
#         if con:
#             return HttpResponseRedirect(reverse('agenda'))

#     return render(request, 'app/appointment_delete.html', {'form': form, 'id': pk})

# def appointment(request):
#     form = AppointmentForm(request.POST or None)
#     if request.method == 'POST':
#         client = request.POST["client_name"]
#         # client_phone = request.POST["client_phone"]
#         start = request.POST["start"]
#         end = request.POST["end"]
#         if form.is_valid():
#             #date = datetime.strptime(request.POST["date"], '%m/%d/%Y')
#             _datetime = datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
#             # new_client, created = Contact.objects.update_or_create(
#             #         phone=client_phone,
#             #         defaults={'name': client_name},
#             #     )
#             contact = Contact.objects.get(pk = client)
#             profesional = Profesional.objects.get(pk=request.POST["profesional"])
#             speciality = Speciality.objects.get(pk=request.POST["speciality"])
#             con = Appointment(start=start, end=end,
#                             profesional=profesional, speciality=speciality, contact=contact)
#             con.save()
#             if con.pk:
#                 send_whatsapp_message(contact.name, contact.phone, _datetime)
#                 return HttpResponseRedirect(reverse('agenda'))

#     return render(request, 'app/appointment.html', {'form': form})

# def send_whatsapp_message(name, phone, _datetime):
#     account_sid = settings.TWILIO_SID
#     auth_token = settings.TWILIO_AUTH_TOKEN
#     from_phone = settings.TWILIO_PHONE
#     client = Client(account_sid, auth_token)
#     date = datetime.strftime(_datetime, "%b-%d-%Y")
#     time = datetime.strftime(_datetime, "%H:%M")
#     try:
#         message = client.messages.create(
#                                     from_=f"{from_phone}",
#                                     body=f'{name}: Your appointment is coming up on {date} at {time}',
#                                     to=f'whatsapp:{phone}'
#                                 )
#     except twilio.base.exceptions.TwilioRestException:
#         print('Error sending whatsapp')
#     else:
#         print(f"Enviado: {message.sid}")

# def contact(request):
#     template_name = 'app/index.html'
#     mess = ''
#     if request.method == 'POST':
#         # Code block for POST request
#         name = request.POST["name"]
#         email = request.POST["email"]
#         subject = request.POST["subject"]
#         message = request.POST["message"]
#         con = Contact(name=name, email=email,
#                       subject=subject, message=message)
#         con.save()
#         if con.pk:
#             mess = 'OK'
#         else:
#             mess = 'FAIL'
#     else:
#         # Code block for GET request (will also match PUT, HEAD, DELETE, etc)
#         mess = 'FAIL'

#     return HttpResponse(mess)


# def signup(request):
#     template_name = 'app/index.html'
#     mess = ''
#     if request.method == 'POST':
#         # Code block for POST request
#         email = request.POST["email2"]
#         con = Signup(email=email)
#         con.save()
#         if con.pk:
#             mess = 'OK'
#         else:
#             mess = 'FAIL'
#     else:
#         mess = 'FAIL'
#         # Code block for GET request (will also match PUT, HEAD, DELETE, etc)
#     return HttpResponse(mess)

# class ListadoVentas(LoginRequiredMixin, ListView):
#     model = Invoice
#     context_object_name = 'invoices'

# def ventas_profesional(request):
#     form = VentasMonthForm(request.POST or None)

#     return render(request, 'app/ventas_month_form.html', {'form': form, 'report':'ventas-profesional-report'})

# def ventas_diarias(request):
#     form = VentasMonthForm(request.POST or None)

#     return render(request, 'app/ventas_month_form.html', {'form': form, 'report':'ventas-diarias-report'})


# class VentasProfesionalReport(LoginRequiredMixin, ListView):
#     context_object_name = 'invoices'
#     template_name = 'app/ventas_profesional_report.html'

#     def get_queryset(self):
#         queryset = Invoice.objects.all()
#         if self.request.GET.get("month"):
#             selection = self.request.GET.get("month")
#             queryset = InvoiceDetail.objects.filter(invoice__date__month=selection)
#             # print(queryset)
#         return queryset

# class VentasDiariasReport(LoginRequiredMixin, ListView):
#     context_object_name = 'invoices'
#     template_name = 'app/ventas_diarias_report.html'

#     def get_queryset(self):
#         queryset = Invoice.objects.all()
#         if self.request.GET.get("month"):
#             selection = self.request.GET.get("month")
#             queryset = InvoiceDetail.objects.filter(invoice__date__month=selection)
#             # print(queryset)
#         return queryset


# class CrearVenta(LoginRequiredMixin, CreateView):
#     model = Invoice
#     template_name = 'app/venta.html'
#     form_class = InvoiceForm
#     success_url = reverse_lazy('listado_ventas')

#     def get_pr_obj(self):
#         pr_id = self.request.get["event_id"]
#         return Appointment.objects.get(id=pr_id)

#     def get_form_kwargs(self):
#         """
#         Returns the keyword arguments for instantiating the form.
#         """
#         invoice = 'FACT-'
#         kwargs = super(CrearVenta, self).get_form_kwargs()
#         if self.request.GET.get("event_id", False):
#             pr_id = self.request.GET["event_id"]
#             pr_obj = Appointment.objects.get(id=pr_id)
#             clientid = pr_obj.contact.id
#             date = pr_obj.created_on
#             date = datetime.strftime(date,"%Y-%m-%d")
#             init = {
#                     'contact': clientid,
#                     'date': date,
#                     'invoice': invoice
#                 }
#         else:
#             init = {
#                     'invoice': invoice
#                 }
#         kwargs.update({'initial': init})
#         return kwargs

#     def get(self, request, *args, **kwargs):
#         """Primero ponemos nuestro object como nulo, se debe tener en
#         cuenta que object se usa en la clase CreateView para crear el objeto"""
#         self.object = None
#         #Instanciamos el formulario de la Compra que declaramos en la variable form_class
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         #Instanciamos el formset
#         detalle_orden_compra_formset=DetalleInvoiceFormSet()
#         #Renderizamos el formulario de la compra y el formset
#         return self.render_to_response(self.get_context_data(form=form,
#                                                             detalle_compra_form_set=detalle_orden_compra_formset))

#     def post(self, request, *args, **kwargs):
#         #Obtenemos nuevamente la instancia del formulario de Compras
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         #Obtenemos el formset pero ya con lo que se le pasa en el POST
#         detalle_compra_form_set = DetalleInvoiceFormSet(request.POST)
#         """Llamamos a los métodos para validar el formulario de Compra y el formset, si son válidos ambos se llama al método
#         form_valid o en caso contrario se llama al método form_invalid"""
#         if form.is_valid() and detalle_compra_form_set.is_valid():
#             return self.form_valid(form, detalle_compra_form_set)
#         else:
#             print("failed", form)
#             self.object = None
#             return self.form_invalid(form, detalle_compra_form_set)

#     def form_valid(self, form, detalle_compra_form_set):
#         #Aquí ya guardamos el object de acuerdo a los valores del formulario de Compra
#         self.object = form.save()
#         #Utilizamos el atributo instance del formset para asignarle el valor del objeto Compra creado y que nos indica el modelo Foráneo
#         detalle_compra_form_set.instance = self.object
#         #Finalmente guardamos el formset para que tome los valores que tiene
#         detalle_compra_form_set.save()
#         #Redireccionamos a la ventana del listado de compras
#         return HttpResponseRedirect(self.success_url)

#     def form_invalid(self, form, detalle_compra_form_set):
#             #Si es inválido el form de Compra o el formset renderizamos los errores
#         return self.render_to_response(self.get_context_data(form=form,
#                                                             detalle_compra_form_set = detalle_compra_form_set))

# class ModificarVenta(LoginRequiredMixin, UpdateView):
#     model = Invoice
#     template_name = 'app/venta.html'
#     form_class = InvoiceForm
#     success_url = reverse_lazy('listado_ventas')

#     def get(self, request, *args, **kwargs):
#         #Obtenemos el objeto Compra
#         self.object = self.get_object()
#         #Obtenemos el formulario
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         #Obtenemos los detalles de la compra
#         detalles = InvoiceDetail.objects.filter(invoice=self.object).order_by('pk')
#         detalles_data = []
#         #Guardamos los detalles en un diccionario
#         for detalle in detalles:
#             d = {'product': detalle.product,
#                 'profesional': detalle.profesional,
#                 'price': detalle.price
#                 }
#             detalles_data.append(d)
#         #Ponemos como datos iniciales del formset el diccionario que hemos obtenido
#         detalle_compra_form_set = DetalleInvoiceFormSet(initial=detalles_data)
#         #Renderizamos el formulario y el formset
#         return self.render_to_response(self.get_context_data(form=form,
#                                                             detalle_compra_form_set=detalle_compra_form_set))

#     def post(self, request, *args, **kwargs):
#         #Obtenemos el objeto compra
#         self.object = self.get_object()
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         detalle_compra_form_set = DetalleInvoiceFormSet(request.POST)
#         #Verificamos que los formularios sean validos
#         if form.is_valid() and detalle_compra_form_set.is_valid():
#             return self.form_valid(form, detalle_compra_form_set)
#         else:
#             return self.form_invalid(form, detalle_compra_form_set)

#     def form_valid(self, form, detalle_compra_form_set):
#         #Guardamos el objeto compra
#         self.object = form.save()
#         detalle_compra_form_set.instance = self.object
#         #Eliminamos todas los detalles de la compra
#         InvoiceDetail.objects.filter(invoice = self.object).delete()
#         #Guardamos los nuevos detalles de la compra
#         detalle_compra_form_set.save()
#         return HttpResponseRedirect(self.success_url)

#     def form_invalid(self, form, detalle_compra_form_set):
#         #Renderizamos los errores
#         return self.render_to_response(self.get_context_data(form=form,
#                                                             detalle_compra_form_set = detalle_compra_form_set))

# class Clientes(LoginRequiredMixin, ListView):
#     model = Contact
#     context_object_name = 'clients'
#     template_name = 'app/clientes.html'

# class ModificarCliente(LoginRequiredMixin, UpdateView):
#     model = Contact
#     template_name = 'app/cliente.html'
#     form_class = ContactFormShort
#     success_url = reverse_lazy('clientes')

#     def get(self, request, *args, **kwargs):
#         #Obtenemos el objeto Compra
#         self.object = self.get_object()
#         #Obtenemos el formulario
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         #Obtenemos los detalles de la compra
#         #Renderizamos el formulario y el formset
#         return self.render_to_response(self.get_context_data(form=form  ))

#     def post(self, request, *args, **kwargs):
#         #Obtenemos el objeto compra
#         self.object = self.get_object()
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         #Verificamos que los formularios sean validos
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)

#     def form_valid(self, form):
#         #Guardamos el objeto compra
#         self.object = form.save()
#         form.instance = self.object
#         #Guardamos los nuevos detalles de la compra
#         return HttpResponseRedirect(self.success_url)

#     def form_invalid(self, form):
#         #Renderizamos los errores
#         return self.render_to_response(self.get_context_data(form=form ))

# class CrearCliente(LoginRequiredMixin, CreateView):
#     model = Contact
#     template_name = 'app/cliente.html'
#     form_class = ContactFormShort
#     success_url = reverse_lazy('clientes')

# def crear_cliente_ajax_form(request):

#     form = ContactFormShort()

#     return render(request, 'app/client_modal.html', {'form': form})

# def crear_cliente_ajax(request):
#     form = ContactFormShort(request.POST or None)
#     if request.method == 'POST':
#         client_name = request.POST["name"]
#         client_phone = request.POST["phone"]
#         if form.is_valid():
#             created = Contact.objects.create(
#                     phone=client_phone,
#                     name=client_name)

#             some_data_to_dump = {
#             'success': True,
#             'client_name': created.name,
#             'client_id': created.pk
#             }
#         else:
#             print(form)
#             some_data_to_dump = {
#             'success': False,
#             }

#     data = json.dumps(some_data_to_dump)
#     return HttpResponse(data, content_type='application/json')


# class ListadoCaja(LoginRequiredMixin, ListView):
#     model = Caja
#     context_object_name = 'cajas'
#     # def get_queryset(self):
#     #     """Return the last five published questions."""
#     #     return Caja.objects.all()

#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         # Add in the publisher
#         records = Caja.objects.filter(status=0)
#         if records.count() == 0:    # No open caja at the moment
#             context['allow_create'] = 0
#         else:
#             context['allow_create'] = 1
#         return context

# class CrearCaja(LoginRequiredMixin, CreateView):
#     model = Caja
#     template_name = 'app/caja.html'
#     form_class = CajaForm
#     success_url = reverse_lazy('caja')

#     def get(self, request, *args, **kwargs):
#         """Primero ponemos nuestro object como nulo, se debe tener en
#         cuenta que object se usa en la clase CreateView para crear el objeto"""
#         self.object = None
#         #Instanciamos el formulario de la Compra que declaramos en la variable form_class
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         #Instanciamos el formset
#         detalle_caja_formset=DetalleCajaFormSet()
#         #Renderizamos el formulario de la compra y el formset
#         return self.render_to_response(self.get_context_data(form=form,
#                                                             detalle_caja_form_set=detalle_caja_formset))

#     def post(self, request, *args, **kwargs):
#         #Obtenemos nuevamente la instancia del formulario de Compras
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         #Obtenemos el formset pero ya con lo que se le pasa en el POST
#         detalle_caja_formset = DetalleCajaFormSet(request.POST)
#         """Llamamos a los métodos para validar el formulario de Compra y el formset, si son válidos ambos se llama al método
#         form_valid o en caso contrario se llama al método form_invalid"""
#         if form.is_valid() and detalle_caja_formset.is_valid():
#             return self.form_valid(form, detalle_caja_formset)
#         else:
#             print("failed", form)
#             self.object = None
#             return self.form_invalid(form, detalle_caja_formset)

#     def form_valid(self, form, detalle_caja_formset):
#         #Aquí ya guardamos el object de acuerdo a los valores del formulario de Compra
#         self.object = form.save(commit=False)
#         # self.object['usuario'] = self.request.user
#         setattr(self.object, 'usuario', self.request.user)
#         self.object.save()
#         #Utilizamos el atributo instance del formset para asignarle el valor del objeto Compra creado y que nos indica el modelo Foráneo
#         detalle_caja_formset.instance = self.object
#         #Finalmente guardamos el formset para que tome los valores que tiene
#         detalle_caja_formset.save()
#         #Redireccionamos a la ventana del listado de compras
#         return HttpResponseRedirect(self.success_url)

#     def form_invalid(self, form, detalle_caja_formset):
#             #Si es inválido el form de Compra o el formset renderizamos los errores
#         return self.render_to_response(self.get_context_data(form=form,
#                                                             detalle_caja_formset = detalle_caja_formset))

# class ModificarCaja(LoginRequiredMixin, UpdateView):
#     model = Caja
#     template_name = 'app/caja.html'
#     form_class = CajaForm
#     success_url = reverse_lazy('caja')

#     def get(self, request, *args, **kwargs):
#         #Obtenemos el objeto Compra
#         self.object = self.get_object()
#         #Obtenemos el formulario
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         #Obtenemos los detalles de la compra
#         detalles = CajaDetalle.objects.filter(caja=self.object).order_by('pk')
#         detalles_data = []
#         #Guardamos los detalles en un diccionario
#         for detalle in detalles:
#             d = {'concepto': detalle.concepto,
#                 'monto': detalle.monto,
#                 }
#             detalles_data.append(d)
#         #Ponemos como datos iniciales del formset el diccionario que hemos obtenido
#         detalle_caja_form_set = DetalleCajaFormSet(initial=detalles_data)
#         #Renderizamos el formulario y el formset
#         return self.render_to_response(self.get_context_data(form=form,
#                                                             detalle_caja_form_set=detalle_caja_form_set))

#     def post(self, request, *args, **kwargs):
#         #Obtenemos el objeto compra
#         self.object = self.get_object()
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         detalle_caja_form_set = DetalleCajaFormSet(request.POST)
#         #Verificamos que los formularios sean validos
#         if form.is_valid() and detalle_caja_form_set.is_valid():
#             return self.form_valid(form, detalle_caja_form_set)
#         else:
#             return self.form_invalid(form, detalle_caja_form_set)

#     def form_valid(self, form, detalle_caja_form_set):
#         #Guardamos el objeto compra
#         self.object = form.save()
#         detalle_caja_form_set.instance = self.object
#         #Eliminamos todas los detalles de la compra
#         CajaDetalle.objects.filter(caja = self.object).delete()
#         #Guardamos los nuevos detalles de la compra
#         detalle_caja_form_set.save()
#         return HttpResponseRedirect(self.success_url)

#     def form_invalid(self, form, detalle_caja_form_set):
#         #Renderizamos los errores
#         print("failed", form)
#         return self.render_to_response(self.get_context_data(form=form,
#                                                             detalle_caja_form_set = detalle_caja_form_set))

# class CerrarCaja(LoginRequiredMixin, UpdateView):
#     model = Caja
#     template_name = 'app/caja_cerrar.html'
#     form_class = CierreCajaForm
#     success_url = reverse_lazy('caja')

#     def get_queryset(self):
#         queryset = Caja.objects.filter(status=0)
#             # print(queryset)
#         return queryset

#     def get(self, request, *args, **kwargs):
#         #Obtenemos el objeto Compra
#         self.object = self.get_object()
#         #Obtenemos el formulario
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         #Obtenemos los detalles de la compra
#         #Renderizamos el formulario y el formset
#         return self.render_to_response(self.get_context_data(form=form  ))

#     def post(self, request, *args, **kwargs):
#         #Obtenemos el objeto compra
#         self.object = self.get_object()
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         #Verificamos que los formularios sean validos
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)

#     def form_valid(self, form):
#         #Guardamos el objeto compra
#         self.object = form.save(commit=False)
#         # self.object['usuario'] = self.request.user
#         setattr(self.object, 'status', 1)
#         self.object.save()
#         self.object = form.save()
#         form.instance = self.object
#         #Guardamos los nuevos detalles de la compra
#         return HttpResponseRedirect(self.success_url)

#     def form_invalid(self, form):
#         #Renderizamos los errores
#         return self.render_to_response(self.get_context_data(form=form ))

# def get_previous_caja(request):
#     if request.method == 'GET':
#         record = Caja.objects.filter(status=1).order_by('-fecha')[0]
#         if record:
#             some_data_to_dump = {
#                 'success': True,
#                 'monto_cierre': str(record.monto_cierre),
#                 }
#         else:
#             some_data_to_dump = {
#             'success': False,
#             }

#     data = json.dumps(some_data_to_dump)
#     return HttpResponse(data, content_type='application/json')

# def get_venta_dia(request):
#     if request.method == 'GET':
#         date =  request.GET['id_fecha'][:19]
#         date = datetime.strptime(date,'%Y-%m-%d %H:%M:%S')
#         record = InvoiceDetail.objects.filter(invoice__date=date).aggregate(Sum('price'))
#         if record:
#             some_data_to_dump = {
#                 'success': True,
#                 'total_ventas': str(record['price__sum']).replace("None","0.00"),
#                 }
#         else:
#             some_data_to_dump = {
#             'success': False,
#             }

#     data = json.dumps(some_data_to_dump)
#     return HttpResponse(data, content_type='application/json')