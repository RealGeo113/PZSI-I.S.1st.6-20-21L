/*
    w folderze static umieszczamy wszystkie skrypty ktore sa statyczne
    tzn maja wplyw na nasze strony ale one sa niezmienne
    np. skrypty js'a, arkusze css etc.
 */

function deleteRoom(room_id){
    fetch("/delete-room", {
        method: "POST",
        body: JSON.stringify({room_id: room_id}),
    }).then((_res) => {
        window.location.href = "/rooms";
    });
}


function deleteNote(note_id){
    fetch("/delete-note", {
        method: "POST",
        body: JSON.stringify({note_id: note_id}),
    }).then((_res) => {
        window.location.href = "/notes";
    });
}


function editNote(note_id){
    fetch("/edit_note/", {
        method: "POST",
        body: JSON.stringify({note_id: note_id}),
    }).then((_res) => {
        window.location.href = "/edit-note/" + note_id;
    });
}

function addUser(user_id){
    fetch("/add-user", {
        method: "POST",
        body: JSON.stringify({user_id: user_id}),
    }).then((_res) => {
        window.location.href = "/users";
    });
}

function acceptUser(relation_id){
    fetch("/accept-user", {
        method: "POST",
        body: JSON.stringify({relation_id: relation_id}),
    }).then((_res) => {
        window.location.href = "/friends";
    });
}

function declineUser(relation_id){
    fetch("/decline-user", {
        method: "POST",
        body: JSON.stringify({relation_id: relation_id}),
    }).then((_res) => {
        window.location.href = "/users";
    });
}

function blockUser(relation_id){
    fetch("/block-user", {
        method: "POST",
        body: JSON.stringify({relation_id: relation_id}),
    }).then((_res) => {
        window.location.href = "/friends";
    });
}