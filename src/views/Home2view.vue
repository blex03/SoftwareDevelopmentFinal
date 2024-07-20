<template>
  <main>
    <h2>Home</h2>
    <div class="login-section">
      <div class="input-field">
        <label for="Netid">NetID:</label>
        <input type="text" id="Netid" v-model="netid" placeholder="Enter your NetID">
      </div>
      <div class="input-field">
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="password" placeholder="Enter your password">
      </div>
      <div class="button-group">
        <button v-for="userType in userTypes" :key="userType" @click="login(userType)">
          {{ userType }} Login
        </button>
      </div>
    </div>
  </main>
</template>

<script>
import axios from 'axios';
import { mapActions } from 'vuex';
import router from '../router';

export default {
  data() {
    return {
      userTypes: ['Student', 'Professor', 'Admin'],
      netid: '',
      password: '' // Ensure secure handling of passwords
    };
  },
  methods: {
    ...mapActions(['setUser']),
    
    async login(userType) {
      try {
        const response = await this.fetchUserDetails(this.netid, this.password);
        console.log(response.data)
        if (response.data) {
          const userData = response.data;
          this.setUser({
            username: userData.Netid,
            name: userData.Name,
            type: userType
          });
            if (userData.Type !== userType) {
            console.error(`Cannot login as ${userType}. Invalid user type.`);
            return; // Exit the function, preventing login
          }
          console.log(`Logged in as ${userData.Name} (${userType})`);
          this.redirectUser(userType);
        } else {
          console.error('User not found or invalid credentials');
        }
      } catch (error) {
        console.error('Login error:', error);
      }
    },

    fetchUserDetails(netid, password) {
      return axios.post('https://kxxirxcj4g.execute-api.us-east-1.amazonaws.com/test/Users', {
        "operation": "read",
        "payload": {
          "Key": {
            "Netid": netid,
            "password": password
          }
        }
      });
    },

    redirectUser(userType) {
      if (userType === 'Student') {
        router.push({ name: 'student' });
      } else if (userType === 'Professor') {
        router.push({ name: 'professor' });
      } else if (userType === 'Admin') {
        router.push({ name: 'admin' });
      }
    }
  }
}
</script>
<style>
.login-page {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f5f5f5;
}

.login-section {
  background-color: white;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
}

.input-field {
  margin-bottom: 15px;
}

.input-field label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.input-field input {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.button-group {
  display: flex;
  justify-content: center;
}

.button-group button {
  padding: 8px 15px;
  border: none;
  border-radius: 4px;
  background-color: #007bff;
  color: white;
  cursor: pointer;
}

.button-group button:not(:last-child) {
  margin-right: 10px;
}
</style>
  
