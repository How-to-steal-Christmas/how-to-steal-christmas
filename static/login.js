function login() {
    let email = $('#email').val();
    let password = $('#password').val();

    $.ajax({
        type: "POST",
        url: "/user/login",
        data: {email_give: email, password_give: password},
        success: function (response) {
            if (response['result'] === 'success') {
                $.cookie('mytoken', response['token']);
                alert('로그인 완료!')
                window.location.href = '/'
            } else {
                alert(response['msg'])
            }
        }
    });
}