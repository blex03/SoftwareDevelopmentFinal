<template>
  <main class="user-info">
    <h2>User Information</h2>
    <div class="info-container">
      <p><strong>Name:</strong> {{ name }}</p>
      <p><strong>NetID:</strong> {{ username }}</p>
      <p><strong>Account Type:</strong> {{ type }}</p>
    </div>
  </main>
</template>
  

  
  <script>
  import { computed } from 'vue';
  import { useStore } from 'vuex';
  
  export default {
    setup() {
      const store = useStore();
      const username = computed(() => store.state.user.username);
      const name = computed(() => store.state.user.name);
      const type = computed(() => store.state.user.type);
  
      return {
        username,
        name,
        type
      };
    }
  }
  </script>
  
  <style>
.user-info {
  text-align: center;
  font-size: 20px; 
}

.info-container {
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 30px;
  margin-top: 20px;
  background-color: #f5f5f5;
  width: 80%; 
  margin: 0 auto; 
}

.info {
  margin: 15px 0;
  font-size: 24px; 
}
</style>
  
  
