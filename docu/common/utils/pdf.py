from django.conf import settings
from fpdf import FPDF
from pathlib import Path


class PDF(FPDF):

    def __init__(
        self,
        antecedente='',
        materia='',
        de='',
        cargo_de='',
        a='',
        cargo_a='',
        adjunto='',
        distribuciones_internas_asociadas=[],
        tiene_distribuciones_externas=False,
        distribuciones_externas_asociadas=[],
        servicio='',
        telefono=None,
        **kwargs
    ):
        super(PDF, self).__init__(**kwargs)

        self._headers_cell_height = 5.5
        self.set_margins(25.23, 40, 25.23)
        self.set_auto_page_break(auto=True, margin=25)

        # Header
        self.ant = antecedente
        self.mat = materia

        # Pre footer
        self.de = de
        self.cargo_de = cargo_de
        self.a = a
        self.cargo_a = cargo_a
        self.adj = adjunto
        self.distribuciones_internas = distribuciones_internas_asociadas  # (list)
        self.tiene_distribuciones_externas = tiene_distribuciones_externas
        self.distribuciones_externas = distribuciones_externas_asociadas  # (it would be a dictionary)

        # Footer
        self._direccion = 'Balmaceda #916, La Serena, Chile'
        self._pagina_web = 'www.hospitalserena.cl'
        self._iniciales_responsabilidad_director_hls = 'LIMC'
        self.servicio = servicio
        self.telefono = telefono

        # Adding Custom font
        # Getting fonts from the static folder
        static_fonts_path = Path.joinpath(
            settings.STATICFILES_DIRS[0],
            'resources',
            'pdf',
            'fonts',
            'Manrope'
        )

        self.add_font(
            'Manrope-Regular',
            '',
            Path.joinpath(static_fonts_path, 'Manrope-Regular.ttf')
        )
        self.add_font(
            'Manrope-Medium',
            '',
            Path.joinpath(static_fonts_path, 'Manrope-Medium.ttf')
        )
        self.add_font(
            'Manrope-Bold',
            'B',
            Path.joinpath(static_fonts_path, 'Manrope-Bold.ttf')
        )

    # overriding header
    def header(self):

        # Rendering logo:
        image_path = Path.joinpath(
            settings.STATICFILES_DIRS[0],
            'resources',
            'pdf',
            'images'
        )

        # Background
        self.image(
            Path.joinpath(image_path, 'background.png'),
            0,
            0,
            w=self.w,
            h=self.h
        )

        # Logo image
        self.image(
            Path.joinpath(image_path, 'logo_hls.png'),
            x=20.31,
            y=12,
            w=58.24
        )

    def _generate_first_page_header(self):

        # Printing title:
        self.set_font('Manrope-Bold', 'B', 10)
        self.set_text_color(20, 109, 246)

        self.set_draw_color(20, 109, 246)
        self.set_line_width(0.5)
        self.line(x1=116.66, y1=28, x2=116.66, y2=46.7)

        self.set_xy(-95.88, 26.44)
        self.cell(
            60,
            self._headers_cell_height,
            "ORD: ",
            border=False,
            align='L',
            ln=True
        )

        self.set_text_color(20, 109, 246)
        self.set_font('Manrope-Bold', 'B', 10)
        self.set_x(-95.88)
        self.cell(
            60,
            self._headers_cell_height,
            "ANT: ",
            border=False,
            align='L',
            ln=False
        )

        self.set_text_color(0, 0, 0)
        self.set_font('Manrope-Regular', '', 10)
        self.set_x(-86.08)
        self.cell(
            60,
            self._headers_cell_height,
            self.ant,
            border=False,
            align='L',
            ln=True
        )

        self.set_text_color(20, 109, 246)
        self.set_font('Manrope-Bold', 'B', 10)
        self.set_x(-95.88)
        self.cell(
            60,
            self._headers_cell_height,
            "MAT: ",
            border=False,
            align='L',
            ln=False
        )

        self.set_text_color(0, 0, 0)
        self.set_font('Manrope-Regular', '', 10)
        self.set_x(-86.08)
        self.cell(
            60,
            self._headers_cell_height,
            self.mat,
            border=False,
            align='L',
            ln=True
        )

        self.set_text_color(0, 0, 0)
        self.set_font('Manrope-Regular', '', 10)
        self.set_x(-95.88)
        self.cell(
            60,
            self._headers_cell_height,
            'La Serena,',
            border=False,
            align='L',
            ln=False
        )

        # Performing a line break:
        self.ln(12)

    def generate_inform_header(self):

        self._generate_first_page_header()

        self.set_font('Manrope-Bold', 'B', 9)
        de_cell = 'De: '
        self.cell(
            self.get_string_width(de_cell),
            5,
            de_cell,
            border=False,
            ln=False
        )

        self.set_font('Manrope-Regular', '', 9)
        bold_cell = self.de
        self.cell(
            self.get_string_width(bold_cell),
            5,
            bold_cell,
            border=False,
            ln=True
        )

        # Cargo De
        self.set_font('Manrope-Bold', 'B', 9)
        self.cell(
            self.get_string_width(self.cargo_de),
            5,
            self.cargo_de,
            border=False,
            ln=True
        )

        self.set_text_color(20, 109, 246)
        self.cell(
            0,
            5,
            f"A: {self.a}",
            border=False,
            ln=True
        )

        # Cargo A
        self.cell(
            self.get_string_width(self.cargo_a),
            5,
            self.cargo_a,
            border=False,
            ln=True
        )

        self.set_draw_color(20, 109, 246)
        self.set_line_width(0.5)

        x1 = self.get_x()  # 25.23
        x2 = self.get_x() + 164.77

        y1 = y2 = self.get_y() + 6.27

        self.line(x1=x1, y1=y1, x2=x2, y2=y2)

        self.ln(11)

    def generate_firma(self):

        half_page_y_pos = self.eph/2

        self.set_draw_color(20, 109, 246)
        self.set_line_width(0.5)

        x1 = self.get_x() + 47.44
        x2 = self.get_x() + 124.77

        # si me pasé de la hoja, creo una nueva y pongo 
        # la firma al medio de la hoja
        if self.get_y() + 40 > 218:

            self.add_page()
            self.set_y(half_page_y_pos)
            y1 = y2 = self.y

        else:

            y1 = y2 = self.get_y() + 40

        self.line(x1=x1, y1=y1, x2=x2, y2=y2)
        self.ln()

        self.set_text_color(0, 0, 0)
        self.set_font('Manrope-Medium', '', 9)

        # Pie de firma
        de_w = self.get_string_width(self.de)
        de_y = y1

        self.set_xy(x=((self.w - de_w) / 2), y=de_y + 2)
        self.cell(
            de_w,
            5,
            self.de,
            border=False,
            align='C',
            ln=True
        )

        cargo_w = self.get_string_width(self.cargo_de)
        self.set_font('Manrope-Bold', 'B', 9)
        # self.set_xy(x=((self.w - cargo_w) / 2), y=self.get_y() + 1)
        self.set_xy(x=((self.w - cargo_w) / 2), y=self.y + 1)
        self.cell(
            cargo_w,
            4,
            self.cargo_de,
            border=False,
            ln=True
        )

        hosp_w = self.get_string_width('Hospital de La Serena')
        self.set_x((self.w - hosp_w) / 2)
        self.cell(
            hosp_w,
            4,
            'Hospital de La Serena',
            border=False,
            align='C',
            ln=True
        )

        self.ln(10)

    def inform_footer(self):

        self.set_y(-60)
        
        arf = self._generate_iniciales_de_responsabilidad(self.de)
        self.set_text_color(0, 0, 0)
        self.set_font('Manrope-Medium', '', 7)
        self.set_x(25)
        self.cell(
            0,
            3,
            f'{self._iniciales_responsabilidad_director_hls}/{arf}',
            border=False,
            ln=True
        )

        if self.adj:

            self.cell(
                self.get_string_width('Adj:'),
                3,
                f'Adj: {self.adj}',
                border=False,
                ln=True
            )

        else:
            self.cell(
                self.get_string_width('Adj:'),
                3,
                f'Adj: No hay.',
                border=False,
                ln=True
            )

        # DISTRIBUCIÓN
        self._generar_distribuciones()

        self.ln(5)

    def _generate_iniciales_de_responsabilidad(self, nombre_completo=''):

        palabras_a_eliminar = ["Sr.", "Sra.", "SR.", "SRA."]
        nombre_limpio = nombre_completo

        for palabra in palabras_a_eliminar:

            nombre_limpio = nombre_limpio.replace(palabra, "").strip()

        iniciales = "".join([word[0].capitalize() for word in nombre_limpio.split()])
    

        if iniciales == 'LIMC':
            
            return ''
        
        return iniciales

    def _generar_distribuciones(self):

        self.set_font('Manrope-Bold', 'B', 7)
        self.cell(
            self.get_string_width('Distribución:'),
            3,
            'Distribución: ',
            border=False,
            ln=True
        )

        self.set_font('Manrope-Regular', '', 7)

        if self.tiene_distribuciones_externas:

            distribuciones_externas = [
                {
                    'descripcion': 'Jefe Laboratorio Regional PKU-HC',
                    'direccion': 'Portales 3239, Edificio CDT, 3er Piso, Santiago Centro.'
                }
            ]

            # obtener el diccionario

            for distrib_ext in distribuciones_externas:
                
                for item in distrib_ext:

                    self.cell(
                        0,
                        3,
                        f"- {distrib_ext[item]}",
                        border=False,
                        ln=True
                    )

        if self.distribuciones_internas:

            for distrib_int in self.distribuciones_internas:

                self.cell(
                    0,
                    3,
                    f"- {distrib_int}",
                    border=False,
                    ln=True
                )

    # overriding footer
    def footer(self):

        # Position cursor at 1.5 cm from bottom:
        self.set_y(-20)
        self.set_font("Manrope-Bold", "B", 9)
        self.set_text_color(0, 0, 0)

        # Calculate the center of the footer string
        direccion_w = self.get_string_width(self._direccion)
        splitter_w = self.get_string_width('|') + 5
        pagina_web_w = self.get_string_width(self._pagina_web)

        self.set_x((self.w - (direccion_w + splitter_w + pagina_web_w)) / 2)

        # Footer
        self.cell(
            direccion_w,
            6,
            self._direccion,
            border=False,
            align="C",
            ln=False
        )

        # Draw a vertical line
        self.set_text_color(20, 109, 246)
        self.cell(
            splitter_w,
            6,
            "|",
            border=False,
            align='C',
            ln=False
        )

        self.set_text_color(0, 0, 0)
        self.cell(
            pagina_web_w,
            6,
            self._pagina_web,
            border=False,
            align='C',
            ln=True
        )

        servicio_w = self.get_string_width(self.servicio)
        telefono_w = self.get_string_width(self.telefono) + 3

        self.set_font("Manrope-Bold", "B", 9)

        self.set_x((self.w - (servicio_w + telefono_w)) / 2)
        self.cell(
            (servicio_w + telefono_w),
            6,
            f'{self.servicio} - {self.telefono}',
            border=False,
            align='C',
            ln=False
        )
