from django.urls import path
from . import views
urlpatterns = [
    path('',views.welcome),
    path('login',views.login),
    path('index',views.index),
    path('register1',views.register1),
    path('register2',views.register2), 
    path('login2',views.login2),
    path('rgs1',views.rgs1),
    path('rgs2',views.rgs2),
    path('register_success',views.register_success),
    path('log',views.log),
    path('show',views.show),
    path('del/<int:id>',views.dele),
    path('edit/<int:id>',views.edit),
    path('edcode/<int:id>',views.edcode),
    path('show2',views.show2),
    path('log2',views.log2),
    path('del2/<int:id>',views.dele2),
    path('edit2/<int:id>',views.edit2),
    path('edcode2/<int:id>',views.edcode2),
    path('adminpage',views.adminpage),
    path('verifypage',views.verifypage),
    path('show3',views.show3),
    path('del3/<int:id>',views.dele3),
    path('accept_admin/<int:id>',views.accept_admin),
    path('search_user',views.search_user,name='search_user'), #newly added
    path('search_admin',views.search_admin,name='search_admin'), #newly added
    path('rockballad',views.rockballad),
    #track upload
    path('upld',views.upld), 
    path('upd',views.upd),   
    path('show_audio',views.show_audio),  
    #rupam's song upload
    path('rockupload',views.rockupload),
    path('rockupd',views.rockupd),
    path('rockshow',views.rockshow),
    #kk's song upload
    path('kkupload',views.kkupload),
    path('kkupd',views.kkupd),
    path('kkshow',views.kkshow),
    #user playlist upload
    path('userplaylistupload',views.userplaylistupload),
    path('userplaylistupd',views.userplaylistupd),
    path('userplaylistshow',views.userplaylistshow),
    #custom playlist page
    path('customplaylist',views.customplaylist),
    #for rockballads
    # path('songs/', views.song_list),
    path('api/songs/', views.song_list, name='song-list-api'),
]
