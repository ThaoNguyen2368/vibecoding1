import React, { useState, useEffect } from 'react';
import axios from 'axios';
import StudentList from './components/StudentList';
import StudentForm from './components/StudentForm';
import Statistics from './components/Statistics';
import './App.css';

function App() {
  const [students, setStudents] = useState([]);
  const [classes, setClasses] = useState([]);
  const [statistics, setStatistics] = useState(null);
  const [formData, setFormData] = useState({
    student_id: '',
    name: '',
    birth_year: '',
    major: '',
    gpa: '',
    class_id: ''
  });
  const [editingId, setEditingId] = useState(null);
  const [searchTerm, setSearchTerm] = useState('');

  useEffect(() => {
    fetchStudents();
    fetchClasses();
    fetchStatistics();
  }, []);

  const fetchStudents = async () => {
    try {
      const response = await axios.get('http://localhost:8000/students');
      setStudents(response.data);
    } catch (error) {
      console.error('Error fetching students:', error);
    }
  };

  const fetchClasses = async () => {
    try {
      const response = await axios.get('http://localhost:8000/classes');
      setClasses(response.data);
    } catch (error) {
      console.error('Error fetching classes:', error);
    }
  };

  const fetchStatistics = async () => {
    try {
      const response = await axios.get('http://localhost:8000/statistics');
      setStatistics(response.data);
    } catch (error) {
      console.error('Error fetching statistics:', error);
    }
  };

  const handleSearch = async () => {
    if (searchTerm.trim()) {
      try {
        const response = await axios.get(`http://localhost:8000/students/search?name=${searchTerm}`);
        setStudents(response.data);
      } catch (error) {
        console.error('Error searching students:', error);
      }
    } else {
      fetchStudents();
    }
  };

  const handleExportCSV = async () => {
    try {
      console.log('Starting CSV export...');
      
      // Check if backend is available
      const healthCheck = await axios.get('http://localhost:8000/');
      console.log('Backend health check:', healthCheck.data);
      
      const response = await axios.get('http://localhost:8000/export/csv', {
        responseType: 'blob'
      });
      
      console.log('Export response status:', response.status);
      console.log('Export response headers:', response.headers);
      console.log('Export response data type:', typeof response.data);
      
      // Create blob from response data
      const blob = new Blob([response.data], { type: 'text/csv;charset=utf-8;' });
      console.log('Blob created:', blob.size, 'bytes');
      
      // Create download link
      const url = window.URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', 'students.csv');
      link.style.visibility = 'hidden';
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      
      // Clean up
      window.URL.revokeObjectURL(url);
      
      console.log('CSV export completed');
    } catch (error) {
      console.error('Error exporting CSV:', error);
      console.error('Error details:', error.response?.data);
      console.error('Error status:', error.response?.status);
      
      if (error.code === 'NETWORK_ERROR' || error.message.includes('Network Error')) {
        alert('Network Error: Backend server is not running!\n\nPlease start the backend server:\ncd D:\\vibe_coding1\\backend\npython main.py');
      } else {
        alert('Error exporting CSV: ' + error.message);
      }
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
        gpa: '',
        class_id: ''
      });
      
      // Refresh data
      fetchStudents();
      fetchStatistics();
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
      gpa: student.gpa,
      class_id: student.class_id || ''
    });
    setEditingId(student.student_id);
  };

  const handleDelete = async (studentId) => {
    if (window.confirm('Are you sure you want to delete this student?')) {
      try {
        await axios.delete(`http://localhost:8000/students/${studentId}`);
        fetchStudents();
        fetchStatistics();
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
      gpa: '',
      class_id: ''
    });
  };

  return (
    <div className="App">
      <h1>Student Management System</h1>
      
      <Statistics statistics={statistics} />
      
      <div className="search-export">
        <div className="search-box">
          <input
            type="text"
            placeholder="Search by name..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && handleSearch()}
          />
          <button onClick={handleSearch}>Search</button>
          {searchTerm && (
            <button onClick={() => {
              setSearchTerm('');
              fetchStudents();
            }}>Clear</button>
          )}
        </div>
        
        <button className="export-btn" onClick={handleExportCSV}>
          Export CSV
        </button>
      </div>
      
      <StudentForm
        formData={formData}
        onChange={handleChange}
        onSubmit={handleSubmit}
        onCancel={handleCancel}
        isEditing={editingId !== null}
        classes={classes}
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
