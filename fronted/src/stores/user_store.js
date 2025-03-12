// src/stores/index.js
import { defineStore } from 'pinia';
import Cookies from 'js-cookie';
import axios from "axios";
// import CryptoJS from 'crypto-js'
// import enc from 'crypto-js/enc-utf8'
// useAuthStore 用户身份验证状态
export const useAuthStore = defineStore('auth', {
  state: () => ({
    isRegisterMode: false,
    // 因为使用 window.location.href = '/' 进行页面跳转时，浏览器会加载新的页面。 Pinia 存储的数据会重新初始化。
    token: Cookies.get('token') || '',
    user_id: Cookies.get('user_id') || '',
    user_name: Cookies.get('user_name') || '',
    user_email: Cookies.get('user_email') || '',
    isPersonCenter : false,
  }),
  actions: {
    //通过token与数据库中的db_hash_password进行校验,验证成功则返回true，失败则返回false
    async CheckLogin() {
      if (this.user_id) {
        try {
          const response = await axios.get(`http://127.0.0.1:8000/api/user/${this.user_id}/`);
          const db_hash_password = response.data.password;
          if (this.token === db_hash_password) {
            console.log('通过cookie，登录成功');
            return true;
            // 可以在这里更新 UI 或进行其他操作
          } else {
            console.log('通过cookie，登录失败');
            // 清除 token 和 userid
            Cookies.remove('token');
            Cookies.remove('user_id');
            this.clearToken();
            this.clearUserId();
            return false;
          }
        } catch (error) {
          console.error('请求失败:', error);
          alert('请求失败');
          // 清除 token 和 userid
          Cookies.remove('token');
          Cookies.remove('user_id');
          this.clearToken();
          this.clearUserId();
          return false;
        }
      }else {
        console.log('user_id为空');
        return false;
      }

    },

      //获得登录状态
    getLoginMode() {
      return this.loading;
    },

    toggleRegisterMode() {
      this.isRegisterMode = !this.isRegisterMode;
    },

    clearCookies() {
      Cookies.remove('token');
      Cookies.remove('user_id');
      Cookies.remove('user_name');
      Cookies.remove('user_email');
      Cookies.remove('loading');
      this.clearToken();
      this.clearUserId();
    },

    clearToken() {
      this.token = null;
    },
    getToken() {
      return this.token;
    },
    clearUserId() {
      this.user_id = null;
    },
  },
});