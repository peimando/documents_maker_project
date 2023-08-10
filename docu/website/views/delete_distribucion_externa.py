from django.contrib import messages
from django.shortcuts import redirect
from ordinario.models import DistribucionExterna


def delete_distribucion_externa(request, id):

    print(id)

    try:
        distribucion_externa = DistribucionExterna.objects.get(id=id)
    
    except DistribucionExterna.DoesNotExist:
    
        messages.error(
            request, 
            'El objeto no existe.'
        )
    
        return redirect(
            'website:edit_ordinario_inline', 
            slug=distribucion_externa.ordinario.slug
        )

    distribucion_externa.delete()
    
    messages.info(
        request, 
        'Distribucion Externa eliminada correctamente'
    )

    return redirect(
        'website:edit_ordinario_inline', 
        slug=distribucion_externa.ordinario.slug
    )