<template>
    <main class="user-management">
      <h2>User Management</h2>
  
      <!-- Form for Adding Users -->
      <form @submit.prevent="addUser">
        <h3>Add User</h3>
        <div>
          <label for="name">Name:</label>
          <input type="text" id="name" v-model="newUser.Name">
        </div>
        <div>
          <label for="netid">NetID:</label>
          <input type="text" id="netid" v-model= "newUser.NetID">
        </div>
        <div>
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="newUser.password">
        </div>
        <div>
          <label for="type">Type:</label>
          <input type="text" id="type" v-model="newUser.Type">
        </div>
        <button type="submit">Add User</button>
      </form>
  
      <!-- Form for Removing Users -->
      <form @submit.prevent="removeUser">
        <h3>Remove User</h3>
        <div>
          <label for="remove-netid">NetID:</label>
          <input type="text" id="remove-netid" v-model="removeUserCredentials.NetID">
        </div>
        <div>
          <label for="remove-password">Password:</label>
          <input type="password" id="remove-password" v-model="removeUserCredentials.password">
        </div>
        <button type="submit">Remove User</button>
      </form>
    </main>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        newUser: {
          NetID: '',
          password: '',
          Name: '',
          Type: ''
        },
        removeUserCredentials: {
          NetID: '',
          password: ''
        }
      };
    },
    methods: {
      addUser() {
        const payload = {
          operation: 'create',
          payload: {
            Item: this.newUser
          }
        };
        axios.post('https://kxxirxcj4g.execute-api.us-east-1.amazonaws.com/test/Users', payload)
          .then(() => {
            alert('User added successfully');
            this.resetForm();
          })
          .catch(error => {
            console.error('Error adding user:', error);
          });
      },
      removeUser() {
        const payload = {
          operation: 'delete',
          payload: {
            Key: this.removeUserCredentials
          }
        };
        axios.post('https://kxxirxcj4g.execute-api.us-east-1.amazonaws.com/test/Users', payload)
          .then(() => {
            alert('User removed successfully');
            this.resetRemoveForm();
          })
          .catch(error => {
            console.error('Error removing user:', error);
          });
      },
      resetForm() {
        this.newUser = { NetID: '', password: '', Name: '', Type: '' };
      },
      resetRemoveForm() {
        this.removeUserCredentials = { NetID: '', password: '' };
      }
    }
  }
  </script>
  
  <style>
  .user-management {
    /* Styles for your user management component */
  }
  
  .user-management form {
    margin-bottom: 20px;
  }
  
  .user-management label {
    display: block;
    margin-bottom: 5px;
  }
  
  .user-management input {
    margin-bottom: 10px;
    width: 100%;
    padding: 8px;
  }
  
  .user-management button {
    padding: 10px 15px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  .user-management button:hover {
    background-color: #0056b3;
  }
  </style>
  