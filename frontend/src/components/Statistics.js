import React from 'react';

const Statistics = ({ statistics }) => {
  if (!statistics) {
    return <div className="statistics">Loading statistics...</div>;
  }

  return (
    <div className="statistics">
      <h2>Statistics</h2>
      <div className="stats-grid">
        <div className="stat-card">
          <h3>Total Students</h3>
          <p className="stat-number">{statistics.total_students}</p>
        </div>
        
        <div className="stat-card">
          <h3>Average GPA</h3>
          <p className="stat-number">{statistics.average_gpa}</p>
        </div>
      </div>
      
      <div className="students-by-major">
        <h3>Students by Major</h3>
        <div className="major-list">
          {Object.entries(statistics.students_by_major).map(([major, count]) => (
            <div key={major} className="major-item">
              <span className="major-name">{major}:</span>
              <span className="major-count">{count}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Statistics;
