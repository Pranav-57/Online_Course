from django.shortcuts import redirect, render
from course.models.courses import Course
from .models import Cart
from django.db.models import Q
from django.contrib import messages
from usercourse.models import UserCourse

# Create your views here.
def add_to_cart(request, pk):
    if request.user.is_authenticated:
        course = Course.objects.get(slug=pk)
        if course.instructor == request.user:
            return redirect("course_detail", slug=pk)

        try:
            cart_product = Cart.objects.get(Q(user=request.user) & Q(course=course))
            messages.info(request,'Course Already Cart.')

        except:
            try:
                buy_product = UserCourse.objects.get(Q(user=request.user) & Q(course=course))
                messages.info(request,'Course Already Purchased.')
                return redirect('mylearning')
            except:
                messages.success(request,'Course Added To Cart.')
                Cart(user=request.user, course=course).save()

        return redirect('cart')
    return redirect('login')

def cart(request):
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user)
        return render(request, 'cart/cart.html',{"carts":carts})
    else:
        return redirect('login')

def remove_from_cart(request, pk):
    if request.method == "GET":
        if request.user.is_authenticated:
            course = Course.objects.get(slug=pk)
            if course.instructor == request.user:
                return redirect("course_detail", slug=course.slug)
            cart = Cart.objects.get(Q(course=course) & Q(user=request.user))
            cart.delete()
            messages.success(request,'Course Remove From Cart.')
            return redirect("cart")
        else:
            messages.info(request,'You are not login.')
            return redirect('login')