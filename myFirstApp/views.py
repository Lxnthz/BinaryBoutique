from django.shortcuts import render
from .models import Users, Certificate, Karakteristik, Courses, Feedback
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.utils.safestring import mark_safe


def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request, 'register.html')

def homepage(request):
    username = request.POST['uname']
    password = request.POST['password']
    akun = Users.objects.filter(username = username, password = password)
    if not akun.exists():
        context = {
            'pesan_login': "-Akunmu gaada deck"
        }
        return render(request,'login.html', context)
    context = {
        'akun': akun.first(),
    }
    
    return render(request, 'homepage.html', context)

def daftarpengguna(request):
    username = request.POST['uname']
    password = request.POST['password']
    email = request.POST['email']
    fullname = request.POST['fname']
    cek = Users.objects.filter(username = username)
    if cek.exists():
        context ={
            'pesan_register': "Pilih username lain dek"
        }
        return render(request, 'register.html', context)
    else:
        akun = Users(username = username, password = password, email = email, fullname = fullname)
        akun.save()
        return render(request, 'login.html')

def learn(request,id):
    akun = Users.objects.get(id = id)
    context ={
        'akun' :akun,
    }
    return render(request,'learn.html', context)


def backtoHome(request,id):
    akun = Users.objects.get(id=id)
    context ={
        'akun': akun,
    }
    return render(request,'homepage.html', context)

def change_password(request,id):
    current_password = request.POST['current-password']
    new_password = request.POST['new-password']
    confirm_password = request.POST['confirm-password']
    akun = Users.objects.get(id=id)
    if new_password != confirm_password:
        context = {
            'pesan': "- Harap cek kembali password baru yang anda masukkan!",
            'akun': akun,
        }
        return render(request, 'settings-page.html', context)
    else: 
        if akun.password == current_password:
            akun.password = new_password
            akun.save()
            return render(request,'login.html')
        else:
            context = {
                'pesan': "- Harap cek kembali password lama yang anda masukkan", 
                'akun': akun,
            }
            return render(request, 'settings-page.html', context)

def delete_account(request, id):
    delete = request.POST['confirmation']
    akun = Users.objects.get(id=id)
    if delete != "DELETE":
        context = {
            'delete_pesan' : "- Anda sudah yakin untuk menghapus akun?",
            'akun': akun,
        }
        return render(request,'settings-page.html', context)
    else:
        akun.delete()
        return render(request,'login.html')
    
def basic_html(request, id):
    akun = Users.objects.get(id=id)
    context = {
        'akun': akun,
    }
    return render(request, 'html-basics.html', context)

def intro_html(request,id):
    akun = Users.objects.get(id=id)
    certifitate = Certificate.objects.filter(user_id=id, course_id=1)
    if certifitate.exists():
        certifitate = "Already added"
    else:
        certifitate = ""
    context = {
        'akun' : akun,
        'certificate': certifitate,
    } 
    return render(request, 'html-intro.html', context)

def settings_page(request,id):
    akun = Users.objects.get(id=id)
    context = {
        'akun': akun
    }
    return render(request, 'settings-page.html', context)

def add_course(request, id , course):
    # create
    sertifikat = Certificate(user_id=id, course_id = course)
    sertifikat.save()
    return redirect('/go_to_user/' + str(id) + '/')

def go_to_user(request, id):
    akun = Users.objects.get(id=id)
    certificate = Certificate.objects.filter(user_id=id)
    courses = []
    for i in certificate:
        course = Courses.objects.get(id=i.course_id)
        course_detail = {
            'course': course,
        }
        courses.append(course_detail)

    context = {
        'akun': akun,
        'courses': courses,
    }
    return render(request, 'user.html', context)
    
def remove_course(request, id, course):
    course = Certificate.objects.get(course_id=course, user_id=id)
    course.delete()
    return redirect('/go_to_user/' + str(id) + '/')

def update_akun(request, id):
    fullname = request.POST['fname']
    username = request.POST['uname']
    email = request.POST['email']
    password = request.POST['password']
    akun = Users.objects.get(id=id)
    akun.fullname = fullname
    akun.username = username
    akun.email = email
    akun.password = password
    
    akun.save()
    return render(request, 'login.html')

def account_settings(request, id):
    akun = Users.objects.get(id=id)
    context = {
        'akun': akun
    }
    return render(request, 'account-settings.html', context)

def intro_css(request,id):
    akun = Users.objects.get(id=id)
    certifitate = Certificate.objects.filter(user_id=id, course_id=2)
    if certifitate.exists():
        certifitate = "Already added"
    else:
        certifitate = ""
    context = {
        'akun' : akun,
        'certificate': certifitate,
    } 
    return render(request, 'css-intro.html', context)

def feedback(request, id):
    akun = Users.objects.get(id=id)

    if request.method == 'POST':
        feedback_content = request.POST.get('feedback')
        Feedback.objects.create(content=feedback_content, user_id=akun)
        context = {
            'akun': akun
        }

        return render(request, 'homepage.html', context)

    context = {
        'akun': akun,
    }
    return render(request, 'feedback.html', context)

def intro_js(request,id):
    akun = Users.objects.get(id=id)
    certifitate = Certificate.objects.filter(user_id=id, course_id=3)
    if certifitate.exists():
        certifitate = "Already added"
    else:
        certifitate = ""
    context = {
        'akun' : akun,
        'certificate': certifitate,
    } 
    return render(request, 'js-intro.html', context)

def intro_php(request,id):
    akun = Users.objects.get(id=id)
    certifitate = Certificate.objects.filter(user_id=id, course_id=4)
    if certifitate.exists():
        certifitate = "Already added"
    else:
        certifitate = ""
    context = {
        'akun' : akun,
        'certificate': certifitate,
    } 
    return render(request, 'php-intro.html', context)

def intro_cpp(request,id):
    akun = Users.objects.get(id=id)
    certifitate = Certificate.objects.filter(user_id=id, course_id=5)
    if certifitate.exists():
        certifitate = "Already added"
    else:
        certifitate = ""
    context = {
        'akun' : akun,
        'certificate': certifitate,
    } 
    return render(request, 'cpp-intro.html', context)


def intro_ruby(request,id):
    akun = Users.objects.get(id=id)
    certifitate = Certificate.objects.filter(user_id=id, course_id=7)
    if certifitate.exists():
        certifitate = "Already added"
    else:
        certifitate = ""
    context = {
        'akun' : akun,
        'certificate': certifitate,
    } 
    return render(request, 'ruby-intro.html', context)

def intro_java(request,id):
    akun = Users.objects.get(id=id)
    certifitate = Certificate.objects.filter(user_id=id, course_id=8)
    if certifitate.exists():
        certifitate = "Already added"
    else:
        certifitate = ""
    context = {
        'akun' : akun,
        'certificate': certifitate,
    } 
    return render(request, 'java-intro.html', context)

def intro_python(request,id):
    akun = Users.objects.get(id=id)
    certifitate = Certificate.objects.filter(user_id=id, course_id=6)
    if certifitate.exists():
        certifitate = "Already added"
    else:
        certifitate = ""
    context = {
        'akun' : akun,
        'certificate': certifitate,
    } 
    return render(request, 'python-intro.html', context)




