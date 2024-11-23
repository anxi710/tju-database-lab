<template>
    <div>

        <div class="header">
            已完成订单
        </div>

        <div class="body">

            <el-table :data="tableData" style="width: 100%" class="table" stripe
                :default-sort="{ prop: 'orderTime', order: 'descending' }" show-summary>
                <el-table-column prop="orderTime" label="订餐时间" sortable />
                <el-table-column prop="shopName" label="店铺名称" />
                <el-table-column prop="foodName" label="食物名称" />
                <el-table-column prop="orderPrice" label="订单金额" sortable />
                <el-table-column prop="orderWay" label="配送方式" />
                <el-table-column prop="consName" label="订餐人姓名" />
                <el-table-column prop="consAddress" label="送餐地址" />
            </el-table>

        </div>

    </div>
</template>

<script>
export default {
    name: 'finishedOrder',
    data() {
        return {
            tableData: [
                {
                    orderTime: '2021-06-01 12:00:00',
                    shopName: '麦当劳',
                    foodName: '麦辣鸡腿堡',
                    orderPrice: 18,
                    orderWay: '外卖',
                    consName: '张三',
                    consAddress: '广东省广州市天河区'
                },
                {
                    orderTime: '2021-06-01 12:00:00',
                    shopName: '麦当劳',
                    foodName: '麦辣鸡腿堡',
                    orderPrice: 18,
                    orderWay: '外卖',
                    consName: '张三',
                    consAddress: '广东省广州市天河区'
                },
                {
                    orderTime: '2021-06-01 12:00:00',
                    shopName: '麦当劳',
                    foodName: '麦辣鸡腿堡',
                    orderPrice: 18,
                    orderWay: '外卖',
                    consName: '张三',
                    consAddress: '广东省广州市天河区'
                },
                {
                    orderTime: '2021-06-01 12:00:00',
                    shopName: '麦当劳',
                    foodName: '麦辣鸡腿堡',
                    orderPrice: 18,
                    orderWay: '外卖',
                    consName: '张三',
                    consAddress: '广东省广州市天河区'
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
    width: 100%;
    height: 10%;
    text-align: center;
    line-height: 64px;
    font-size: 20px;
    font-weight: 800;
    border-bottom: 1px solid #e3e3e3;
}

.body {

    width: 68%;
    margin: auto;
    margin-top: 30px;
}
</style>