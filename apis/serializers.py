from rest_framework import serializers

from books.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["name"]


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)  # Nested details for GET
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(), write_only=True  # For POST/PUT
    )

    class Meta:
        model = Book
        # fields = ['id', 'title', 'available', 'author', 'author_id']
        fields = "__all__"

    def create(self, validated_data):
        # Extract the writable author_id field
        author = validated_data.pop('author_id')
        # Do NOT include 'author' (the nested read-only field) in validated_data
        return Book.objects.create(author=author, **validated_data)
    
    def update(self, instance, validated_data):
        author = validated_data.pop('author_id', None)
        if author is not None:
            instance.author = author
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
