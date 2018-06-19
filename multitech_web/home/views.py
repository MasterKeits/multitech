from django.views import generic
from .models import Contact


class IndexView(generic.TemplateView):
	template_name = 'home/index.html'


class ContactView(generic.ListView):
	template_name = 'home/contact.html'
	context_object_name = 'contact_list'

	def get_queryset(self):
		# contacts_list = Contact.objects.filter()
		contacts_list = Contact.objects.order_by('contact_position')
		return contacts_list


class AutosView(generic.TemplateView):
	template_name = 'home/autos.html'


class ForkLiftView(generic.TemplateView):
	template_name = 'home/forklift.html'
