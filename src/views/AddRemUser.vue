<template>
  <header class="UserManagement">
    <div>
      <h2>User Management</h2>
      <nav>
        <!-- Form for Adding Users -->
        <form @submit.prevent="addUser">
          <h3>Add User</h3>
          <label for="netid">NetID:</label>
          <input type="text" v-model="newUser.Netid" placeholder="NetID">
          <br>

          <label for="password">Password:</label>
          <input type="password" v-model="newUser.password" placeholder="Password">
          <br>

          <label for="name">Name:</label>
          <input type="text" v-model="newUser.Name" placeholder="Name">
          <br>

          <label for="type">Type:</label>
          <select v-model="newUser.Type">
            <option disabled value="">Please select one</option>
            <option>Student</option>
            <option>Professor</option>
            <option>Admin</option>
          </select>
          <br>

          <button type="submit">Add User</button>
        </form>

        <!-- Form for Removing Users -->
        <form @submit.prevent="removeUser">
          <h3>Remove User</h3>
          <label for="remove-netid">NetID:</label>
          <input type="text" v-model="removeUserCredentials.Netid" placeholder="NetID">
          <br>
          <label for="remove-password">Password:</label>
          <input type="password" v-model="removeUserCredentials.password" placeholder="Password">
          <br>
          <button type="submit">Remove User</button>
        </form>
        <ViewUsersComp/>
      </nav>
    </div>
  </header>
</template>

<script>
import axios from 'axios';
import ViewUsersComp from '../components/ViewUsersComp.vue';

export default {
  components: {
      ViewUsersComp
    },

  data() {
    return {
      newUser: {
        Netid: '',
        password: '',
        Name: '',
        Type: ''
      },
      removeUserCredentials: {
        Netid: '',
        password: ''
      }
    };
  },
  methods: {
    addUser() {
    // Constructing the payload with NetID and Password first
    const payload = {
      operation: 'create',
      payload: {
        Item: {
          Netid: this.newUser.Netid,
          password: this.newUser.password,
          Name: this.newUser.Name,
          Type: this.newUser.Type
        }
      }
    };
    axios.post('https://kxxirxcj4g.execute-api.us-east-1.amazonaws.com/test/Users', payload)
      .then(() => {
        console.log('User added successfully', payload);
        this.resetAddForm();
      })
      .catch(error => {
        console.error('Error adding user:', error);
      });
  },
    removeUser() {
      const payload = {
          "operation": "delete",
          "payload": {
              "Key": {
                  "Netid": this.removeUserCredentials.Netid,
                  "password": this.removeUserCredentials.password
              }
          }
      };
      console.log(payload);
      axios.post('https://kxxirxcj4g.execute-api.us-east-1.amazonaws.com/test/Users', payload)
        .then(response => {
          console.log('Response from API:', response.data);
          console.log('User removed successfully');
          this.resetRemoveForm();
        })
        .catch(error => {
          console.error('Error removing user:', error);
        });
    },
    resetAddForm() {
      this.newUser = { Netid: '', password: '', Name: '', Type: '' };
    },
    resetRemoveForm() {
      this.removeUserCredentials = { Netid: '', password: '' };
    }
  }
};
</script>

<style scoped>
    /* give the header itself a background color, a border, and add some padding to the content */
    .UserManagement {
  background-color: #fcfcfc;
  border-bottom: 1px solid #e0e0e0;
  }
  
  /* make the title within the header a larger and bolder font */
  .UserManagement h1 {
  font-size: 2rem;
  font-weight: bold;
  }
  
  input {
    margin-top: 5px;
    margin-bottom: 20px;
    width: 750px;
  }
  
  label {
    margin-right: 10px;
  }
  
  button {
    display: flex;
    justify-content: center;
    margin-top: 20px;
    background: rgb(4, 4, 51);
    color: white;
    width: 100px;
  }
  
  .add_edit{
  display: flex;
  gap: 10px;
  }
  
  .page-elements {
    display: flex;
  }
</style>
