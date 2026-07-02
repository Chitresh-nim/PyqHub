from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login as login_session, logout as logout_session
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Subject, PYQ, Bookmark
from django.db.models import Q
from django.core.paginator import Paginator
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PaperSerializer, SearchSerializer

def check_auth(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please login first to access this page.")
        return False
    return True
        
def home(request):
    if not check_auth(request):
        return redirect('login')
    recent_papers = PYQ.objects.order_by("-id")[:7]
    return render(request, "PyqApp/home.html",{"recent_papers":recent_papers})

def papers(request):
    if not check_auth(request):
        return redirect('login')
    paper = PYQ.objects.all()
    return render(request, "PyqApp/papers.html", {"papers" : paper})

def dashboard(request):
    if not check_auth(request):
        return redirect('login')
    profile = request.user.profile
    bookmarks = Bookmark.objects.filter(user= request.user).select_related("paper", "paper__subject")
    return render(request, "PyqApp/dashboard.html", {"bookmarks": bookmarks, "profile": profile})

def admin_dash(request):
    if not check_auth(request):
        return redirect('login')
    if not request.user.is_staff:
        return redirect('home')
    return render(request, "PyqApp/admin_dash.html")

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
        
    else:
        form = RegisterForm()
    return render( request, "PyqApp/register.html", {'form' : form})

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            try:
                user_obj = User.objects.get(email=email)
            except User.DoesNotExist:
                return HttpResponse("Email does not exist")

            username = user_obj.username
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login_session(request, user)
                return redirect("home")
    else:
        form = LoginForm()
        return render(request, "PyqApp/login.html", {"form": form})
    
def logout(request):
    logout_session(request)
    return redirect('login')

@api_view(['GET'])
def search_subjects(request):
    q = request.GET.get("q", "")
    subjects = Subject.objects.filter(Q(title__icontains=q) | Q(code__icontains=q))[:5]

    serializer = SearchSerializer(subjects, many=True)
    data = serializer.data

    return Response(data)



def subject_detail(request, id):
    subject = Subject.objects.get(id=id)
    papers = PYQ.objects.filter(subject=subject)

    return render(request, "PyqApp/subject_detail.html",{
        "subject": subject,
        "papers": papers
    })

def branch_detail(request, branch):
    papers = PYQ.objects.filter(subject__branch__iexact=branch)

    return render(request, "PyqApp/subject_detail.html", {
        "papers": papers
    })

 
@api_view(["GET"])
def filter_paper(request):
    branch = request.GET.get("branch")
    semester = request.GET.get("semester")
    year= request.GET.get("year")
    papers = PYQ.objects.all()

    if branch:
        papers = papers.filter(subject__branch__iexact=branch)

    if semester:
        papers = papers.filter(subject__semester__iexact=semester)

    if year:
        papers = papers.filter(year=year)

    page = request.GET.get('page', 1)
    paginator = Paginator(papers,5)
    page_obj = paginator.get_page(page)

    serializer = PaperSerializer(page_obj, many=True)

    data = serializer.data

    for i,  paper in enumerate(page_obj):
        data[i]["is_bookmarked"] = (
            request.user.is_authenticated and Bookmark.objects.filter(user = request.user, paper=paper).exists()
        )
    return Response({
        "papers": data,
        "current_page": page_obj.number,
        "total_pages" : paginator.num_pages,
        "has_next": page_obj.has_next(),
        "has_previous": page_obj.has_previous(),
    })


@api_view(["POST"])
def toggle_bookmark(request, paper_id):
    bookmark = Bookmark.objects.filter(user=request.user, paper_id=paper_id).first()
    if bookmark:
        bookmark.delete()
        return Response({
            "bookmarked": False,
            "message": "Removed Bookmark"
        })
    Bookmark.objects.create(
        user=request.user,
        paper_id=paper_id
    )

    return Response({
        "bookmarked":True,
        "message": "Bookmarked"
    })

@login_required
def edit_profile(request):
    profile = request.user.profile
    if request.method == "POST":
        if "profile_picture" in request.FILES:
            profile.profile_picture = (
                request.FILES["profile_picture"]
            )
            profile.save()

        username = request.POST.get("username")
        if username:
            request.user.username = username
            request.user.save()
        return redirect("dashboard")
    return render(
        request,
        "PyqApp/edit_profile.html"
        ,{"profile": profile}
    )

            




