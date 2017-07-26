from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Plot, Booking, Applicant
from .forms import PlotForm, BookingForm, ApplicantForm


def home(request):
    return render(request, "index.html")


def search(request):
    queryset_list = Plot.objects.all().order_by('plot_no')
    query = request.GET["q"]
    if query:
        queryset_list = queryset_list.filter(
            Q(plot_no__icontains=query) |
            Q(booking_info__booked_by__applicants_name__icontains=query)
        ).distinct()
        paginator = Paginator(queryset_list, 4)
        page_request_var = "page"
        page = request.GET.get(page_request_var)
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)
        context = {
            "object_list": queryset,
            "title": "Find Plot",
            "value": query,
            "page_request_var": page_request_var,
        }
        return render(request, "search_listings.html", context)
    else:
        return render(request, "index.html")


def plot_detail(request, pk=None):
    instance = get_object_or_404(Plot, pk=pk)
    context = {
        "instance": instance,
    }
    return render(request, "plot_detail.html", context)


def booking_detail(request, pk=None):
    instance = get_object_or_404(Booking, pk=pk)
    context = {
        "instance": instance,
    }
    return render(request, "booking_detail.html", context)


def applicant_detail(request, pk=None):
    instance = get_object_or_404(Applicant, pk=pk)
    context = {
        "instance": instance,
    }
    return render(request, "applicant_detail.html", context)


def plot_update(request, pk=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Plot, pk=pk)
    form = PlotForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
            "instance": instance,
            "form": form,
        }
    return render(request, "plot_form.html", context)


def booking_update(request, pk=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Booking, pk=pk)
    form = BookingForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
            "instance": instance,
            "form": form,
        }
    return render(request, "booking_form.html", context)


def applicant_update(request, pk=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Applicant, pk=pk)
    form = ApplicantForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
            "instance": instance,
            "form": form,
        }
    return render(request, "applicant_form.html", context)


def plot_delete(request, pk=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Plot, pk=pk)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("plot:home")


def booking_delete(request, pk=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Booking, pk=pk)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("plot:home")


def applicant_delete(request, pk=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Applicant, pk=pk)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("plot:home")


def plot_form(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    if request.method == 'POST':
        form = PlotForm(request.POST or None)
        if form.is_valid():
            if form.cleaned_data != {}:
                instance = form.save(commit=False)
                instance.save()
                return HttpResponseRedirect(instance.get_absolute_url())
    else:
        form = PlotForm()
    context = {
        'form': form,
    }
    return render(request, 'plot_form.html', context)


def booking_form(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    if request.method == 'POST':
        form = BookingForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect(instance.get_absolute_url())
    else:
        form = BookingForm()
    context = {
        'form': form,
    }
    return render(request, 'booking_form.html', context)


def applicant_form(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    if request.method == 'POST':
        form = ApplicantForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect(instance.get_absolute_url())
    else:
        form = ApplicantForm()
    context = {
        'form': form,
    }
    return render(request, 'applicant_form.html', context)


def profile(request, pk=None):
    user = get_object_or_404(User, pk=pk)
    context = {
        "user": user,
    }
    return render(request, "profile.html", context)
