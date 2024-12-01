from rest_framework.viewsets import ModelViewSet
from .models import Course, Lesson, Comment, Rating
from .serializers import CourseSerializer, LessonSerializer, CommentSerializer, RatingSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter
from django.core.mail import send_mail
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status

class CustomPagination(PageNumberPagination):
    '''Custom pagination with page size of 1'''
    page_size = 2

class CourseViewSet(ModelViewSet):
    '''Handles CRUD operations for the Course model.'''
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'description' , 'created_at' , 'content', 'author']
    ordering_fields = ['created_at', 'title']
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        '''Send an email when a new course is created.'''
        instance = serializer.save()
        send_mail(
            subject="New Course Created",
            message=f"Course '{instance.title}' has been added.",
            from_email='saidovsarvarbek@hotmail.com',
            recipient_list=["saidovsarvarbek02@gmail.com"],
        )

class LessonViewSet(ModelViewSet):
    '''Handles CRUD operations for the Lesson model.'''
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'course__title']
    ordering_fields = ['created_at', 'title']

class CommentViewSet(ModelViewSet):
    '''Handles CRUD operations for the Comment model.'''
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'course__title']
    ordering_fields = ['created_at', 'title']


class RatingViewSet(ModelViewSet):
    '''Handles rating (Liked/Didn't like) for lessons.'''
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


