async function loadMap() {

    const data = await fetchData("/map/latest");

    if (!data.map_data_base64) return;

    const canvas = document.getElementById("mapCanvas");
    const ctx = canvas.getContext("2d");

    const width = data.width;
    const height = data.height;

    canvas.width = width;
    canvas.height = height;

    const binary = atob(data.map_data_base64);
    const buffer = new Uint8Array(binary.length);

    for (let i = 0; i < binary.length; i++) {
        buffer[i] = binary.charCodeAt(i);
    }

    const imageData = ctx.createImageData(width, height);

    for (let i = 0; i < buffer.length; i++) {

        let value = buffer[i];

        let color;

        if (value === 100) {
            color = 0;   // Occupied → Black
        } else if (value === 0) {
            color = 255; // Free → White
        } else {
            color = 127; // Unknown → Gray
        }

        imageData.data[i*4] = color;
        imageData.data[i*4 + 1] = color;
        imageData.data[i*4 + 2] = color;
        imageData.data[i*4 + 3] = 255;
    }

    ctx.putImageData(imageData, 0, 0);
}