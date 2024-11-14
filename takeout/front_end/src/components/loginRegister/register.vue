<template>
    <!-- 注册表单 -->
    <div class="registerBox">

        <div class="head">同舟共济外卖平台</div>

        <div>

            <el-form label-width="60px" class="registerForm" :model="registerForm"
                :rules="registerRules" ref="registerForm">

                <el-form-item prop="username">
                    <el-input v-model="registerForm.username" spellcheck="false" prefix-icon="el-icon-user"
                        placeholder="用户名" />
                </el-form-item>

                <el-form-item prop="telephone">
                    <el-input v-model="registerForm.telephone" spellcheck="false" prefix-icon="el-icon-phone"
                        placeholder="电话号码" />
                </el-form-item>

                <el-form-item prop="password">
                    <el-input v-model="registerForm.password" show-password spellcheck="false"
                        placeholder="6 - 12 位大小写字母或数字" prefix-icon="el-icon-lock" />
                </el-form-item>

                <el-form-item prop="confirmPassword">
                    <el-input v-model="registerForm.confirmPassword" spellcheck="false" show-password
                        prefix-icon="el-icon-check" placeholder="确认密码" />
                </el-form-item>

            </el-form>

            <div>
                <el-button class="btns" @click="doubleCheck">注册</el-button>
            </div>

            <div class="loginBtn">
                <span @click="handleClick('loginBox')">登录</span>
            </div>

            <!-- 二次确认 -->
            <el-dialog title="请再次确认信息！" :visible.sync="dialogVisible" width="400px"
                @close="handleCancel()" append-to-body>
                <span>您确定注册吗？</span>
                <span slot="footer" class="dialog-footer">
                    <el-button @click="handleCancel">取消</el-button>
                    <el-button type="primary" @click="handleConfirm">确认</el-button>
                </span>
            </el-dialog>

        </div>

    </div>

</template>

<script>
import {checkValidMobile, checkValidPassword} from '@/utils/validate.js'

export default {
    name: 'registerBox',
    data() {
        var checkConfirmPassword = (rule, value, callback) => {
            if (value == this.registerForm.password) {
                return callback();
            }
            callback(new Error('两次输入密码不一致!'));
        };
        return {
            dialogVisible: false,
            registerForm: {
                username: '',
                telephone: '',
                password: '',
                confirmPassword: ''
            },
            registerRules: {
                username: [{
                    required: true,
                    message: '请设置用户名',
                    trigger: 'blur'
                }],
                telephone: [
                    {
                        required: true,
                        message: '请绑定电话',
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
                ]
            }
        }
    },
    methods: {
        handleClick(box) {
            this.$emit('changeBox', box); // 触发父组件的 changeBox 事件
        },
        // 提交按钮点击时，触发验证并显示确认对话框
        doubleCheck() {
            this.$refs.registerForm.validate(valid => {
                if (valid) {
                    this.dialogVisible = true;  // 显示确认对话框
                } else {
                    return;
                }
            })
        },
        // 确认对话框的取消按钮
        handleCancel() {
            this.dialogVisible = false;
        },
        // 确认对话框的确认按钮
        handleConfirm() {
            this.dialogVisible = false;
            this.register();
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
                                // 页面变为登录页面
                                this.$emit('changeBox', 'loginBox')
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
        }
    }
}
</script>

<style lang="less" scoped>
@import "@/assets/css/loginRegister.css";

.registerBox {
    height: 420px;
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
</style>