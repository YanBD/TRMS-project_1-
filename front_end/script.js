
async function authorize() {
    const userval = document.getElementById("User").value
    const phrasevar = document.getElementById("phrase").value

    const data = {
        username: userval,
        passphrase: phrasevar
    }

    const url = "http://127.0.0.1:5000/userbase"

    const httpresponse = await fetch(url, {
    method: "PATCH",
    headers: {
    'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
    });
    var employbody = await httpresponse.json()
    sessionStorage.setItem('user',employbody.empId)
    if (employbody) {
        alert (`welcome ${employbody.username}`)
        window.location.href='employee_portal.html'
    } else {
        alert("Login attempt failed")
    }
}
