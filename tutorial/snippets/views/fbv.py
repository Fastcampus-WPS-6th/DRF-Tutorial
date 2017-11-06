from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import Snippet
from ..serializers import SnippetSerializer

__all__ = (
    'snippet_list',
    'snippet_detail',
)

"""
snippets/urls.py에 urlpatterns작성
config/urls.py에 snippets.urls를 include

아래의 snippet_list 뷰가
    /snippets/ 에 연결되도록 url을 구성

아래의 snippet_detail뷰가
    /snippets/<pk>/ 에 연결되도록 url 구성
    ex) /snippets/3/
"""


# 이 뷰는 api_view형태로 동작함 (request에 HttpRequest가 아닌 Request가 주어짐)
# GET, POST요청에 대해서만 동작
@api_view(['GET', 'POST'])
def snippet_list(request, format=None):
    if request.method == 'GET':
        # snippets는 모든 Snippet의 쿼리셋
        snippets = Snippet.objects.all()
        # 쿼리셋을 serialize할 때는 many=True옵션 추가
        serializer = SnippetSerializer(snippets, many=True)
        # 데이터를 적절히 렌더링해주는 Response객체를 리턴
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        # 인스턴스에 주어진 데이터가 유효할 경우
        if serializer.is_valid():
            # 인스턴스의 save()메서드를 호출해 Snippet객체를 생성
            serializer.save()
            # HTTP상태코드(201 created)로 Snippet생성에 사용된 serializer의 내용을 보내줌
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 유효하지 않으면 인스턴스의 에러들을 HTTP 400 Bad request상태코드와 함께 보내줌
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk, format=None):
    # pk에 해당하는 Snippet이 존재하는지 확인 후 snippet변수에 할당
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # GET요청시에는 snippet을 serialize한 결과를 보여줌
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        # DELETE요청시에는 해당 Snippet인스턴스를 삭제
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
