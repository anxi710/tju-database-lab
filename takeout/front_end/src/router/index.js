import Vue from 'vue'
import VueRouter from 'vue-router'

import loginRegister from '@/views/loginRegister'
import userPage from '@/views/userPage'
import manage from '@/components/MyManage'

Vue.use(VueRouter)

export default new VueRouter({
    mode:'history',
    routes: [
        {
            path:'/',
            redirect:'/login'
        },
        {
            path: '/login',
            name: 'login',
            component: loginRegister
        },
        {
            path: '/user',
            component: userPage,
            meta: {
                title: "用户界面"
            }
        },
        {
            path: '/manage',
            component: manage,
            meta: {
                title: "后台管理界面"
            }
        },
    ]
})