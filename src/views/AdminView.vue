<template>
  <header class="admin-view">
    <div>
    <h2>Administrator</h2>
      <nav>
        <ul>
          <li>
            <RouterLink :to="{ name: 'AddRemCourse' }" class="AddRemCourse center-hor">Add and Remove Course</RouterLink>
          </li>
          <li>
            <RouterLink :to="{ name: 'AddRemUser' }" class="AddRemUser center-hor">Add and Remove Users</RouterLink>
          </li>
          <li>
            <RouterLink :to="{ name: 'home' }" class="signout">Sign Out</RouterLink>
          </li>
        </ul>
      </nav>
    </div>
  </header>
</template>


<style>
/* give the header itself a background color, a border, and add some padding to the content */
.admin-view {
background-color: #fcfcfc;
border-bottom: 1px solid #e0e0e0;
}
/* make the title within the header a larger and bolder font */
.admin-view h1 {
font-size: 2rem;
font-weight: bold;
}
</style>