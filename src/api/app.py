from flask import Flask, request, jsonify
from src.gradebook import Student, GradeBook


def create_app():
    app = Flask(__name__)
    gradebook = GradeBook()

    def student_data(student):
        return {
            "name": student.name,
            "roll_no": student.roll_number,
            "average": student.average()
        }

    @app.post("/students")
    def add_student():
        data = request.get_json(silent=True)

        if not isinstance(data, dict):
            return jsonify(error="Invalid JSON body"), 400

        if "name" not in data or "roll_no" not in data:
            return jsonify(error="Name and roll_no are required"), 400

        if type(data["roll_no"]) is not int or data["roll_no"] <= 0:
            return jsonify(error="Invalid roll number"), 400

        try:
            student = Student(data["name"], data["roll_no"])
            gradebook.add_student(student)
        except (ValueError, TypeError) as e:
            return jsonify(error=str(e)), 400

        return jsonify(student_data(student)), 201

    @app.get("/students/<int:id>")
    def get_student(id):
        student = gradebook.find_student_by_roll_number(id)

        if student is None:
            return jsonify(error="Student not found"), 404

        return jsonify(student_data(student)), 200

    @app.post("/students/<int:id>/scores")
    def add_score(id):
        student = gradebook.find_student_by_roll_number(id)

        if student is None:
            return jsonify(error="Student not found"), 404

        data = request.get_json(silent=True)

        if not isinstance(data, dict) or "score" not in data:
            return jsonify(error="Score is required"), 400

        if len(student.scores) >= 6:
            return jsonify(error="Maximum 6 scores allowed"), 400

        score = data["score"]

        if type(score) not in (int, float) or not 0 <= score <= 100:
            return jsonify(error="Score must be between 0 and 100"), 400

        student.add_score(score)

        return jsonify(
            roll_no=id,
            scores=student.scores
        ), 200

    @app.get("/students/<int:id>/average")
    def get_average(id):
        student = gradebook.find_student_by_roll_number(id)

        if student is None:
            return jsonify(error="Student not found"), 404

        return jsonify(
            roll_no=id,
            average=student.average()
        ), 200

    @app.get("/students")
    def get_all_students():
        return jsonify([
            student_data(student)
            for student in gradebook.students
        ]), 200

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
