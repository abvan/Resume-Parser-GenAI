
// Sample candidate data
const candidateData = [
  {
    name: "John Smith",
    experience: "5",
    role: "SAP Developer",
    jobId: "SG-SAP-001",
    matchScore: 92,
    comment: "Excellent SAP ABAP skills and strong experience with S/4HANA implementation."
  },
  {
    name: "Emily Johnson",
    experience: "3",
    role: "Data Engineer",
    jobId: "SG-DE-002",
    matchScore: 85,
    comment: "Good Python and SQL skills, but lacks direct experience with cloud platforms like Azure."
  },
  {
    name: "Michael Brown",
    experience: "7",
    role: "SAP Developer",
    jobId: "SG-SAP-001",
    matchScore: 95,
    comment: "Outstanding candidate with comprehensive SAP expertise and leadership experience."
  },
  {
    name: "Sarah Davis",
    experience: "2",
    role: "Data Analyst",
    jobId: "SG-DA-003",
    matchScore: 68,
    comment: "Limited experience with advanced analytics tools, requires significant training."
  },
  {
    name: "Alex Chen",
    experience: "6",
    role: "Data Engineer",
    jobId: "SG-DE-002",
    matchScore: 89,
    comment: "Strong technical skills in big data technologies and cloud architecture."
  },
  {
    name: "Maria Garcia",
    experience: "4",
    role: "PBI Engineer",
    jobId: "SG-PBI-004",
    matchScore: 78,
    comment: "Good Power BI skills but needs improvement in DAX and M language."
  },
  {
    name: "David Wilson",
    experience: "1",
    role: "Data Analyst",
    jobId: "SG-DA-003",
    matchScore: 55,
    comment: "Entry-level candidate, insufficient experience for the role requirements."
  },
  {
    name: "Lisa Wang",
    experience: "8",
    role: "Consultant",
    jobId: "SG-CON-005",
    matchScore: 91,
    comment: "Exceptional analytical skills and proven track record in client management."
  },
  {
    name: "Robert Taylor",
    experience: "5",
    role: "Data Engineer",
    jobId: "SG-DE-002",
    matchScore: 82,
    comment: "Solid foundation in data engineering, good potential for growth."
  },
  {
    name: "Jennifer Lee",
    experience: "3",
    role: "SAP Developer",
    jobId: "SG-SAP-001",
    matchScore: 74,
    comment: "Moderate SAP skills, would benefit from additional FIORI training."
  },
  {
    name: "Thomas Anderson",
    experience: "2",
    role: "PBI Engineer",
    jobId: "SG-PBI-004",
    matchScore: 61,
    comment: "Basic Power BI knowledge, lacks experience with complex data modeling."
  },
  {
    name: "Amanda Rodriguez",
    experience: "6",
    role: "Data Analyst",
    jobId: "SG-DA-003",
    matchScore: 87,
    comment: "Strong statistical analysis background and excellent visualization skills."
  },
  {
    name: "Kevin Brown",
    experience: "4",
    role: "Data Engineer",
    jobId: "SG-DE-002",
    matchScore: 45,
    comment: "Limited technical skills, requires extensive training in modern data technologies."
  },
  {
    name: "Sophie Martin",
    experience: "2",
    role: "Data Analyst",
    jobId: "SG-DA-003",
    matchScore: 35,
    comment: "Insufficient experience and skills for the position requirements."
  }
];

// Show loading for 3 seconds, then show results
// setTimeout(() => {
//   document.getElementById('loadingOverlay').style.display = 'none';
//   document.getElementById('resultsContainer').style.display = 'block';
//   populateTable();
// }, 3000);

// Populate table immediately when page loads
document.addEventListener('DOMContentLoaded', function() {
  //populateTable();
});

function populateTable() {
  const tableBody = document.getElementById('tableBody');
  tableBody.innerHTML = '';
  candidateData.forEach(candidate => {
    const row = document.createElement('tr');
    
    // Determine score class
    let scoreClass = 'score-fair';
    if (candidate.matchScore >= 85) scoreClass = 'score-excellent';
    else if (candidate.matchScore >= 70) scoreClass = 'score-good';
    // Determine verdict based on match score
    let verdict = '';
    let verdictClass = '';
    if (candidate.matchScore >= 65) {
      verdict = 'Shortlist';
      verdictClass = 'status-shortlist';
    } else if (candidate.matchScore >= 40) {
      verdict = 'Hold';
      verdictClass = 'status-hold';
    } else {
      verdict = 'Reject';
      verdictClass = 'status-reject';
    }
    row.innerHTML = `
      <td><span class="candidate-name">${candidate.name}</span></td>
      <td>${candidate.experience}</td>
      <td><span class="role-badge">${candidate.role}</span></td>
      <td><span class="job-id">${candidate.jobId}</span></td>
      <td><span class="match-score ${scoreClass}">${candidate.matchScore}%</span></td>
      <td><span class="status-badge ${verdictClass}">${verdict}</span></td>
      <td class="comment-cell">${candidate.comment}</td>
    `;
    
    tableBody.appendChild(row);
  });
}