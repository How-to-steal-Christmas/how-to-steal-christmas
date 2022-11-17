function register() {

    let username = $('#username').val()
    let email = $('#email').val()
    let password = $('#password').val()

    console.log(username, email, password);
    $.ajax({
        type: "POST",
        url: "/user/register",
        data: {username_give: username, email_give: email, pw_give: password},
        success: function (response) {
            console.log(response)
            if (response['result'] === 'success') {
                alert("회원가입 성공!");
                window.location.href = '/login'
            } else {
                alert("회원가입 실패")
                window.location.reload();
            }
        }
    });
}
