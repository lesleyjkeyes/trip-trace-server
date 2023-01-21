from rest_framework.decorators import api_view
from rest_framework.response import Response
from triptraceapi.models import User


@api_view(['POST'])
def check_user(request):
    uid = request.data['uid']

    user = User.objects.filter(uid=uid).first()

    if user is not None:
        data = {
          'id': user.id,
          'uid': user.uid,
          'about': user.about,
          'first_name': user.first_name,
          'last_name': user.last_name,
          'image_url': user.image_url,
          'email': user.email
        }
        return Response(data)
    else:
        data = { 'valid': False }
        return Response(data)


@api_view(['POST'])
def register_user(request):

    user = User.objects.create(
        about=request.data['about'],
        uid=request.data['uid'],
        first_name=request.data['first_name'],
        last_name=request.data['last_name'],
        image_url=request.data['image_url'],
        email=request.data['email']
    )

    # Return the user info to the client
    data = {
      'id': user.id,
      'uid': user.uid,
      'about': user.about,
      'first_name': user.first_name,
      'last_name': user.last_name,
      'image_url': user.image_url,
      'email': user.email
    }
    return Response(data)
