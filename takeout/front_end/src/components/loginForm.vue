<template>
    <!-- 登录表单 -->
    <div class="login_box">
        <div class="head">同舟共济外卖平台</div>
        <div>
            <el-form label-width="0" class="login_form" :model="login_form" :rules="login_rules" ref="login_form">
                <!-- 用户名 -->
                <el-form-item prop="username">
                    <el-input v-model="login_form.username" spellcheck="false" placeholder="用户名" />
                </el-form-item>
                <!-- 密码 -->
                <el-form-item prop="password">
                    <el-input v-model="login_form.password" show-password spellcheck="false" placeholder="密码" />
                </el-form-item>
                <!-- 按钮 -->
                <el-form-item class="btns">
                    <el-button type="primary" @click="llogin()">登录</el-button>
                </el-form-item>
            </el-form>

            <div>
                <div class="operate">
                    <span id="op1" @click="change(2)">注册</span>
                    <span id="op2" @click="change(3)">忘记密码</span>
                </div>
            </div>

        </div>
    </div>
</template>

<script>
export default {
    name: 'loginForm',
    data() {
        var checkPassword = (rule, value, cb) => {
            const regPassword = /(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).{6,12}$/;
            if (regPassword.test(value)) {
                // 合法的手机号码
                return cb()
            }
            cb(new Error('包含大写字母、小写字母、数字，长度在6-12位之间'))
        };
        var checkMobile = (rule, value, cb) => {
            const regMobile = /^(0|86|17951)?(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$/;
            if (regMobile.test(value)) {
                // 合法的手机号码
                return cb()
            }
            cb(new Error('手机号码格式不正确'))
        };
        return {
            getcode_show: true,
            time_count: '',
            timer: null,
            login_form: {
                username: '',
                password: '',
            },
            login_rules: {
                username: [
                    {
                        required: true,
                        message: '请输入电话',
                        trigger: 'blur'
                    },
                    {
                        validator: checkMobile,
                        trigger: 'blur'
                    }
                ],
                password: [{
                    required: true,
                    message: '请输入密码',
                    trigger: 'blur'
                }]
            }
        }
    },
    methods: {
        llogin() {
            this.$refs.login_form.validate(valid => {
                if (!valid)
                    return;
                else //验证通过再发送请求
                    this.login();
            })
        },
        async login() {
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

.login_box {
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

.btns {
    text-align: center;
}

.operate {
    text-align: center;
    color: #000;
    opacity: .5;
    font-weight: 400;
    font-size: 16px;
    margin-left: 28px;
}

#op1 {
    padding-left: 15px;
    padding-right: 30px;
    border-right: 1px solid #bdb9b9;
    cursor: pointer;
}

#op2 {
    padding-left: 30px;
    padding-right: 15px;
    cursor: pointer;
}
</style>