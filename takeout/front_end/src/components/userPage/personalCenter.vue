<template>
    <el-container>

        <el-header class="header">
            个人信息
        </el-header>

        <el-main class="body">
            <el-form ref="form" :model="form" label-width="20%" label-position="left" :disabled="modifyOrNot">
                <el-form-item label="头像" prop="profilePhoto">
                    <el-avatar
                        shape="square"
                        :size="50"
                        :src="personalInfoForm.profilePhotoURL"
                        icon="el-icon-user-solid">
                    </el-avatar>
                </el-form-item>
                <el-form-item label="用户名" prop="userName">
                    <span>{{ personalInfoForm.userName }}</span>
                </el-form-item>
                <el-form-item label="姓名" prop="realName">
                    <el-input v-model="personalInfoForm.realName" style="width: 150px"></el-input>
                </el-form-item>
                <el-form-item label="性别" prop="sex">
                    <el-select v-model="personalInfoForm.sex" style="width: 150px">
                        <el-option label="男" value="男"></el-option>
                        <el-option label="女" value="女"></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="电话" prop="phone">
                    <el-input v-model="personalInfoForm.phone" style="width: 220px"></el-input>
                </el-form-item>
                <el-form-item label="常用地址" prop="usualAddress">
                    <el-input v-model="personalInfoForm.usualAddress" style="width:220px"></el-input>
                </el-form-item>
            </el-form>

            <div style="padding-left:80px; padding-top: 10px">
                <el-button type="primary" @click="modify()">开始修改</el-button>
                <el-button type="primary" @click="confirm()">确认修改</el-button>
            </div>
        </el-main>

    </el-container>
</template>

<script>
export default {
    data() {
        return {
            personalInfoForm: {
                profilePhotoURL: 'https://avatars.githubusercontent.com/u/77193761?v=4',
                userName: 'Anxi',
                realName: '徐先生',
                sex: '男',
                phone: '1872065088x',
                usualAddress: '友园四号楼'
            },
            modifyOrNot: true
        }
    },
    methods: {
        getdata() {
            this.$axios.get("/api/user/usermsg").then((res) => {
                console.log(res.data);
                if (res.data.status == 200) {
                    this.form.age = res.data.data.age;
                    this.form.mail = res.data.data.mail;
                    this.form.phone = res.data.data.phone;
                    this.form.real_name = res.data.data.real_name;
                    this.form.sex = res.data.data.sex;
                    this.form.user_name = res.data.data.user_name;
                }
            })
        },
        modify() {
            this.modifyOrNot = !this.modifyOrNot
        },
    },
    mounted() {
        // this.getdata()
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