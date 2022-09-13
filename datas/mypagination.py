from rest_framework.pagination import PageNumberPagination

class Mypage(PageNumberPagination):
    page_size = 5
    page_query_param = "Page number"