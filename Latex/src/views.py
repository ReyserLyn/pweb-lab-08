from django.http import JsonResponse
from rest_framework.decorators import api_view
from djangoApiRest.api.models import Contacto
from djangoApiRest.api.serializers import ContactoSerializer

@api_view(['GET'])
def getContacto(request):
    contactos = Contacto.objects.all()
    serializer = ContactoSerializer(contactos, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def getContactoById(request, id):
    try:
        contacto = Contacto.objects.get(id=id)
        serializer = ContactoSerializer(contacto)
        return JsonResponse(serializer.data)
    except Contacto.DoesNotExist:
        return JsonResponse({"message": "Contacto no encontrado"}, status=404)
    
@api_view(['POST'])
def postContacto(request):
    serializer = ContactoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)

@api_view(['PUT'])
def putContacto(request, pk):
    try:
        contacto = Contacto.objects.get(id=pk)
    except Contacto.DoesNotExist:
        return JsonResponse({"message": "Contacto no encontrado"}, status=404)
    
    serializer = ContactoSerializer(instance=contacto, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)

@api_view(['DELETE'])
def deleteContacto(request, pk):
    try:
        contacto = Contacto.objects.get(id=pk)
        contacto.delete()
        return JsonResponse({"message": "Contacto eliminado"})
    except Contacto.DoesNotExist:
        return JsonResponse({"message": "Contacto no encontrado"}, status=404)
