    socket.on("coordinate broadcast", function(msg) {
      if ((active_tab == "Status") && (isActive == true)) {
        console.groupCollapsed('Coordinate msg received:');
        for (var k in msg)
            console.log(k + ':' + msg[k]);
        console.groupEnd();

        updateCoordinateGrid(msg);
      }
    });
