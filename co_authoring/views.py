from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from co_authoring.models import file_record,user_access

from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import authenticate, login ,get_user_model
from django.http import JsonResponse
from django.core import serializers
from django.urls import reverse
import json
from django.http import HttpResponse

# Create your views here.

def home_page(request):
    return render(request,'Home.html')


def user_sign_up(request):
    if request.method == 'POST':
        register_form = request.POST

        try:

            existed_user=User.objects.get(username=register_form['email'])
               

        except User.DoesNotExist:
            existed_user=None
            
        if existed_user is None:
            # Creating newly registered user in auth.user table with is_active = False
            user = User.objects.create_user(username=register_form['email'],
                                            email=register_form['email'],
                                            password=register_form['choose_password'],
                                            first_name=register_form['first_name'],
                                            last_name=register_form['last_name'],
                                            is_active=True)
            
            messages.success(request,
                            'Congratulations! You have been registered succesfully at Creative Coders. You can login now.')  # <-

            return redirect('/')

        else:
            ## form = request.POST
            messages.warning(request, 'This user is already registered with us')   
            return redirect('/')

    else:
        ## form = request.POST
        messages.error(request, 'Please register from our Home page using registration form ')

        return redirect('/')
        # return render(request, 'home.html', {'form': form})
    # return render(request,'Home.html')   


def user_login(request):
    if request.method == 'POST':
        user_name=request.POST['email']
        pass1= request.POST['password']
        # print("UserName is:",user_name,pass1)
        # existed_user=User.objects.get(username="sanchitagarg@gmail.com")
        # print("existed user", existed_user.first_name)

        user_record = auth.authenticate(request, username=user_name,password=pass1)
        print("USER_LOGIN IS:", user_login)
        if user_record is not None and user_record.is_superuser is False:
            auth.login(request, user_record)
            
            #CREATING SESSION AT USING LOGIN
            # request.session['user_session_at_login']=user_login.first_name
           
            # messages.success(request,'Welcome to online test portal of Anjaniya Soft Solutions')
            return redirect('my_profile')
        else:
            messages.warning(request, 'Wrong User-ID/Password. Make sure that you have completed email verification process (if registered)')
            return redirect('/')
    else:
        messages.error(request, 'Please login from Home page of Anjaniya Soft Solutions ')
        return redirect('/')


def user_personal_page_home(request):
    # print("succes")
    return render(request,'User_Personal_Page_home.html')


def my_profile(request):
    return render(request,'my_profile.html')


def user_papers_detail(request):
    # data = [
    #     {'title': 'Title1', 'author': 'author1', 'abstract': 'abstract1'},
    #     {'title': 'Title2', 'author': 'author2', 'abstract': 'abstract2'},
    #     {'title': 'Title3', 'author': 'author3', 'abstract': 'abstract3'}
    # ]
    
    data = file_record.objects.filter(user_detail_id=request.user.id)
    return render(request,'user_papers_detail.html',{'data_list':data})


def user_shared_papers_detail(request):
    user_access_all_records = user_access.objects.filter(user_name = request.user)    
    return render(request,'user_shared_papers_detail.html',{'user_access_all_records':user_access_all_records})




def create_new_editor_page(request):
    return render(request,'create_new_editor_page.html')




def editor_page(request,paper_id):
    # print(paper_id)
    paper_record=file_record.objects.filter(id=paper_id)
    paper_records_list = list(paper_record)
    # print(JsonResponse(paper_record))
    # all_records=file_record.objects.all()    

    return render(request, 'editor_page.html',{'paper_record':paper_records_list})
    # return render(request,'editor_page.html')



# def editor_page_shared_paper(request,paper_id):
#     # print(paper_id)
#     shared_paper_record=file_record.objects.filter(id=paper_id)
#     shared_paper_record_list = list(shared_paper_record)
#     # print(JsonResponse(paper_record))
#     # all_records=file_record.objects.all()    

#     return render(request, 'editor_page.html',{'shared_paper_record':shared_paper_record_list})
#     # return render(request,'editor_page.html')



def create_new_form_action(request):

    data = request.POST
    title = data.get("title")
    authors = data.get("authors")
    abstract = data.get("abstract")
    keywords = data.get("keywords")
    introduction = data.get("introduction")
    methods = data.get("methods")
    results = data.get("results")
    conclusion = data.get("conclusion")
    references = data.get("references")

    file_record.objects.create(user_detail_id_id=request.user.id,title=title,authors=authors,abstract=abstract,key_words=keywords,introduction=introduction,methods=methods,results=results,conclusion=conclusion,references=references).save()
    return redirect('/user_papers_detail')







def form_data(request,paper_id):
    # data = {
    #     'title': 'Research Paper',
    #     'author': 'John',
    #     'abstract': 'New York'
    # }

    # afterwords we will do acc to ids
    data = request.POST
    title = data['title']
    authors = data['authors']
    abstract = data['abstract']
    keywords = data['keywords']
    introduction = data['introduction']
    methods = data['methods']
    results = data['results']
    conclusion = data['conclusion']
    references = data['references']

    # print("title is",title)

    # file_record.objects.filter(user_detail_id=request.user.id).update(title=data['title']).save()
    # file_record.objects.filter(user_detail_id=1).update(title="abc")

    # if(len(title) > 0):
    #     # print("in title if is",request.user.id)
    #     file_record.objects.filter(id=paper_id).update(title=data['title'])
        
    
    # elif(len(authors) > 0):
    #     # file_record.objects.filter(user_detail_id=request.user.id).update(authors=data['authors'])
    #     file_record.objects.filter(id=paper_id).update(authors=data['authors'])
    
    # elif(len(abstract) > 0):
    #     file_record.objects.filter(id=paper_id).update(abstract=data['abstract'])
    
    # elif(len(keywords) > 0):
    #     file_record.objects.filter(id=paper_id).update(keywords=data['keywords'])
    
    # elif(len(introduction) > 0):
    #     print("hi")
    #     file_record.objects.filter(id=paper_id).update(introduction=data['introduction'])
    
    # elif(len(methods) > 0):
    #     file_record.objects.filter(id=paper_id).update(methods=data['methods'])
    
    # elif(len(results) > 0):
    #     file_record.objects.filter(id=paper_id).update(results=data['results'])
    
    # elif(len(conclusion) > 0):
    #     file_record.objects.filter(id=paper_id).update(conclusion=data['conclusion'])
    
    # elif(len(references) > 0):
    #     file_record.objects.filter(id=paper_id).update(references=data['references'])
    
   
    if(len(title) > 0):
        file_record.objects.filter(id=paper_id).update(title=data['title'])
        
    
    if(len(authors) > 0):
        file_record.objects.filter(id=paper_id).update(authors=data['authors'])
    
    if(len(abstract) > 0):
        file_record.objects.filter(id=paper_id).update(abstract=data['abstract'])
    
    if(len(keywords) > 0):
        file_record.objects.filter(id=paper_id).update(key_words=data['keywords'])
    
    if(len(introduction) > 0):
        file_record.objects.filter(id=paper_id).update(introduction=data['introduction'])
    
    if(len(methods) > 0):
        file_record.objects.filter(id=paper_id).update(methods=data['methods'])
    
    if(len(results) > 0):
        file_record.objects.filter(id=paper_id).update(results=data['results'])
    
    if(len(conclusion) > 0):
        file_record.objects.filter(id=paper_id).update(conclusion=data['conclusion'])
    
    if(len(references) > 0):
        file_record.objects.filter(id=paper_id).update(references=data['references'])
    
    
    # authors = data['authors']
    # print("title and authors are",len(title)," " ,len(authors))
    # co_authoring_file_record_details=co_authoring_file_record.objects.filter(profile_id=request.user).update(
    # name=details['name'], dept="",mobile=details['mobile'],college="",address=details['address'],country=details['country'],state=details['state'],city=details['city'],pincode=details['pincode'],is_profile_set=True

    # )
    url = reverse('editor_page', kwargs={'paper_id': paper_id})
    return redirect(url)




def ajax_action(request):
    record_id=request.GET.get('record_id')
    # print("record id is", record_id)
    record_for_ajax = file_record.objects.all()
    record = record_for_ajax.filter(id=record_id)

    # for i in record:
    #     print(i.title)

    # return render(request,'editor_page.html',{'record':record})
    # data=(serializers.serialize("json", record))

    data=list(record.values())
    return JsonResponse(data,safe=False)

    # print(data)
    # return HttpResponse(data, content_type="text/json-comment-filtered")

    # record_for_ajax = file_record.objects.filter(user_detail_id=request.user.id)
    # record_data = serializers.serialize('json', record_for_ajax)

    # return JsonResponse({'record': record_data}, safe=False)
    
    
    
    
    
    



def share_paper_action(request):
    data = request.POST
    paper_detail = file_record.objects.filter(id=data['paper_id']).first()
    user_record = User.objects.get(id=paper_detail.user_detail_id_id)
    
    user_access.objects.create(user_name = data['username'],
    access_type="edit",suggestion="No suggestions",file_record_access_id_id=data['paper_id'],
    owner_id=user_record.id,owner_name=user_record.first_name,paper_title=paper_detail.title)
    return redirect('/user_papers_detail')
    
    
    
    
    
    
    
    
    