from django.urls import path
from . import views

urlpatterns=[
    path('',views.loginPage, name='sign-in'),
    path('logout/',views.logoutPage, name='log-out'),
    path('signup/',views.signupPage, name='sign-up'),

    path('welcome/', views.welcome, name='welcome'),
    path('profile/<str:pk>',views.profile, name='profile'),
    path('users/', views.usersPage,name='users'),
    path('users/<str:pk>', views.usersPageSearch,name='users-page'),

    path('requests/<str:pk>',views.elevatedRequests, name='requests'),
    path('access-requests/',views.accessRequests,name='access-requests'),
    path('delete-requests/<str:pk>',views.deleteRequest,name='delete-requests'),
    path('approve-requests/<str:pk>',views.approveRequest,name='approve-requests'),
    path('deny-requests/<str:pk>',views.denyRequest,name='deny-requests'),

    path('delete-user/<str:pk>', views.deleteUser,name='delete-user'),
    path('edit-user/<str:pk>',views.editUser, name='edit-user'),
    path('add-user',views.addUser,name="add-user"),
]