# Limit-Offset-Pagination-in-Django-REST-Framework
Limit Offset Pagination is one of the pagination styles available in Django REST Framework that allows the client to specify the maximum number of items to be returned in a response, as well as the offset to start from. Here's how you can implement it in Django REST Framework:

1. Add 'rest_framework.pagination.LimitOffsetPagination' to your DEFAULT_PAGINATION_CLASS in settings.py:

 REST_FRAMEWORK = {
    
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10
    
}

2. In your view, set the pagination_class attribute to LimitOffsetPagination.
3. In your request, include the limit and offset query parameters:

Note that the PAGE_SIZE setting in settings.py determines the default page size if the client doesn't specify a limit.
