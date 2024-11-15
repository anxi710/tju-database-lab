<template>
    <div style="width: 100%; height: 100vh;">

        <div class="topBar">

            <div id="logoBox">
                <img src="../assets/images/logo.png" height="35px"
                    alt="同济大学" style="padding-left: 10px" />
                <span style="color: #05d4eb; font-size: 20px; padding-left: 5px">
                    同舟共济外卖平台
                </span>
            </div>

            <p id="greetings">😃Hi {{this.username}} ~ 今天吃点什么？😉</p>

            <p id="mode">用户模式</p>

        </div>

        <div class="body">

            <div class="menuBar">
                <el-menu default-active="1" class="navigationMenu"
                    background-color="#FFEAC5" text-color="black"
                    active-text-color="#FFB200" @select="handleSelect">
                    <el-menu-item index="1">
                        <i class="el-icon-food"></i>
                        <span slot="title" class="menuItem">美食广场</span>
                    </el-menu-item>

                    <el-submenu index="2">
                        <template slot="title">
                            <i class="el-icon-shopping-cart-2"></i>
                            <span class="menuItem">订单</span>
                        </template>
                        <el-menu-item-group>
                            <el-menu-item index="3" class="menuItem">待收货订单</el-menu-item>
                            <el-menu-item index="4" class="menuItem">已完成订单</el-menu-item>
                            <el-menu-item index="5" class="menuItem">未发货订单</el-menu-item>
                        </el-menu-item-group>
                    </el-submenu>

                    <el-menu-item index="6">
                        <template slot="title">
                            <i class="el-icon-star-off"></i>
                            <span class="menuItem">收藏</span>
                        </template>
                    </el-menu-item>

                    <el-menu-item index="7">
                        <template slot="title">
                            <i class="el-icon-chat-line-square"></i>
                            <span class="menuItem">评论中心</span>
                        </template>
                    </el-menu-item>

                    <el-menu-item index="8">
                        <template slot="title">
                            <i class="el-icon-house"></i>
                            <span class="menuItem">个人中心</span>
                        </template>
                    </el-menu-item>

                </el-menu>
            </div>

            <div class="main" style="padding-left: 20px;">
                <div id="usershop" v-show="active == 1">
                    <shopFood></shopFood>
                </div>

                <!-- <div id="userfinished" v-show="active == 3">
                    <userfinished></userfinished>
                </div>

                <div id="usersending" v-show="active == 4">
                    <usersending></usersending>
                </div>

                <div id="userunsend" v-show="active == 5">
                    <userunsend></userunsend>
                </div>

                <div id="indimag" v-show="active == 6">
                    <indimsg></indimsg>
                </div>

                <div id="changepwd" v-show="active == 7">
                    <changepwd></changepwd>
                </div> -->

            </div>
        </div>
    </div>
</template>

<script>
import shopFood from '@/components/userPage/shopFood.vue'
// import userfinished from '@/components/UserOrder/UserFinished.vue'
// import usersending from '@/components/UserOrder/UserSending.vue'
// import userunsend from '@/components/UserOrder/UserUnsend.vue'
// import indimsg from '@/components/UserMsg/IndiMsg.vue'
// import changepwd from '@/components/UserMsg/ChPwd.vue'
export default {
    components: {
        shopFood,
        // userfinished: userfinished,
        // usersending: usersending,
        // userunsend: userunsend,
        // indimsg: indimsg,
        // changepwd: changepwd,
    },
    data() {
        return {
            username: 'Anxi',
            active: 1,
        };
    },
    methods: {
        handleSelect(index) {
            this.active = index;
        }
    },
}
</script>

<style scoped>
.topBar {
    width: 100%;
    height: 55px;

    display: flex;
    align-items: center;

    background-color: #FDD58F;
}

#logoBox {
    display: flex;
    align-items: center;
}

#greetings {
    font-size: 16px;
    color: black;

    /* 定位在窗口右侧 */
    position: absolute;
    right: 100px;
}

#mode {
    font-size: 14px;
    color: rgb(0, 0, 0, 0.5);

    /* 定位在窗口右侧 */
    position: absolute;
    right: 10px;

    padding-right: 10px;
}

.body {
    width: 100%;
    height: 100% - 55px;

    display: flex;
    /* 内部两组件水平对齐 */
    align-items: normal;
    justify-content: space-around;
}

.menuBar {
    width: 220px;
    height: 100%;
    background-color: #FFEAC5;
}

.navigationMenu {
    width: 100%;
    min-height: 100%;
}

.menuItem {
    font-size: 17px;
}

.main {
    width: 88%;
    height: 100%;
}
</style>