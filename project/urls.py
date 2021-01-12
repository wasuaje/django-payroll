"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
#from app.views import contact, signup, home1
from app import views

# router.register(r'api/services', apiviews.ServiceViewSet)
# router.register(r'api/profesionals', apiviews.ProfesionalViewSet)
# router.register(r'api/contacts', apiviews.ContactViewSet)
# router.register(r'api/appointments', apiviews.AppointmentList)

urlpatterns = [
    path('webapp/', views.index, name='index'),
    # path('webapp/clientes', views.Clientes.as_view(), name='clientes'),
    # path('webapp/modificar-cliente/<int:pk>/', views.ModificarCliente.as_view(), name="modificar-cliente"),
    # path('webapp/crear-cliente/', views.CrearCliente.as_view(), name="crear-cliente"),
    # path('webapp/crear-cliente-ajax-form/', views.crear_cliente_ajax_form, name="crear-cliente-ajax-form"),
    # path('webapp/crear-cliente-ajax/', views.crear_cliente_ajax, name="crear-cliente-ajax"),
    # path('webapp/finish', views.finish, name='finish'),
    # path('webapp/success', views.success, name='success'),
    # path('webapp/appointment', views.appointment, name='appointment'),
    # path('webapp/appointment-modal', views.appointment_modal, name='appointment-modal'),
    # path('webapp/arqueo-modal', views.arqueo_modal, name='arqueo-modal'),
    # path('webapp/appointment/<str:startdate>/', views.appointment, name='appointment_param'),
    # path('webapp/appointment-delete/<int:pk>/', views.appointment_delete, name='appointment-delete'),
    # path('webapp/profesional-all/', views.get_profesionals, name='profesional-all'),
    # path('webapp/agenda', views.agenda, name='agenda'),
    # path('webapp/get_events', views.get_events, name='get_events'),
    # path('webapp/admin/', admin.site.urls),
    # path('webapp/ventas/', views.ListadoVentas.as_view(), name="listado_ventas"),
    # path('webapp/crear_venta/', views.CrearVenta.as_view(), name="crear_venta"),
    # path('webapp/modificar_venta/<int:pk>/', views.ModificarVenta.as_view(), name="modificar_venta"),
    # path('webapp/contact/', views.contact, name='contact'),
    # path('webapp/signup/', views.signup, name='signup'),
    # path('webapp/ventas-diarias/', views.ventas_diarias, name="ventas-diarias"),
    # path('webapp/ventas-diarias-report/', views.VentasDiariasReport.as_view(), name="ventas-diarias-report"),
    # path('webapp/ventas-profesional/', views.ventas_profesional, name="ventas-profesional"),
    # path('webapp/ventas-profesional-report/', views.VentasProfesionalReport.as_view(), name="ventas-profesional-report"),
    # path('webapp/caja', views.ListadoCaja.as_view(), name='caja'),
    # path('webapp/crear-caja/', views.CrearCaja.as_view(), name="crear-caja"),
    # path('webapp/cierre-caja/<int:pk>/', views.CerrarCaja.as_view(), name="cierre-caja"),
    # path('webapp/modificar-caja/<int:pk>/', views.ModificarCaja.as_view(), name="modificar-caja"),
    # path('webapp/get-previous-caja/', views.get_previous_caja, name="get-prev-caja"),
    # path('webapp/get-venta-dia/', views.get_venta_dia, name="get-venta-dia"),
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls'))

]

# urlpatterns = format_suffix_patterns(urlpatterns)
