from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField


class GreetingIndex(models.Model):
    photo = models.ImageField(max_length=300, verbose_name="Картинка")
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    category = models.ForeignKey("CategoryGreeting", verbose_name="Категория", on_delete=models.PROTECT, null=True,
                                 default=1, max_length=2)

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_id", self.pk})

    class Meta:
        verbose_name = "Приветствие"
        verbose_name_plural = "Приветствия"


class CategoryGreeting(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок", db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class CollectionIndex(models.Model):
    photo = models.ImageField(max_length=200, verbose_name="Картинка")
    title = models.CharField(max_length=255, verbose_name="Заголовок")

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_id", self.pk})

    class Meta:
        verbose_name = "Коллекция"
        verbose_name_plural = "Коллекции"


class NoveltyIndex(models.Model):
    photo = models.ImageField(max_length=200, verbose_name="Картинка")
    title = models.CharField(max_length=255, verbose_name="Заголовок")

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_id", self.pk})

    class Meta:
        verbose_name = "Новинка"
        verbose_name_plural = "Новинки"


class PopularIndex(models.Model):
    photo = models.ImageField(max_length=200, verbose_name="Картинка")
    title = models.CharField(max_length=255, verbose_name="Заголовок")

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_id", self.pk})

    class Meta:
        verbose_name = "Популярное"
        verbose_name_plural = "Популярные"


class DiscountIndex(models.Model):
    ad_photo = models.ImageField(max_length=200, verbose_name="Картинка с объявлением")
    discount_on_photo = models.SmallIntegerField(verbose_name="Скидка на картинке")
    photo = models.ImageField(max_length=200, verbose_name="Картинка")
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    description = models.CharField(max_length=100, verbose_name="Описание")
    sizes = ArrayField(models.FloatField(verbose_name="Размер"), verbose_name="Размеры")
    old_price = models.IntegerField(verbose_name="Старая цена")
    new_price = models.IntegerField(verbose_name="Новая цена")

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_id", self.pk})

    class Meta:
        verbose_name = "Скидка"
        verbose_name_plural = "Скидки"


class NewsletterIndex(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    phone_number = models.CharField(max_length=30, verbose_name="Номер телефона")

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
