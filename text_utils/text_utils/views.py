from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # params = {'name':'harry', 'place':'Kolkata'}
    return render(request, 'index.html')

def about(request):
    # return render(request, 'about.html')
    return HttpResponse("This is about page")

def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    analyzed = ""
    params = {'purpose':'', 'analyzed_text':analyzed}
    flag = 1
    if removepunc == 'on':
        flag = 0
        all_puncs = '''.?,!":;'-/...<>_%^&*#@()[]{}'''
        for char in djtext:
            if char not in all_puncs:
                analyzed += char
        params = {'purpose':'Removed Puctuations', 'analyzed_text':analyzed}
        print(djtext)
        print(removepunc)
        # return render(request, 'analyze.html', params)
    if fullcaps == 'on':
        flag = 0
        if analyzed == '':
            analyzed = djtext
        analyzed = analyzed.upper()
        params['analyzed_text'] = analyzed
        if params['purpose']:
            params['purpose'] += ',All Caps'
        else:
            params['purpose'] += 'All Caps'
    if newlineremove == 'on':
        flag = 0
        if analyzed == '':
            analyzed = djtext
        analyzed = analyzed.replace('\n','')
        analyzed = analyzed.replace('\r','')
        params['analyzed_text'] = analyzed
        if params['purpose']:
            params['purpose'] += ',Remove New Line'
        else:
            params['purpose'] = 'Remove New Line'
    if flag == 1:
        return HttpResponse('<h1>Error</h1>')
    else:
        return render(request, 'analyze.html', params)