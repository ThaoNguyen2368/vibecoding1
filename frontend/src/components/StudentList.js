import React from 'react';

const StudentList = ({ students, onEdit, onDelete }) => {
  return (
    <div className="student-list">
      <h2>Student List</h2>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Major</th>
            <th>GPA</th>
            <th>Class</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {students.map((student) => (
            <tr key={student.id}>
              <td>{student.student_id}</td>
              <td>{student.name}</td>
              <td>{student.major}</td>
              <td>{student.gpa}</td>
              <td>{student.class_info ? student.class_info.class_name : '-'}</td>
              <td>
                <button 
                  onClick={() => onEdit(student)}
                  className="edit-btn"
                >
                  Edit
                </button>
                <button 
                  onClick={() => onDelete(student.student_id)}
                  className="delete-btn"
                >
                  Delete
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default StudentList;
