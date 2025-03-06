// src/stores/index.js
import { defineStore } from 'pinia';
import Cookies from 'js-cookie';
import axios from "axios";

// useAuthStore 用户身份验证状态
export const useAuthStore = defineStore('auth', {
  state: () => ({
    isRegisterMode: false,
    loading: false,
    token: Cookies.get('token') || '',
    user_id: Cookies.get('user_id') || '',
  }),
  actions: {
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

    toggleRegisterMode() {
      this.isRegisterMode = !this.isRegisterMode;
    },
    setRegisterMode(mode) {
      this.isRegisterMode = mode;
    },

    clearCookies() {
      Cookies.remove('token');
      Cookies.remove('user_id');
      this.clearToken();
      this.clearUserId();
    },

    // 设置token
    setToken(token) {
      this.token = token;
    },
    clearToken() {
      this.token = null;
    },
    getToken() {
      return this.token;
    },
    getUserId() {
      return this.user_id;
    },
    clearUserId() {
      this.user_id = null;
    },


    toggleLoginMode() {
      this.loading = !this.loading;
    },
    setLoginMode(mode) {
      this.loading = mode;
    },
  },
});