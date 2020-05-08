from django.shortcuts import render  , redirect
from django.http import JsonResponse
from .models import User , CourseInfo ,UserGroup , Cart , Order ,QualifiedTeacher
from django.conf import settings
import time
import random
import os
from django.db.models  import Q
from dwebsocket.decorators import accept_websocket,require_websocket

# Create your views here.

#首页
def home(request):
    try:
        courseList = CourseInfo.objects.all()
        return render(request, 'yxtx/home.html', {
            "title": "首页",
            "courseList": courseList,
        })
    except:
        return render(request, 'yxtx/home.html', {
            "title": "首页",
        })
#课程详情界面
def courseInformation(request , cid):
    courseInfo = CourseInfo.objects.get(orderId=cid)
    university = User.objects.get(userphone=courseInfo.userphone).userUniversity

    return render(request , 'yxtx/courseInfomation.html' , {
        "title":"详情",
        "cid":cid ,
        "courseInfo":courseInfo ,
        "university":university ,

    })
#发布信息
# 1进入页面，首先判断是否进行资质认证，
#     如果没有跳转资质认证。
# 2认证过以后才能进入publish页面
def publish(request , flag):
    userphone = request.session.get("userphone")
    try:
        QualifiedTeacher.objects.get(userId=userphone)
    except:
        return redirect('/identification/0/')

    if int(flag) == 0:
        return render(request, 'yxtx/publish.html', {
            "title": "发布"
        })
    if int(flag) == 1:
        return render(request, 'yxtx/publish.html', {
            "title": "发布",
            "submitSuccess": "提交成功!"
        })
    if int(flag) == 2:
        return render(request, 'yxtx/publish.html', {
            "title": "发布",
            "flag":'1'
        })
#资质认证页面
def identification(request , flag):
    # 访问页面
    if flag == '0':
        return  render(request , 'yxtx/identification.html')
    # 提交页面
    if flag == '1':
        userId = request.session.get("userphone")
        if request.method == "POST":
            userIdCard = request.POST.get("idcard")#身份证
            xueli = request.POST.get("xueli") #marjorQualified
            experience = request.POST.get("experience")
            cancourse = request.POST.get("cancourse")
            majorqualied = request.POST.get("majorqualied")
            c = QualifiedTeacher.createQualifiedTeachert(userId , userIdCard ,xueli ,experience ,cancourse ,majorqualied)
            c.save()
            return redirect('/publish/2/')
#提交发布信息
    #userphone   用户手机号码
    #orderId    订单号
    #publish_text   课程介绍
    #userImg      上传图片
    #price      价钱
    #publish_type    课程类型
    #is_delete    是否删除
def publish_submit(request):
    if request.method == "POST":
        isture = isLogin(request)
        if isture == 0 :
            return redirect('/login/')
        usertoken = request.session.get("token")
        username = request.session.get("username")
        userphone = User.objects.get(userToken=usertoken).userphone  # 获取用户邮箱
        orderId = random.randrange(1, 1000000)
        orderid = str(orderId)
        publish_text = request.POST.get("publish_text")
        f = request.FILES["userImg"]
        userImg = os.path.join(settings.COURSE, orderid + ".png")
        with open(userImg, "wb") as fp:
            for data in f.chunks():
                fp.write(data)
        price = request.POST.get("price")
        publish_type = request.POST.get("publish_type")

        courseInfo = CourseInfo.createcourseinfo(userphone , username  ,  orderid  , publish_text , userImg , price , publish_type , False )
        courseInfo.save()
        return redirect('/publish/1/')
#查看信息
def messages(request):
    userphone = request.session.get("userphone")
    groupList = UserGroup.objects.filter(userForm=userphone)
    return render(request, 'yxtx/messages.html' , {
        "title": "消息" ,
        "grouplists":groupList ,
    })
#聊天室
#shopid 可以拿到 touser id
def chart(request ,  shopid , flag):
    fromuser = request.session.get("userphone")
    fromusername = request.session.get("username")
    touser = CourseInfo.objects.get(orderId=shopid)
    if flag == '0':

        # id = str(time.time() + random.randrange(1, 100000))
        # chat = Chat.createchat(id , shopid ,fromuser ,touser.userphone ,touser.userName ,fromusername )
        # chat.save()
        try:
            usergroup = UserGroup.createUserGroup(fromuser , touser.userphone ,touser.userName,shopid , 0 , 1)
            usergroup.save()
            usergroup2 = UserGroup.createUserGroup(touser.userphone ,fromuser,  fromusername, shopid,0, 0)
            usergroup2.save()
        except:
            userphone = UserGroup.objects.get(Q(userTo=touser.userphone) & Q(userForm=fromuser) )
            userphone.shopId = shopid
            userphone.save()
            userphone2 = UserGroup.objects.get(Q(userTo=fromuser) & Q(userForm=touser.userphone))
            userphone2.shopId = shopid
            userphone2.save()
        from_to_user = {}
        from_to_user['userForm'] = fromuser
        from_to_user['userTo'] = touser.userphone
        from_to_user['userName'] = touser.userName
        userphone = UserGroup.objects.get(Q(userTo=touser.userphone) & Q(userForm=fromuser))
        shopid = userphone.shopId
        # print(shopid)
        return render(request , 'yxtx/chart.html' , {
            "title":"聊天室" ,
            "touser":touser ,
            "from_to_user": from_to_user,
            "flag":0 ,
            "buyer":1,
            "shopId":shopid
        })
    else:
        # print(fromuser + "    " +  touser.userphone)
        from_to_user = UserGroup.objects.filter(userForm=fromuser).filter(shopId=shopid)
        shopid = from_to_user[0].shopId
        # print(shopid)
        return render(request, 'yxtx/chart.html', {
            "title": "聊天室",
            "touser": touser ,
            "from_to_user":from_to_user[0] ,
            "flag":1,
            "buyer": from_to_user[0].buyer,
            "shopId": shopid
        })
#我的
def mine(request):
    username = request.session.get("username", "未登录")
    usertoken = request.session.get("token")
    userImg = 0
    try:
        user = User.objects.get(userToken=usertoken)
        userphone = user.userphone
        userImg = "/static/mdeia/"+userphone+".png"
    except User.DoesNotExist as  e:
        pass
    return render(request, 'yxtx/mine.html' , {
        "title": "我的" ,
        "username":username ,
        "userImg" :userImg ,
    })
#登录+事物回滚
from django.db import transaction
@transaction.atomic
def login(request):
    if request.method == "POST":
        userphone = request.POST.get("userphone")
        userpasswd = request.POST.get("userPasswd")
        try:
            user = User.objects.get(userphone = userphone)
            if user.userPasswd != userpasswd :
                return redirect('/login/')
            else:
                token = time.time() + random.randrange(1, 100000)
                user.userToken = str(token)
                user.save()
                request.session["username"] = user.userName
                request.session["token"] = user.userToken
                request.session["userphone"] = user.userphone
                return redirect('/mine/')

        except User.DoesNotExist as e:
            return redirect('/login/')

    return render(request, 'yxtx/login.html'  ,  {
        "title": "登陆"
    })
#注册页面          ---------人脸检测未完成
def register(request):
    if request.method == "POST":
        userphone = request.POST.get("userphone")
        userPasswd  = request.POST.get("userPass")
        userName    = request.POST.get("userName")
        userUniversity = request.POST.get("userUniversity")
        userFace = 0
        token = time.time() + random.randrange(1, 100000)
        userToken = str(token)
        f = request.FILES["userImg"]
        userImg = os.path.join(settings.MDEIA_ROOT, userphone + ".png")
        with open(userImg, "wb") as fp:
            for data in f.chunks():
                fp.write(data)

        user = User.createuser(userphone,userPasswd,userName,userUniversity,userImg,userFace,userToken)
        user.save()
        request.session["username"] = userName
        request.session["token"] = userToken
        request.session["userphone"] = userphone
        return redirect('/mine/')
    else:
        return  render(request , 'yxtx/register.html' , {
            "title": "注册"
        })
#检查账户是否存在
def checkuserid(request):
    userphone = request.POST.get("userphone")
    try:
        user = User.objects.get(userphone = userphone)
        return JsonResponse({"data":"改用户已经被注册","status":"error"})
    except User.DoesNotExist as e:
        return JsonResponse({"data":"可以注册","status":"success"})

#退出登录
from django.contrib.auth import logout
def quit(request):
    logout(request)

    return redirect('/mine/')
#测试页面
def test(request):
    return  render(request , 'yxtx/test2.html')
#判断用户是否登录
    #1.判断是否登录
    #2.判断是否异机登录
def isLogin( request):
    user_is_login = request.session.get("userphone")
    usertoken = request.session.get("token")
    if user_is_login and usertoken:
        try:
            userphone = User.objects.get(userphone=user_is_login)
            if userphone.userToken != usertoken:
                return 0
        except User.DoesNotExist as e:
            return 0
    else:
        return 0
#进行聊天界面
from collections import defaultdict
import json
allconn = defaultdict(list)
@accept_websocket
def mess_connect(request , fromuser , touser):
    global allconn
    if request.is_websocket():
        allconn[fromuser] = request.websocket
        while True:
            try:
                message = request.websocket.wait()
                if not message:
                    break
                else:
                    # 遍历请求地址中的消息
                    for message in request.websocket:
                        # 将信息发至自己的聊天框
                        mess = str(message, encoding="utf-8")

                        fromdata = {
                            'fromuser' : fromuser ,
                            'message':mess
                        }
                        json_data = json.dumps(fromdata)
                        request.websocket.send(json_data)

                        todata = {
                            'touser': touser,
                            'message': mess
                        }
                        json_data = json.dumps(todata)
                        try:
                            allconn[touser].send(json_data)
                        except:
                            fromdata = {
                                'fromuser': fromuser,
                                'message': '对方不在线'
                            }
                            json_data = json.dumps(fromdata)
                            request.websocket.send(json_data)
            except:
                pass
#删除消息
def delete_usergroup(request):
    userphone = request.session.get("userphone")
    userto = request.POST.get("piduserTo")
    UserGroup.objects.filter(userForm=userphone).filter(userTo=userto).delete()
    UserGroup.objects.filter(userForm=userto).filter(userTo=userphone).delete()
    return JsonResponse({"status": "success"})
#购物车
def cart(request , flag):
    userphone = request.session.get("userphone")
    carts = Cart.objects.filter(userAccount=userphone)
    sumprice = 0
    # 获得总价钱
    # 1取出用户的所有数据
    # 2判断isChose是否为1
    #     如果为1
    #         进行productprice累加数据
    userinfos = Cart.objects.filter(userAccount=userphone)
    for item in userinfos:
        if item.isChose:
            sumprice = sumprice + int(item.productprice)

    return render(request, 'yxtx/cart.html', {
        "carts":carts,
        "sumprice":sumprice ,
        "flag":flag
    })
# 修改购物车
def changecart(request,flag):
    shopid = request.POST.get("shopid")
    userphone = request.session.get("userphone")
    # 创建订单
    if(flag == '0'):
        courseinfo = CourseInfo.objects.get(orderId=shopid)
        sellname = courseinfo.userName
        try:
            c=Cart.objects.get(productid=shopid)
            return JsonResponse({"data": 0, "status": "false"})
        except:
            c = Cart.createCart(userAccount=userphone , sellName=sellname , productid= shopid ,
                                productprice=courseinfo.price,productimg=courseinfo.userImg , productname=courseinfo.publish_type)
            c.save()
            return JsonResponse({"data": 0, "status": "success"})

    # 删除订单
    if (flag == '1'):
        # 1取出Cart中用户数据
        # 2找出productid 数据
        # 3进行更改isdelete为1
        sumprice = 0
        userinfos = Cart.objects.filter(userAccount=userphone)
        product = userinfos.get(productid=shopid)
        product.isDelete = 1
        product.save()
        # 1取出用户的所有数据
        # 2判断isChose是否为1
        #     如果为1
        #         进行productprice累加数据
        for item in userinfos:
            if item.isChose:
                sumprice = sumprice +int(item.productprice)
        return JsonResponse({"price": sumprice, "status": "success"})
    #是否选择
    if(flag == '2'):
        status = request.POST.get("status")
        # //表示状态为ischoose设置为0
        product =Cart.objects.filter(userAccount=userphone).get(productid=shopid)
        if status == '0':
            # 1取出对应用户的那一条产品的数据
            # 2修改ischoose为0
            product.isChose = 0
            product.save()
            return JsonResponse({ "status": "success"})
        # 表示状态为ischoose设置为1
        if status == '1':
            # 1取出对应用户的那一条产品的数据
            # 2修改ischoose为1
            product.isChose = 1
            product.save()
            return JsonResponse({"status": "success"})
#提交订单
def order(request , sumprice):
    userphone = request.session.get("userphone")
    # 1拿出总价钱sumprice 调用支付接口

    # 2拿出本地用户useraccount的所有数据
    # 3遍历其长度：
    #     判断是否ischoose是否为1
    #     3.1生成订单号
    #     3.2获取每一项shopid
    #     3.3获取userID
    #     3.4通过shopid从courseinfo获取sellid
    #     3.5插入order表中
    users = Cart.objects.filter(userAccount=userphone)
    for item in users:
        if item.isChose:
            orderid = time.time() + random.randrange(1, 100000)
            shopid = item.productid
            sellid = CourseInfo.objects.get(orderId=shopid).userphone
            c = Order.createCart(str(orderid) , shopid , userphone , sellid)
            c.save()
            item.isDelete = 1
            item.orderid = orderid
            item.save()
    return redirect('/cart/1/')
#查看订单信息
def showorder(request):
    # 1.创建datalist=[]
    # 2取出属于本地用户的userID的orderID
    # 3利用orderID取出cart表中的sellname，productname ，productimg , productid
    # 4将此添.
    userid = request.session.get("userphone")
    datalist = []
    userorderids = Order.objects.filter(userid=userid)
    for item in userorderids:
        u = {}
        info = Cart.obj2.get(orderid=item.orderid)
        u['sellname'] = info.sellName
        u['productname'] = info.productname
        u['productimg'] = info.productimg
        u['productid'] = info.productid
        datalist.append(u)

    return render(request , 'yxtx/showorder.html' , {
        "showorderList" : datalist
    })