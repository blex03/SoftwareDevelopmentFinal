<template>
    <header class="professor-view">
      <div>
      <h2>Welcome, Professor {{ name }}</h2>
        <nav>
          <ul>
            <li>
              <RouterLink :to="{ name: 'TeachingSchedule' }" class="TeachingSchedule center-hor">Teaching Schedule</RouterLink>
            </li>
            <li>
              <RouterLink :to="{ name: 'ClassRoster' }" class="ClassRoster center-hor">Class Roster</RouterLink>
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
    const name = computed(() => store.state.user.name);

    return {
      name
    };
  }
}
</script>


<style>
/* give the header itself a background color, a border, and add some padding to the content */
.professor-view {
  background-color: #fcfcfc;
  border-bottom: 1px solid #e0e0e0;
}

/* make the title within the header a larger and bolder font */
.professor-view h1 {
  font-size: 2rem;
  font-weight: bold;
}




</style>
