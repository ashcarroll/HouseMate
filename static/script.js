document.addEventListener('DOMContentLoaded', initialise);

function initialise() {
    let completeTask = document.querySelectorAll('.complete-task-form')

    completeTask.forEach(function(form) {
        form.addEventListener('submit', formSubmit);
    });
}

function formSubmit(event) {
    event.preventDefault();

    let form = event.target;
    removeCompletedTask(form);
}

function removeCompletedTask(form) {
    let doneTask = form.closest('li');
    if (doneTask) {
        doneTask.remove();
    }
}