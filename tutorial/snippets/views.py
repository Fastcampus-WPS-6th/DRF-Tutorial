from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from snippets.serializers import SnippetSerializer
from .models import Snippet
"""
snippets/urls.py에 urlpatterns작성
config/urls.py에 snippets.urls를 include

아래의 snippet_list 뷰가
    /snippets/ 에 연결되도록 url을 구성
"""


# CSRF인증을 사용하지 않음
@csrf_exempt
def snippet_list(request):
    if request.method == 'GET':
        # snippets는 모든 Snippet의 쿼리셋
        snippets = Snippet.objects.all()
        # 쿼리셋을 serialize할 때는 many=True옵션 추가
        serializer = SnippetSerializer(snippets, many=True)
        # JSON방식으로 response.
        # 기본적으로 JsonResponse는 dict형 객체를 받아 처리하나,
        # safe옵션이 False이면 주어진 데이터가 dict가 아니어도 됨 (지금의 경우 리스트 객체가 옴)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        # request로 전달된 데이터들을 JSONParser를 사용해 파이썬 데이터 형식으로 파싱
        data = JSONParser().parse(request)
        # 처리된 데이터를 사용해 SnippetSerializer인스턴스를 생성
        serializer = SnippetSerializer(data=data)
        # 인스턴스에 주어진 데이터가 유효할 경우
        if serializer.is_valid():
            # 인스턴스의 save()메서드를 호출해 Snippet객체를 생성
            serializer.save()
            # HTTP상태코드(201 created)로 Snippet생성에 사용된 serializer의 내용을 보내줌
            return JsonResponse(serializer.data, status=201)
        # 유효하지 않으면 인스턴스의 에러들을 HTTP 400 Bad request상태코드와 함께 보내줌
        return JsonResponse(serializer.errors, status=400)
