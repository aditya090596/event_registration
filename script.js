document.getElementById("registrationForm").addEventListener("submit", async function (e) {
  e.preventDefault();

  // Collect form data
  const formData = {
    cname: document.getElementById("cname").value,
    cemail: document.getElementById("cemail").value,
    eventid: document.getElementById("eventid").value,
    eventname: document.getElementById("eventname").value
  };

  // Replace with your actual API Gateway endpoint URL
  const apiUrl = "https://tslnf4hmmf.execute-api.ap-south-1.amazonaws.com/dev/register";

  try {
    const response = await fetch(apiUrl, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(formData)
    });

    const result = await response.json();
    document.getElementById("responseMessage").innerText = "✅ " + result.message;
  } catch (error) {
    document.getElementById("responseMessage").innerText = "❌ Error: " + error.message;
  }
});
