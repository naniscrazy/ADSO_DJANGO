from django.http import JsonResponse
from django.views import View
from .models import AuthorModel, VideoGameModel
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

"""CRUD AUTHOR"""

@method_decorator(csrf_exempt, name='dispatch')  # Desactivar CSRF solo para pruebas, dispach manejar solicitudes http
class AuthorCreateView(View):
    
    def post(self, request): #Self referencia a la clase, request es la solicitud
        try:
            data = json.loads(request.body)  # Cargar el cuerpo de la solicitud como JSON
            author = AuthorModel.objects.create(**data) # Crear un nuevo autor
            
            # Obtener todos los autores
            authors = AuthorModel.objects.all().values()  # Obtener todos los autores como diccionarios covertiri los los objetos en dicionarios
            
            return JsonResponse({
                'message': 'Author created successfully',
                'new_author_id': author.id,
                'authors': list(authors)  # Convertir a lista para serializar
            }, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        
        
@method_decorator(csrf_exempt, name='dispatch')
class AuthorDeleteView(View):
    
    def delete(self, request, pk):
        try:
            author = AuthorModel.objects.filter(id=pk)
            author.delete()
            return JsonResponse({'message': 'Author deleted successfully'}, status=204)
        except AuthorModel.DoesNotExist:
            return JsonResponse({'error': 'Author not found'}, status=404)
        
@method_decorator(csrf_exempt, name='dispatch')
class AuthorListView(View):
    
    def get(self, request):
        try:
            authors = AuthorModel.objects.all().values()  # Obtener todos los autores como diccionarios
            return JsonResponse(list(authors), safe=False, status=200)  # Retornar lista de autores
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        
        
@method_decorator(csrf_exempt, name='dispatch')
class AuthorUpdateView(View):
    
    def patch(self, request, pk):
        author = AuthorModel.objects.filter(id=pk).first()  # Obtener el autor, o None si no existe
        if not author:
            return JsonResponse({'error': 'Author not found'}, status=404)
        
        try:
            data = json.loads(request.body)  # Cargar el cuerpo de la solicitud como JSON
            for field, value in data.items():  # Iterar sobre los campos a actualizar
                setattr(author, field, value)  # Establecer el nuevo valor para cada campo
            author.save()  # Guardar los cambios
            return JsonResponse({'message': 'Author updated successfully'}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
       
""""CRUD VIDEO JUEGOS"""
@method_decorator(csrf_exempt, name='dispatch')  # Desactivar CSRF solo para pruebas 
class VideoGameListView(View):
    def get(self, request):
        try:
            # Obtener todos los videojuegos
            video_games = VideoGameModel.objects.all().values()
            return JsonResponse(list(video_games), safe=False, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        
@method_decorator(csrf_exempt, name='dispatch')  # Desactivar CSRF solo para pruebas
class VideoGameCreateView(View): 
    
    def post(self, request):
        try:
            data = json.loads(request.body)  # Cargar el cuerpo de la solicitud como JSON
            
            # Crear el videojuego directamente
            video_game = VideoGameModel.objects.create(
                name=data["name"],
                Release_Date=data["Release_Date"],
                author_id=data["author"]  # Se espera que el ID del autor esté en los datos
            )
            
            return JsonResponse({
                'message': 'Video game created successfully',
                'new_video_game_id': video_game.id
            }, status=201)
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        
@method_decorator(csrf_exempt, name='dispatch')
class VideoGameDeleteView(View):
    def delete(self, request, pk):
        try:
            VideoGameModel.objects.filter(id=pk).delete()
            return JsonResponse({'message': 'Video game deleted'}, status=200)
        except VideoGameModel.DoesNotExist:
            return JsonResponse({'error': 'Not found'}, status=404)

@method_decorator(csrf_exempt, name='dispatch')
class VideoGameUpdateView(View):
    def put(self, request, pk):
        try:
            video_game = VideoGameModel.objects.get(id=pk)
            data = json.loads(request.body)
            
            # Actualizar los campos dinámicamente
            for field, value in data.items():
                if field == 'author':
                    # Obtener la instancia de AuthorModel a partir del id
                    value = VideoGameModel.objects.get(id=value)
                setattr(video_game, field, value)
            video_game.save()
            
            return JsonResponse({'message': 'Video game updated'}, status=200)
        except VideoGameModel.DoesNotExist:
            return JsonResponse({'error': 'Not found'}, status=404)
        except AuthorModel.DoesNotExist:
            return JsonResponse({'error': 'Author not found'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

