from django.shortcuts import render
from rest_framework import viewsets, status, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import ChatSerializer
from .models import Chat
from .commons import prompt_settings
import openai
from .permissions import IsOwnerReadOnly
from .throttlings import ChatAPIThrottle
from drf_spectacular.utils import extend_schema, extend_schema_view, inline_serializer, OpenApiResponse


@extend_schema_view(
    update = extend_schema(
        exclude=True
    ),
    partial_update = extend_schema(
        exclude=True
    ),
    list = extend_schema(
        summary="추천 전체 리스트 api",
        description="내가 추천받은 내역 전체 리스트"
    ),
    create = extend_schema(
        summary="추천 내역 저장 api",
        description="추천받은 데이트코스를 저장"
    ),
    destroy = extend_schema(
        summary="추천 내역 삭제",
        description="추천받았던 내역을 삭제"
    ),
    retrieve = extend_schema(
        summary="추천 상세내역 api",
        description="내가 추천받았던 코스의 상세내역"
    ),
)
class ChatViewSet(viewsets.ModelViewSet):
    serializer_class = ChatSerializer
    queryset = Chat.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerReadOnly]   

    def list(self, request, *args, **kwargs):
        query = Chat.objects.filter(author=request.user.pk).order_by('-created_at')
        queryset = self.filter_queryset(query)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    
    def create(self, request, *args, **kwargs):
        data = request.data
        data['author'] = request.user.pk
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        return Response({
            "detail": "메소드(Method) \"PUT\"은 허용되지 않습니다."
        }, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def partial_update(self, request, *args, **kwargs):
        return Response({
            "detail": "메소드(Method) \"PATCH\"는 허용되지 않습니다."
        }, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    
    
    # def get_queryset(self):
    #     return Chat.objects.filter(author=self.request.user.pk).order_by('-created_at')


class ChatBotApiView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [ChatAPIThrottle]

    @extend_schema(
            request=inline_serializer(
                name='ChatBotApiSerializer',
                fields={
                    'datePlace': serializers.CharField(max_length=50, required=True),
                    'dateSeason': serializers.CharField(max_length=10, required=True),
                    'dateStart': serializers.CharField(max_length=100, required=True),
                    'dateEnd': serializers.CharField(max_length=100, required=True),
                    'dateTransport': serializers.CharField(max_length=50, required=True),
                }
            ),
            summary="OpenAI api 호출",
            description="OpenAI api를 호출하여 데이트 코스 추천 요청",
            responses={
                500: OpenApiResponse({
                    "detail": "Internal Server Error"
                }),
                504: OpenApiResponse({
                    'detail': "Timeout" 
                })
            }
    )
    def post(self, request):
        datePlace = request.data.get('datePlace')
        dateSeason = request.data.get('dateSeason')
        dateStart = request.data.get('dateStart')
        dateEnd = request.data.get('dateEnd')
        dateTransport = request.data.get('dateTransport')
        question = self.make_question(datePlace, dateSeason, dateStart, dateEnd, dateTransport)
        if question:
            messages = prompt_settings[:]
            messages.append({
                "role": "user",
                "content": question
            })
            response = openai.OpenAI().chat.completions.create(
                model="gpt-3.5-turbo-1106",
                messages=messages,
                temperature=0.5,
            )
            
            answer = response.choices[0].message.content
            return Response({
                "result": "success",
                "detail": {
                    "question": question,
                    "answer": answer
                },
            }, status=status.HTTP_200_OK)
        else:
            return Response({"result": "fail", "detail": "파라미터를 확인해주세요"}, status=status.HTTP_400_BAD_REQUEST)
    
    def make_question(*args):
        season = {'spring': '봄', 'summer': '여름', 'fall': '가을', 'winter': '겨울'}
        transport = {'walk':'걸어서', 'public': '대중교통을 이용해서', 'myCar': '내 차를 타고'}

        return f'{args[1]}에서 데이트를 할거야. 지금 계절은 {season[args[2]]}이고, 데이트는 {args[3]}에 만나서 {args[4]}까지 할거야. {transport[args[5]]} 이동할 건데 {season[args[2]]}에 맞게 데이트 코스를 계획해줘'


    
request_gpt = ChatBotApiView.as_view()