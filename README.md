# Instrucciones y cosas utiles para Django

### Importar modelos desde la shell de python:
1) `python proyecyto.py shell`
2) `from app import modelo`
3) `from django.contrib.auth.models import User` Esto importa el modelo usuario de django

Dentro de la shell podemos usar codigo de python y ademas se puede crear variables.

### Utilidades de la Shell
1) Mostrar datos de una tabla `User.objects.all()`
2) Fltrar estos datos `User.objects.filter(username="algo")`

Los filtros se pueden mezclar con las funciones `first()`, `last()` entre otros.

Si hacemos `user = User.objects.filter(username="algo")` nos va a guardar lo que esta query retorne como una variable la cual dsps podemos llamar.

Con la funciona `user.pk` nos retorna la primary key del elemento guardado

Ejemplo de mi app:
```
>>> user = User.objects.filter(username='hanz').first()
>>> user
<User: hanz>
>>> user.pk
1
>>> user.id
1
```

Como conseguir todos los posr de un usuario:
```
>>> user.post_set.all()
<QuerySet [<Post: Test post 1>, <Post: Test post 2!>]>
```
### Como agregar cosas a la base de datos desde la shell:
```
>>> user
<User: hanz>
>>> Post.objects.all()
<QuerySet []>
>>> Post_1 = Post(title='Test post 1', content = 'Primer test!', author=user)
>>> Post.objects.all()
<QuerySet []>
>>> Post_1.save()
>>> Post.objects.all()
<QuerySet [<Post: Post object (1)>]>
```

Al crear el nuevo post no fue necesario incluir la fecha como el modelo lo especifica debido a la utilidad de django de date time. Es importante hacer el save del post para poder subirlo a la db

Tambien se puede igualar el autor usando el id de usuario:
```
>>> user
<User: hanz>
>>> Post_2 = Post(title='Test post 2!', content = 'Segundo post!!', author_id=user.id)
>>> Post_2.save()
>>> Post.objects.all()
<QuerySet [<Post: Test post 1>, <Post: Test post 2!>]>
```

Verificacion de que se agregar automaticamente la fecha:
```
>>> post = Post.objects.first()
>>> post
<Post: Test post 1>
>>> post.date_posted
datetime.datetime(2022, 12, 5, 5, 14, 0, 802476, tzinfo=datetime.timezone.utc)
```

A base del Post podemos conseguir mas info del autor usando `post.author.dato` como por ejemplo el mail. `post.author.email`.

## Crear forms y user input:
Django provee unos forms pre creados para distintos tipos de inputs de usuarios. Por ejemplo en un register podemos importa el form de Django `from django.contrib.auth.forms import UserCreationForm` y luego simplemente lo llamamos `form = UserCreationForm()`.