from django.urls import path
from . import views_user, views_postagens, views, views_comentarios, views_reviews

urlpatterns = [
    # Django API REST framework
    path('usuario/', views.UsersAPIView.as_view(), name='usuarios'),
    path('postagem/', views.PostagensAPIView.as_view(), name='postagens'),
    path('like/', views.LikePostagensAPIView.as_view(), name='likes'),
    path('review/', views.ReviewAPIView.as_view(), name='reviews'),

    path('usuario/<int:pk>/postagem/', views.PostagemAPIView.as_view(), name='usuario_postagens'),

    path('usuario/<int:pk>/', views.UserAPIView.as_view(), name='usuario'),
    path('postagem/<int:pk>/', views.PostagemAPIView.as_view(), name='postagem'),
    path('like/<int:pk>/', views.LikePostagemAPIView.as_view(), name='like'),
    path('review/<int:pk>/', views.ReviewAPIView.as_view(), name='review'),
    path('usuario/create/', views.UsersAPIViewCreate.as_view(), name='criar'),

    #Pure Django Framework
    path('register/', views_user.RegisterUser),
    path('info/', views_user.mostrar_detalhes),
    path('', views_user.LoginUser),
    path('changeMyPass/', views_user.AlterarSenhaUser),
    path('changeMyName/', views_user.AlterarLoginUser),
    path('changeMyEmail/', views_user.AlterarNomeUser),
    path('deleteMyUser/', views_user.DeletarMinhaConta),
    path('listarUsers/', views_user.ListarUsuarios),
    path('apagarConta/', views_user.ApagarOutraConta),
    path('meusPosts/', views_user.mostrar_meus_posts),

    path('listarPostagens/', views_postagens.listar_postagens),
    path('outrosPosts/', views_postagens.mostrar_posts_visita),
    path('criarNovaPostagem/', views_postagens.criar_nova_postagem),
    path('apagarOuEditarComentarioPostagem/', views_comentarios.editar_apagar_comentario_postagem),
    path('apagarOuEditarComentarioReview/', views_comentarios.editar_apagar_comentario_review),
    path('admOuCriadorApagaComentarioEmPost/', views_comentarios.adm_ou_criador_apaga_comentario_em_post),
    path('admOuCriadorApagaComentarioEmReview/', views_comentarios.adm_ou_criador_apaga_comentario_em_review),

    path('listarReviews/', views_reviews.listar_review),
    path('criarReviews/', views_reviews.criar_nova_review),
    path('listarOutrosReviews/', views_reviews.mostrar_reviews_visita),

    path('adicionandoAmigo/', views_user.adicionar_amigo),
    path('verPedidosdeAmizade/', views_user.ver_pedidos_de_amizade),
]
