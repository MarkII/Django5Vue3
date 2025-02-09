from rest_framework.serializers import ModelSerializer
from users.models import  Users 


class UserRegisterSerializer(ModelSerializer):
    
    class Meta:
        model = Users
        fields = ['id', 'email', 'username', 'password']
        
    def create(self, validated_data):
        password =  validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
       
        if password is not None:
           instance.set_password(password)
        instance.save()
        return instance
        

class UserInfoSerializer(ModelSerializer):
    
    class Meta:
        model = Users
        fields = ['id', 'email', 'username', 'first_name', 'last_name']
        
        
class UserUpadateSerializer(ModelSerializer):
    
    class Meta:
        model = Users
        fields = ['first_name', 'last_name']