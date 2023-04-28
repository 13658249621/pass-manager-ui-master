<template>
  <div>
    <div class="module-header">
      <h3>passwd-ui</h3>
    </div>
    <div class="module-content">
      <div class="tool-bar">
        <el-input  placeholder="info or comment" v-model="q" style="width: 200px;" class="filter-item" @keyup.enter.native="handleSearch" />
        <el-button class="filter-item" type="primary" icon="el-icon-search" @click="handleSearch">Search</el-button>
        <el-button class="filter-item" style="margin-left: 10px;" type="primary" icon="el-icon-edit" @click="handleAdd">Add</el-button>
      </div>
      <br/>
      <el-table :data="tableData" border style="width: 100%" >
        <el-table-column prop="info" label="简介"></el-table-column>
        <el-table-column prop="account" label="账号"></el-table-column>
        <el-table-column prop="website" label="网址">
          <template slot-scope="scope">
            <span class="span-text" v-if="scope.row.website!== undefined" v-for="(site, index) in scope.row.website.split(',')">
              <a link :href="site" target="_blank">地址{{index+1}} </a>
            </span>
          </template>
        </el-table-column>
        <el-table-column prop="comment" label="注释"></el-table-column>
        <el-table-column
          fixed="right"
          label="操作"
          width="200">
          <template slot-scope="scope">
            <el-button @click="handleClick(scope.row)" type="text" size="small" >查看</el-button>
            <el-button @click="handleCopyPasswd(scope.row)" type="text" size="small">copy</el-button>
            <el-button @click="handleDelete(scope.row)" type="text" size="small">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
      <!-- 分页器 -->
      <div class="block" style="margin-top:15px;">
        <el-pagination align='center' @size-change="handleSizeChange" @current-change="handleCurrentChange"
                       :current-page="currentPage"
                       :page-sizes="[1,5,10,20]"
                       :page-size="pageSize"
                       layout="total, sizes, prev, pager, next, jumper"
                       :total="pageTotal">
        </el-pagination>
      </div>
      <!-- 抽屉 添加内容 -->
      <el-drawer :title="drawerTitle" :visible.sync="drawer1" :direction="direction2" :before-close="handleClose">
        <el-form ref="form" :model="form" label-width="80px">
          <el-form-item label="简介">
            <el-input v-model="form.info"></el-input>
          </el-form-item>
          <el-form-item label="创建时间" disabled="true">
            <el-input v-model="form.create_time" disabled></el-input>
          </el-form-item>
          <el-form-item label="更新时间">
            <el-input v-model="form.update_time" disabled></el-input>
          </el-form-item>
          <el-form-item label="昵称">
            <el-input v-model="form.nickname"></el-input>
          </el-form-item>
          <el-form-item label="账号">
            <el-input v-model="form.account"></el-input>
          </el-form-item>
          <el-form-item label="密码">
            <el-input
              v-model="form.password"
              :type="type"
              class="pwd-input"
              placeholder="请输入密码">
            <i slot="suffix"
              class="icon-style"
              :class="elIcon"
              autocomplete="auto"
              @click="flag = !flag"/>
            </el-input>
          </el-form-item>
          <el-form-item label="网址">
            <el-input v-model="form.website"></el-input>
          </el-form-item>
          <el-form-item label="绑定的邮箱">
            <el-select v-model="form.bind_email" placeholder="绑定的邮箱">
              <el-option v-for="item in emailList" :label="item.account" :value="item.account"></el-option>
            </el-select>
            <el-button @click="emailAdd">添加新的邮箱</el-button>
          </el-form-item>
          <el-form-item label="绑定手机号码">
            <el-select v-model="form.bind_phone" placeholder="绑定的邮箱">
              <el-option v-for="item in phoneList" :label="item.account" :value="item.account"></el-option>
            </el-select>
            <el-button @click="phoneAdd">添加新的手机号</el-button>
          </el-form-item>
          <el-form-item label="备注">
            <el-input v-model="form.comment"></el-input>
          </el-form-item>
          <el-form-item style="text-align: right">
            <el-button type="primary" @click="onSubmit">Save</el-button>
            <el-button>Cancel</el-button>
          </el-form-item>
        </el-form>
      </el-drawer>

      <!--  抽屉 添加新的手机号码-->
      <el-drawer :title="drawerTitle" :visible.sync="drawer2" :direction="direction2" :before-close="handleClose">
        <PhoneAdd @func="onEmitIndex1"></PhoneAdd>
      </el-drawer>

      <!--  抽屉 添加新的手机号码-->
      <el-drawer :title="drawerTitle" :visible.sync="drawer3" :direction="direction3" :before-close="handleClose">
        <PhoneAdd @func="onEmitIndex2"></PhoneAdd>
      </el-drawer>

    </div>

  </div>
</template>

<script>
import copyToClipboard from "../utils/util";
import EmailAdd from "../components/EmailAdd";
import PhoneAdd from "../components/PhoneAdd";

export default {
  components:{
    PhoneAdd,
    EmailAdd
  },
  computed: {
    type() {
      return this.flag ? "text" : "password";
    },
    elIcon() {
      return this.flag ? "el-icon-minus" : "el-icon-view";
    }
  },
  created:function() {
    const _this = this
    this.pageSelect()
    this.updateEmailList()
    this.$axios.get('/phoneList')
      .then(function (response) {
        const res = response.data
        console.log(res)
        _this.phoneList = response.data.data
      }).catch(function (error) {
      console.log(error);
    });
  },

  data() {
    return {
      confirm_new_pwd:"1",
      tableData: [],
      currentPage:1,
      pageSize: 5,
      pageTotal:20,
      q:'',

      drawerTitle:"",
      drawer1: false,
      direction1: 'rtl',

      drawer2: false,
      direction2: 'rtl',

      drawer3: false,
      direction3: 'rtl',

      form: {
        info: '',
        create_time:'',
        update_time:'',
        nickname: '',
        account: '',
        password: '',
        website: '',
        bind_email: '',
        bind_phone: '',
        comment: ''
      },

      pwd: "123456",
      flag: false,

      emailList:[],
      phoneList:[]
    }
  },
  methods:{
    updateEmailList(){
      console.log("UPdate")
      const _this = this
      this.$axios.get('/emailList')
        .then(function (response) {
          const res = response.data
          console.log(res)
          _this.emailList = response.data.data
        }).catch(function (error) {
        console.log(error);
      });
    },

    pageSelect() {
      const _this = this
      this.$axios.get('/page', {
        params: {
          pageNum: this.currentPage,
          pageSize: this.pageSize,
          q: this.q
        }
      }).then(function (response) {
        const res = response.data
        _this.tableData = res.data.data
        _this.pageSize = res.data.pageSize
        _this.currentPage = res.data.pageNum
        _this.pageTotal = res.data.pageTotal
        console.log(res)
      }).catch(function (error) {
        console.log(error);
      });
    },

    // copy password to clipboard
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
    handleClick(row){
      this.drawer1 = true
      this.form = row
      this.drawerTitle = "编辑"

    },
    //每页条数改变时触发 选择一页显示多少行
    handleSizeChange(val) {
      console.log(`每页 ${val} 条`);
      this.pageSize = val;
      this.pageSelect()
    },
    //当前页改变时触发 跳转其他页
    handleCurrentChange(val) {
      console.log(`当前页: ${val}`);
      this.currentPage = val;
      this.pageSelect()
    },
    handleClose(done) {
      done();
    },
    // 搜索表格内容 请求后端
    handleSearch(){
      this.pageSelect()
    },
    handleAdd(){
      this.form = {}
      this.drawer1 = true
      console.log("ADD")
      this.drawerTitle1 = "添加"
    },
    handleDelete(row){
      const _this = this
      const id = row['id']
      this.$confirm('此操作将删除这条记录, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        //点击确定的操作(调用接口)
        _this.$axios.get('/delete', {
          params: {
            id:id
          }
        }).then(function (response) {
          _this.pageSelect()
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
    // 保存，或者 更新数据
    onSubmit() {
      console.log('submit!');
      // this.form['create_time'] = this.form['create_time1'] + this.form['create_time2']
      // this.form['update_time'] = this.form['update_time1'] + this.form['update_time2']
      var url = this.form['id'] === undefined || this.form['id'] === '' ? '/add' : '/update'
      const _this = this
      this.$axios.get(url, {
        params: _this.form
      }).then(function (response) {
        const h = _this.$createElement;
        _this.$notify({
          title: '提示',
          message: h('i', { style: 'color: teal'}, '操作完成')
        });
        _this.drawer1 = false
        _this.pageSelect()
        console.log(response)
      }).catch(function (error) {
        console.log(error);
      });
    },
    emailAdd(){
      this.drawer2 = true
    },

    phoneAdd(){
      this.drawer3 = true
    },

    onEmitIndex1(data){
      console.log(data)
      // 隐藏抽屉
      this.drawer2 = false
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
    },
    onEmitIndex2(data){
      console.log(data)
      // 隐藏抽屉
      this.drawer3 = false
      const _this = this
      this.$axios.get('/phoneAdd', {
        params: data
      }).then(function (response) {
        const res = response.data
        console.log(res)
        _this.updateEmailList()
        _this.form["bing_phone"] = data["account"]
      }).catch(function (error) {
        console.log(error);
      });
    }
  }
}
</script>

<style>

.el-table .hidden-row {
  display: none;
}
.tool-bar{
  text-align: right;
}
</style>
