from django.shortcuts import render,get_object_or_404,redirect
from .models import Comments,Company
from django.http import JsonResponse
from django.db.models import Q
from django.urls import reverse

# Create your views here.


def index(request):
  comanies =Company.objects.filter(is_approved=True).order_by('created_date')
  companies_count=comanies.count()
  current =comanies[:6]

  current_count=current.count()

  context={
    'companies':comanies,
    'companies_count':companies_count,
    'current_company':current,
    'current_count':current_count
  }

  return render(request,'index.html',context)



def post_detail(request,company_id):
  company = get_object_or_404(Company,id=company_id)

  comments =Comments.objects.filter(is_approved=True,company=company)
  comments_count=comments.count()
  context={
    'company':company,
    'comments':comments,
    'comments_count':comments_count
  }
  return render(request,'detail.html',context)

def company_save(request):
  if request.method =="POST":
    name = request.POST.get('name')
    inn = request.POST.get('inn')
    address = request.POST.get('address')
    phone = request.POST.get('phone')
    description =request.POST.get('msg')
    avg_rating = 0
    company =Company(name=name,inn=inn,address=address,phone=phone,description=description,avg_rating=avg_rating,is_approved=False)
    company.save()
    return JsonResponse({'status':'Success','msg':'Message successfully saved!'})
  else:
    return JsonResponse({'status':'Failed','msg':'Something went wrong!'})

def comment_save(request):
   if request.method =="POST":
    
    owner_name = request.POST.get('name')
    email = request.POST.get('email')
    description = request.POST.get('msg')
    rating = request.POST.get('rating')
    company_id = int(request.POST.get('company_id'))

    
    try:
      company =Company.objects.get(id=company_id)
      comment_count =Comments.objects.filter(company=company).count()
      
      if comment_count > 0:
        company.avg_rating = (float(company.avg_rating) + float(rating))/(comment_count + 1)
      else:
        company.avg_rating = rating

      company.save()

      comment =Comments(
        owner_name =owner_name, 
        email=email,
        description=description,
        rating=rating,
        company=company,is_approved=True)
      comment.save()
      return JsonResponse({'status':'Success','msg':'Comment successfully saved!'})
    except Exception as e:
      return  JsonResponse({'status':'Failed','msg':str(e)})
    else:
      print('seealom1')
      return JsonResponse({'status':'Failed','msg':'Company not found!'})


def search(request):
  search_text= request.GET.get('search')

  comanies =Company.objects.filter(is_approved=True).filter(Q(name__icontains=search_text) | Q(description__icontains=search_text)|Q(phone__icontains=search_text)|Q(inn__icontains=search_text)).order_by('created_date')

  companies_count=comanies.count()
  current =comanies[:6]

  current_count=current.count()

  context={
    'companies':comanies,
    'companies_count':companies_count,
    'current_company':current,
    'current_count':current_count
  }

  return render(request,'result.html',context)

def sort(request):
  sort =request.GET.get('sort',None)
  if sort:
    if sort =='asc':
      comanies =Company.objects.filter(is_approved=True).order_by('created_date')
    elif sort =='desc':
      comanies =Company.objects.filter(is_approved=True).order_by('-created_date')
  else:
    comanies =Company.objects.filter(is_approved=True).order_by('created_date')
  companies_count=comanies.count()
  current =comanies[:6]

  current_count=current.count()
  context={
    'companies':comanies,
    'companies_count':companies_count,
    'current_company':current,
    'current_count':current_count
  }
  return render(request,'result.html',context)

