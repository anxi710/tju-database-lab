<template>
    <el-container>

        <el-header class="header">
            已完成订单
        </el-header>

        <el-main class="body">

            <el-table :data="tableData" style="width: 100%; font-size: 16px;"
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
    name: 'finishedOrder',
    data() {
        return {
            tableData: [
                {
                    shopName: '奈哥酸菜鱼',
                    foodName: '酸菜鱼',
                    orderPrice: 25,
                    orderWay: '外卖',
                    consName: '张三',
                    consAddress: '友园六号楼'
                },
                {
                    shopName: '奈哥酸菜鱼',
                    foodName: '麻辣烤鱼',
                    orderPrice: 32,
                    orderWay: '自提',
                    consName: '李四',
                    consAddress: '友园四号楼'
                },
                {
                    shopName: '奈哥酸菜鱼',
                    foodName: '麻辣鱼',
                    orderPrice: 25,
                    orderWay: '外卖',
                    consName: '张三',
                    consAddress: '友园六号楼'
                },
                {
                    shopName: '豪大大香鸡排',
                    foodName: '香辣鸡排',
                    orderPrice: 12,
                    orderWay: '外卖',
                    consName: '王五',
                    consAddress: '友园五号楼'
                },
                {
                    shopName: '豪大大香鸡排',
                    foodName: '原味鸡排',
                    orderPrice: 10,
                    orderWay: '自提',
                    consName: '赵六',
                    consAddress: '友园三号楼'
                },
                {
                    shopName: '熊大爷现包饺子',
                    foodName: '鲜肉饺子',
                    orderPrice: 10,
                    orderWay: '外卖',
                    consName: '张三',
                    consAddress: '友园四号楼'
                },
                {
                    shopName: '熊大爷现包饺子',
                    foodName: '韭菜鸡蛋饺子',
                    orderPrice: 10,
                    orderWay: '外卖',
                    consName: '张三',
                    consAddress: '友园四号楼'
                },
                {
                    shopName: '小麻鲜',
                    foodName: '香辣烤鱼',
                    orderPrice: 32,
                    orderWay: '外卖',
                    consName: '李四',
                    consAddress: '友园四号楼'
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