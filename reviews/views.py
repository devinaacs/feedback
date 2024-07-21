from django.shortcuts import render, HttpResponseRedirect

# Create your views here.


def review(request):
    if request.method == "POST":
        entered_username = request.POST["username"]
        return HttpResponseRedirect(f"/thank-you")

    return render(request, "reviews/review.html")


def thank_you(request):
    return render(request, "reviews/thank_you.html")
