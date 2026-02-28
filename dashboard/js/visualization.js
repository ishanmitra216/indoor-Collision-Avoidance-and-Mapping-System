async function updateRobotState() {

    const data = await fetchData("/robot/state");

    document.getElementById("robot-state").innerHTML = `
        X: ${data.x} <br>
        Y: ${data.y} <br>
        Theta: ${data.theta} <br>
        Status: ${data.status}
    `;
}

async function updateCollisionStatus() {

    const data = await fetchData("/collision/status");

    document.getElementById("collision-status").innerHTML = `
        Detected: ${data.detected} <br>
        Distance: ${data.distance}
    `;
}