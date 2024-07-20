// this file creates the router instance that is used by our application

// we start by importing the createRouter and createWebHistory functions, as well as the components describing each of our views
import { createRouter, createWebHistory } from "vue-router";
import { createStore } from 'vuex';
import HomeView from "../views/Home2View.vue";
import StudentView from "../views/StudentView.vue";
import ProfessorView from "../views/ProfessorView.vue";
import AdminView from "../views/AdminView.vue";
import CourseView from  "../views/CourseView.vue";
import TeachingSchedule from "../views/TeachingSchedule.vue";
import ClassRoster from "../views/ClassRoster.vue";
import ProfileView from "../views/ProfileView.vue";
import StudentSchedule from "../views/StudentSchedule.vue";
import AddRemCourse from "../views/AddRemCourse.vue";
import AddRemUser from "../views/AddRemUser.vue";


const router = createRouter({
  // the history mode determines how vue router interacts with the url.
  // createWebHistory() simulates the default browser behavior of changing
  // the path of the url based on the current document.
  // import.meta.env.BASE_URL is a vite feature that you don't need to worry about
  // and can safely use. it refers to the current path to the directory being
  // served by vite, which in this project is always the same directory
  // (and therefore import.meta.env.BASE_URL is '/')
  history: createWebHistory(import.meta.env.BASE_URL),

  // each entry to this routes array has a path (what goes in the URL to access
  // this page), a name (check out components/AppHeader.vue for how this is used)
  // and, most importantly, the component that should be rendered for the view
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/student",
      name: "student",
      component: StudentView
    },
    {
      path: "/student/StudentSchedule",
      name: "StudentSchedule",
      component: StudentSchedule
    },
    {
      path: "/student/Courses",
      name: "Courses",
      component: CourseView
    },
    {
      path: "/student/ProfileView",
      name: "ProfileView",
      component: ProfileView
    },
    {
      path: "/professor",
      name: "professor",
      component: ProfessorView
    },
    {
      path: "/professor/TeachingSchedule",
      name: "TeachingSchedule",
      component: TeachingSchedule
    },
    {
      path: "/professor/ClassRoster",
      name: "ClassRoster",
      component: ClassRoster
    },
    {
      path: "/professor/ProfileView",
      name: "ProfileView",
      component: ProfileView
    },
    {
      path: "/admin",
      name: "admin",
      component: AdminView
    },
    {
      path: "/admin/AddRemUser",
      name: "AddRemUser",
      component: AddRemUser
    },
    {
      path: "/admin/AddRemCourse",
      name: "AddRemCourse",
      component: AddRemCourse
    },
  ],
});

export default router;

