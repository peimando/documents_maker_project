let document_link = document.getElementById('download_document').addEventListener('click', download_file);

function download_file() {

    let document_url = "{% url 'website:download_document' object.slug %}"

    let antecedente = document.getElementById('antecedente').textContent;
    let materia = document.getElementById('materia').textContent;
    let de = document.getElementById('de').textContent;
    let cargo_de = document.getElementById('cargo_de').textContent;
    let a = document.getElementById('a').textContent;
    let cargo_a = document.getElementById('cargo_a').textContent;
    let cuerpo = document.getElementById('cuerpo').textContent;
    let adjunto = document.getElementById('adjunto').textContent;
    let tipo_distribucion = document.getElementById('tipo_distribucion').textContent;
    let distribucion_interna = document.getElementById('distribucion_interna').textContent;

    data = {
        'antecente': antecedente,
        'materia': materia,
        'de': de,
        'cargo_de': cargo_de,
        'a': a,
        'cargo_a': cargo_a,
        'cuerpo': cuerpo,
        'adjunto': adjunto,
        'tipo_distribucion': tipo_distribucion,
        'distribucion_interna': distribucion_interna,
        'distribucion_externa': distribucion_externa,
        'servicio': servicio,
        'telefono': telefono,
    }

    fetch(document_url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: data
    })
    .then(response => response.json())
    .then(response => console.log(data));

};
