from django.db import models

# Create your models here.
class Category(models.Model):
    '''类别表'''
    cname = models.CharField(max_length=10)  # 类别名称

    def __str__(self):
        return self.cname


class Goods(models.Model):
    '''商品表'''
    gname = models.CharField(verbose_name='商品名称', max_length=100)
    gdesc = models.CharField(max_length=100)
    oldprice = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.gname


class Goodsdetailname(models.Model):
    '''详情名称'''
    gdname = models.CharField(max_length=30)

    def __str__(self):
        return self.gdname


class GoodsDetail(models.Model):
    '''商品详情表'''
    gdurl = models.ImageField(upload_to='')
    detailname = models.ForeignKey(Goodsdetailname, on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)

    def __str__(self):
        return self.detailname.gdname


class Time(models.Model):
    '''尺寸表'''
    tname = models.CharField(max_length=10)

    def __str__(self):
        return self.tname


class Color(models.Model):
    '''颜色表'''
    colorname = models.CharField(max_length=10)
    colorurl = models.ImageField(upload_to='color/')

    def __str__(self):
        return self.colorname


class Inventory(models.Model):
    '''库存表'''
    count = models.PositiveIntegerField()
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    size = models.ForeignKey(Time, on_delete=models.CASCADE)


