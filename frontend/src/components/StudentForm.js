import React from 'react';

const StudentForm = ({ 
  formData, 
  onChange, 
  onSubmit, 
  onCancel, 
  isEditing 
}) => {
  return (
    <div className="student-form">
      <h2>{isEditing ? 'Edit Student' : 'Add Student'}</h2>
      <form onSubmit={onSubmit}>
        <div className="form-group">
          <label htmlFor="student_id">Student ID:</label>
          <input
            type="text"
            id="student_id"
            name="student_id"
            value={formData.student_id}
            onChange={onChange}
            required
            disabled={isEditing}
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="name">Name:</label>
          <input
            type="text"
            id="name"
            name="name"
            value={formData.name}
            onChange={onChange}
            required
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="birth_year">Birth Year:</label>
          <input
            type="number"
            id="birth_year"
            name="birth_year"
            value={formData.birth_year}
            onChange={onChange}
            required
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="major">Major:</label>
          <input
            type="text"
            id="major"
            name="major"
            value={formData.major}
            onChange={onChange}
            required
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="gpa">GPA:</label>
          <input
            type="number"
            step="0.1"
            min="0"
            max="4"
            id="gpa"
            name="gpa"
            value={formData.gpa}
            onChange={onChange}
            required
          />
        </div>
        
        <div className="form-buttons">
          <button type="submit">
            {isEditing ? 'Update Student' : 'Add Student'}
          </button>
          {isEditing && (
            <button type="button" onClick={onCancel}>
              Cancel
            </button>
          )}
        </div>
      </form>
    </div>
  );
};

export default StudentForm;
