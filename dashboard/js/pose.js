async function loadPose() {

    const data = await fetchData("/pose/latest");

    document.getElementById("pose-data").innerHTML = `
        X: ${data.x} <br>
        Y: ${data.y} <br>
        Theta: ${data.theta} <br>
        Timestamp: ${data.timestamp}
    `;
}