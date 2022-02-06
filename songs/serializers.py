from rest_framework import serializers

from .models import Singer, Tracks


# class SingerSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=30)
#
#     def create(self, validated_data):
#         print(validated_data)
#         return Singer.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         pass

# class SingerSerializer(serializers.HyperlinkedModelSerializer):
#     track = serializers.HyperlinkedRelatedField(view_name='track-detail', read_only=True, many=True)
#     field1 = serializers.SerializerMethodField(method_name='compute_field1')
#
#     class Meta:
#         model = Singer
#         fields = "__all__"
#         extra_kwargs = {
#             'url': {'view_name': 'singers'},
#         }
#
#     def to_representation(self, instance):
#         ret = super().to_representation(instance)
#         ret['name'] = instance.id
#         return ret
#
#     def to_internal_value(self, data):
#         data = data['data']
#         data_ret = super().to_internal_value(data)
#
#         return data_ret
#
#     def compute_field1(self, obj):
#         return obj.id

class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = ('name',)


class TrackSerializer(serializers.ModelSerializer):
    singer = SingerSerializer(many=True)
    album = serializers.StringRelatedField()

    class Meta:
        model = Tracks
        fields = "__all__"
        # depth = 3

    def create(self, validated_data):
        singers = validated_data.pop('singer')
        # print(singers)
        # print(validated_data)
        singer_list = []
        for elm in singers:
            singer, _ = Singer.objects.get_or_create(**elm)
            singer_list.append(singer)
        track, _ = Tracks.objects.get_or_create(**validated_data)
        track.singer.set(singer_list)
        return track


class TrackDetailSerializer(serializers.ModelSerializer):
    singer = SingerSerializer(many=True)
    album = serializers.StringRelatedField()

    class Meta:
        model = Tracks
        exclude = ('id',)

    def update(self, instance, validated_data):
        if validated_data.get('singer', False):
            singers = validated_data.pop('singer')
            singer_list = []
            for elm in singers:
                singer, _ = Singer.objects.get_or_create(**elm)
                singer_list.append(singer)
            instance.singer.set(singer_list)

        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance
