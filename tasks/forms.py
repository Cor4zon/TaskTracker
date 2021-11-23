from django import forms

class ProjectForm(forms.Form):
    title = forms.CharField(label="Название:")
    description = forms.CharField(label="Описание:", widget=forms.Textarea)
    deadline = forms.DateField(label="Deadline:", initial="2022-01-01")


class TaskForm(forms.Form):
    title = forms.CharField(label="Название:")
    description = forms.CharField(label="Описание:", widget=forms.Textarea)
    status = forms.IntegerField(label="Приоритет:", initial=0)
    deadline = forms.DateField(label="Deadline:", initial="2022-01-01")
    employee = forms.IntegerField(label="Сотрудник:", initial=1)


