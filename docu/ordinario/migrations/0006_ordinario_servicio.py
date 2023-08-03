# Generated by Django 4.2.3 on 2023-08-01 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordinario', '0005_ordinario_slug_alter_ordinario_distribucion_externa'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordinario',
            name='servicio',
            field=models.CharField(blank=True, choices=[('ASENF', 'Asenf'), ('CAPMED', 'Capítulo Médico'), ('CSMC', 'Centro de Salud Mental Centro (CESAM Centro)'), ('CSMLC', 'Centro de Salud Mental Las Compañías (CESAM Las Compañías)'), ('CBDC', 'Comité Bipartito de Capacitación'), ('CDA', 'Comité de Adquisiciones'), ('CDADMI', 'Comité de Auditoría de Muertes Maternas Infantiles'), ('CDEM', 'Comité de Emergencia'), ('CDET', 'Comité de Ética'), ('CDFARM', 'Comité de Farmacia'), ('CDPART', 'Comité de Participación'), ('CDSU', 'Comité de Satisfacción Usuaria'), ('CIAAS', 'Comité IAAS'), ('CMEL', 'Comité para el Mejoramiento del Entorno Laboral (MEL)'), ('CGLEGES', 'Comité para la Gestión de Listas de Espera GES'), ('CGLENOGES', 'Comité para la Gestión de Listas de Espera No GES'), ('CPARI', 'Comité Paritario'), ('DCSP', 'Departamento de Calidad y Seguridad del Paciente'), ('DPCDI', 'Departamento de Planificación, Control y Desarrollo Institucional'), ('Dirección', 'Dirección'), ('FENATS', 'Fenats'), ('FENPRUSS', 'Fenpruss'), ('HSMP', 'Hogar de Salud Mental Protegido'), ('HDDA', 'Hospital de Día Adulto'), ('JARINF', 'Jardín Infantil'), ('PSQA', 'Psiquiatría Adultos'), ('PSQIA', 'Psiquiatría Infanto Adolescente'), ('SDCA', 'Servicio de Cirugía Adultos'), ('SDCI', 'Servicio de Cirugía Infantil'), ('SDEM', 'Servicio de Especialidades Médicas'), ('SDEO', 'Servicio de Especialidades Odontológicas'), ('SDM', 'Servicio de Medicina'), ('SDMFR', 'Servicio de Medicina Física y Rehabilitación'), ('SDN', 'Servicio de Neurología'), ('SDOYG', 'Servicio de Obstetricia y Ginecología'), ('SDOFT', 'Servicio de Oftalmología'), ('SDOTO', 'Servicio de Otorrinolaringología'), ('SDPED', 'Servicio de Pediatría'), ('SDPEN', 'Servicio de Pensionado'), ('SDURO', 'Servicio de Urología'), ('SDABA', 'Subdepartamento de Abastecimiento'), ('SDAC', 'Subdepartamento de Apoyos Clínicos'), ('SDCADVL', 'Subdepartamento de Calidad de Vida Laboral'), ('SDCIDVL', 'Subdepartamento de Ciclo de Vida Laboral'), ('SDDL', 'Subdepartamento de Desarrollo Laboral'), ('SDPTODFIN', 'Subdepartamento de Finanzas'), ('SDPTOSL', 'Subdepartamento de Seguridad Laboral'), ('SDA', 'Subdirección Administrativa (SDA)'), ('SDGCAA', 'Subdirección de Gestión Clínica de Atención Ambulatoria (SDGCAA)'), ('SDGCAC', 'Subdirección de Gestión Clínica de Atención Cerrada (SDGCAC)'), ('SDGP', 'Subdirección de Gestión de Las Personas (SDGP)'), ('SDGC', 'Subdirección de Gestión del Cuidado (SDGC)'), ('SDIROP', 'Subdirección de Operaciones'), ('UPC', 'Unidad de Pacientes Crítico Adulto (UPC)'), ('UDAC', 'Unidad de Abastecimiento Clínico'), ('UNANC', 'Unidad de Abastecimiento No Clínico'), ('UNDAP', 'Unidad de Acreditación de Prestadores'), ('UNDAD', 'Unidad de Admisión'), ('UACPCO', 'Unidad de Análisis Clínico, Planificación y Control Operacional'), ('UDAYB', 'Unidad de Análisis y Bodegas'), ('UDADP', 'Unidad de Apoyo de Pabellón'), ('UNDA', 'Unidad de Archivo'), ('UNDARQ', 'Unidad de Arquitectura'), ('UNAJ', 'Unidad de Asesoría Jurídica'), ('UNACESS', 'Unidad de Atención y Control de Salud Sexual (UNACESS)'), ('UNAUDINT', 'Unidad de Auditoría Interna'), ('UDAS', 'Unidad de Autorización Sanitaria'), ('UDBS', 'Unidad de Banco de Sangre'), ('UNBGS', 'Unidad de Bienestar y Gestión Social'), ('UNCMA', 'Unidad de Cirugía Mayor Ambulatoria'), ('UDCL', 'Unidad de Clima Laboral'), ('UDCRP', 'Unidad de Comunicaciones y Relaciones Públicas'), ('UDC', 'Unidad de Contabilidad'), ('UDCP', 'Unidad de Control de Procesos'), ('UDCPAD', 'Unidad de Cuidados Paliativos y Alivio del Dolor'), ('UNDDC', 'Unidad de Desarrollo de Competencias'), ('UNEH', 'Unidad de Emergencia Hospitalaria'), ('UNDEND', 'Unidad de Endoscopía'), ('UEIC', 'Unidad de Equipos Industriales y Calderas'), ('UEQMED', 'Unidad de Equipos Médicos'), ('UNDEST', 'Unidad de Estadísticas'), ('UNDESTER', 'Unidad de Esterilización'), ('UDF', 'Unidad de Farmacia'), ('UNDGC', 'Unidad de Gestión Comercial'), ('UDGCM', 'Unidad de Gestión de Camas y Movilización'), ('UDGGES', 'Unidad de Gestión de Garantías Explícitas de Salud (GES)'), ('UGCM', 'Unidad de Gestión del Cuidado de Matronería'), ('UDGP', 'Unidad de Gestión del Personal'), ('UNGRA', 'Unidad de Gestión del Riesgo Asistencial'), ('UDGU', 'Unidad de Gestión del Usuario'), ('UGD', 'Unidad de Gestión Documental (UGD)'), ('UHEF', 'Unidad de Hemodinamia y Electrofisiología'), ('UHD', 'Unidad de Hospitalización Domiciliaria'), ('UDIMG', 'Unidad de Imagenología'), ('UIAAS', 'Unidad de Infecciones Asociadas a la Atención de Salud (IAAS)'), ('ULCNI', 'Unidad de Laboratorio de Cardiología No Invasiva'), ('UNA', 'Unidad de Nutrición y Alimentación'), ('UOH', 'Unidad de Oncología y Hematología'), ('UPCC', 'Unidad de Pacientes Crítico Coronarios (UPCC)'), ('UPCN', 'Unidad de Pacientes Crítico Neonatal (UPCN)'), ('UPR', 'Unidad de Prevención de Riesgos'), ('UPP', 'Unidad de Priorización de Pacientes'), ('UNDPROY', 'Unidad de Proyectos'), ('UNDQUIM', 'Unidad de Quimioterapia'), ('UDREC', 'Unidad de Recaudación'), ('UDRYS', 'Unidad de Reclutamiento y Selección'), ('UDRCGRD', 'Unidad de Registro Clínico GRD'), ('UDRAD', 'Unidad de Relación Asistencial Docente'), ('UDRL', 'Unidad de Relaciones Laborales'), ('UDREM', 'Unidad de Remuneraciones'), ('UNSOCU', 'Unidad de Salud Ocupacional'), ('UDSGL', 'Unidad de Servicios Generales y Lavandería'), ('UTICS', 'Unidad de Tecnologías de la Información y Comunicación (TICS)'), ('UDTES', 'Unidad de Tesorería'), ('UTIP', 'Unidad de Tratamiento Intermedio Pediátrico (UTIP)'), ('UDVEP', 'Unidad de Vigilancia Epidemiológica'), ('UDCDINV', 'Unidad de Control de Inventario'), ('ULABCLI', 'Unidad Laboratorio Clínico'), ('ULDCI', 'Unidad Laboratorio de Citopatología'), ('UNPREQ', 'Unidad Prequirúrgica')], null=True),
        ),
    ]
