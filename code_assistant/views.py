import markdown
from django.shortcuts import render
from django.views import View
from .langchain import ask_query
from django.http import JsonResponse
from .forms import QueryForm


class Home(View):
    def get(self, request):
        return render(request, 'code_assistant/home.html')
    
    def post(self, request):
        form = QueryForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            response = ask_query(query)
            markdown_response = markdown.markdown(response,
                                                  extensions=['fenced_code', 'codehilite'])
        #     request.session['ai_content'] = markdown_response
        # ai_content = request.session.get('ai_content', '')
        return JsonResponse({'ai_content': markdown_response})