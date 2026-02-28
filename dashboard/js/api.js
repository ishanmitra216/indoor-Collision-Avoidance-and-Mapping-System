const API_BASE = "http://localhost:8000";

async function fetchData(endpoint) {
    const response = await fetch(`${API_BASE}${endpoint}`);
    return await response.json();
}