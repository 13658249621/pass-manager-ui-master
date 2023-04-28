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
      <el-form-item label="类型">
        <el-input v-model="form.type"></el-input>
      </el-form-item>
      <el-form-item label="手机号码">
        <el-input v-model="form.account"></el-input>
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
        type: '',
        account: '',
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

