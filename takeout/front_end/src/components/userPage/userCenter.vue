<template>
    <el-container>

        <el-header class="header">
            个人信息
        </el-header>

        <el-main class="body">
            <el-form v-if="~is_modify" ref="userInfoForm" :model="userInfoForm" label-width="20%" label-position="left" :disabled="true">
                <el-form-item label="头像" prop="profilePhoto">
                    <el-avatar
                        shape="square"
                        :size="50"
                        :src="userInfoForm.profilePhotoUrl"
                        icon="el-icon-user-solid">
                    </el-avatar>
                </el-form-item>
                <el-form-item label="用户名" prop="userName">
                    <span>{{ userInfoForm.username }}</span>
                </el-form-item>
                <el-form-item label="姓名" prop="realName">
                    <span>{{ userInfoForm.realname }}</span>
                </el-form-item>
                <el-form-item label="性别" prop="sex">
                    <span>{{ userInfoForm.sex === "" ? "" : (userInfoForm.sex == "man" ? "男" : "女") }}</span>
                </el-form-item>
                <el-form-item label="电话" prop="phone">
                    <span>{{ userInfoForm.telephone }}</span>
                </el-form-item>
            </el-form>

            <el-form v-else ref="tmpInfoForm" :model="tmpInfoForm" label-width="20%" label-position="left" :disabled="false">
                <el-form-item label="头像" prop="profilePhoto">
                    <el-upload
                        class="avatar-uploader"
                        action="http://127.0.0.1:5000/api/user/profilePhoto/upload"
                        :data="userInfoForm"
                        :show-file-list="false"
                        :on-success="handleAvatarSuccess"
                        :before-upload="beforeAvatarUpload"
                    >
                        <img v-if="tmpInfoForm.profilePhotoUrl" :src="tmpInfoForm.profilePhotoUrl" class="avatar">
                        <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                    </el-upload>
                </el-form-item>
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
                    <el-input v-model="tmpInfoForm.phone" style="width: 220px"></el-input>
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
                profilePhotoUrl: '',
                username: 'anxi',
                realname: '',
                sex: '',
                telephone: ''
            },
            tmpInfoForm: {
                profilePhotoUrl: '',
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
            this.$axios.get('/api/user/info', {
                params: {
                    username: username
                }
            }).then((res) => {
                console.log(res.data);
                if (res.data.status === 200) {
                    const data = res.data;
                    this.personalInfoForm.profilePhotoUrl = data.profilePhotoUrl;
                    this.personalInfoForm.userName = username;
                    this.personalInfoForm.realName = data.realName;
                    this.personalInfoForm.sex = data.sex;
                    this.personalInfoForm.telephone = data.telephone;
                    this.tmpInfoForm.profilePhotoUrl = data.profilePhotoUrl;
                    this.tmpInfoForm.username = username;
                    this.tmpInfoForm.realname = data.realName;
                    this.tmpInfoForm.sex      = data.sex;
                    this.tmpInfoForm.telephone    = data.telephone;
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
            this.tmpInfoForm.telephone    = this.userInfoForm.telephone;
            this.is_modify = ~this.is_modify;

            this.$axios.post
        },
        handleAvatarSuccess() {
            this.$notify({
                title: '成功',
                message: '头像上传成功',
                type: 'success'
            });
            this.tmpInfoForm.profilePhotoUrl = "http://localhost:5000/api/user/profilePhoto/get?" + "username=" + this.tmpInfoForm.username;
        },
        beforeAvatarUpload(file) {
            const checkType = file.type === 'image/jpeg' || file.type === 'image/png' ||
                file.type === 'image/jpg';

            if (!checkType) {
                this.$notify.error({
                    title: '错误',
                    message: '上传头像图片只能是 PNG 或 JPG 或 JPEG 格式!'
                });
            }
            return checkType;
        }
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

.avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
    width: 60px;
    height: 60px;
}
.avatar-uploader .el-upload:hover {
border-color: #409EFF;
}
.avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 50px;
    height: 50px;
    text-align: center;
}
.avatar {
    width: 80px;
    height: 80px;
    display: block;
}
</style>