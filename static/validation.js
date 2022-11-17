let elInputUsername = document.querySelector('#username')
let elInputEmail = document.querySelector('#email')
let elInputPassword = document.querySelector('#password')
let elInputPasswordConfirm = document.querySelector('#password-confirm')
let elJoinbutton = document.querySelector('#register-button')

let elFailuremessage = document.querySelector('.failure-message')
let elSuccessmessage = document.querySelector('.success-message')
let elFailurePwmessage = document.querySelector('.failure-password-message')
let elSuccessmMailmessage = document.querySelector('.success-mail-message')
let elFailureMailmessage = document.querySelector('.failure-mail-message')
let elMismatchmessage = document.querySelector('.mismatch-message')

elJoinbutton.disabled = true;

// Validation Check
const IsValidateEmail = (elInputEmail) => {
    return /^[A-Za-z0-9.\-_]+@([A-Za-z0-9-]+\.)+[A-Za-z]{2,6}$/.test(elInputEmail)
} // E-mail 양식 검증
const IsValidateName = (elInputUsername) => {
    return /^[a-zA-Zㄱ-힣0-9-_.]{2,12}$/.test(elInputUsername)
} // 한글, 영문, 특수문자 (- _ .) 포함한 2 ~ 12글자 닉네임
const IsValidatePw = (elInputPassword) => {
    return /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/.test(elInputPassword)
} // 최소 8 자, 하나 이상의 문자, 하나의 숫자 및 하나의 특수 문자 정규식


elInputUsername.onkeyup = function () {
    if (isMoreThan2Length(elInputUsername.value) && /^[a-zA-Zㄱ-힣0-9-_.]{2,12}$/.test(elInputUsername.value)) {
        elSuccessmessage.classList.remove('hide')
        elFailuremessage.classList.add('hide')
    } else {
        elSuccessmessage.classList.add('hide')
        elFailuremessage.classList.remove('hide')
    }
}

elInputEmail.onkeyup = function () {
    if (/^[A-Za-z0-9.\-_]+@([A-Za-z0-9-]+\.)+[A-Za-z]{2,6}$/.test(elInputEmail.value)){
        elSuccessmMailmessage.classList.remove('hide')
        elFailureMailmessage.classList.add('hide')
    } else {
        elSuccessmMailmessage.classList.add('hide')
        elFailureMailmessage.classList.remove('hide')
    }
}

elInputPassword.onkeyup = function () {
    if (checkSpace(elInputPassword.value)){
        elFailurePwmessage.classList.remove('hide')
    } else {
        elFailurePwmessage.classList.add('hide')
    }
}

elInputPasswordConfirm.onkeyup = function () {
    if (isMatch(elInputPassword.value, elInputPasswordConfirm.value)) {
        elMismatchmessage.classList.add('hide')
    } else {
        elMismatchmessage.classList.remove('hide')
    }
}

elInputUsername.addEventListener('keyup', button)
elInputPassword.addEventListener('keyup', button)
elInputPasswordConfirm.addEventListener('keyup', button)

//비밀번호 값과 비밀번호 확인값이 일치하는지 판별하는 함수
function isMatch(password1, password2) {
    if (password1 === password2) {
        return true;
    } else {
        return false;
    }
}

function isMoreThan2Length(value) {
    return value.length >= 2
}

function button() {
    switch (!(elInputUsername.value && elInputPassword.value && elInputPasswordConfirm.value)) {
        case true :
            elJoinbutton.disabled = true;
            break;
        case false :
            elJoinbutton.disabled = false;
            break;
    }
}

function checkSpace(str) {
    if (str.search(/\s/) != -1) {
        return true;
    } else {
        return false;
    }
}
