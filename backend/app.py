import React, { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);

  const uploadFile = async () => {
    if (!file) {
      alert("Please select a file");
      return;
    }

    const formData = new FormData();
    formData.append("resume", file);

    try {
      console.log("File selected:", file);

      const res = await axios.post(
        "https://resume-analyzer-5aeq.onrender.com/analyze",
        formData
      );

      console.log("RESULT FROM BACKEND:", res.data);

      setResult(res.data);
    } catch (error) {
      console.error("Error:", error);
      alert("Error connecting to backend");
    }
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>🚀 AI Resume Analyzer</h1>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <br /><br />

      <button onClick={uploadFile}>Analyze Resume</button>

      {result && (
        <div style={{ marginTop: "30px" }}>
          <h3>ATS Score: {result.score}%</h3>

          <h4>Skills Found:</h4>
          <p>{result.skills_found.join(", ")}</p>

          <h4>Job Match:</h4>
          <p>
            Software Engineer: {result.job_match.software_engineer}%
          </p>
          <p>
            Data Scientist: {result.job_match.data_scientist}%
          </p>

          <h4>Missing Skills:</h4>
          <p>{result.missing_skills.software_engineer.join(", ")}</p>

          <h4>🤖 AI Feedback:</h4>
          <ul>
            {result.ai_feedback.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;