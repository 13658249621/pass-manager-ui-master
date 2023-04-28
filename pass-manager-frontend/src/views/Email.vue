<template>
  <div>
    <div class="module-header">
      <h3>Email</h3>
    </div>
    <div class="module-content">
        <div class="tool-bar">
          <el-button class="filter-item" style="margin-left: 10px;" type="primary" icon="el-icon-edit" @click="AddEmail">Add</el-button>
        </div>
        <br/>
      <el-table
        :data="tableData"
        style="width: 100%">
        <el-table-column prop="id" label="id" width="50"></el-table-column>
        <el-table-column prop="create_time" label="创建时间" width="200"></el-table-column>
        <el-table-column prop="email_name" label="邮箱名称" width="180"></el-table-column>
        <el-table-column prop="account" label="邮箱" width="240"></el-table-column>
        <el-table-column label="地址" width="70">
          <template slot-scope="scope">
            <span class="span-text" v-if="scope.row.website!== undefined">
              <a link :href="scope.row.website" target="_blank">地址1</a>
            </span>
          </template>
        </el-table-column>
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
              content="复制邮箱">
              <el-button @click="handleCopyEmail(scope.row)" type="text" size="small"slot="reference">copy1</el-button>
            </el-popover>
            <el-popover
              placement="top-start"
              title="提示"
              width="200"
              trigger="hover"
              content="复制密码">
              <el-button @click="handleCopyPasswd(scope.row)" type="text" size="small"slot="reference">copy2</el-button>
            </el-popover>
            <el-popover
              placement="top-start"
              title="提示"
              width="200"
              trigger="hover"
              content="删除邮箱">
              <el-button @click="deleteEmail(scope.row)" type="text" size="small"slot="reference">删除</el-button>
            </el-popover>
          </template>
        </el-table-column>
      </el-table>

      <!-- 抽屉 添加内容 -->
      <el-drawer :title="drawerTitle" :visible.sync="drawer" :direction="direction" :before-close="handleClose">
        <EmailAdd @func="onEmitIndex"></EmailAdd>
      </el-drawer>
    </div>
  </div>
</template>

<script>
import copyToClipboard from "../utils/util";
import EmailAdd from "@/components/EmailAdd";

export default {

  components: {
    EmailAdd
  },

  created:function() {
    this.updateEmailList()
  },
  data() {
    return {
      tableData: [],

      drawerTitle:"",
      drawer: false,
      direction: 'rtl',

      form: {
        create_time:'',
        update_time:'',
        email_name: '',
        account: '',
        password: '',
        website: '',
        comment: ''
      },

    }
  },
  methods:{

    updateEmailList() {
      const _this = this
      this.$axios.get('/emailList',)
        .then(function (response) {
          const res = response.data
          _this.$data.tableData = res.data
          console.log(_this.$data.tableData)
        }).catch(function (error) {
        console.log(error);
      });
    },
    handleCopyEmail(row){
      const _this = this
      copyToClipboard(row.account, function () {
        const h = _this.$createElement;
        _this.$notify({
          title: '提示',
          message: h('i', { style: 'color: teal'}, '复制成功')
        });
        console.log('复制成功');
      })
    },
    handleCopyPasswd(row){
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
    AddEmail(){
      this.form = {}
      this.drawer = true
      this.drawerTitle = "添加"
    },
    handleClose(done) {
      done();
    },
    deleteEmail(row){
      const _this = this
      const id = row['id']
      this.$confirm('此操作将删除这条记录, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        //点击确定的操作(调用接口)
        _this.$axios.get('/emailDel', {
          params: {
            id:id
          }
        }).then(function (response) {
          _this.updateEmailList()
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

    onEmitIndex(data){
      console.log(data)
      // 隐藏抽屉
      this.drawer = false
      const _this = this
      this.$axios.get('/emailAdd', {
        params: data
      }).then(function (response) {
        const res = response.data
        console.log(res)
        _this.updateEmailList()
        _this.form["bind_email"] = data["account"]
      }).catch(function (error) {
        console.log(error);
      });
    }


  }
}
</script>
<style>

.tool-bar{
  text-align: right;
}
</style>
