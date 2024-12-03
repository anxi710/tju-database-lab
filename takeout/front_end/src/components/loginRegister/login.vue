<template>
    <!-- 登录表单 -->
    <div class="loginBox">

        <div class="head">黄渡外卖</div>

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
                <span id="registerBoxBtn" @click="handleClick('registerBox')">注册</span>
                <span style="border-left: 1px solid rgb(0, 0, 0, 0.8)"></span>
                <span id="forgetBoxBtn" @click="handleClick('forgetBox')">忘记密码</span>
            </div>

        </div>

    </div>
</template>

<script>
import { checkValidPassword } from '@/utils/validate.js'

export default {
    name: 'loginBox',
    data() {
        return {
            loginForm: {
                username: '',
                password: '',
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
            }
        }
    },
    methods: {
        handleClick(box) {
            this.$emit('changeBox', box)
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
            this.$axios.post("/api/user/login", this.loginForm).then((res) => {
                console.log(res.status);
                // 200 登录成功
                if (res.data.code != 200) {
                    return this.$notify({
                        title: '错误',
                        message: res.data.msg,
                        type: 'error',
                        duration: 1000
                    })
                } else {
                    this.$notify({
                        title: '成功',
                        message: '登录成功',
                        type: 'success',
                        duration: 1000
                    })

                    // 将用户名和角色存入localStorage
                    window.localStorage.setItem('username', this.loginForm.username);
                    window.localStorage.setItem('role', res.data.role);

                    console.log(window.localStorage.getItem('username'));
                    console.log(window.localStorage.getItem('role'));

                    // 暂停一秒后跳转
                    setTimeout(() => {
                        if (res.data.role == 'user')
                            this.$router.push('/user')
                        else
                            this.$router.push('/admin')
                    }, 1000);
                }
            }).catch(() => {
                // console.log(res.response.data);
                this.$notify.error({
                    title: '错误',
                    message: "网络故障"
                })
            })
        }
    }
}
</script>

<style lang="less" scoped>
@import "@/assets/css/loginRegister.css";

.loginBox {
    height: 300px;
    width: 450px;

    /* 设置窗口为毛玻璃效果 */
    background: rgba(255, 255, 255, 0.82);
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

.otherBoxes {
    text-align: center;
    color: black;
    opacity: 0.6;
    font-weight: 400;
    font-size: 14px;
    margin-left: 28px;

    // 鼠标悬停时变蓝
    span:hover {
        color: #409EFF;
    }
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