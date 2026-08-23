from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

SCHOOLS = [
    {"id": 1, "name": "Lahore Grammar School", "logo": "logo.jpg", "branches": [
        {"id": 101, "name": "LGS Multan Cantt", "image": "logo.jpg", "address": "Multan Cantt, Multan, Punjab", "classes": "Playgroup – A Level", "curriculum": "Cambridge", "gender": "Co-education", "facilities": ["Sports", "Science Labs", "Library", "Computer Lab"], "verified": "August 2026"},
        {"id": 102, "name": "LGS Multan Gulgasht", "image": "logo.jpg", "address": "Gulgasht Colony, Multan, Punjab", "classes": "Playgroup – O Level", "curriculum": "Cambridge", "gender": "Co-education", "facilities": ["Sports", "Library", "Computer Lab"], "verified": "August 2026"}]},
    {"id": 2, "name": "Beaconhouse School System", "logo": "logo.jpg", "branches": [
        {"id": 201, "name": "Beaconhouse Multan Cantt", "image": "logo.jpg", "address": "Multan Cantt, Multan, Punjab", "classes": "Early Years – A Level", "curriculum": "Cambridge", "gender": "Co-education", "facilities": ["Sports", "Library", "Computer Lab", "Transport"], "verified": "August 2026"}]},
    {"id": 3, "name": "The City School", "logo": "logo.jpg", "branches": [
        {"id": 301, "name": "The City School Bosan Road", "image": "logo.jpg", "address": "Bosan Road, Multan, Punjab", "classes": "Playgroup – A Level", "curriculum": "Cambridge", "gender": "Co-education", "facilities": ["Sports", "Science Labs", "Library"], "verified": "July 2026"}]},
    {"id": 4, "name": "Bloomfield Hall School", "logo": "logo.jpg", "branches": [
        {"id": 401, "name": "Bloomfield Hall Mumtazabad", "image": "logo.jpg", "address": "Mumtazabad, Multan, Punjab", "classes": "Playgroup – O Level", "curriculum": "Cambridge", "gender": "Co-education", "facilities": ["Sports", "Library", "Transport"], "verified": "August 2026"}]}
]

@app.route("/")
def home():
    return render_template("index.html", schools=SCHOOLS, total_branches=sum(len(s["branches"]) for s in SCHOOLS))

@app.route("/schools")
def schools():
    q = request.args.get("q", "").strip().lower()
    results = [s for s in SCHOOLS if not q or q in s["name"].lower()]
    return render_template("schools.html", schools=results, query=request.args.get("q", ""))

@app.route("/school/<int:school_id>")
def school(school_id):
    school = next((s for s in SCHOOLS if s["id"] == school_id), None)
    if not school:
        return "School not found", 404
    return render_template("school.html", school=school)

@app.route("/school/<int:school_id>/branch/<int:branch_id>")
def branch(school_id, branch_id):
    school = next((s for s in SCHOOLS if s["id"] == school_id), None)
    if not school:
        return "School not found", 404
    branch = next((b for b in school["branches"] if b["id"] == branch_id), None)
    if not branch:
        return "Branch not found", 404
    return render_template("branch.html", school=school, branch=branch)

@app.route("/api/schools")
def api_schools():
    return jsonify(SCHOOLS)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
