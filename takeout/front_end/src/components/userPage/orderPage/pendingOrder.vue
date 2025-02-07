<template>
    <el-container>

        <el-header class="header">
            待收货订单
        </el-header>

        <el-main class="body">

            <el-table :data="tableData" style="width: 100%; font-size: 16px"
                class="table" stripe show-summary>
                <el-table-column prop="shopName" label="店铺名称" />
                <el-table-column prop="foodName" label="食物名称" />
                <el-table-column prop="orderPrice" label="订单金额" sortable />
                <el-table-column prop="orderWay" label="配送方式" />
                <el-table-column prop="consName" label="订餐人姓名" />
                <el-table-column prop="consAddress" label="送餐地址" />
            </el-table>

        </el-main>

    </el-container>
</template>

<script>
export default {
    name: 'pendingOrder',
    data() {
        return {
            tableData: [
                {
                    shopName: '豪大大香鸡排',
                    foodName: '可乐鸡排套餐',
                    orderPrice: 21,
                    orderWay: '外卖',
                    consName: '王五',
                    consAddress: '友园四号楼'
                },
                {
                    shopName: '豪大大香鸡排',
                    foodName: '汉堡套餐',
                    orderPrice: 20,
                    orderWay: '外卖',
                    consName: '王五',
                    consAddress: '友园四号楼'
                },
                {
                    shopName: '豪大大香鸡排',
                    foodName: '香辣鸡排',
                    orderPrice: 12,
                    orderWay: '自提',
                    consName: '王五',
                    consAddress: '友园四号楼'
                },
                {
                    shopName: '小麻鲜',
                    foodName: '麻辣小龙虾套餐',
                    orderPrice: 30,
                    orderWay: '外卖',
                    consName: '李四',
                    consAddress: '友园六号楼'
                },
                {
                    shopName: '小麻鲜',
                    foodName: '香辣烤鱼饭',
                    orderPrice: 15,
                    orderWay: '自提',
                    consName: '李四',
                    consAddress: '友园六号楼'
                }
            ],
        }
    },
    methods: {
        getdata() {
            // this.$axios.get("/api/user/sending").then((res) => {
            //     console.log(res.data);
            //     if (res.data.status == 200) {
            //         this.tableData = res.data.tabledata;
            //     }
            // })
        }
    },
    mounted() {
        this.getdata();
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
    width: 90%;
    margin: auto;
    margin-top: 10px;
}
</style>