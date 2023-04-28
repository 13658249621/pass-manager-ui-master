<template>
  <div>
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
      <el-form-item label="邮件类型">
        <el-input v-model="form.email_name"></el-input>
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
      <el-form-item label="备注">
        <el-input v-model="form.comment"></el-input>
      </el-form-item>
      <el-form-item style="text-align: right">
        <el-button type="primary" @click="onSubmit">Save</el-button>
        <el-button>Cancel</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  computed: {
    type() {
      return this.flag ? "text" : "password";
    },
    elIcon() {
      return this.flag ? "el-icon-minus" : "el-icon-view";
    }
  },
  created:function() {

  },
  data() {
    return {
      form: {
        email_name: '',
        account: '',
        password: '',
        website: '',
        comment: ''
      },
    }
  },
  methods:{
    onSubmit(){
      this.$emit("func", this.form)
    }
  }
}
</script>


<style>


</style>

