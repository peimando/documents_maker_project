from website.common.utils import PDF
from django.conf import settings
from django.http import FileResponse
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent.parent


def report(data):

    pdf = PDF(
        format='Letter',
        ant=data['ant'],
        mat=data['mat'],
        de=data['de'],
        cargo_de=data['cargo_de'],
        a=data['a'],
        cargo_a=data['cargo_a'],
        adj=data['adj'],
        tipo_distribucion=data['tipo_distribucion'],
        distribuciones_internas=data['distribuciones_internas'],
        distribuciones_externas=data['distribucion_externa'],  # dict of distribuciones externas
        servicio=data['servicio'],
        telefono=data['telefono'],
    )

    pdf.add_page()

    pdf.generate_inform_header()

    print(pdf.get_y())

    # Body of the ordinario
    pdf.set_text_color(111, 105, 99)
    pdf.set_font('Manrope-Regular', '', 10)
    pdf.write_html(data['cuerpo'])

    print('Despues del cuerpo: ', pdf.get_y()) # 245

    pdf.generate_firma()

    print('Despues de la firma: ', pdf.get_y())

    pdf.inform_footer()
    
    # Output file
    data['mat'] = data['mat'].lower().replace(' ', '_')

    path = BASE_DIR / 'documentos'
    fname = f"ordinario_{datetime.now().strftime('%d%m%y')}_{data['mat']}.pdf"

    file_path = Path.joinpath(path, fname)

    pdf.output(str(file_path), 'F')

    return FileResponse(
        open(f'{file_path}', 'rb'),
        as_attachment=True,  # False => if I don't want to download
        content_type='application/pdf'
    )
