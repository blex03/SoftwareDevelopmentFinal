<template>
    <header class="AddRemCourse">
      <div>
      <h2>Course Management</h2>
        <nav>
          <b>Add/Edit Course: </b>
          <div class="page-elements">
            <form @submit.prevent="submitForm">
              <label for="id">Course ID:</label>
              <input type="number" v-model.number="course.CourseID" placeholder="Course ID">
              <br>
  
              <label for="subject">Subject Area:</label>
              <input type="text" v-model="course.Subject_Area" placeholder="Subject Area">
              <br>
  
              <label for="coursenum">Course Number:</label>
              <input type="number" v-model.number="course.Course_Number" placeholder="Course Number">
              <br>
  
              <label for="coursename">Course Name:</label>
              <input type="text" v-model="course.Course_Name" placeholder="Course Name">
              <br>
  
              <label for="professor">Professor:</label>
              <input type="text" v-model="course.Instructor" placeholder="Professor">
              <br>
  
              <label for="description">Description:</label>
              <input type="text" v-model="course.Description" placeholder="Course Description">
              <br>
              <div class="add_edit">
                <button @click="setOperation('create')">Add Course</button>
                <button @click="setOperation('update')">Edit Course</button>
              </div>
              
              <br>
              <br>
              <b>Remove Course:</b>
              <br>
              <label for="remove_id">Course ID:</label>
              <input type="number" v-model.number="course.CourseID_Remove" placeholder="Course ID">
              <br>
              <button @click="setOperation('delete')">Remove Course</button>
            </form>
            <ViewCourseComponent/>
          </div>
          <RouterLink :to="{ name: 'home' }" class="signout">Sign Out</RouterLink>
          
        </nav>
        
      </div>
    </header>
  </template>
  
  <script>
  import axios from 'axios';
  import ViewCourseComponent from '../components/ViewCourseComponent.vue';
  
  export default {
    components: {
      ViewCourseComponent
    },
  
  
  data() {
    return {
      course: {
        CourseID: null,
        Course_Name: '',
        Course_Number: null,
        Description: '',
        Instructor: '',
        Subject_Area: '',
      },
      currentOperation: "create",
    };
  },
  methods: {
    setOperation(operation) {
      this.currentOperation = operation;
      this.submitCourse(); // Call submitCourse after setting the operation
    },
    submitCourse() {
      let payload;
  
      if (this.currentOperation === 'create') {
        payload = {
          operation: 'create',
          payload: {
            Item: { ...this.course },
          },
        };
      } else if (this.currentOperation === 'update') {
        payload = {
          operation: 'update',
          payload: {
            Key: {
              CourseID: this.course.CourseID,
            },
            UpdateExpression: 'set Course_Name = :name, Course_Number = :number, Description = :desc, Instructor = :instr, Subject_Area = :area',
            ExpressionAttributeValues: {
              ':name': this.course.Course_Name,
              ':number': this.course.Course_Number,
              ':desc': this.course.Description,
              ':instr': this.course.Instructor,
              ':area': this.course.Subject_Area,
            },
            ReturnValues: 'UPDATED_NEW',
          },
        };
      } else if (this.currentOperation === 'delete') {
        payload = {
          operation: 'delete',
          payload: {
            Key: {
              CourseID: this.course.CourseID_Remove,
            },
          },
        };
      }
      console.log(this.currentOperation, payload)
  
      axios.post('https://kxxirxcj4g.execute-api.us-east-1.amazonaws.com/test//CourseDB', payload)
        .then(response => {
          console.log('Response from API:', response.data);
          this.resetForm();
          // Handle the response as needed
        })
        .catch(error => {
          console.error('Error:', error);
          // Handle any errors
        });
    },
  resetForm() {
    this.course = {
      CourseID: null,
      Course_Name: '',
      Course_Number: null,
      Description: '',
      Instructor: '',
      Subject_Area: '',
    };
  },

  }
  };
  </script>
  
  
  
  <style scoped>
  /* give the header itself a background color, a border, and add some padding to the content */
  .AddRemCourse {
  background-color: #fcfcfc;
  border-bottom: 1px solid #e0e0e0;
  }
  
  /* make the title within the header a larger and bolder font */
  .AddRemCourse h1 {
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