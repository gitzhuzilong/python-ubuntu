dfrom django.shortcuts import render,redirect
from django.http import JsonResponse
from axf.models import SlideShow, MainDescription, Product,CategorieGroup,ChildGroup,User,Address,Cart,Order
import random
from django.contrib.auth import logout
import uuid
from axf.sms import send_sms
# Create your views here.

def home(request):
    slideList = SlideShow.objects.all()

    mainList = MainDescription.objects.all()
    for item in mainList:
        products = Product.objects.filter(categoryId=item.categoryId)
        item.product1 = products.get(productId=item.product1)
        item.product2 = products.get(productId=item.product2)
        item.product3 = products.get(productId=item.product3)
    return render(request, 'home/home.html',{"slideList":slideList, "mainList":mainList})

def market(request, gid, cid, sid):
    leftCategorieList = CategorieGroup.objects.all()

    products = Product.objects.filter(categoryId=gid)

    if cid != "0":
        products = products.filter(childId=cid)
    if sid == "1":
        pass
    elif sid == "2":
        products = products.order_by("price")
    elif sid == "3":
        products = products.order_by("-price")
    childs = ChildGroup.objects.filter(categorie__categorieId=gid)
    return render(request, 'market/market.html', {'leftCategorieList':leftCategorieList, 'products':products, 'childs':childs, 'gid':gid,'cid':cid})

def order(request):
    tokenValue = request.COOKIES.get("token")
    order = Order.orders2.filter(user__tokenValue=tokenValue).get(flag=0)
    order.flag = 1
    order.save()

    carts = Cart.objects.filter(user__tokenValue=tokenValue).filter(order=order).filter(isCheck=True)
    for cart in carts:
        cart.isOrder = False
        cart.save()

    newOrder = Order.create(str(uuid.uuid4()), User.objects.get(tokenValue=tokenValue), Address.objects.get(pk=1), 0)
    newOrder.save()
    oldCarts = Cart.objects.filter(user__tokenValue=tokenValue)
    for cart in oldCarts:
        cart.order = newOrder
        cart.save()
    return JsonResponse({"error":0})
def cart(request):
    tokenValue = request.COOKIES.get("token")
    if not tokenValue:
        return redirect('/login/')
    try:
        user = User.objects.get(tokenValue=tokenValue)
    except User.DoesNotExist as e:
        return JsonResponse({'error':2})
    carts = Cart.objects.filter(user__tokenValue=tokenValue)
    return render(request, 'cart/cart.html', {'carts':carts})

def changecart2(request):
    cartid = request.POST.get("cartid")
    cart = Cart.objects.get(pk=cartid)
    cart.isCheck = not cart.isCheck
    cart.save()
    return JsonResponse({"error":0, "flag":cart.isCheck})
def changecart(request, flag):
    num = 1
    if flag == "1":
        num = -1
    tokenValue = request.COOKIES.get("token")
    if not tokenValue:
        return JsonResponse({'error': 1})
    try:
        user = User.objects.get(tokenValue=tokenValue)
    except User.DoesNotExist as e:
        return JsonResponse({'error': 2})

    gid = request.POST.get('gid')
    cid = request.POST.get('cid')
    pid = request.POST.get('pid')
    product = Product.objects.filter(categoryId=gid,childId=cid).get(productId=pid)

    try:
        cart = Cart.objects.filter(user__tokenValue=tokenValue).filter(product__categoryId=gid).get(product__productId=pid)
        if flag == "2":
            if product.storeNums == "0":
                return JsonResponse({"error": 0, "num":cart.num})
        cart.num = cart.num + num
        product.storeNums = str(int(product.storeNums) - num)
        product.save()
        if cart.num == 0:
            cart.delete()
        else:
            cart.save()
    except Cart.DoesNotExist as e:
        if flag == "1":
            return JsonResponse({"error":0, "num":0})
        try:
            order = Order.orders2.filter(user__tokenValue=tokenValue).get(flag=0)
        except Order.DoesNotExist as e:
            orderId = str(uuid.uuid4())
            address = Address.objects.get(pk=1)
            order = Order.create(orderId,user,address,0)
            order.save()
        cart = Cart.create(user, product, order, 1)
        cart.save()
        product.storeNums = str(int(product.storeNums) - num)
        product.save()
    return JsonResponse({'error': 0, 'num':cart.num})

def mine(request):
    phone = request.session.get('phoneNum', default='未登录')
    return render(request, 'mine/mine.html', {'phone':phone})

def detail(request, gid, cid, pid):
    products = Product.objects.filter(categoryId=gid)
    products = products.filter(childId=cid).filter(productId=pid)
    return render(request, 'detail/detail.html', {'products': products, 'gid':gid, 'cid':cid, 'pid': pid})

def quit(request):
    logout(request)
    return redirect('/mine/')

def login(request):
    if request.method == 'GET':
        if request.is_ajax():
            strNum = '1234567890'
            rand_str = ''
            for i in range(0, 6):
                rand_str += strNum[random.randrange(0, len(strNum))]
            msg = "您的验证码是：%s。请不要把验证码泄露给其他人。"%rand_str
            phone = request.GET.get('phoneNum')
            # send_sms(msg, phone)
            request.session["code"] = rand_str
            print("*********", rand_str)
            response = JsonResponse({"data": "ok"})
            return response
        else:
            return render(request, "mine/login.html")
    else:
        phone = request.POST.get("username")
        passwd = request.POST.get("passwd")
        code = request.session.get("code")

        if passwd == code:
            # 验证码验证成功
            # 判断用户是否存在
            uuidStr = str(uuid.uuid4())
            try:
                user = User.objects.get(pk=phone)
                user.tokenValue = uuidStr
                user.save()
            except User.DoesNotExist as e:
                # 注册
                user = User.create(phone, None, uuidStr, "hhhh")
                user.save()
            request.session["phoneNum"] = phone
            response = redirect("/mine/")
            response.set_cookie("token", uuidStr)
            return response
        else:
            # 验证码验证失败
            return redirect("/login/")

def address(request):
    addresses = Address.objects.filter(user__phoneNum=request.session.get('phoneNum'))
    return render(request, 'mine/address.html', {'addresses':addresses})
def addAddress(request):
    if request.method == 'GET':
        return render(request, 'mine/addaddress.html')
    else:
        name = request.POST.get('name')
        sex = request.POST.get('sex')
        if sex == "0":
            sex = True
        sex = False
        telphone = request.POST.get('telphone')
        address_2 = request.POST.get('address_2')
        address_3 = request.POST.get('address_3')
        address_4 = request.POST.get('address_4')
        address_5 = request.POST.get('address_5')
        address_6 = request.POST.get('address_6')
        postCode = request.POST.get('postCode')
        allAddress = address_2 + address_3 + address_4 + address_5 + address_6
        phone = request.session.get('phoneNum')
        user = User.objects.get(pk=phone)
        address = Address.create(name, sex, telphone, postCode, allAddress, address_2, address_3, address_4, address_5, address_6, user)
        address.save()
        return redirect('/mine/address/')

