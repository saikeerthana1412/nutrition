from django.shortcuts import render
from django.http import HttpResponse
#from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


from django.template import loader
import pandas as pd
from scipy.optimize import linprog
from sqlalchemy import create_engine
import pymysql
from tabulate import tabulate
from itertools import zip_longest
import mysql.connector

def welcome(request):
    template=loader.get_template('frst.html')
    return HttpResponse(template.render()) 
#database connection
engine = create_engine('mysql+pymysql://localhost')

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="nutrient_sources"
)

#action

def say_hello(request):
    #return HttpResponse('COST EFFICIENT BALANCED DIET')
    # mydata = Member.objects.all()
    template = loader.get_template('main.html')
   
    return HttpResponse(template.render())

def optimize():
    
    sources = pd.read_sql_query('SELECT * FROM `nutrients_info`', con=db)
    
    names = sources["SOURCES"].to_numpy()
    fats = sources["Fats"].to_numpy()
    carb = sources["Carbohydrates"].to_numpy()
    prot = sources["Protiens"].to_numpy()
    fiber = sources["Fiber"].to_numpy()
    neg = -1
    cal = sources["Calories"].to_numpy()
    
    obj = sources["Price"].to_numpy()
    lhs_eq = [cal]
    rhs_eq = [2500]
    lhs_ineq = [fats, fats*neg, carb, carb*neg, prot, prot*neg, fiber, fiber*neg]
    rhs_ineq = [109, -62, 406, -281, 219, -63, 42, -28]
    
    bnd = (0,float("inf"))
    sum=0
    opt = linprog( c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, A_eq=lhs_eq, b_eq=rhs_eq, bounds=bnd)
    round_to_tenths = [round(num, 1) for num in opt.x] 
    
    opt_list=zip(names, round_to_tenths,obj,round_to_tenths*obj)
    filtered_data = [row for row in iter(opt_list) if row[1] > 0]
    table = {
        'headers': ['Name', 'Optimize_quantity', 'Prices', 'Total'],
        'rows': filtered_data
    }
        
    return table

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

        p=[s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21,s22,s23,s24,s25,s26,s27,s28,s29,
           s30,s31,s32,s33,s34,s35,s36,s37,s38,s39]
        
        list2=['brown_rice','oats','quinoa','whole_wheat_bread','whole_wheat_pasta','chickpeas',
                     'black_beans','kidney_beans','lentils','almonds','walnuts','chia_seeds','flax_seeds','peanuts','paneer','milk','cheese',
                      'yogurt','chicken','salmon','eggs','olive_oil','coconut_oil','broccoli','bell_pepper','tomato','carrot','sweet_potatoes',
                      'spinach','banana','apple','orange','grapes','avacado','lemons','kiwi','papaya','peas','sprouts']
        res = {list2[i]: p[i] for i in range(len(list2))}

        mycursor = db.cursor()

	#or put new inputed array here    
        
        
        for x in range(39):
            sql = "UPDATE nutrients_info SET Price = %s WHERE ID = %s"
            val = (p[x], x+1)
            
            mycursor.execute(sql, val)
            db.commit()
        
        optimized_table = optimize()
        optimized_prices = [row[2] for row in optimized_table['rows']]
        sum_of_prices = sum(optimized_prices)

        
        # n=len(list2)
        # for i in range(0,n):
        #     if list1[i] is None:
        #         res={list2[i]: '0'}
        #     else:
        #         res={list2[i]:list1[i]}
        #responce=JsonResponse(res, safe=False)
        #upadate_prices()
        template=loader.get_template('base.html')
        context={
              'display' : res,
              'my_text': optimized_table,
              'add': sum_of_prices,
             
        }
        
        
        
        #html = "<html><body>PRICES<br> %s.</body></html>" %res
        return HttpResponse(template.render(context, request))


    
def facts(request):
    # html= "<html><style>h1{background-color: rgb(138, 166, 95); color: white;  }</style><body><h1><br>Did You Know???<br></h1>  <p></p>   </body></html>"
    # return HttpResponse(html)
    template= loader.get_template('home.html')
    return HttpResponse(template.render())       

