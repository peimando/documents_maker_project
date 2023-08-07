from datetime import datetime
from django.http import FileResponse
from django.views.generic import View
from common.utils.pdf import PDF
from pathlib import Path
from django.shortcuts import get_object_or_404
from ordinario.models import Ordinario


BASE_DIR = Path(__file__).resolve().parent.parent.parent


class DownloadDocument(View):

    template_name = 'website/add_ordinario.html'

    def get(self, request, *args, **kwargs):

        ordinario = get_object_or_404(Ordinario, slug=kwargs['slug'])

        print(ordinario.antecendente)

        # print(request.POST.get('antecedente'))

        # Actualizar los campos en el PDF:
        # - es_distribucion_interna 
        # - distribuciones_internas_asociadas
        # - es_distribucion_externa
        # - distribuciones_externas_asociadas 
        data = {
            'antecente': ordinario.antecendente,
            'materia': ordinario.materia,
            'de': ordinario.de,
            'cargo_de': ordinario.cargo_de,
            'a': ordinario.a,
            'cargo_a': ordinario.cargo_a,
            'cuerpo': ordinario.cuerpo,
            'adjunto': request.POST.get('adjunto', ''),
            'tipo_distribucion': request.POST.get('tipo_distribucion', ''),
            'distribucion_interna': request.POST.getlist('distribucion_interna', []),
            'distribucion_externa': request.POST.get('distribucion_externa', ''),
            # 'direccion_distribucion_externa': request.GET.get('direccion_distribucion_externa', ''),
            'servicio': request.POST.get('servicio', ''),
            'telefono': request.POST.get('telefono', ''),
        }

        pdf = PDF(
            format='Letter',
            ant=data['antecente'],
            mat=data['materia'],
            de=data['de'],
            cargo_de=data['cargo_de'],
            a=data['a'],
            cargo_a=data['cargo_a'],
            adj=data['adjunto'],
            tipo_distribucion=data['tipo_distribucion'],
            distribuciones_internas=data['distribucion_interna'],
            distribuciones_externas=data['distribucion_externa'],  # dict of distribuciones externas
            servicio=data['servicio'],
            telefono=data['telefono'],
        )

        pdf.add_page()

        pdf.generate_inform_header()

        # Body of the ordinario
        pdf.set_text_color(111, 105, 99)
        pdf.set_font('Manrope-Regular', '', 10)
        pdf.write_html(data['cuerpo'])

        pdf.generate_firma()

        pdf.inform_footer()
        
        # Output file
        data['materia'] = data['materia'].lower().replace(' ', '_')

        path = BASE_DIR / 'documentos'
        fname = f"ordinario_{datetime.now().strftime('%d%m%y')}_{data['mat']}.pdf"

        file_path = Path.joinpath(path, fname)

        pdf.output(str(file_path), 'F')

        return FileResponse(
            open(f'{file_path}', 'rb'),
            as_attachment=True,  # False => if I don't want to download
            content_type='application/pdf'
        )


# class DownloadDocument(View):

#     template_name = 'website/add_ordinario.html'

#     def get(self, request, *args, **kwargs):

#         ordinario_slug = kwargs['slug']
#         ordinario_obj = Ordinario.objects.get(slug=ordinario_slug)

#         print(ordinario_obj)
