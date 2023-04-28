<template>
  <div>
    <div class="module-header">
      <h3>Phone</h3>
    </div>
    <div class="module-content">
      <div class="tool-bar">
        <el-button class="filter-item" style="margin-left: 10px;" type="primary" icon="el-icon-edit">Add</el-button>
      </div>
      <br/>
      <el-table
        :data="tableData"
        style="width: 100%">
        <el-table-column prop="id" label="id" width="50"></el-table-column>
        <el-table-column prop="create_time" label="创建时间" width="180"></el-table-column>
        <el-table-column prop="type" label="类型" width="180"></el-table-column>
        <el-table-column prop="account" label="手机号码" width="240"></el-table-column>
        <el-table-column
          fixed="right"
          label="操作"
          width="200">
          <template slot-scope="scope">
            <el-popover
              placement="top-start"
              title="提示"
              width="200"
              trigger="hover"
              content="复制手机号">
              <el-button @click="handleCopy(scope.row)" type="text" size="small"slot="reference">copy</el-button>
            </el-popover>
            <el-popover
              placement="top-start"
              title="提示"
              width="200"
              trigger="hover"
              content="点击删除手机号码">
              <el-button @click="deletePhone(scope.row)" type="text" size="small"slot="reference">删除</el-button>
            </el-popover>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
import copyToClipboard from "../utils/util";

export default {
  created:function() {
    this.updatePhoneList()
  },
  data() {
    return {
      tableData: []
    }
  },
  methods:{
    updatePhoneList(){
      const _this = this
      this.$axios.get('/phoneList',)
        .then(function (response) {
          const res = response.data
          _this.$data.tableData = res.data
          console.log(_this.$data.tableData)
        }).catch(function (error) {
        console.log(error);
      });
    },

    // 复制手机号码
    handleCopy(row){
      const _this = this
      copyToClipboard(row.password, function () {
        const h = _this.$createElement;
        _this.$notify({
          title: '提示',
          message: h('i', { style: 'color: teal'}, '复制成功')
        });
        console.log('复制成功');
      })
    },
    deletePhone(row){
      const _this = this
      const id = row['id']
      this.$confirm('此操作将删除这条记录, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        //点击确定的操作(调用接口)
        _this.$axios.get('/phoneDel', {
          params: {
            id:id
          }
        }).then(function (response) {
          _this.updatePhoneList()
          console.log(res)
        }).catch(function (error) {
          console.log(error);
        });
      }).catch(() => {
        //几点取消的提示
        const h = _this.$createElement;
        _this.$notify({
          title: '提示',
          message: h('i', { style: 'color: teal'}, '取消操作')
        });
      });
    },
    handleClose(done) {
      done();
    },
  }
}
</script>
<style>

.tool-bar{
  text-align: right;
}
</style>
