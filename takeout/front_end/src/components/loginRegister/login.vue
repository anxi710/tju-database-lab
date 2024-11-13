<template>
    <!-- 登录表单 -->
    <div class="loginBox" v-if="curBox == 'loginBox'">

        <div class="head">同舟共济外卖平台</div>

        <div>

            <el-form label-width="60px" class="loginForm" :model="loginForm" :rules="loginRules" ref="loginForm">
                <!-- 用户名 -->
                <el-form-item prop="username">
                    <el-input prefix-icon="el-icon-user" v-model="loginForm.username" spellcheck="false"
                        placeholder="用户名" clearable />
                </el-form-item>
                <!-- 密码 -->
                <el-form-item prop="password">
                    <el-input prefix-icon="el-icon-lock" v-model="loginForm.password" spellcheck="false"
                        placeholder="密码" show-password />
                </el-form-item>
            </el-form>

            <div>
                <el-button class="btns" @click="login()">登录</el-button>
            </div>

            <div class="otherBoxes">
                <span id="registerBoxBtn" @click="changeBox('registerBox')">注册</span>
                <span style="border-left: 1px solid rgb(0, 0, 0, 0.5)"></span>
                <span id="forgetBoxBtn" @click="changeBox('forgetBox')">忘记密码</span>
            </div>

        </div>

    </div>
</template>

<script>
export default {
    name: 'loginBox',
    data() {
        var checkValidPassword = (rule, value, callback) => {
            const regexRule = /^[a-zA-Z1-9]{6,12}$/;
            if (regexRule.test(value)) {
                return callback() // 合法的密码
            }
            callback(new Error('密码必须由 6 - 12 位大小写字母或数字组成'))
        };
        var checkValidMobile = (rule, value, callback) => {
            const regMobile = /^(0|86|17951)?(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$/;
            if (regMobile.test(value)) {
                // 合法的手机号码
                return callback()
            }
            callback(new Error('手机号码格式不正确'))
        };
        var checkConfirmPassword = (rule, value, callback) => {
            if ((this.curBox == 'registerBox' && value === this.registerForm.password) ||
                (this.curBox == 'forgetBox' && value === this.forgetForm.password)) {
                return callback()
            }
            callback(new Error('两次输入密码不一致'))
        };
        return {
            getcode_show: true,
            time_count: '',
            timer: null,
            curBox: 'loginBox',
            loginForm: {
                username: '',
                password: '',
            },
            registerForm: {
                username: '',
                telephone: '',
                password: '',
                confirmPassword: ''
            },
            forgetForm: {
                telephone: '',
                password: '',
                confirmPassword: ''
            },
            loginRules: {
                username: [{
                    required: true,
                    message: '请输入用户名',
                    trigger: 'blur'
                }],
                password: [
                    {
                        required: true,
                        message: '请输入密码',
                        trigger: 'blur'
                    },
                    {
                        validator: checkValidPassword,
                        trigger: 'blur'
                    }
                ]
            },
            registerRules: {
                username: [{
                    required: true,
                    message: '请设置用户名',
                    trigger: 'blur'
                }],
                password: [
                    {
                        required: true,
                        message: '请设置密码',
                        trigger: 'blur'
                    },
                    {
                        validator: checkValidPassword,
                        trigger: 'blur'
                    }
                ],
                confirmPassword: [
                    {
                        required: true,
                        message: '请再次输入密码',
                        trigger: 'blur'
                    },
                    {
                        validator: checkConfirmPassword,
                        trigger: 'blur'
                    }
                ],
                telephone: [
                    {
                        required: true,
                        message: '请绑定电话',
                        validator: checkValidMobile,
                        trigger: 'blur'
                    }
                ]
            },
            forgetRules: {
                telephone: [
                    {
                        required: true,
                        message: '请输入电话',
                        validator: checkValidMobile,
                        trigger: 'blur'
                    }
                ],
                password: [
                    {
                        required: true,
                        message: '请输入密码',
                        trigger: 'blur'
                    }
                ],
                confirmPassword: {
                    required: true,
                    message: '请再次输入密码',
                    validator: checkConfirmPassword,
                    trigger: 'blur'
                }
            }
        }
    },
    methods: {
        // 提交按钮点击时，触发验证并显示确认对话框
        doubleCheck() {
            console.log(this.forgetForm.password, this.forgetForm.confirmPassword);
            this.$refs.forgetForm.validate(valid => {
                if (valid) {
                    this.dialogVisible = true;  // 显示确认对话框
                } else {
                    this.$message.error('表单验证失败');
                }
            });
        },

        // 取消操作，关闭确认对话框
        handleCancel() {
            this.dialogVisible = false;
        },

        register() {
            this.$refs.reg_form.validate(valid => {
                if (!valid)
                    return;
                else {
                    if (this.reg_form.vercode == '')
                        return;
                    else {
                        this.$axios.request({
                            method: 'POST',
                            url: '/api/user/register/test',
                            data: {
                                username: this.reg_form.username,
                                password: this.reg_form.password,
                                vercode: this.reg_form.vercode,
                                telephone: this.reg_form.telephone
                            }
                        }).then((res) => {
                            // console.log(res.status);
                            if (res.data.status == 200) {
                                this.$message({
                                    message: '注册成功',
                                    type: 'success'
                                })
                                this.target = 1;
                                // 页面变为登录页面
                            } else {
                                this.$message({
                                    message: res.data.msg,
                                    type: 'error'
                                })
                            }
                        })
                    }
                }
            })
        },
        changeBox(box) {
            console.log(box);
            // 切换当前表单
            this.curBox = box;
        },
        login() {
            this.$refs.loginForm.validate(valid => {
                if (!valid)
                    return;
                else //验证通过再发送请求
                    this.login1();
            })


        },
        async login1() {

            this.$axios.post("/api/user/login", this.login_form).then((res) => {
                console.log(res.status);
                //200登录成功
                if (res.data.code != 200) {
                    return this.$message({
                        message: res.data.msg,
                        type: 'error '
                    })
                } else {
                    this.$message({
                        message: '登录成功',
                        type: 'success'
                    })

                    window.localStorage.setItem("token", res.data.token);

                    if (res.data.role == 0)
                        this.$router.push('/user')
                    else
                        this.$router.push('/manage')
                }
            }).catch(() => {
                // console.log(res.response.data);
                this.$message({
                    message: "网络故障",
                    type: 'error'
                })
            })

        }
    }
}
</script>

<style lang="less" scoped>
.container {
    height: 100%;
    width: 100%;
    background-color: #FCFFE0;
}

.head {
    text-align: center;
    height: 50px;
    line-height: 50px;
    font-size: larger;
    font-size: 23px;
    color: #97D9E1;
    padding: 7px;
}

.loginBox {
    height: 300px;
    width: 450px;

    /* 设置窗口为毛玻璃效果 */
    background: rgba(255, 255, 255, 0.75);
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    -webkit-backdrop-filter: blur(4px);
    backdrop-filter: blur(4px);
    border-radius: 20px;
    border: 1px solid rgba(137, 160, 163, 0.18);

    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}

.registerBox {
    height: 420px;
    width: 450px;

    /* 设置窗口为毛玻璃效果 */
    background: rgba(255, 255, 255, 0.75);
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    -webkit-backdrop-filter: blur(4px);
    backdrop-filter: blur(4px);
    border-radius: 20px;
    border: 1px solid rgba(137, 160, 163, 0.18);

    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}

.forgetBox {
    height: 350px;
    width: 450px;

    /* 设置窗口为毛玻璃效果 */
    background: rgba(255, 255, 255, 0.75);
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    -webkit-backdrop-filter: blur(4px);
    backdrop-filter: blur(4px);
    border-radius: 20px;
    border: 1px solid rgba(137, 160, 163, 0.18);

    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}

.btns {
    margin: 0px 0px 15px 0px;

    background: #C2D9FF;

    position: relative;
    left: 50%;
    transform: translateX(-50%);

    font-family: '霞鹜文楷'
}

.el-form-item {
    width: 87%;
}

.otherBoxes {
    text-align: center;
    color: #000;
    opacity: 0.5;
    font-weight: 400;
    font-size: 16px;
    margin-left: 28px;
}

#registerBoxBtn {
    margin-left: 15px;
    margin-right: 30px;
    cursor: pointer;
}

#forgetBoxBtn {
    margin-left: 30px;
    margin-right: 15px;
    cursor: pointer;
}
</style>