# from django.conf.urls import url
from django.urls import path, include, re_path

from . import views

urlpatterns = [
path('', views.home_page, name='home_page'),
path('user_sign_up/', views.user_sign_up, name='user_sign_up'),
path('user_login/', views.user_login, name='user_login'),

path('user_personal_page_home/', views.user_personal_page_home, name='User_Personal_Page_home'),
path('my_profile/', views.my_profile, name='my_profile'),
path('user_papers_detail/', views.user_papers_detail, name='user_papers_detail'),
path('user_shared_papers_detail/', views.user_shared_papers_detail, name='user_shared_papers_detail'),
path('create_new_editor_page/', views.create_new_editor_page, name='create_new_editor_page'),

path('editor_page/<slug:paper_id>/', views.editor_page, name='editor_page'),
path('form_data/<slug:paper_id>/', views.form_data, name='form_data'),
path('create_new_form_action/', views.create_new_form_action, name='create_new_form_action'),

path('ajax/', views.ajax_action, name='ajax'),


path('share_paper_action/', views.share_paper_action, name='share_paper_action'),







# path('instant_test_register/', views.instant_test_user_profile_register, name='instant_test_register'),
# path('instant_test_activate_user/<slug:uidb64>/<slug:token>/',views.instant_test_user_profile_activate, name='instant_test_activate_user'),
# path('instant_test_reset_password/<slug:uidb64>/<slug:token>/',views.instant_test_user_profile_allow_reset_password, name='instant_test_reset_password'),
# path('instant_test_teacher_scheduled_test_specific_view/<str:tests_to_view>/', views.instant_test_teacher_scheduled_test_specific_view, name='instant_test_teacher_scheduled_test_specific_view'),

# path('instant_test_download_question_paper/<int:test_id>/', views.instant_test_download_question_paper, name='instant_test_download_question_paper'),

]