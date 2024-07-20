<template>
  <header class="Users">
    <div>
      <nav>
        <b>Users:</b>
        <ul v-if="users.length > 0">
          <li v-for="user in users" :key="user.Netid">
            Netid: {{ user.Netid }} - Password: {{ user.password }} - Name: {{ user.Name }} - Account Type: {{ user.Type }}
          </li>
        </ul>
        <p v-else>
          No users found.
        </p>
      </nav>
    </div>
  </header>
</template>

<script>
import axios from 'axios';

export default {
  data() {
      return {
          users: [], // Changed to 'users'
      };
  },
  created() {
      this.fetchUsers(); // Fetch users when the component is created
  },
  methods: {
      fetchUsers() {
          const payload = {
              operation: 'scan',
              payload: {} 
          };
          axios.post('https://kxxirxcj4g.execute-api.us-east-1.amazonaws.com/test/Users', payload)
              .then(response => {
                  console.log('Users fetched:', response.data);
                  this.users = response.data; // Assuming response.data contains the array of users
                  console.log('Users fetched:', this.users);
              })
              .catch(error => {
                  console.error('Error fetching users:', error);
              });
      },
  }
};
</script>

<style>
  /* Your styles for the Users component */
</style>
