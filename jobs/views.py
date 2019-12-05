from django.shortcuts import render
from .models import Job


def job_view(request):
    jobs = Job.objects.all()
    context = {
        "jobs": jobs,
        "title": "Jobs",
    }
    return render(request, "jobs/jobs.html", context)


def job_detail_view(request, job_id):
    job = Job.objects.get(id=job_id)

    context = {
        "job": job,
        "title": job.title,
    }
    return render(request, "jobs/detail.html", context)
