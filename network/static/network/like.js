function unlike(postId) {
    fetch(`unlike/${postId}`, {
        method: "POST"
    })
        .then(response => console.log(response))

    const btn = document.getElementById(`like-btn/${postId}`)
    btn.textContent = String.fromCodePoint(127770);
    btn.setAttribute('onclick', `like(${postId})`);

    const lks = document.getElementById(`like-count/${postId}`)
    let num = Number(lks.textContent); num = num - 1;
    lks.textContent = num;
}

function like(postId) {
    fetch(`like/${postId}`)
        .then(response => console.log(response))

    const btn = document.getElementById(`like-btn/${postId}`)
    btn.textContent = String.fromCodePoint(127774);
    btn.setAttribute('onclick', `unlike(${postId})`);

    const lks = document.getElementById(`like-count/${postId}`)
    let num = Number(lks.textContent); num = num + 1;
    lks.textContent = num;
}

