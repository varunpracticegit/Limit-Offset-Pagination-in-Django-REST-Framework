from rest_framework.pagination import LimitOffsetPagination

class MyLimitOffsetPagination(LimitOffsetPagination):
   
   '''This will set a default records limit per page   https://127.0.0.1:8000/studentapi
   but if user search with manual limit then it show the results accordingly eg:
   https://127.0.0.1:8000/studentapi?limit=7 --> Now it will return 7 records per page
   '''
   default_limit = 5      

   '''limit_query_param is used to set custom query string by overriding the default string  
   "limit" --> https://127.0.0.1:8000/studentapi?limit=
   But, once we orride the value of "limit" to custom string then the records will get shown
   for the set limit string eg: --> https://127.0.0.1:8000/studentapi?mylimit=7. Here "mylimit"
   is the "limit_query_param". 
   '''      

   limit_query_param = 'mylimit'

   '''offset_query_param is used to set custom offset query string by overriding the default
   string ('offset'). Now you can get the records through https://127.0.0.1:8000/studentapi?mylimit=7&offset=5
   and this url will show 7 records per page with the offset of 5 means that the 6th record will
   be shown at first. But after overriding the default query string( eg --> myoffset), we will
   get the records accordingly eg --> https://127.0.0.1:8000/studentapi?mylimit=7&myoffset=5'''

   offset_query_param = 'myoffset'

   '''This means that clients can request between 1 and 6 results per page, but cannot request
     more than 100 results in a single page even if they set page_size to a larger value. '''
   
   max_limit = 6