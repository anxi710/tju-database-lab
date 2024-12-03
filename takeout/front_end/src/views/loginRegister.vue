<template>

    <el-container class="container">

        <el-header class="header">
            <img src="../assets/images/logo2.png" height=35px alt="同济大学"
                style="padding-left: 10px" />
        </el-header>

        <el-main>
            <!-- 登录表单 -->
            <loginBox v-if="curBox === 'loginBox'" @changeBox="changeBox" />

            <!-- 注册表单 -->
            <registerBox v-else-if="curBox === 'registerBox'" @changeBox="changeBox" />

            <!-- 找回密码 -->
            <forgetBox v-else @changeBox="changeBox" />
        </el-main>

    </el-container>

</template>

<script>
import loginBox from '@/components/loginRegister/login.vue'
import registerBox from '@/components/loginRegister/register.vue'
import forgetBox from '@/components/loginRegister/forget.vue'

export default {
    name: 'loginRegister',
    components: {
        loginBox,
        registerBox,
        forgetBox
    },
    data() {
        return {
            curBox: 'loginBox'
        }
    },
    methods: {
        changeBox(box) {
            console.log(box);
            this.curBox = box;
        }
    }
}
</script>

<style lang="less" scoped>
.container {
    height: 100%;
    width: 100%;
    background-color: #FCFFE0;
    background-image: url('../assets/images/background.png');
    // 居中显示
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

.header {
    width: 100%;
    height: 55px;
    background-color: white;
    display: flex;
    align-items: center;
}
</style>