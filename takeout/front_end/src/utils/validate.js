export function checkValidPassword(rule, value, callback) {
    const regexRule = /^[a-zA-Z1-9]{6,12}$/;
    if (regexRule.test(value)) {
        return callback() // 合法的密码
    }
    callback(new Error('密码必须由 6 - 12 位大小写字母或数字组成'))
}

export function checkValidMobile(rule, value, callback) {
    const regMobile = /^(0|86|17951)?(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$/;
    if (regMobile.test(value)) {
        // 合法的手机号码
        return callback()
    }
    callback(new Error('手机号码格式不正确'))
}
