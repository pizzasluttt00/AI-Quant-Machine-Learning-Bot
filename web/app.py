from flask import Flask, render_template, request, redirect, url_for, jsonify import json import os from utils import load_config, save_config

app = Flask(name)

CONFIG_PATH = os.path.join(os.path.dirname(file), '../config.json')

@app.route('/') def dashboard(): config = load_config() return render_template('dashboard.html', config=config)

@app.route('/update_config', methods=['POST']) def update_config(): config = load_config() for key in request.form: value = request.form[key] if value.lower() == 'true': value = True elif value.lower() == 'false': value = False elif value.isdigit(): value = int(value) config_path = key.split("::") ref = config for k in config_path[:-1]: ref = ref.setdefault(k, {}) ref[config_path[-1]] = value

save_config(config)
return redirect(url_for('dashboard'))

@app.route('/config') def view_config(): config = load_config() return jsonify(config)

if name == 'main': app.run(host='0.0.0.0', port=5000, debug=True)


