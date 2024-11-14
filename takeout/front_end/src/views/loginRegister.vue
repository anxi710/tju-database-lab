<template>

    <div class="container">

        <!-- 登录表单 -->
        <loginBox v-if="curBox === 'loginBox'" @changeBox="changeBox" />

        <!-- 注册表单 -->
        <registerBox v-else-if="curBox === 'registerBox'" @changeBox="changeBox" />

        <!-- 找回密码 -->
        <forgetBox v-else @changeBox="changeBox" />

    </div>

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
}
</style>