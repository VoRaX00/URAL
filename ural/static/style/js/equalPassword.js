document.addEventListener('DOMContentLoaded', function() {
    var form = document.querySelector('form');
    var password1Input = document.getElementById('exampleInputPassword1');
    var password2Input = document.getElementById('exampleInputPassword2');

    form.addEventListener('submit', function(event) {
        if (password1Input.value !== password2Input.value) {
            alert('Пароли не совпадают');
            event.preventDefault(); // Остановить отправку формы
        }
    });
});