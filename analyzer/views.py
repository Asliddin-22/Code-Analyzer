from django.shortcuts import render, redirect
from .models import CodeSubmission
from .services import analyze_code_with_genai


def index(request):
    if request.method == 'POST':
        user_code = request.POST.get('code')
        user_purpose = request.POST.get('purpose', "")
        user_title = request.POST.get('title', '')
        user_language = request.POST.get('language', 'python')

        feedback = analyze_code_with_genai(
            raw_code=user_code,
            purpose=user_purpose,
            language=user_language,
        )

        submission = CodeSubmission.objects.create(
            title=user_title,
            purpose=user_purpose,
            code=user_code,
            language=user_language,
            analysis_result={"feedback": feedback}
        )

        return redirect("submission_detail", pk=submission.pk)

    return render(request, 'index.html', )



def delete_submission(request, pk):
    if request.method == 'POST':
        submission = CodeSubmission.objects.get(pk=pk)
        submission.delete()
    return redirect("submission_list")


def submission_detail(request, pk):
    submission = CodeSubmission.objects.get(pk=pk)
    return render(request, 'submission_detail.html', {'submission': submission})


def submission_list(request):
    submissions = CodeSubmission.objects.all().order_by('-created_at')
    return render(request, 'submission_list.html', {'submissions': submissions})