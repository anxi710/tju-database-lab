<template>
    <div style="width: 100%; height: 100vh;">

        <el-container>
            <el-header class="header">
                <div id="logoBox">
                    <img src="../assets/images/logo.png" height="35px"
                        alt="同济大学" style="padding-left: 10px" />
                    <span style="color: #05d4eb; font-size: 20px; padding-left: 5px">
                        黄渡外卖
                    </span>
                </div>

                <p id="greetings">😃Hi {{ this.username }} ~ 今天吃点什么？😉</p>

                <p id="mode">用户模式</p>
            </el-header>

            <el-container>
                <el-aside style="width: 220px;">
                    <el-menu default-active="1" class="navigationMenu"
                        background-color="#FFEAC5" text-color="black"
                        active-text-color="#FFB200" @select="handleSelect">
                        <el-menu-item index="1">
                            <i class="el-icon-food"></i>
                            <span slot="title" class="menuItem">美食广场</span>
                        </el-menu-item>

                        <el-submenu index="8">
                            <template slot="title">
                                <i class="el-icon-shopping-cart-2"></i>
                                <span class="menuItem">订单</span>
                            </template>
                            <el-menu-item-group>
                                <el-menu-item index="2" class="menuItem">待收货订单</el-menu-item>
                                <el-menu-item index="3" class="menuItem">已完成订单</el-menu-item>
                                <el-menu-item index="4" class="menuItem">未发货订单</el-menu-item>
                            </el-menu-item-group>
                        </el-submenu>

                        <el-menu-item index="5">
                            <template slot="title">
                                <i class="el-icon-star-off"></i>
                                <span class="menuItem">收藏</span>
                            </template>
                        </el-menu-item>

                        <el-menu-item index="6">
                            <template slot="title">
                                <i class="el-icon-chat-line-square"></i>
                                <span class="menuItem">评论中心</span>
                            </template>
                        </el-menu-item>

                        <el-menu-item index="7">
                            <template slot="title">
                                <i class="el-icon-house"></i>
                                <span class="menuItem">个人中心</span>
                            </template>
                        </el-menu-item>

                    </el-menu>
                </el-aside>

                <el-main style="padding-left: 30px; width: 100%">
                    <div id="shopFood" v-if="active == 1">
                        <shopFood></shopFood>
                    </div>

                    <div id="pendingOrder" v-else-if="active == 2">
                        <pendingOrder></pendingOrder>
                    </div>

                    <div id="finishedOrder" v-else-if="active == 3">
                        <finishedOrder></finishedOrder>
                    </div>

                    <div id="unfilledOrder" v-else-if="active == 4">
                        <unfilledOrder></unfilledOrder>
                    </div>


                    <div id="personalCenter" v-else-if="active == 7">
                        <personalCenter></personalCenter>
                    </div>

                </el-main>
            </el-container>

        </el-container>

    </div>
</template>

<script>
import shopFood from '@/components/userPage/shopFood.vue'
import pendingOrder from '@/components/userPage/orderPage/pendingOrder.vue'
import finishedOrder from '@/components/userPage/orderPage/finishedOrder.vue'
import unfilledOrder from '@/components/userPage/orderPage/unfilledOrder.vue'

import personalCenter from '@/components/userPage/personalCenter.vue'

export default {
    components: {
        shopFood,
        pendingOrder,
        finishedOrder,
        unfilledOrder,

        personalCenter
    },
    data() {
        return {
            username: 'Anxi',
            active: 1,
        };
    },
    methods: {
        handleSelect(index) {
            console.log(index);
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
}

#mode {
    font-size: 14px;
    color: rgb(0, 0, 0, 0.5);

    /* 定位在窗口右侧 */
    position: absolute;
    right: 10px;

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