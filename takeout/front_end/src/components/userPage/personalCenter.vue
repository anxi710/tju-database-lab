<template>
    <el-container>

        <el-header class="header">
            个人信息
        </el-header>

        <el-main class="body">
            <el-form ref="personalInfoForm" :model="personalInfoForm" label-width="20%" label-position="left" :disabled="modifyOrNot">
                <el-form-item label="头像" prop="profilePhoto">
                    <el-avatar
                        v-if="modifyOrNot == true"
                        shape="square"
                        :size="50"
                        :src="personalInfoForm.profilePhotoUrl"
                        icon="el-icon-user-solid">
                    </el-avatar>
                    <el-upload
                        v-else
                        class="avatar-uploader"
                        action="http://127.0.0.1:5000/api/user/profilePhoto/upload"
                        :data="personalInfoForm"
                        :show-file-list="false"
                        :on-success="handleAvatarSuccess"
                        :before-upload="beforeAvatarUpload"
                    >
                        <img v-if="uploadImageUrl" :src="uploadImageUrl" class="avatar">
                        <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                    </el-upload>
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
            </el-form>

            <div style="padding-left:80px; padding-top: 10px">
                <el-button v-if="modifyOrNot" type="primary" @click="modify()">开始修改</el-button>
                <el-button v-else type="primary" @click="cancel()">取消修改</el-button>
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
                profilePhotoUrl: '',
                userName: 'anxi',
                realName: '',
                sex: '',
                phone: '',
                usualAddress: ''
            },
            modifyOrNot: true,
            uploadImageUrl: ''
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
                    this.personalInfoForm.phone = data.telephone;
                }
            }).catch((error) => {
                console.error('请求失败:', error);
            });
        },
        modify() {
            this.modifyOrNot = !this.modifyOrNot
        },
        handleAvatarSuccess(res, file) {
            this.uploadImageUrl = URL.createObjectURL(file.raw);
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