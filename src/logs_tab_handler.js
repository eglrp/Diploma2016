    $(document).on("click", ".logs_page", function() {
      socket.emit("get logs list");
      socket.emit("get available space");
    });
