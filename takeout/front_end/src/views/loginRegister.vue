<template>
    <div class="container">

        <!-- 登录表单 -->
        <div class="loginBox" v-if="curBox == 'loginBox'">

            <div class="head">同舟共济外卖平台</div>

            <div>

                <el-form label-width="100px" class="loginForm" :model="loginForm" :rules="loginRules" ref="loginForm">
                    <!-- 用户名 -->
                    <el-form-item prop="username" label="用户名">
                        <el-input v-model="loginForm.username" spellcheck="false" placeholder="用户名"/>
                    </el-form-item>
                    <!-- 密码 -->
                    <el-form-item prop="password" label="密码">
                        <el-input v-model="loginForm.password" show-password spellcheck="false" placeholder="密码"/>
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

        <!-- 注册表单 -->
        <div class="registerBox" v-if="curBox == 'registerBox'">

            <div class="head">同舟共济外卖平台</div>

            <div>

                <el-form label-width="100px" class="reg_form" :model="registerForm"
                    :rules="registerRules" ref="registerForm">

                    <el-form-item prop="username" label="用户名">
                        <el-input v-model="registerForm.username" spellcheck="false"/>
                    </el-form-item>

                    <el-form-item prop="username" label="电话">
                        <el-input v-model="registerForm.telephone" spellcheck="false"/>
                    </el-form-item>

                    <el-form-item prop="password" label="密码">
                        <el-input v-model="registerForm.password" show-password
                            spellcheck="false" placeholder="6 - 12 位大小写字母或数字"/>
                    </el-form-item>

                    <el-form-item prop="confirmPassword" label="确认密码">
                        <el-input v-model="registerForm.confirmPassword" spellcheck="false" placeholder="再次输入密码"/>
                    </el-form-item>

                    <el-form-item prop="verificationCode" label="验证码">

                        <el-input v-model="registerForm.vercode" spellcheck="false"
                            placeholder="验证码" style="width:200px"/>

                        <span style="width:120px;font-size: 16px;cursor: pointer;" @click="send_vercode_pre()"
                            v-show="getcode_show">
                            获取验证码
                        </span>

                        <span style="width:120px;font-size: 16px;cursor: pointer;" v-show="!getcode_show">
                            {{ time_count }}s后重新获取
                        </span>
                    </el-form-item>

                </el-form>

                <div>
                    <el-button type="primary" @click="register()">注册</el-button>
                </div>

                <div>
                    <span @click="changeBox('loginBox')"
                        style="text-align: center; opacity: 0.5; font-size: 16px; cursor:pointer;">登录</span>
                </div>
            </div>
        </div>

        <!-- 找回密码 -->
        <div class="forgetBox" v-if="curBox == 'forgetBox'">
            <div class="head">同舟共济外卖平台</div>
            <div>
                <el-form class="reg_form" :model="forgetForm" :rules="forgetRules" ref="forgetForm">

                    <el-form-item prop="telephone">
                        <el-input prefix-icon="iconfont icon-password" v-model="forgetForm.telephone"
                            spellcheck="false" placeholder="手机号码"/>
                    </el-form-item>

                    <!-- 密码 -->
                    <el-form-item prop="password">
                        <el-input prefix-icon="iconfont icon-password" v-model="reg_form.password" show-password
                            spellcheck="false" placeholder="新密码"></el-input>
                    </el-form-item>

                    <el-form-item prop="vercode">
                        <el-input v-model="forgetForm.vercode" spellcheck="false" placeholder="验证码" style="width:230px">
                        </el-input>
                        <span style="width:120px;font-size: 16px;cursor: pointer;" @click="send_vercode_pre()"
                            v-show="getcode_show">
                            获取验证码
                        </span>

                        <span style="width:120px;font-size: 16px;cursor: pointer;" v-show="!getcode_show">
                            {{ time_count }}s后重新获取
                        </span>
                    </el-form-item>
                    <!-- 按钮 -->
                    <el-form-item class="btns">
                        <el-button type="primary" @click="findback()">确认修改</el-button>
                    </el-form-item>

                </el-form>
                <div>
                    <div>
                        <span @click="changeBox('loginBox')"
                            style="margin-left:210px;color: #000;opacity: .5;font-weight: 400;font-size: 16px;cursor:pointer;">登录</span>
                    </div>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
export default {
    name: 'loginRegister',
    data() {
        var checkValidPassword = (rule, value, callback) => {
            const regexRule = /^[a-zA-Z1-9]{6,12}$/;
            if (regexRule.test(value)) {
                return callback() // 合法的密码
            }
            callback(new Error('密码格式不正确，密码必须由 6-12 位大小写字母或数字组成'))
        };
        var checkValidMobile = (rule, value, cb) => {
            const regMobile = /^(0|86|17951)?(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$/;
            if (regMobile.test(value)) {
                // 合法的手机号码
                return cb()
            }
            cb(new Error('手机号码格式不正确'))
        };
        var checkConfirmPassword = (rule, value, callback) => {
            if (value === this.registerForm.password) {
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
                password: '',
                confirmPassword: '',
                telephone: '',
                verificationCode: ''
            },
            forgetForm: {
                telephone: '',
                password: '',
                confirmPassword: '',
                verificationCode: '',
            },
            loginRules: {
                username: [{
                        required: true,
                        message: '请输入用户名',
                        trigger: 'blur'
                }],
                password: [ {
                        required: true,
                        message: '请输入密码',
                        trigger: 'blur'
                }]
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
                        message: '请绑定手机号',
                        trigger: 'blur'
                    },
                    {
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
                        trigger: 'blur'
                    },
                    {
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
                ]
            },
        }
    },
    methods: {
        findback(){
            this.$refs.findback_form.validate(valid => {
                if (!valid)
                    return;
                else if(this.findback_form.vercode=='')
                    return;
                else{
                    console.log(111);
                }
            })
        },
        register(){
            this.$refs.reg_form.validate(valid => {
                if (!valid)
                    return;
                else{
                    if(this.reg_form.vercode=='')
                        return;
                    else{
                        this.$axios.request({
                            method:'POST',
                            url:'/api/user/register/test',
                            data:{
                                username:this.reg_form.username,
                                password:this.reg_form.password,
                                vercode:this.reg_form.vercode,
                                telephone:this.reg_form.telephone
                            }
                        }).then((res)=>{
                            // console.log(res.status);
                            if(res.data.status==200)
                            {
                                this.$message({
                                message: '注册成功',
                                type: 'success'
                                })
                            this.target = 1;
                            // 页面变为登录页面
                            }else{
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
            this.curBox = box;
        },
        login() {
            this.$refs.login_form.validate(valid => {
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

        },

        // 获取验证码
        send_vercode_pre() {
            this.$refs.reg_form.validate(valid => {
                if (!valid) {
                    return;
                }
                else {
                    this.send_vercode();
                    // this.set_interval();
                }
            })
        },
        send_vercode() {
            this.$axios.request({
                method: 'POST',
                url: "/api/user/register/send_sms",
                data: {
                    telephone: this.reg_form.telephone
                }
            }).then(() => {
                this.$message({
                        message: '验证码发送成功',
                        type: 'success'
                    })
            })
        },
        set_interval() {
            const TIME_COUNT = 60;
            if (!this.timer) {
                this.time_count = TIME_COUNT;
                this.getcode_show = false;
                this.timer = setInterval(() => {
                    if (this.time_count > 0 && this.time_count <= TIME_COUNT) {
                        this.time_count--;
                    } else {
                        this.getcode_show = true;
                        clearInterval(this.timer);
                        this.timer = null;
                    }
                }, 1000);
            }
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
    color:#97D9E1;
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

.btns {
    margin: 0px 0px 20px 0px;

    background: #C2D9FF;

    position: relative;
    left: 50%;
    transform: translateX(-50%);
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
    height: 360px;
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

.input {
    width: 350px;
    height: 50px;
    margin-left: 50px;
}

.el-form-item {
    width: 90%;
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