from .models import Company


def meta_tags(request,company_id):
  company = Company.objects.get(id=company_id)
  title =company.name
  description =company.description
  return {'title':title,'description':description}