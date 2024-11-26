<template>
    <el-container>
        <el-header class="header">
                <div id="logoBox">
                    <img src="../assets/images/logo.png" height="35px"
                        alt="同济大学" style="padding-left: 10px" />
                    <span style="color: #05d4eb; font-size: 20px; padding-left: 5px">
                        黄渡外卖
                    </span>
                </div>

                <p id="greetings">😃Hi {{ this.adminName }} ~ 又是愉快的一天！😉</p>

                <p id="profilePhoto">
                    <el-avatar
                        size="medium"
                        :src="profilePhotoURL"
                        icon="el-icon-user-solid"
                    />
                </p>
        </el-header>

        <el-container>
            <el-aside style="width: 220px; height: 100vh">
                <el-menu default-active="1" background-color="#FFEAC5"
                    text-color="black" active-text-color="#FFB200" @select="handleSelect">

                    <el-menu-item index="1">
                        <i class="el-icon-s-shop"></i>
                        <span slot="title">美食管理</span>
                    </el-menu-item>

                    <el-submenu index="100">
                        <template slot="title">
                            <i class="el-icon-s-promotion"></i>
                            <span>外卖管理</span>
                        </template>
                        <el-menu-item-group>
                            <el-menu-item index="2">未接单</el-menu-item>
                            <el-menu-item index="3">正在配送</el-menu-item>
                            <el-menu-item index="4">已送达</el-menu-item>
                        </el-menu-item-group>
                    </el-submenu>

                    <el-submenu index="101">
                        <template slot="title">
                            <i class="el-icon-s-order"></i>
                            <span>订单管理</span>
                        </template>
                        <el-menu-item-group>
                            <el-menu-item index="5">待接单</el-menu-item>
                            <el-menu-item index="6">未完成</el-menu-item>
                            <el-menu-item index="7">已完成</el-menu-item>
                        </el-menu-item-group>
                    </el-submenu>

                </el-menu>
            </el-aside>

            <el-main class="main">
                <div id="manageFood" v-show="active == 1">
                    <manageFood></manageFood>
                </div>

                <!-- <div id="manageserver" v-show="active == 2">
                    <manageserver></manageserver>
                </div>

                <div id="managedispatcher" v-show="active == 3">
                    <managedispatcher></managedispatcher>
                </div>


                <div id="wuliuended" v-show="active == 4">
                    <wuliuended></wuliuended>
                </div>

                <div id="wuliuunended" v-show="active == 5">
                    <wuliuunended></wuliuunended>
                </div>
                <div id="ordersended" v-show="active == 6">
                    <ordersended></ordersended>
                </div>
                <div id="ordersending" v-show="active == 7">
                    <ordersending></ordersending>
                </div>

                <div id="orderunsend" v-show="active == 8">
                    <orderunsend></orderunsend>
                </div> -->
            </el-main>
        </el-container>
    </el-container>
</template>

<script>
import manageFood from '@/components/adminPage/manageFood.vue'
// import manageserver from '@/components/ManageServer.vue'
// import managedispatcher from '@/components/ManageDispatcher.vue'
// import wuliuended from '@/components/ManageWuliu/WuliuEnded.vue'
// import wuliuunended from '@/components/ManageWuliu/WuliuUnended.vue'
// import ordersended from '@/components/ManageOrder/BeSended.vue'
// import ordersending from '@/components/ManageOrder/BeSending.vue'
// import orderunsend from '@/components/ManageOrder/UnSend.vue'

export default {
    components: {
        manageFood,
        // manageserver: manageserver,
        // managedispatcher: managedispatcher,
        // wuliuended: wuliuended,
        // wuliuunended: wuliuunended,
        // ordersended: ordersended,
        // ordersending: ordersending,
        // orderunsend: orderunsend
    },
    data() {
        return {
            active: 1,
            adminName: '管理员',
            profilePhotoURL: 'https://avatars.githubusercontent.com/u/77191763'
        }
    },
    methods: {
        handleSelect(index) {
            this.active = index;
        }
    },
}
</script>

<style scoped>
.header {
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

    text-align: center;
}

#profilePhoto {
    /* 定位在窗口右侧 */
    position: absolute;
    right: 20px;
    padding-right: 10px;
}

.navigationMenu {
    width: 99%;
    min-height: 100%;
}

.menuItem {
    font-size: 17px;
}
</style>