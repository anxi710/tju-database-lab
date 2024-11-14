<template>
    <!-- 找回密码 -->
    <div class="forgetBox">

        <div class="head">同舟共济外卖平台</div>

        <div>

            <el-form label-width="60px" class="forgetForm" :model="forgetForm"
                :rules="forgetRules" ref="forgetForm">

                <el-form-item prop="telephone">
                    <el-input prefix-icon="el-icon-phone" v-model="forgetForm.telephone" spellcheck="false"
                        placeholder="电话号码" clearable />
                </el-form-item>

                <el-form-item prop="password">
                    <el-input prefix-icon="el-icon-lock" v-model="forgetForm.password" show-password spellcheck="false"
                        placeholder="新密码" />
                </el-form-item>

                <el-form-item prop="confirmPassword">
                    <el-input prefix-icon="el-icon-check" v-model="forgetForm.confirmPassword" show-password
                        spellcheck="false" placeholder="确认密码" />
                </el-form-item>

            </el-form>

            <div>
                <el-button class="btns" @click="doubleCheck()">修改</el-button>
            </div>

            <div style="text-align: center;">
                <span @click="handleClick('loginBox')"
                    style="color: rgb(0, 0, 0, 0.5); font-size: 16px; cursor:pointer;">登录</span>
            </div>

        </div>

        <!-- 二次确认 -->
        <el-dialog title="请再次确认信息！" :visible.sync="dialogVisible" width="400px"
            @close="handleCancel()" append-to-body>
            <span>您确定修改密码吗？</span>
            <span slot="footer" class="dialog-footer">
                <el-button @click="handleCancel">取消</el-button>
                <el-button type="primary" @click="handleConfirm">确认</el-button>
            </span>
        </el-dialog>

    </div>

</template>

<script>
import { checkValidMobile, checkValidPassword} from '@/utils/validate.js'

export default {
    name: 'forgetBox',
    data() {
        var checkConfirmPassword = (rule, value, callback) => {
            if (value == this.forgetForm.password) {
                return callback();
            }
            callback(new Error('两次输入密码不一致!'));
        };
        return {
            dialogVisible: false,
            forgetForm: {
                telephone: '',
                password: '',
                confirmPassword: ''
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
            this.$emit('changeBox', box)
        },
        // 提交按钮点击时，触发验证并显示确认对话框
        doubleCheck() {
            this.$refs.forgetForm.validate(valid => {
                if (valid) {
                    this.dialogVisible = true;  // 显示确认对话框
                } else {
                    return;
                }
            });
        },

        // 取消操作，关闭确认对话框
        handleCancel() {
            this.dialogVisible = false;
        },

        // 确认操作，关闭确认对话框并提交修改密码请求
        handleConfirm() {
            this.dialogVisible = false;
            this.forget();
        },

        // 提交修改密码请求
        forget() {
            this.$axios.post("/api/user/forget", this.forgetForm).then((res) => {
                console.log(res.status);
                //200修改成功
                if (res.data.code != 200) {
                    return this.$message({
                        message: res.data.msg,
                        type: 'error '
                    })
                } else {
                    this.$message({
                        message: res.data.msg,
                        type: 'success'
                    })
                }
            })
        },
    }
}
</script>

<style lang="less" scoped>
@import "@/assets/css/loginRegister.css";

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
</style>