from datetime import datetime
from django.contrib import messages
from django.http import FileResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import View, FormView, CreateView
from django.urls import reverse_lazy
from common.utils import PDF
from website.forms import OrdinarioPdfForm, AddOrdinarioForm
from pathlib import Path
from ordinario.models import Ordinario



BASE_DIR = Path(__file__).resolve().parent.parent.parent

class AddOrdinario(CreateView):

    models = Ordinario

    form_class = AddOrdinarioForm

    template_name = 'website/add_ordinario.html'
   
    def form_valid(self, form):
        
        self.object = form.save(commit=False)

        # ant = form.cleaned_data['ant']
        # mat = form.cleaned_data['mat']
        # de = form.cleaned_data['de']
        # cargo_de = form.cleaned_data['cargo_de']
        # a = form.cleaned_data['a']
        # cargo_a = form.cleaned_data['cargo_a']
        # cuerpo = form.cleaned_data['cuerpo']
        # adj = form.cleaned_data['adj']
        # tipo_distribucion = form.cleaned_data['tipo_distribucion']
        # distribuciones_internas = form.cleaned_data['distribuciones_internas']
        # distribucion_externa = form.cleaned_data['distribucion_externa']
        # direccion_distribucion_externa = form.cleaned_data['direccion_distribucion_externa']
        # servicio = form.cleaned_data['servicio']
        # servicio = dict(form.fields['servicio'].choices)[servicio]
        # telefono = form.cleaned_data['telefono']

        # selected_choices = distribuciones_internas
        # choices = dict(form.fields['distribuciones_internas'].choices)

        # selected_choices_values = [choices[selected_key] for selected_key in choices.keys() if selected_key in selected_choices]

        # form_data = {
        #     'ant': ant,
        #     'mat': mat,
        #     'de': de,
        #     'cargo_de': cargo_de,
        #     'a': a,
        #     'cargo_a': cargo_a,
        #     'cuerpo': cuerpo,
        #     'adj': adj,
        #     'tipo_distribucion': tipo_distribucion,
        #     'distribuciones_internas': selected_choices_values,
        #     'distribucion_externa': distribucion_externa,
        #     'direccion_distribucion_externa': direccion_distribucion_externa,
        #     'servicio': servicio,
        #     'telefono': str(telefono)
        # }

        # print(form_data)

        # self.object = form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            f"El ordinario '{self.object.mat}'\
                se ha generado correctamente."
        )

        return super().form_valid(form)

    def get_success_url(self) -> str:
        
        return reverse_lazy(
            'website:home'
        )



# def index(request):

#     form = OrdinarioPdfForm(request.POST or None)
#     template_name = 'website/index.html'

#     context = {
#         'form': form
#     }

#     if request.POST:

#         if form.is_valid():

#             ant = form.cleaned_data.get('ant')
#             mat = form.cleaned_data.get('mat')
#             de = form.cleaned_data.get('de')
#             cargo_de = form.cleaned_data.get('cargo_de')
#             a = form.cleaned_data.get('a')
#             cargo_a = form.cleaned_data.get('cargo_a')
#             cuerpo = form.cleaned_data.get('cuerpo')
#             adj = form.cleaned_data.get('adj')
#             tipo_distribucion = form.cleaned_data.get('tipo_distribucion')
#             distribuciones_internas = form.cleaned_data.get('distribuciones_internas')
#             distribucion_externa = form.cleaned_data.get('distribucion_externa')
#             direccion_distribucion_externa = form.cleaned_data.get('direccion_distribucion_externa')
#             servicio = form.cleaned_data.get('servicio')
#             servicio = dict(form.fields['servicio'].choices)[servicio]
#             telefono = form.cleaned_data.get('telefono')

#             selected_choices = distribuciones_internas
#             choices = dict(form.fields['distribuciones_internas'].choices)

#             selected_choices_values = [choices[selected_key] for selected_key in choices.keys() if selected_key in selected_choices]

#             form_data = {
#                 'ant': ant,
#                 'mat': mat,
#                 'de': de,
#                 'cargo_de': cargo_de,
#                 'a': a,
#                 'cargo_a': cargo_a,
#                 'cuerpo': cuerpo,
#                 'adj': adj,
#                 'tipo_distribucion': tipo_distribucion,
#                 'distribuciones_internas': selected_choices_values,
#                 'distribucion_externa': distribucion_externa,
#                 'direccion_distribucion_externa': direccion_distribucion_externa,
#                 'servicio': servicio,
#                 'telefono': str(telefono)
#             }

#             return redirect('website:report', **form_data)
               

#             # generate_pdf(form_data)

#     context['form'] = OrdinarioPdfForm()

#     return render(request, template_name, context)


# def report(request):

#     data = {
#         'ant': request.GET.get('ant', ''),
#         'mat': request.GET.get('mat', ''),
#         'de': request.GET.get('de', ''),
#         'cargo_de': request.GET.get('cargo_de', ''),
#         'a': request.GET.get('a', ''),
#         'cargo_a': request.GET.get('cargo_a', ''),
#         'cuerpo': request.GET.get('cuerpo', ''),
#         'adj': request.GET.get('adj', ''),
#         'tipo_distribucion': request.GET.get('tipo_distribucion', ''),
#         'distribuciones_internas': request.GET.getlist('distribuciones_internas', []),
#         'distribucion_externa': request.GET.get('distribucion_externa', ''),
#         'direccion_distribucion_externa': request.GET.get('direccion_distribucion_externa', ''),
#         'servicio': request.GET.get('servicio', ''),
#         'telefono': request.GET.get('telefono', ''),
#     }

#     print(data)

#     pdf = PDF(
#         format='Letter',
#         ant=data['ant'],
#         mat=data['mat'],
#         de=data['de'],
#         cargo_de=data['cargo_de'],
#         a=data['a'],
#         cargo_a=data['cargo_a'],
#         adj=data['adj'],
#         tipo_distribucion=data['tipo_distribucion'],
#         distribuciones_internas=data['distribuciones_internas'],
#         distribuciones_externas=data['distribucion_externa'],  # dict of distribuciones externas
#         servicio=data['servicio'],
#         telefono=data['telefono'],
#     )

#     pdf.add_page()

#     pdf.generate_inform_header()

#     print(pdf.get_y())

#     # Body of the ordinario
#     pdf.set_text_color(111, 105, 99)
#     pdf.set_font('Manrope-Regular', '', 10)
#     pdf.write_html(data['cuerpo'])

#     print('Despues del cuerpo: ', pdf.get_y()) # 245

#     pdf.generate_firma()

#     print('Despues de la firma: ', pdf.get_y())

#     pdf.inform_footer()
    
#     # Output file
#     data['mat'] = data['mat'].lower().replace(' ', '_')

#     path = BASE_DIR / 'documentos'
#     fname = f"ordinario_{datetime.now().strftime('%d%m%y')}_{data['mat']}.pdf"

#     file_path = Path.joinpath(path, fname)

#     pdf.output(str(file_path), 'F')

#     return FileResponse(
#         open(f'{file_path}', 'rb'),
#         as_attachment=True,  # False => if I don't want to download
#         content_type='application/pdf'
#     )
