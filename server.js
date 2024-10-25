const express = require('express');
const axios = require('axios');

const app = express();
const port = process.env.PORT || 3000;

// GitHub repo and owner information
const owner = "pacific-devops";  // Replace with your GitHub username or org
const repo = "Hello_master";     // Replace with your repository name

// Endpoint to fetch GitHub Actions workflow run details
app.get('/workflow', async (req, res) => {
  try {
    // Use the GITHUB_TOKEN passed from the GitHub Actions workflow
    const githubToken = process.env.GITHUB_TOKEN;
    
    const response = await axios.get(`https://api.github.com/repos/${owner}/${repo}/actions/runs`, {
      headers: {
        Authorization: `Bearer ${githubToken}`,  // Use the GitHub token for authentication
      }
    });

    const workflowRuns = response.data.workflow_runs[0];  // Get the most recent workflow run

    // Send the workflow run data back to the client (your frontend)
    res.json({
      run_number: workflowRuns.run_number,
      status: workflowRuns.status,
      conclusion: workflowRuns.conclusion,
      commit_sha: workflowRuns.head_sha,
      commit_message: workflowRuns.head_commit.message,
      commit_author: workflowRuns.head_commit.author.name,
      commit_date: workflowRuns.head_commit.timestamp,
      deploy_time: workflowRuns.created_at
    });

  } catch (error) {
    res.status(500).json({ error: 'Error fetching workflow details' });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
