from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import LoginRole, Product
from product.serialiers import LoginSerializer


class Loginview(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = []
    def post(self,request):
        """
            # API - Product Create and Update

            # URL - /psychiatric/assessment/values/

            # Sample request for create

                {
                    "username":"company",
                    "password":"company@123"
                }

            # Sample Response:

                    {
                        "status": "success",
                        "message": "Login Successful",
                        "token": "5777a73fe30487f2130a4ca375b4ec506bbc6d89",
                        "role_type": "Admin",
                        "access_type": "Edit"
                    }

            # Sample Request for update

                {
                    "username":"user",
                    "password":"User@123"
                }


            # Sample response

                {
                    "status": "success",
                    "message": "Login Successful",
                    "token": "f0c568ac41b2840739aec19bed2e4a3e6ea501fa",
                    "role_type": "User",
                    "access_type": "View"
                }
        """

        try:
            data = request.data
            serializer = LoginSerializer(data=data)
            is_valid = serializer.is_valid(raise_exception=True)
            if is_valid:
                check_user = User.objects.get(username=request.data["username"],is_active=True)

                user = authenticate(username=check_user.username, password=request.data["password"])

                if user is not None:
                    login(request,user)
                    token, created = Token.objects.get_or_create(user=user)
                    role = LoginRole.objects.get(user_id=request.user.id)
                    return Response({"status": "success", "message": "Login Successful",'token':token.key,'role_type':role.role_type,'access_type':role.access_type})
                else:
                    return Response({"status": "failure", "message": "Invalid Username or Password"},status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist as ce:
            print('Exception {}'.format(ce.args))
            return Response({'status': 'failure', 'message': 'Invalid Username or Passwords'}, status=status.HTTP_400_BAD_REQUEST)
        except LoginRole.DoesNotExist as ce:
            print('Exception {}'.format(ce.args))
            return Response({'status': 'failure', 'message': 'Role Comment Not Available'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print('Exception {}'.format(e.args))
            return Response({"status": "fail", "message": "Something went wrong. Please try again later"},
                            status=status.HTTP_400_BAD_REQUEST)

class ProductView(generics.GenericAPIView):
    def post(self,request):
        """
            # API - Product Create and Update

            # URL - /psychiatric/assessment/values/

            # Sample request for create

                {
                    "name":"shirt",
                    "stock":20
                }

            # Sample Response:

                    {
                        "status": "success",
                        "message": "Product Details Created Successfully"
                    }

            # Sample Request for update

                {
                    "id":1,
                    "name":"tshirt",
                    "stock":20,
                    "is_active":True
                }

            # Sample response

                {
                    "status": "success",
                    "message": "Product Details Updated Successfully"
                }
        """

        try:
            data = request.data
            role = LoginRole.objects.get(user_id=request.user.id)
            if role.access_type != 'Edit':
                return Response({'status': 'fail', 'message': 'You Are Not Allow to add or modify products'},
                                status=status.HTTP_400_BAD_REQUEST)
            # Create or Update or Delete Products
            id = data.get('id')
            if id:
                product = Product.objects.get(id=id,is_active=True)
                product.name = data.get('name')
                product.stock = data.get('stock')
                if data.get('is_active'):
                    product.is_active = False
                product.modified_by = request.user.username
                product.save()
                return Response({'status': 'success', 'message': 'Product Details Updated Successfully'})
            else:
                create_product = Product.objects.create(name=data.get('name'),stock=data.get('stock'),created_by=request.user.username)
                return Response({'status': 'success', 'message': 'Product Details Created Successfully'})

        except LoginRole.DoesNotExist as ce:
            print('Exception {}'.format(ce.args))
            return Response({'status': 'failure', 'message': 'Role Comment Not Available'},
                            status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print('Exception {}'.format(e.args))
            return Response({"status": "fail", "message": "Something went wrong. Please try again later"},
                            status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        """
        # API - Get Product Details

        # URL - product/

        # Sample response

            {
                "status": "success",
                "message": "Product Details",
                "data": [
                    {
                        "id": 1,
                        "name": "tshirt",
                        "stock": 20
                    }
                ]
            }

        """

        try:
            product = Product.objects.filter(is_active=True).values('id','name','stock')
            return Response({'status': 'success', 'message': 'Product Details','data':product})
        except Exception as e:
            print('Exception {}'.format(e.args))
            return Response({"status": "fail", "message": "Something went wrong. Please try again later"},
                            status=status.HTTP_400_BAD_REQUEST)
