from django.db import models

# Create your models here.
# 用户模型类
class User(models.Model):
    #手机号码
    userphone = models.CharField(max_length=31)
    # 密码
    userPasswd  = models.CharField(max_length=20)
    # 昵称
    userName = models.CharField(max_length=20)
    # 大学名称
    userUniversity = models.CharField(max_length=100)
    # 头像路径
    userImg     = models.CharField(max_length=150)
    #人脸识别
    userFace =  models.CharField(max_length=10000)
    # touken验证值，每次登陆之后都会更新
    userToken   = models.CharField(max_length=50)


    @classmethod
    def createuser(cls,phone,passwd,name,university,img,face,token):
        u = cls(userphone = phone,userPasswd = passwd,userName=name,userUniversity=university,userImg=img,userFace =face,userToken=token)
        return u

#课程信息
    #useremail   用户邮箱
    #orderId    订单号
    #publish_text   课程介绍
    #userImg      上传图片
    #price      价钱
    #publish_type    课程类型
    #is_delete    是否删除
class CourseManager(models.Manager):
    def get_queryset(self):
        return super(CourseManager, self).get_queryset().filter(isDelete=False)
class CourseInfo(models.Model):
    # 手机
    userphone = models.CharField(max_length=31)
    #用户名
    userName = models.CharField(max_length=20)
    #订单号
    orderId = models.CharField(primary_key=True,max_length=20)
    #课程介绍
    publish_text = models.CharField(max_length=2000)
    #上传图片
    userImg = models.CharField(max_length=150)
    #价钱
    price =models.IntegerField()
    #课程类型
    publish_type = models.CharField(max_length=20)
    #是否删除
    isDelete = models.BooleanField(default=False)
    #发布时间
    date =  models.DateTimeField(auto_now_add=False, auto_now=True)

    objects = CourseManager()
    @classmethod
    def createcourseinfo(cls, phone,  username , orderid  , publish_text, userimg, price, publish_type, isdelete ):
        u = cls(userphone=phone , userName= username  ,  orderId=orderid, publish_text=publish_text, userImg=userimg,
                price=price, publish_type=publish_type ,isDelete= isdelete )
        return u

class UserGroup(models.Model):
    #信息发送者
    userForm = models.CharField(max_length=31)
    #信息接受者
    userTo = models.CharField(max_length=31)
    #to name
    toName = models.CharField(max_length=21)
    #商品Id
    shopId = models.CharField(max_length=20)
    #聊天信息
    usersInfo = models.CharField(max_length=2000)
    #用户信息不在线 ， 消息记录提醒
    userRemind = models.IntegerField()
    #购买方
    buyer = models.BooleanField(default=True)
    class Meta:
        unique_together = ('userForm', 'userTo')

    @classmethod
    def createUserGroup(cls, userform, userto,toname, shopid, userremind , buyer):
        u = cls(userForm= userform , userTo=userto , toName=toname, shopId= shopid ,userRemind= userremind,  buyer=buyer)
        return u

class CartManager2(models.Manager):
    def get_queryset(self):
        return super(CartManager2, self).get_queryset().filter(isDelete=True)
class CartManager1(models.Manager):
    def get_queryset(self):
        return super(CartManager1, self).get_queryset().filter(isDelete=False)
#购物车
class Cart(models.Model):
    #用户账号
    userAccount = models.CharField(max_length=20)
    #卖家名字
    sellName = models.CharField(max_length=20)
    #商品ID
    productid = models.CharField(max_length=30)
    #商品价格
    productprice = models.CharField(max_length=10)
    #是否勾选商品
    isChose = models.BooleanField(default=True)
    #商品图片
    productimg = models.CharField(max_length=150)
    #商品名字
    productname = models.CharField(max_length=100)
    #订单id
    orderid = models.CharField(max_length=20,default="0")
    #是否删除
    isDelete = models.BooleanField(default=False)

    objects = CartManager1()
    obj2 = CartManager2()
    @classmethod
    def createCart(cls, userAccount, sellName,productid, productprice, productimg ,productname  ):
        u = cls(userAccount= userAccount , sellName=sellName , productid=productid, productprice= productprice
                ,  productimg=productimg ,productname=productname )
        return u
#订单
class Order(models.Model):
    #订单ID
    orderid = models.CharField(max_length=20)
    #商品id
    shopid = models.CharField(max_length=20)
    #用户id
    userid  = models.CharField(max_length=20)
    #卖家id
    sellid  = models.CharField(max_length=20)

    @classmethod
    def createCart(cls, orderid, shopid, userid, sellid):
        u = cls(orderid=orderid, shopid=shopid, userid=userid, sellid=sellid)
        return u
#教师资格认证
class QualifiedTeacher(models.Model):
    #用户id
    userId = models.CharField(max_length=20)
    #用户省份证
    userIdCard = models.CharField(max_length=40)
    #学历
    postgraduateQualified = models.CharField(max_length=40)
    #是否有教学经验
    isexperience = models.CharField(max_length=10)
    #能带哪些课程
    canCourse = models.CharField(max_length=10)
    #有哪些专业证书
    majorQualified = models.CharField(max_length=100)

    @classmethod
    def createQualifiedTeachert(cls, userId, userIdCard, postgraduateQualified, isexperience , canCourse , majorQualified):
        u = cls(userId=userId, userIdCard=userIdCard, postgraduateQualified=postgraduateQualified, isexperience=isexperience ,
                canCourse=canCourse, majorQualified=majorQualified )
        return u

#黑名单
class Blacklist(models.Model):
    #用户id
    userId = models.CharField(max_length=20)
    #账号被封的原因
    reason = models.CharField(max_length=400)
    #用户Ip地址
    ip = models.CharField(max_length=20)
    @classmethod
    def createBlacklist(cls , userId , reason , ip):
        u = cls(userId= userId , reason= reason
                 , ip = ip)
        return  u
#打卡记录
class DaKa(models.Model):
    #订单id
    orderid = models.CharField(max_length=20)
    #用户id
    userId = models.CharField(max_length=20)
    #卖家id
    sellid = models.CharField(max_length=20)
    #课程id
    courseid = models.CharField(max_length=20)
    #用户打卡次数
    userdaka = models.CharField(max_length=10)
    #卖家打卡次数
    selldaka = models.CharField(max_length=10)
    #反馈信息
    backinfo = models.CharField(max_length=100)
    @classmethod
    def createBlacklist(cls , orderid ,userId , sellid , courseid , userdaka, selldaka, backinfo):
        u = cls(orderid= orderid , userId=userId , sellid = sellid ,courseid=courseid,userdaka=userdaka,
                selldaka=selldaka,backinfo=backinfo)
        return  u
