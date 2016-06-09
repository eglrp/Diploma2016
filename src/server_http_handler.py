    @app.route("/")
    def index():
      rtk.logm.updateAvailableLogs()
      return render_template("index.html", logs = rtk.logm.available_logs, system_status = reach_tools.getSystemStatus())
