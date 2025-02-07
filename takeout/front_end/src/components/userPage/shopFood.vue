<template>

    <el-container>

        <el-header class="header">
            <el-autocomplete
                style="width: 280px;"
                prefix-icon="el-icon-search"
                v-model="curShopName"
                :fetch-suggestions="querySearch"
                placeholder="搜索店铺"
                @select="handleSelect"
                clearable
            ></el-autocomplete>
        </el-header>

        <el-main>
            <el-row
                v-if="food.length > 0"
                :gutter="10"
                type="flex"
                justify="center"
                style="flex-wrap: wrap; justify-content: flex-start; width:100%;"
            >
                <el-col style="width: 330px; margin-top: 10px" v-for="i in food.length" :key="i">
                    <foodCard :food="food[i - 1]" @order="order"></foodCard>
                </el-col>
            </el-row>

            <el-dialog
                title="订餐表"
                :visible.sync="dialog"
                class="dialog"
                width="400px"
                append-to-body
                @close="handleCancel()"
            >
                <div>
                    <el-form ref="orderForm" :model="orderForm" label-width="100px"
                        :rules="orderFormRules">
                        <el-form-item label="店铺名称：">
                            {{ this.curShopName }}
                        </el-form-item>

                        <el-form-item label="食物名称：">
                            {{ this.orderFood.name }}
                        </el-form-item>

                        <el-form-item label="价格：">
                            {{ this.orderFood.price }}
                        </el-form-item>

                        <el-form-item label="取餐方式：" prop="orderWay">
                            <el-select v-model="orderForm.orderWay" placeholder="请选择取餐方式">
                                <el-option label="自提" value="自提"></el-option>
                                <el-option label="外送" value="外送"></el-option>
                            </el-select>
                        </el-form-item>

                        <el-form-item label="客户姓名：" prop="consName">
                            <el-input v-model="orderForm.consName"></el-input>
                        </el-form-item>

                        <el-form-item label="客户电话：" prop="consPhone">
                            <el-input v-model="orderForm.consPhone"></el-input>
                        </el-form-item>

                        <el-form-item label="送餐地址：" prop="consAddress">
                            <el-input v-model="orderForm.consAddress"></el-input>
                        </el-form-item>

                    </el-form>
                    <div style="text-align: center;">
                        <el-button type="primary" @click="handleConfirm()">提交</el-button>
                        <el-button @click="handleCancel()">取消</el-button>
                    </div>
                </div>
            </el-dialog>
        </el-main>

</el-container>
</template>

<script>
import { checkValidMobile } from '@/utils/validate.js'
import foodCard from '@/components/userPage/foodCard.vue'

export default {
    name: "shopFood",
    components: {
        foodCard
    },
    data() {
        return {
            curShopName: '',
            shops: [],
            dialog: false,
            orderForm: {
                foodName: '',
                orderPrice: '',
                orderWay: '',
                consName: '',
                consPhone: '',
                consAddress: ''
            },
            food: [

            ],
            orderFood: {},
            orderFormRules: {
                orderWay: [
                    { required: true, message: '请选择取餐方式', trigger: 'blur' }
                ],
                consName: [
                    { required: true, message: '请输入客户姓名', trigger: 'blur' }
                ],
                consPhone: [
                    { required: true, message: '请输入客户电话', trigger: 'blur' },
                    { validator: checkValidMobile, trigger: 'blur' }
                ],
                consAddress: [
                    { required: true, message: '请输入送餐地址', trigger: 'blur' }
                ]
            }
        }
    },
    methods: {
        handleConfirm() { // 确定点单处理逻辑
            console.log("handleConfirm");
            this.$refs.orderForm.validate(valid => {
                if (valid) {
                    this.$axios.post("/api/order/addOrder", {
                        username: window.localStorage.getItem('username'),
                        foodName: this.orderFood.name,
                        orderPrice: this.orderFood.price,
                        orderWay: this.orderForm.orderWay,
                        consName: this.orderForm.consName,
                        consPhone: this.orderForm.consPhone,
                        consAddress: this.orderForm.consAddress
                    }).then((res) => {
                        console.log(res.data);
                        if (res.data.code == 200) {
                            this.$message({
                                message: '点单成功',
                                type: 'success'
                            });
                            this.dialog = false;
                            this.orderForm = {
                                foodName: '',
                                orderMoney: '',
                                orderWay: '',
                                consName: '',
                                consPhone: '',
                                consAddress: ''
                            }
                        } else {
                            this.$message({
                                message: '点单失败',
                                type: 'error'
                            });
                        }
                    })
                }
            });
        },

        handleCancel() { // 取消点单处理逻辑
            // 关闭弹窗
            this.dialog = false;
            // 清空表单数据
            this.orderForm = {
                shopName: '',
                orderMoney: '',
                orderWay: '',
                consName: '',
                consPhone: '',
                consAddress: ''
            }
        },

        querySearch(queryString, cb) {
            var shops = this.shops;
            var results = queryString ? shops.filter(this.createFilter(queryString)) : shops;
            // 调用 callback 返回建议列表的数据
            cb(results);
        },

        createFilter(queryString) {
            return (shop) => {
                return (shop.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0);
            };
        },

        loadAllShop() {
            this.$axios.get("/api/shop/loadAllShop").then((res) => {
                console.log(res.data);
                if (res.data.code == 200) {
                    for (let i = 0; i < res.data.data.length; i++) {
                        this.shops.push({
                            "value": res.data.data[i].name,
                            "address": res.data.data[i].address
                        })
                    }
                }
            })

            console.log(this.shops);
        },

        handleSelect(item) {
            console.log(item.value);
            console.log(this.curShopName)

            this.$axios.get("/api/shop/loadShopFood", {
                params: {
                    shopName: item.value
                }
            }).then((res) => {
                console.log(res.data);
                if (res.data.code == 200) {
                    this.food = res.data.data;
                }
            })
        },

        order(food) {
            console.log(food);
            this.orderFood = food;
            this.dialog = true;
        }
    },

    mounted() {
        //this.getdata();
        this.loadAllShop();
    }
}
</script>

<style scoped>
.header {
    width: 100%;
    height: 10%;
    text-align: left;
    border-bottom: 1px solid #e3e3e3;
}

</style>