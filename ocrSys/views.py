from django.shortcuts import render, render_to_response

def scanDocument(request):
    template = 'scan_document.html'
    context = {}
    return render_to_response(template, context)