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
    fetch("/edit-note", {
        method: "POST",
        body: JSON.stringify({note_id: note_id}),
    }).then((_res) => {
        window.location.href = "/add-note";
    });
}