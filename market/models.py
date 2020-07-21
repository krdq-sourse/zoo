from django.db import models


class Category(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Manufacturer(models.Model):
    """Производитель"""
    name = models.CharField("Производитель", max_length=150)
    description = models.TextField("Описание")
    country = models.CharField("Страна", max_length=60)
    image = models.ImageField("Изображение", upload_to="manufacturers/")
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"


class Animal(models.Model):
    """Животное"""
    name = models.CharField("Животное", max_length=150)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="animals/")
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Животное"
        verbose_name_plural = "Животные"


class Product(models.Model):
    """Товар"""
    name = models.CharField("Название", max_length=150)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="products/")
    price = models.FloatField("Цена", default=0)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    animal = models.ForeignKey(Animal, verbose_name="Животное", on_delete=models.SET_NULL, null=True)
    manufacturer = models.ForeignKey(Manufacturer, verbose_name="Производитель", on_delete=models.SET_NULL, null=True)
    availability = models.BooleanField("Наличиие товара", default=True)
    url = models.SlugField(max_length=150, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Stock(models.Model):
    """Акции"""
    name = models.CharField("Название акции")
    product = models.ForeignKey(Product, verbose_name="Продукт", on_delete=models.SET_NULL, null=True)
    discount = models.FloatField("Скидка", default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Скидка"
        verbose_name_plural = "Скидки"


class PhotoOfProduct(models.Model):
    name = models.CharField("Назвние")
    