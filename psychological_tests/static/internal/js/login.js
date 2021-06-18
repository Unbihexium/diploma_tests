$(document).ready(function (){
    $('#loginButton').click(
        function (e) {
            let username =$('#username').val();
            let password =$('#password').val();

            if (username === '' || password === '') {
                // TODO: Сообщение  об ошибке
                return
            }

            $.ajax({
                type: 'POST',
                url: '/login/',
                beforeSend: function (request) {
                    request.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                },
                data: {
                    'username': username,
                    'password': password
                },
                success: function () {
                    window.location.href = '/';
                }
            })
        }
    )
})
