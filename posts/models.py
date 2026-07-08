from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.urls import reverse
class Post(models.Model):
    title = models.CharField("заголовок", max_length=200)
    text = models.TextField ("текст")
    author = models.ForeignKey(
        User,
        verbose_name="Автор",
        on_delete=models.CASCADE,
        related_name="posts",

        )
    favorites = models.ManyToManyField(User,verbose_name="В избранном у пользователя", related_name="favotite_posts")
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "пост"
        verbose_name_plural = "посты"
    
    def __str__ (self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

class Comment(models.Model):
    
    post = models.ForeignKey(Post, verbose_name="пост", on_delete=models.CASCADE,
related_name="comments")
    author = models.ForeignKey(User, verbose_name="автор", on_delete=models.CASCADE,
 related_name="comments")
    text = models.TextField("текст комментария ")
    created_at = models.DateTimeField("дата создания", auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "комментарий"
        verbose_name_plural = "комментарии"

    def __str__(self):
        return f"Комментарий от {self.autor} к {self.post}"
    
    