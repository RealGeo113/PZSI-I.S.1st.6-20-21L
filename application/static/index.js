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