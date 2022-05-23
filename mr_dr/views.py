import imp
from django.contrib import messages
from django.shortcuts import redirect, render
from .models import MrDr
from .forms import AskQuestionForm
from django.core.mail import send_mail

def mr_dr(request):
    if request.method == 'POST':
        form = AskQuestionForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            MrDr.objects.create(name=cd['name'] ,email=cd['email'], title=cd['title'], question=cd['question'])
            # send email to abdi group
            send_mail(
                'hello',
                cd['name'],
                cd['email'],
                ['mr.dr@abdi-group.com'],
                fail_silently=False,
            )
            # send email to questioner
            send_mail(
                'گروه خدمات مهندسی نفت گاز پتروشیمی عبدی',
                cd['name'],
                'mr.dr@abdi-group.com',
                [cd['email']],
                fail_silently=False,
            )
            messages.success(request, 'you have added your question to the site')
            return redirect('mr-dr:mr-dr')
    else:
        form = AskQuestionForm()
        mr_dr = MrDr.objects.all()
    return render(request, 'mr_dr/mr_dr.html', {'form':form,'mr_dr':mr_dr})








    # questions = MrDr.objects.all()
    # if request.method == "POST":
    #     form = AskQuestionForm(request.POST)
    #     if form.is_valid():
    #         questioner_name = request.POST['questioner-name']
    #         questioner_email = request.POST['questioner-email']
    #         questioner_title = request.POST['questioner-title']
    #         questioner_question = request.POST['questioner-question']
    #         questioner_email = request.POST['questioner-email']
    #         questioner_title = request.POST['question-title']
    #         questioner_question = request.POST['question']
    #         mr_dr = MrDr.objects.create(name=questioner_name, email=questioner_email, body=questioner_question, title=questioner_title)
    #         form.save()
    #         mr_dr.save()

    #         # send email to questioner
    #         send_mail(
    #             'پیام جدید',
    #             questioner_name,
    #             'mr.dr@abdi-group.com',
    #             [questioner_email],
    #             fail_silently=False,
    #         )
            
    #         # send email to abdi group
    #         send_mail(
    #             'hello',
    #             questioner_question,
    #             questioner_email,
    #             ['mr.dr@abdi-group.com'],
    #             fail_silently=False,
    #         )
    #     return render(request, 'mr_dr/mr_dr.html',{'questions':questions, 'form':form})
    # else:
    #     return render(request, 'mr_dr/mr_dr.html',{'questions':questions, 'form':form})


