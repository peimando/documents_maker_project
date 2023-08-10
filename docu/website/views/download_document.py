from datetime import datetime
from django.http import FileResponse
from django.views.generic import View
from common.utils.pdf import PDF
from pathlib import Path
from django.shortcuts import get_object_or_404
from ordinario.models import Ordinario, DistribucionExterna
from django.forms.models import model_to_dict


BASE_DIR = Path(__file__).resolve().parent.parent.parent


class DownloadDocument(View):

    template_name = 'website/add_ordinario.html'

    def get(self, request, *args, **kwargs):

        ordinario = get_object_or_404(Ordinario, slug=kwargs['slug'])

        distribuciones_externas = DistribucionExterna.objects.filter(ordinario=ordinario).values('descripcion', 'direccion')

        print(distribuciones_externas)

        pdf = PDF(
            format='Letter',
            antecedente=ordinario.antecedente,
            materia=ordinario.materia,
            de=ordinario.de,
            cargo_de=ordinario.cargo_de,
            a=ordinario.a,
            cargo_a=ordinario.cargo_a,
            adjunto=ordinario.adjunto,
            distribuciones_internas_asociadas=ordinario.distribuciones_internas_asociadas,
            tiene_distribuciones_externas=ordinario.tiene_distribucion_externa,
            distribuciones_externas_asociadas=distribuciones_externas,  # dict of distribuciones externas
            servicio=ordinario.servicio,
            telefono=str(ordinario.telefono),
        )

        pdf.add_page()

        pdf.generate_inform_header()

        # Body of the ordinario
        pdf.set_text_color(111, 105, 99)
        pdf.set_font('Manrope-Regular', '', 10)
        pdf.write_html(ordinario.cuerpo)

        pdf.generate_firma()

        pdf.inform_footer()
        
        # Output file
        name = ordinario.materia.lower().replace(' ', '_')

        path = BASE_DIR / 'documentos'
        fname = f"ordinario_{datetime.now().strftime('%d%m%y')}_{name}.pdf"

        file_path = Path.joinpath(path, fname)

        pdf.output(str(file_path), 'F')

        return FileResponse(
            open(f'{file_path}', 'rb'),
            as_attachment=True,  # False => if I don't want to download
            content_type='application/pdf'
        )
