from course.views.courses import course
from course.views.mylearning import cart
from django.shortcuts import render, redirect, HttpResponse
from course.models.courses import Course
from coursesellingwebsite import settings
from time import time
from .models import Payment
from django.views.decorators.csrf import csrf_exempt
from usercourse.models import UserCourse
import razorpay
from cart.models import Cart
from django.db.models import Q
from django.contrib import messages

# Create your views here.

client = razorpay.Client(auth=(settings.KEY_ID, settings.KEY_SECRET))

def CreateOrder(request, slug):
    if request.user.is_authenticated:  
        course = Course.objects.get(slug=slug)
        if course.instructor == request.user:
            return redirect("course_detail", slug=course.slug)
        order = None
        payment = None
        user = request.user
        try:
            user_course = UserCourse.objects.get(user=user, course=course)
            messages.info(request, "Course Already Purchased.")
            return redirect("mylearning")
        except:
            user_course = None
        action = request.GET.get('action')
        if action == "create_payment":
            if user_course:
                return redirect('mylearning')
            else:
                DATA = {
                    "amount" : int((course.price - ((course.price * course.discount) / 100)) * 100), 
                    "currency" : "INR",  
                    "receipt" : f"code_yourself_{int(time())}",
                    "notes" : {
                        "email" : user.email
                    }
                }
                order = client.order.create(data=DATA)

                payment = Payment(
                    user = user,
                    course = course,
                    order_id = order.get('id') 
                )
                # total_students = course.students+1
                
                # my_course.save()
                course.students = course.students + 1
                payment.save()
                course.save()

        return render(request, 'payment/checkout.html',{"course":course, 'order':order, "payment":payment,'user':user})

    else:
        return redirect('login')

@csrf_exempt
def verify_payment(request):
    if request.method == "POST":
        data = request.POST
        try:
            client.utility.verify_payment_signature(data)
            razorpay_order_id = data['razorpay_order_id']
            razorpay_payment_id = data['razorpay_payment_id']

            payment = Payment.objects.get(order_id=razorpay_order_id)
            print(payment.course)
            User_Course = UserCourse(user=payment.user, course=payment.course)
            User_Course.save()

            payment.payment_id = razorpay_payment_id
            payment.user_course = User_Course
            payment.status = True
            # Course = Course.objects.get(id=payment.course)
            # print(Course)

            try:
                cart = Cart.objects.get(Q(course=payment.course) & Q(user=request.user))
                cart.delete()

            except:
                pass

            payment.save()
            messages.success(request, f"Great Choice {request.user}")
            return redirect('mylearning')
        except:
            return HttpResponse('Invalid Payment')

    return redirect('home')