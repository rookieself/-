from django.db import models
from PIL import Image
from django.forms import modelform_factory

class Main(models.Model):
    img = models.CharField(max_length=255, verbose_name='图片连接地址')
    name = models.CharField(max_length=80, verbose_name='名字')
    trackid = models.CharField(max_length=16, verbose_name='id')

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


# Create your models here.


class axf(Main):
    class Meta:
        db_table = 'axf_wheel'
        verbose_name = '图片轮播图表'
        verbose_name_plural = verbose_name


class MainNav(Main):
    class Meta:
        db_table = 'axf_nav'
        verbose_name = '导航表'
        verbose_name_plural = verbose_name


class MainMustBuy(Main):
    class Meta:
        db_table = 'axf_mustbuy'
        verbose_name = '每日必买表'
        verbose_name_plural = verbose_name


class MainShop(Main):
    class Meta:
        db_table = 'axf_shop'
        verbose_name = '商店商品表'
        verbose_name_plural = verbose_name


class MainShow(Main):
    categoryid = models.CharField(max_length=20, verbose_name='分类id')
    brandname = models.CharField(max_length=70, verbose_name='商品的名称')
    img1 = models.CharField(max_length=255, verbose_name='图片的1id')
    childcid1 = models.CharField(max_length=20, verbose_name='商品1的id')
    productid1 = models.CharField(max_length=20, verbose_name='商品1的编号')
    longname1 = models.CharField(max_length=100, verbose_name='商品1的名称')
    price1 = models.FloatField(default=1, verbose_name='商品1的价格')
    marketprice1 = models.FloatField(default=1, verbose_name='市场价格1')

    img2 = models.CharField(max_length=255, verbose_name='图片的2id')
    childcid2 = models.CharField(max_length=20, verbose_name='商品2的id')
    productid2 = models.CharField(max_length=20, verbose_name='商品2的编号')
    longname2 = models.CharField(max_length=100, verbose_name='商品2的名称')
    price2 = models.FloatField(default=1, verbose_name='商品2的价格')
    marketprice2 = models.FloatField(default=1, verbose_name='市场价格2')

    img3 = models.CharField(max_length=255, verbose_name='图片3的id')
    childcid3 = models.CharField(max_length=20, verbose_name='商品3的id')
    productid3 = models.CharField(max_length=20, verbose_name='商品3的编号')
    longname3 = models.CharField(max_length=100, verbose_name='商品3的名称')
    price3 = models.FloatField(default=1, verbose_name='商品3的价格')
    marketprice3 = models.FloatField(default=1, verbose_name='市场价格3')

    class Meta:
        db_table = 'axf_mainshow'
        verbose_name = '商品展示'
        verbose_name_plural = verbose_name


class MainFoodTypes(models.Model):
    typeid = models.IntegerField(default=1, verbose_name='类型id')
    typename = models.CharField(max_length=255, verbose_name='类别名称')
    childtypenames = models.CharField(max_length=255, verbose_name='子类名称')
    typesort = models.IntegerField(default=1, verbose_name='类型顺序')

    def __str__(self):
        return self.typename

    class Meta:
        db_table = 'axf_foodtypes'
        verbose_name = '食品类型'
        verbose_name_plural = verbose_name


# productid,productimg,productname,productlongname,isxf,
# pmdesc,specifics,price,marketprice,categoryid,childcid,
# childcidname,dealerid,storenums,productnum
# 商品信息表
class Goods(models.Model):
    productid = models.IntegerField(default=1, )
    productimg = models.CharField(max_length=255)
    productname = models.CharField(max_length=255)
    productlongname = models.CharField(max_length=255)
    isxf = models.BooleanField(default=False)
    pmdesc = models.BooleanField(default=False)
    specifics = models.CharField(max_length=80)
    price = models.FloatField(default=0)
    marketprice = models.FloatField(default=0)
    categoryid = models.IntegerField(default=1)
    childcid = models.IntegerField(default=1)
    childcidname = models.CharField(max_length=255)
    dealerid = models.IntegerField(default=1)
    storenums = models.IntegerField(default=1)
    productnum = models.IntegerField(default=1)

    def __str__(self):
        return self.productname

    class Meta:
        db_table = 'axf_goods'
        verbose_name = '商品信息表'
        verbose_name_plural = verbose_name


#  用户的模型类：用户表
class AXFUser(models.Model):
    # 输入时对输入数据的限定
    username = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=150)
    email = models.CharField(max_length=70,unique=False)
    # 文件的上传，
    uicon = models.ImageField(upload_to='uploads/%Y/%m/%d/')
    # 设置一个激活开关，默认是没有激活
    is_active = models.BooleanField(default=False)
    # 逻辑删除数据，让用户看不到删除的数据，可以恢复数据，默认可见
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'axf_user'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name


# 购物车表
class Cart(models.Model):
    user = models.ForeignKey(AXFUser, on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    goods_num = models.IntegerField(default=1)
    is_select = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'cart'
        verbose_name = '购物车'
        verbose_name_plural = verbose_name


# 购物车表
class Shopping_Address(models.Model):
    user = models.ForeignKey(AXFUser, on_delete=models.CASCADE)
    address = models.ForeignKey(Goods, on_delete=models.CASCADE)
    goods_num = models.IntegerField(default=1)
    is_select = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'cart'
        verbose_name = '购物车'
        verbose_name_plural = verbose_name

