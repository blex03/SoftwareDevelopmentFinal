<template>
  <header class="student-view">
    <div>
      <h2>Hello Student: {{ username }}</h2>
      <nav>
        <ul>
          <li>
            <RouterLink :to="{ name: 'StudentSchedule' }" class="StudentSchedule center-hor">View Class Schedule</RouterLink>
          </li>
          <li>
            <RouterLink :to="{ name: 'Courses' }" class="Courses center-hor">Add/Drop Classes</RouterLink>
          </li>
          <li>
            <RouterLink :to="{ name: 'ProfileView' }" class="ProfileView center-hor">View Profile</RouterLink>
          </li>
          <li>
            <RouterLink :to="{ name: 'home' }" class="signout">Sign Out</RouterLink>
          </li>
        </ul>
      </nav>
    </div>
  </header>
</template>

<script>
import { computed } from 'vue';
import { useStore } from 'vuex';

export default {
  setup() {
    const store = useStore();
    const username = computed(() => store.state.user.username);

    return {
      username
    };
  }
}
</script>

<style>
/* give the header itself a background color, a border, and add some padding to the content */

</style>