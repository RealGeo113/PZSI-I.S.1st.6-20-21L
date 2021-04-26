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

async function addMessages(msg, scroll) {
    if (typeof msg.name !== "undefined") {
        var date = dateNow();

        if (typeof msg.time !== "undefined") {
            var n = msg.time;
        } else {
            var n = date;
        }
        var global_name = await loadName();

        var content =
            '<div class="container">' +
            '<b style="color:#000" class="right">' +
            msg.name +
            "</b><p>" +
            msg.message +
            '</p><span class="time-right">' +
            n +
            "</span></div>";
        if (global_name == msg.name) {
            content =
                '<div class="container darker">' +
                '<b style="color:#000" class="left">' +
                msg.name +
                "</b><p>" +
                msg.message +
                '</p><span class="time-left">' +
                n +
                "</span></div>";
        }
        // update div
        var messageDiv = document.getElementById("messages");
        messageDiv.innerHTML += content;
    }

    if (scroll) {
        scrollSmoothToBottom("messages");
    }
}

async function loadName() {
    return await fetch("/user/get-name")
        .then(async function (response) {
            return await response.json();
        })
        .then(function (text) {
            return text["name"];
        });
}

async function loadRoom() {
    return await fetch("/room/get-id")
        .then(async function (response){
            return await response.json()
        })
        .then(function (text){
            return text["room_id"]
        })
}

async function loadMessages() {
    return await fetch("/get-messages")
        .then(async function (response) {
            return await response.json();
        })
        .then(function (text) {
            console.log(text);
            return text;
        });
}

$(function () {
    $(".msgs").css({ height: $(window).height() * 0.7 + "px" });

    $(window).bind("resize", function () {
        $(".msgs").css({ height: $(window).height() * 0.7 + "px" });
    });
});

function scrollSmoothToBottom(id) {
    var div = document.getElementById(id);
    $("#" + id).animate(
        {
            scrollTop: div.scrollHeight - div.clientHeight,
        },
        500
    );
}

function dateNow() {
    var date = new Date();
    var aaaa = date.getFullYear();
    var gg = date.getDate();
    var mm = date.getMonth() + 1;

    if (gg < 10) gg = "0" + gg;

    if (mm < 10) mm = "0" + mm;

    var cur_day = aaaa + "-" + mm + "-" + gg;

    var hours = date.getHours();
    var minutes = date.getMinutes();
    var seconds = date.getSeconds();

    if (hours < 10) hours = "0" + hours;

    if (minutes < 10) minutes = "0" + minutes;

    if (seconds < 10) seconds = "0" + seconds;

    return cur_day + " " + hours + ":" + minutes;
}







