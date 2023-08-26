from django.shortcuts import render

import razorpay

from .models import Coffee
from django.views.decorators.csrf import csrf_exempt
from humanize import intcomma

AUTH_TUPLE = ("rzp_test_CZTLnF0Ob91xQz", "aWfB4EPcttupzOCGxmt7vBL4")


# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        amount = int(request.POST.get("amount"))
        print(name, amount)

        rzp_client = razorpay.Client(auth=AUTH_TUPLE)
        # payment capture 1 to auto-capture payment records
        payment = rzp_client.order.create(
            {"amount": amount * 100, "currency": "INR", "payment_capture": "1"}
        )
        coffee = Coffee(name=name, amount=amount, payment_id=payment["id"])
        coffee.save()

        print(payment)

        return render(request, "index.html", {"payment": payment, "key": AUTH_TUPLE[0]})

    return render(request, "index.html")


@csrf_exempt
def success(request):
    if request.method == "POST":
        a = request.POST
        print("success post request:", a)
        payment_id = a["razorpay_payment_id"]
        razorpay_order_id = a["razorpay_order_id"]

        if "error" in a:
            return render(
                request,
                "success.html",
                {"error": "Payment is failed. Please try again.", "is_success": False},
            )

        coffee_user = Coffee.objects.filter(payment_id=razorpay_order_id).first()

        is_success = False
        coffee_user_name = None
        coffee_user_amount = None

        if coffee_user:
            coffee_user.paid = True
            coffee_user.save()

            coffee_user_name = coffee_user.name
            coffee_user_amount = coffee_user.amount

            greet_text = f"Thank you {coffee_user_name} for ordering {intcomma(coffee_user_amount)} cups of coffee."
            is_success = True
        else:
            greet_text = "Sorry! Your payment is failed."

        return render(
            request,
            "success.html",
            {
                "greet_text": greet_text,
                "is_success": is_success,
                "payment": {
                    "id": payment_id,
                    "amount": coffee_user_amount,
                },
                "user": {"name": coffee_user_name},
            },
        )

    return render(request, "success.html")
