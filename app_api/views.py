from django.shortcuts import render
from  .models import Users 
from .serializers import  UsersSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response




# home-page
def index(request):
    return render(request,"home.html")

 # api for users    
@api_view(['GET' , 'POST'])
def usersListView(request):
    data= {}
    # to fetch data from databse in json format.
    if request.method == 'GET':
        user = Users.objects.all()
        serializer = UsersSerializer(user , many =True)
        returnArr = { 'data': serializer.data}
        return Response(returnArr)
        # send the data
    elif request.method =='POST':
        serializer=UsersSerializer(data = request.data)
        
        if serializer.is_valid():
            # check if the data already exists in the database
            if Users.objects.filter(email=request.data['email']).exists():
                data = {'error':'Data already exists in the database.'}
            else:
                serializer.save()
                data = serializer.data
            returnArr = { 'data': data}
            return Response(returnArr)
        else:
            data = {'error':serializer.errors}
            returnArr = {'data': data}
            return Response(returnArr)
    
             
@api_view(['DELETE' , 'GET' , 'PUT'])
def userListView(request , pk):
    sts = 'false'
    stscode = 404
    data = {}   
    try:
        user = Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return Response({'status':sts,'status_code':stscode})
        # delete the particular data with id 
    if request.method == 'DELETE':
        user.delete() 
        sts='true'
        stscode=200
        return Response({'status':sts,'status_code':stscode})
        # to fetch the particular data with the help of id  
    elif request.method =='GET':
        serializer = UsersSerializer(user)
        stscode =200
        returnArr = {'data': serializer.data}
        return Response(returnArr)
        # updata the data any particular with id  
    elif request.method == 'PUT':
        serializer=UsersSerializer(user, data = request.data)
        # print(jsonData)
        if serializer.is_valid():
            serializer.save()
            sts = 'true'
            stscode  = 200
            data = serializer.data
            returnArr = { 'data': data}
            return Response(returnArr) 
        else:
            data = {'error':serializer.errors}
            returnArr = {'data': data}
            return Response(returnArr)  
            
       