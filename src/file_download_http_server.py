    @app.route("/logs/download/<path:log_name>")
    def downloadLog(log_name):
      full_log_path = rtk.logm.log_path + "/" + log_name
      return send_file(full_log_path, as_attachment = True)
