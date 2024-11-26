import Vue from 'vue'
import VueRouter from 'vue-router'

import loginRegister from '@/views/loginRegister'
import userPage from '@/views/userPage'
import adminPage from '@/views/adminPage'

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
            component: loginRegister
        },
        {
            path: '/user',
            component: userPage
        },
        {
            path: '/admin',
            component: adminPage
        },
    ]
})