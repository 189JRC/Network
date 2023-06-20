function getCookie(name) {
    const cookie = `; ${document.cookie}`;
    const crumbs = cookie.split(`; ${name}=`);
    if (crumbs.length == 2) return crumbs.pop().split(';').shift();
}

function newPost() {
    const newPostContent = document.getElementById("new-post-input").value;
    const userClass = document.querySelector(".user-id");
    const userId = userClass.getAttribute("id");

    fetch(`add_post/${userId}`, {
        method: "POST",
        headers: { "Content-type": "application/json; charset=UTF-8", "X-CSRFToken": getCookie("csrftoken") },
        body: JSON.stringify({ content: newPostContent })
    })
        .then(response => console.log(response.json()))
        //.then prepend post above other posts
        .then(response => window.location.reload())

    document.getElementById("new-post-input").value = " ";

};

function editPost(postId) {
    const self = event.target;
    self.style.display = 'none';
    const input = self.previousElementSibling;
    input.style.display = "block";
    document.getElementById(`delete-post-btn/${postId}`).style.display = "none";
    document.getElementById(`submit-edit-btn/${postId}`).style.display = "inline";
    document.getElementById(`cancel-edit-btn/${postId}`).style.display = "inline";

}

function cancelEdit(postId) {
    const editBtn = document.getElementById(`edit-post-btn/${postId}`);
    editBtn.previousElementSibling.style.display = 'none';
    editBtn.style.display = "inline";
    document.getElementById(`delete-post-btn/${postId}`).style.display = "inline";
    document.getElementById(`submit-edit-btn/${postId}`).style.display = "none";
    document.getElementById(`cancel-edit-btn/${postId}`).style.display = "none";
}

function updatePost(postId) {
    // gets original post's ID and the new content to replace it with
    const originalPost = document.getElementById(`post-text-content/${postId}`);
    console.log(originalPost.textContent);
    const editedPost = document.getElementById(`edit-post-content/${postId}`).value;
    // POST new content to backend, then update html post content
    fetch(`edit_post/${postId}`, {
        method: "POST",
        body: JSON.stringify({ content: editedPost }),
        headers: { "Content-type": "application/json; charset=UTF-8", "X-CSRFToken": getCookie("csrftoken") },
    })
        .then(originalPost.textContent = `${editedPost}`);
    cancelEdit(postId);
}

function deletePost(postId) {
    //send Get request for post to be deleted
    fetch(`delete_post/${postId}`)
        .then(response => {
            if (!response.ok) {
                console.log("problem deleting post");
            } else {
                // remove post from index page and shift other posts by deleting <br>
                const post = document.getElementById(`post-tile/${postId}`);
                post.remove();
            }
        })
}