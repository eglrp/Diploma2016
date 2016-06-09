    if __name__ == "__main__":
      try:
        socketio.run(app, host = "0.0.0.0", port = 80)
      except KeyboardInterrupt:
        rtk.server_not_interrupted = False
        rtk.led.blinker_not_interrupted = False
        rtk.waiting_for_single = False

        if rtk.coordinate_thread is not None:
            rtk.coordinate_thread.join()

        if rtk.satellite_thread is not None:
            rtk.satellite_thread.join()

        if rtk.led.blinker_thread is not None:
            rtk.led.blinker_thread.join()

