<template>
    <el-container>

        <el-header class="header">
            个人信息
        </el-header>

        <el-main class="body">
            <el-form v-if="~is_modify" ref="userInfoForm" :model="userInfoForm" label-width="20%" label-position="left" :disabled="true">
                <el-form-item label="用户名" prop="userName">
                    <span>{{ userInfoForm.username }}</span>
                </el-form-item>
                <el-form-item label="姓名" prop="realName">
                    <span>{{ userInfoForm.realname }}</span>
                </el-form-item>
                <el-form-item label="性别" prop="sex">
                    <span>{{ userInfoForm.sex === "" ? "" : userInfoForm.sex }}</span>
                </el-form-item>
                <el-form-item label="电话" prop="phone">
                    <span>{{ userInfoForm.telephone }}</span>
                </el-form-item>
            </el-form>

            <el-form v-else ref="tmpInfoForm" :model="tmpInfoForm" label-width="20%" label-position="left">
                <el-form-item label="用户名" prop="userName">
                    <span>{{ userInfoForm.username }}</span>
                </el-form-item>
                <el-form-item label="姓名" prop="realName">
                    <el-input v-model="tmpInfoForm.realname" style="width: 150px"></el-input>
                </el-form-item>
                <el-form-item label="性别" prop="sex">
                    <el-select v-model="tmpInfoForm.sex" style="width: 150px">
                        <el-option label="男" value="男"></el-option>
                        <el-option label="女" value="女"></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="电话" prop="phone">
                    <span>{{ userInfoForm.telephone }}</span>
                </el-form-item>
            </el-form>

            <div style="padding-left:80px; padding-top: 10px">
                <el-button v-if="~is_modify" type="primary" @click="modify()">开始修改</el-button>
                <el-button v-else type="primary" @click="cancel()">取消修改</el-button>
                <el-button type="primary" @click="confirm()">确认修改</el-button>
            </div>
        </el-main>

    </el-container>
</template>

<script>
export default {
    name: 'userCenter',
    data() {
        return {
            userInfoForm: {
                username: '',
                realname: '',
                sex: '',
                telephone: ''
            },
            tmpInfoForm: {
                username: '',
                realname: '',
                sex: '',
                telephone: ''
            },
            is_modify: false
        }
    },
    methods: {
        getData(username) {
            this.$axios.get('/api/user/info/get', {
                params: {
                    username: username
                }
            }).then((res) => {
                console.log(res.data);
                if (res.data.code === 200) {
                    this.userInfoForm.username  = res.data.data.username;
                    this.userInfoForm.realname  = res.data.data.realname;
                    this.userInfoForm.sex       = res.data.data.sex;
                    this.userInfoForm.telephone = res.data.data.telephone;
                    this.tmpInfoForm.username   = res.data.data.username;
                    this.tmpInfoForm.realname   = res.data.data.realname;
                    this.tmpInfoForm.sex        = res.data.data.sex;
                    this.tmpInfoForm.telephone  = res.data.data.telephone;
                    console.log(this.userInfoForm.username);
                }
            }).catch((error) => {
                console.error('请求失败:', error);
            });
        },
        modify() {
            this.is_modify = ~this.is_modify;
        },
        cancel() {
            this.tmpInfoForm.realname = this.userInfoForm.realname;
            this.tmpInfoForm.sex      = this.userInfoForm.sex;
            this.is_modify = ~this.is_modify;
        },
        confirm() {
            this.$axios.post('/api/user/info/update', {
                username: this.userInfoForm.username,
                realname: this.tmpInfoForm.realname,
                sex: this.tmpInfoForm.sex,
            }).then((res) => {
                console.log(res.data);
                if (res.data.code === 200) {
                    this.userInfoForm.realname  = this.tmpInfoForm.realname;
                    this.userInfoForm.sex       = this.tmpInfoForm.sex;
                }
            })

            this.is_modify = ~this.is_modify;
        },
    },
    mounted() {
        // console.log(window.localStorage.getItem('username'));
        this.getData(window.localStorage.getItem('username'));
    }
}
</script>

<style scoped>
.header {
    line-height: 45px;
    text-align: center;
    font-size: 20px;
    font-weight: 600;
    border-bottom: 1px solid #e3e3e3;
}

.body {
    width: 500px;
    /* margin: auto; */
    margin-top: 30px;
    margin-left: 30px;
}

#selectForm.el-form-item__label {
    font-size: 18px;
}

span {
    font-size: 18px;
}

</style>