<template>
    <el-container>

        <el-header class="header">
            未发货订单
        </el-header>

        <el-main class="body">

            <el-table :data="tableData" style="width: 100%; font-size:16px"
                class="table" stripe show-summary>
                <el-table-column prop="shopName" label="店铺名称" />
                <el-table-column prop="foodName" label="食物名称" />
                <el-table-column prop="orderPrice" label="订单金额" sortable />
                <el-table-column prop="orderWay" label="配送方式" />
                <el-table-column prop="consName" label="订餐人姓名" />
                <el-table-column prop="consAddress" label="送餐地址" />
                <!-- 未发货订单有两种状态：未接单 or 接单但未制作完成 -->
                <el-table-column
                    prop="status"
                    label="订单状态"
                    width="100"
                    :filters="[{ text: '未接单', value: '未接单' }, { text: '制作中', value: '制作中' }]"
                    :filter-method="filterTag"
                    filter-placement="bottom-end"
                >
                    <template slot-scope="scope">
                        <el-tag
                            :type="scope.row.status === '未接单' ? 'primary' : 'success'"
                            disable-transitions
                        >
                            {{ scope.row.status }}
                        </el-tag>
                    </template>
                </el-table-column>
            </el-table>

        </el-main>

    </el-container>
</template>

<script>
export default {
    name: 'unfilledOrder',
    data() {
        return {
            tableData: [
                {
                    shopName: '熊大爷现包饺子',
                    foodName: '鲜肉饺子',
                    orderPrice: 10,
                    orderWay: '外卖',
                    consName: '张三',
                    consAddress: '友园四号楼',
                    status: '未接单'
                },
                {
                    shopName: '熊大爷现包饺子',
                    foodName: '韭菜鸡蛋饺子',
                    orderPrice: 10,
                    orderWay: '外卖',
                    consName: '张三',
                    consAddress: '友园四号楼',
                    status: '制作中'
                },
                {
                    shopName: '小麻鲜',
                    foodName: '香辣烤鱼饭',
                    orderPrice: 15,
                    orderWay: '外卖',
                    consName: '李四',
                    consAddress: '友园四号楼',
                    status: '未接单'
                },
                {
                    shopName: '小麻鲜',
                    foodName: '香辣烤鱼饭',
                    orderPrice: 15,
                    orderWay: '外卖',
                    consName: '李四',
                    consAddress: '友园四号楼',
                    status: '制作中'
                }
            ],
        }
    },
    methods: {
        getdata() {
            this.$axios.get("/api/order/loadAllOrder", {
                params: {
                    username: window.localStorage.getItem('username')
                }
            }).then((res) => {
                console.log(res.data);
                if (res.data.code == 200) {
                    for (let i = 0; i < res.data.data.length; i++) {
                        // if (res.data.data[i].status === '未接单' || res.data.data[i].status === '制作中') {
                            this.tableData.push({
                                shopName: res.data.data[i].shopName,
                                foodName: res.data.data[i].foodName,
                                orderPrice: res.data.data[i].orderPrice,
                                orderWay: res.data.data[i].orderWay,
                                consName: res.data.data[i].consName,
                                consAddress: res.data.data[i].consAddress,
                                status: "未接单"
                            });
                        // }
                    }
                }
            })
        },
        filterTag(value, row) {
            return row.status === value;
        },
        filterHandler(value, row, column) {
            const property = column['property'];
            return row[property] === value;
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