var updateBtns = document.getElementsByClassName('like-post')
var bookmarkbtns = document.getElementsByClassName('bookmark')
var rmbookmarks = document.getElementsByClassName('remove-bookmark')


for (i=0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var postId = this.dataset.product
        var action = this.dataset.action
        var user = this.dataset.user
        console.log('postId: ', postId, 'Action: ', action)
        console.log('USER:', user)

        if (user == 'AnonymousUser'){
            console.log('User is not authenticated')
        }else{
            updatePostLikes(postId, action)
        }
    })
}


for (i=0; i < bookmarkbtns.length; i++){
    bookmarkbtns[i].addEventListener('click', function(){
        var postId = this.dataset.product
        var action = this.dataset.action
        var user = this.dataset.user
        console.log('postId: ', postId, 'Action: ', action)
        console.log('USER:', user)

        if (user == 'AnonymousUser'){
            console.log('User is not authenticated')
        }else{
            addToBookmarks(postId, action)
        }
    })
}


for (i=0; i < rmbookmarks.length; i++){
    rmbookmarks[i].addEventListener('click', function(){
        var postId = this.dataset.product
        var action = this.dataset.action
        var user = this.dataset.user
        console.log('postId: ', postId, 'Action: ', action)
        console.log('USER:', user)

        if (user == 'AnonymousUser'){
            console.log('User is not authenticated')
        }else{
            removeBookmark(postId, action)
        }
    })
}


function removeBookmark(postId, action){
    console.log('User is authenticated, sending data...')
    var url ='http://localhost:8000/remove_bookmark'
    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'postId': postId, 'action': action})

    })
    .then((response) =>{
        return response.json();
    })
    .then((data) => {
        console.log('Data: ', data)
        location.reload()
    }); 
}


function addToBookmarks(postId, action){
    console.log('User is authenticated, sending data...')
    var url ='http://localhost:8000/add_bookmark'
    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'postId': postId, 'action': action})

    })
    .then((response) =>{
        return response.json();
    })
    .then((data) => {
        console.log('Data: ', data)
        location.reload()
    }); 
}


function updatePostLikes(postId, action){
    console.log('User is authenticated, sending data...')
    var url ='http://localhost:8000/like_post'
    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'postId': postId, 'action': action})

    })
    .then((response) =>{
        return response.json();
    })
    .then((data) => {
        console.log('Data: ', data)
        location.reload()
    });
}