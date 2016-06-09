    $(document).on("click", "#start_button", function(e) {
      var mode = $("input[name=radio_base_rover]:checked").val();
      console.log("Starting " + mode);
      socket.emit("start " + mode);

      if (mode == "base") {
        chart.cleanStatus(mode, "started");
      }

      $('#start_button').css('display', 'none');
      $('#stop_button').css('display', 'inline-block');
    });
