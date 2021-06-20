(function($) {
    $(document).ready(function () {
        $("#get_update_password").click(function() {
            var result = prompt('Введите пароль', '');
            if(result === ''){
                alert('Нельзя установить пустый пароль!');
                return;
            }else if(result.length !== 8){
                alert('Длина пароля = 8 цифр!');
                return;
            }
            var id = $(this).attr('data-user-id');
            $.ajax(
            {
                type: "get",
                url: "/admin/psychological_tests/userextended/"+id+"/update_password/?password=" + result,
                data: {},
                success: function (result) {
                    alert(result);
                }
            })}
        );
    });
})(django.jQuery);
