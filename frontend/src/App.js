import React, { useState, useEffect } from 'react';
import axios from 'axios';
import StudentList from './components/StudentList';
import StudentForm from './components/StudentForm';
import './App.css';

function App() {
  const [students, setStudents] = useState([]);
  const [formData, setFormData] = useState({
    student_id: '',
    name: '',
    birth_year: '',
    major: '',
    gpa: ''
  });
  const [editingId, setEditingId] = useState(null);

  useEffect(() => {
    fetchStudents();
  }, []);

  const fetchStudents = async () => {
    try {
      const response = await axios.get('http://localhost:8000/students');
      setStudents(response.data);
    } catch (error) {
      console.error('Error fetching students:', error);
    }
  };

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (editingId) {
        await axios.put(`http://localhost:8000/students/${editingId}`, formData);
        setEditingId(null);
      } else {
        await axios.post('http://localhost:8000/students', formData);
      }
      
      // Reset form
      setFormData({
        student_id: '',
        name: '',
        birth_year: '',
        major: '',
        gpa: ''
      });
      
      // Refresh student list
      fetchStudents();
    } catch (error) {
      console.error('Error saving student:', error);
      alert(error.response?.data?.detail || 'Error saving student');
    }
  };

  const handleEdit = (student) => {
    setFormData({
      student_id: student.student_id,
      name: student.name,
      birth_year: student.birth_year,
      major: student.major,
      gpa: student.gpa
    });
    setEditingId(student.student_id);
  };

  const handleDelete = async (studentId) => {
    if (window.confirm('Are you sure you want to delete this student?')) {
      try {
        await axios.delete(`http://localhost:8000/students/${studentId}`);
        fetchStudents();
      } catch (error) {
        console.error('Error deleting student:', error);
      }
    }
  };

  const handleCancel = () => {
    setEditingId(null);
    setFormData({
      student_id: '',
      name: '',
      birth_year: '',
      major: '',
      gpa: ''
    });
  };

  return (
    <div className="App">
      <h1>Student Management System</h1>
      
      <StudentForm
        formData={formData}
        onChange={handleChange}
        onSubmit={handleSubmit}
        onCancel={handleCancel}
        isEditing={editingId !== null}
      />
      
      <StudentList
        students={students}
        onEdit={handleEdit}
        onDelete={handleDelete}
      />
    </div>
  );
}

export default App;
