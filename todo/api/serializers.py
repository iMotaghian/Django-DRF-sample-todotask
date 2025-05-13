from rest_framework import serializers
from ..models import ToDoTask,User

class TodoSerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField()
    
    class Meta:
        model = ToDoTask
        fields = ['absolute_url','id','user','task','status','created_date','updated_date']
        read_only_fields = ['user']
        
    def get_absolute_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)
    
    def to_representation(self,instance):
        rep = super().to_representation(instance)
        request = self.context.get('request')
        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('absolute_url',None)
        return rep
    
    def create(self, validated_data):
        validated_data['user'] = self.context.get('request').user
        return super().create(validated_data)