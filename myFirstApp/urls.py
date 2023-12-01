from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('homepage/', views.homepage, name='homepage'), 
    path('daftarpengguna/', views.daftarpengguna, name='daftarpengguna'),
    path('learn-page/<int:id>/', views.learn, name = 'learn'),
    path('backtoHome/<int:id>/', views.backtoHome, name='backtohome'),
    path('change_password/<int:id>/', views.change_password, name='change_password'),
    path('delete_account/<int:id>/', views.delete_account, name='delete_password'),
    path('basic_html/<int:id>/', views.basic_html, name='basic_html'),
    path('intro_html/<int:id>/', views.intro_html, name='intro_html'),
    path('settings_page/<int:id>/', views.settings_page, name='settings-page'),
    path('add_course/<int:id>/<int:course>/', views.add_course, name='add_course'),
    path('remove_course/<int:id>/<int:course>/', views.remove_course, name='remove_course'),
    path('go_to_user/<int:id>/', views.go_to_user, name='go_to_user'),
    path('update_akun/<int:id>/', views.update_akun, name='update_akun'),
    path('account-settings/<int:id>/', views.account_settings, name="account_settings"),
    path('intro_css/<int:id>/', views.intro_css, name='intro_css'),
    path('feedback/<int:id>/', views.feedback, name="feedback"),
    path('intro_js/<int:id>/', views.intro_js, name="intro_js"),
    path('intro_php/<int:id>/', views.intro_php, name="intro_php"),
    path('intro_cpp/<int:id>/', views.intro_cpp, name="intro_cpp"),
    path('intro_ruby/<int:id>/', views.intro_ruby, name="intro_ruby"),
    path('intro_java/<int:id>/', views.intro_java, name="intro_java"),
    path('intro_python/<int:id>/', views.intro_python, name="intro_python")

]
