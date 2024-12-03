from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Task, Employee
from . import db
from datetime import datetime

main = Blueprint("main", __name__)

@main.route("/")
def index():
    tasks = Task.query.all()
    employees = Employee.query.all()
    return render_template("index.html", tasks=tasks, employees=employees)

@main.route("/add_task", methods=["POST"])
def add_task():
    title = request.form.get("title")
    description = request.form.get("description")
    status = request.form.get("status")
    deadline_str = request.form.get("deadline")  # String en formato 'YYYY-MM-DD'
    employee_id = request.form.get("employee_id")

    # Convertir la fecha a un objeto datetime.date
    try:
        deadline = datetime.strptime(deadline_str, "%Y-%m-%d").date()
    except ValueError:
        flash("Invalid date format. Please use YYYY-MM-DD.")
        return redirect(url_for("main.index"))

    new_task = Task(
        title=title,
        description=description,
        status=status,
        deadline=deadline,
        employee_id=employee_id
    )
    db.session.add(new_task)
    db.session.commit()
    flash("Task added successfully!")
    return redirect(url_for("main.index"))

@main.route("/add_employee", methods=["POST"])
def add_employee():
    name = request.form.get("name")
    email = request.form.get("email")
    new_employee = Employee(name=name, email=email)
    db.session.add(new_employee)
    db.session.commit()
    flash("Employee added successfully!")
    return redirect(url_for("main.index"))

@main.route("/report")
def report():
    employees = Employee.query.all()
    return render_template("report.html", employees=employees)

@main.route("/delete_task/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        flash("Task deleted successfully!")
    else:
        flash("Task not found.")
    return redirect(url_for("main.index"))

@main.route("/edit_task/<int:task_id>")
def edit_task(task_id):
    task = Task.query.get(task_id)
    employees = Employee.query.all()
    if not task:
        flash("Task not found.")
        return redirect(url_for("main.index"))
    return render_template("edit_task.html", task=task, employees=employees)

@main.route("/update_task/<int:task_id>", methods=["POST"])
def update_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        flash("Task not found.")
        return redirect(url_for("main.index"))
    
    # Actualizar los campos de la tarea
    task.title = request.form.get("title")
    task.description = request.form.get("description")
    task.status = request.form.get("status")
    task.deadline = datetime.strptime(request.form.get("deadline"), "%Y-%m-%d").date()
    employee_id = request.form.get("employee_id")
    task.employee_id = employee_id if employee_id else None
    
    db.session.commit()
    flash("Task updated successfully!")
    return redirect(url_for("main.index"))
