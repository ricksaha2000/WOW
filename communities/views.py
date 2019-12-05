from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .models import Community, Comment


def community_view(request):
    communities = Community.objects.all()
    context = {
        'title': 'Communities',
        'communities': communities,
    }
    return render(request, "communities/communities.html", context)


def community_detail_view(request, community_id):
    community = Community.objects.get(id=community_id)
    comments = Comment.objects.filter(community=community).order_by('-timestamp')

    if request.method == "POST":
        if request.user.is_authenticated:
            if request.POST.get('like') == "like":
                community.likes += 1
                community.save()
            elif request.POST.get('like') == "comment":
                comment = request.POST.get('comment')
                user = request.user.username
                Comment.objects.create(community=community, comment=comment, user=user)
                community.comments += 1
                community.save()
        else:
            return redirect("/login/")

    context = {
        'title': community.title,
        'community': community,
        'comments': comments
    }
    return render(request, "communities/detail.html", context)
