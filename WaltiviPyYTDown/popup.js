document.getElementById("download").addEventListener("click", async () => {
  const url = document.getElementById("url").value;
  const status = document.getElementById("status");

  if (!url) {
    status.textContent = "Por favor, insira uma URL.";
    status.className = "status-message error";
    return;
  }

  status.textContent = "Baixando...";
  status.className = "status-message";

  try {
    const response = await fetch("http://localhost:5000/download", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ url }),
    });

    if (!response.ok) throw new Error("Erro ao baixar o vídeo.");

    const blob = await response.blob();
    const downloadUrl = window.URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = downloadUrl;
    a.download = "video.mp4";
    document.body.appendChild(a);
    a.click();
    a.remove();
    status.textContent = "Download concluído!";
    status.className = "status-message success";
  } catch (error) {
    status.textContent = `Erro: ${error.message}`;
    status.className = "status-message error";
  }
});
