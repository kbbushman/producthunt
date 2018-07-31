from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . models import Profile
from . forms import ProfileForm

def profile(request, pk):
  user = User.objects.get(id=pk)
  profile = Profile.objects.get(user=user)
  return render(request, 'profiles/profile_show.html', {'user': user, 'profile': profile})

def profile_edit(request, pk):
  user = User.objects.get(pk=pk)
  profile = Profile.objects.get(user=user)
  if request.method == "POST":
    if profile is not None:
      form = ProfileForm(request.POST, instance=profile)
      if form.is_valid():
        profile = form.save()
        return redirect('profile', pk=user.pk)
    # else:
    #   if form.is_valid():
    #     profile = Profile.objects.create(user=user)
    #     profile = form.save(commit=False)
    #     profile.user = request.user
    #     profile.save()
    #     return redirect('profile', pk=user.pk)
  else:
    form = ProfileForm(instance=profile)
  return render(request, 'profiles/profile_form.html', {'form': form})

def profile_delete(request, pk):
  user = User.objects.get(pk=pk).delete()
  return redirect('home')



# def profile_edit(request, pk):
#   user = User.objects.get(pk=pk)
#   profile = Profile.objects.filter(user=user)
#   # if profile is not None:

#   if request.method == "POST":
#     form = ProfileForm(request.POST, instance=user)
#     if form.is_valid():
#       profile = form.save()
#       return redirect('profile', pk=user.pk)
#   else:
#     form = ProfileForm(instance=user)
#   return render(request, 'profiles/profile_form.html', {'form': form})
