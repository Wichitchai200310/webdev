from django.shortcuts import render, redirect
from .models import Product, Order
from .forms import ProductForm, OrderForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, CartItem, Order
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import path
from django.contrib.auth import views as auth_views  # ใช้สำหรับ login/logout views

# ฟังก์ชันแสดงรายการสินค้า
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

# ฟังก์ชันเพิ่มสินค้า
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form})
# View to delete a product
def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':  # Confirm deletion
        product.delete()
        return redirect('product_list')
    return render(request, 'products/product_confirm_delete.html', {'product': product})
# View to edit a product
def edit_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/product_form.html', {'form': form, 'product': product})

# ฟังก์ชันแสดงรายการคำสั่งซื้อ
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'products/order_list.html', {'orders': orders})

# ฟังก์ชันสร้างคำสั่งซื้อ
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'products/order_form.html', {'form': form})
from django.shortcuts import render

def home(request):
    cart_items = CartItem.objects.filter(user=request.user)  # ดึงข้อมูล cart
    total_price = 0

    for item in cart_items:
        item.total = item.product.price * item.quantity  # คำนวณราคาสินค้าแต่ละรายการ
        total_price += item.total  # เพิ่มไปยังราคารวมทั้งหมด

    return render(request, 'products/home.html', {'cart_items': cart_items, 'total_price': total_price})

from django.shortcuts import render

from django.shortcuts import render

def sales_report(request):
    # ตัวอย่างข้อมูลยอดขาย
    labels = ['January', 'February', 'March', 'April']
    data = [1500, 2300, 1800, 2500]
    
    return render(request, 'products/sales_report.html', {
        'labels': labels,
        'data': data,
    })
# แสดงสินค้าทั้งหมดและตะกร้าสินค้า
@login_required
def home(request):
    products = Product.objects.all()
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'home.html', {
        'products': products,
        'cart': cart_items,
        'total_price': total_price
    })

# เพิ่มสินค้าลงในตะกร้า
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('home')

# ลบสินค้าจากตะกร้า
@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    return redirect('home')

# เช็คเอาท์
@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    if request.method == 'POST':
        order = Order.objects.create(user=request.user, total_price=total_price)
        order.items.set(cart_items)
        order.save()
        
        # ลดจำนวนสินค้าคงเหลือ
        for item in cart_items:
            item.product.stock -= item.quantity
            item.product.save()

        # ล้างตะกร้า
        cart_items.delete()

        return redirect('order_confirmation')

    return render(request, 'checkout.html', {'total_price': total_price})

# ยืนยันคำสั่งซื้อ
@login_required
def order_confirmation(request):
    return render(request, 'order_confirmation.html')
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'บัญชีของคุณถูกสร้างแล้ว! กรุณาล็อกอิน.')
            return redirect('login')  # หลังจากลงทะเบียนแล้วจะพาไปหน้า login
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

# ฟังก์ชันเข้าสู่ระบบ
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('equipment_list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# ฟังก์ชันออกจากระบบ
def logout_user(request):
    logout(request)
    return redirect('login')