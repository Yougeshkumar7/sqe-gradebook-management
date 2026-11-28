import pytest
from src.api.app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


@pytest.fixture
def student(client):
    response = client.post("/students", json={
        "name": "Ali",
        "roll_no": 101
    })
    assert response.status_code == 201
    return 101


def test_create_student(client):
    response = client.post("/students", json={
        "name": "Ali",
        "roll_no": 101
    })

    assert response.status_code == 201
    assert response.is_json
    assert response.get_json() == {
        "name": "Ali",
        "roll_no": 101,
        "average": 0.0
    }


def test_get_student(client, student):
    response = client.get("/students/101")

    assert response.status_code == 200
    assert response.is_json
    assert response.get_json() == {
        "name": "Ali",
        "roll_no": 101,
        "average": 0.0
    }


def test_add_score(client, student):
    response = client.post(
        "/students/101/scores",
        json={"score": 80}
    )

    assert response.status_code == 200
    assert response.is_json
    assert response.get_json() == {
        "roll_no": 101,
        "scores": [80]
    }


def test_get_average(client, student):
    client.post("/students/101/scores", json={"score": 80})
    client.post("/students/101/scores", json={"score": 90})

    response = client.get("/students/101/average")

    assert response.status_code == 200
    assert response.is_json
    assert response.get_json() == {
        "roll_no": 101,
        "average": 85.0
    }


def test_get_all_students(client, student):
    response = client.get("/students")

    assert response.status_code == 200
    assert response.is_json
    assert response.get_json() == [{
        "name": "Ali",
        "roll_no": 101,
        "average": 0.0
    }]


# Task 4 - Negative and Boundary Tests

def test_student_not_found(client):
    response = client.get("/students/999")

    assert response.status_code == 404
    assert "error" in response.get_json()


@pytest.mark.parametrize("score", [-1, 101, "abc"])
def test_invalid_score(client, student, score):
    response = client.post(
        "/students/101/scores",
        json={"score": score}
    )

    assert response.status_code == 400
    assert "error" in response.get_json()


def test_missing_name(client):
    response = client.post("/students", json={
        "roll_no": 102
    })

    assert response.status_code == 400
    assert "error" in response.get_json()
    assert "name" in response.get_json()["error"].lower()


def test_seventh_score(client, student):
    for i in range(6):
        response = client.post(
            "/students/101/scores",
            json={"score": 80}
        )
        assert response.status_code == 200

    response = client.post(
        "/students/101/scores",
        json={"score": 90}
    )

    assert response.status_code == 400
    assert "6" in response.get_json()["error"]


@pytest.mark.parametrize("score", [0, 100])
def test_valid_boundary_score(client, student, score):
    response = client.post(
        "/students/101/scores",
        json={"score": score}
    )

    assert response.status_code == 200
    assert response.get_json()["scores"] == [score]



# Task 5 - Schema and Contract Testing

def test_students_schema(client, student):
    response = client.get("/students")

    assert response.status_code == 200
    assert response.is_json

    data = response.get_json()

    assert isinstance(data, list)
    assert len(data) == 1

    for item in data:
        assert set(item.keys()) == {
            "name", "roll_no", "average"
        }

        assert isinstance(item["name"], str)
        assert type(item["roll_no"]) is int
        assert type(item["average"]) in (int, float)

    assert data[0]["name"] == "Ali"
    assert data[0]["roll_no"] == 101
    assert data[0]["average"] == 0.0

