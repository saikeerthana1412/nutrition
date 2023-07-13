ffrom django.shortcuts import render
from django.http import HttpResponse
#from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import forms

from django.template import loader

#action

def say_hello(request):
    #return HttpResponse('COST EFFICIENT BALANCED DIET')
    # mydata = Member.objects.all()
    template = loader.get_template('hello.html')
   
    return HttpResponse(template.render())
@csrf_exempt
def submit_request(request):
    #if request.method == "POST":
        #list1=forms.SignUp()
        s1=request.POST.get('brown_rice')
        s2=request.POST.get('oats')
        s3=request.POST.get('quinoa')
        s4=request.POST.get('whole_wheat_bread')
        s5=request.POST.get('whole_wheat_pasta')
        s6=request.POST.get('chick_peas')
        s7=request.POST.get('black_beans')
        s8=request.POST.get('kidney_beans')
        s9=request.POST.get('lentils')
        s10=request.POST.get('almonds')
        s11=request.POST.get('walnuts')
        s12=request.POST.get('chia_seeds')
        s13=request.POST.get('flax_seeds')
        s14=request.POST.get('peanuts')
        s15=request.POST.get('paneer')
        s16=request.POST.get('milk')
        s17=request.POST.get('cheese')
        s18=request.POST.get('yogurt')
        s19=request.POST.get('chicken')
        s20=request.POST.get('salmon')
        s21=request.POST.get('eggs')
        s22=request.POST.get('olive_oil')
        s23=request.POST.get('coconut_oil')
        s24=request.POST.get('broccoli')
        s25=request.POST.get('bell_pepper')
        s26=request.POST.get('tomato')
        s27=request.POST.get('carrot')
        s28=request.POST.get('sweet_potatoes')
        s29=request.POST.get('spinach')
        s30=request.POST.get('banana')
        s31=request.POST.get('apple')
        s32=request.POST.get('orange')
        s33=request.POST.get('grapes')
        s34=request.POST.get('avacado')
        s35=request.POST.get('lemons')
        s36=request.POST.get('kiwi')
        s37=request.POST.get('papaya')
        s38=request.POST.get('peas')
        s39=request.POST.get('sprouts')

        list1=[s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21,s22,s23,s24,s25,s26,s27,s28,s29,
           s30,s31,s32,s33,s34,s35,s36,s37,s38,s39]
        
        list2=['brown_rice','oats','quinoa','whole_wheat_bread','whole_wheat_pasta','chickpeas',
                     'black_beans','kidney_beans','lentils','almonds','walnuts','chia_seeds','flax_seeds','peanuts','paneer','milk','cheese',
                      'yogurt','chicken','salmon','eggs','olive_oil','coconut_oil','broccoli','bell_pepper','tomato','carrot','sweet_potatoes',
                      'spinach','banana','apple','orange','grapes','avacado','lemons','kiwi','papaya','peas','sprouts']
        res = {list2[i]: list1[i] for i in range(len(list2))}
        # n=len(list2)
        # for i in range(0,n):
        #     if list1[i] is None:
        #         res={list2[i]: '0'}
        #     else:
        #         res={list2[i]:list1[i]}
        #responce=JsonResponse(res, safe=False)
        template=loader.get_template('base.html')
        context={
              'display' : res
        }
        
        
        
        #html = "<html><body>PRICES<br> %s.</body></html>" %res
        return HttpResponse(template.render(context, request))
    
def facts(request):
    # html= "<html><style>h1{background-color: rgb(138, 166, 95); color: white;  }</style><body><h1><br>Did You Know???<br></h1>  <p></p>   </body></html>"
    # return HttpResponse(html)
    template= loader.get_template('home.html')
    return HttpResponse(template.render())       

