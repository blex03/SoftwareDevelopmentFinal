<template>
  <main class="home">
    <h2>Home</h2>
        <ul>
          <li>
            <RouterLink :to="{ name: 'student' }" class="student center-hor">Student Login</RouterLink>
          </li>
          <li>
            <RouterLink :to="{ name: 'professor' }" class="professor center-hor">Professor Login</RouterLink>
          </li>
          <li>
            <RouterLink :to="{ name: 'admin' }" class="admin center-hor">Admin Login</RouterLink>
          </li>
        </ul>
  </main>
</template>

<style>

.home body {
  background: white;
  margin: 0px;
  padding: 0px;
}

.home p {
  margin-bottom: 1rem;
}
</style>
