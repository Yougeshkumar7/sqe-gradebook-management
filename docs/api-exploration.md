# Lab 12 - Manual API Exploration

## POST /students

Request body: {"name":"Ali","roll_no":101}

Response:
{
  "average": 0.0,
  "name": "Ali",
  "roll_no": 101
}

HTTP Status: 201

## GET /students/101

Request body: 

Response:
{
  "average": 0.0,
  "name": "Ali",
  "roll_no": 101
}

HTTP Status: 200

## POST /students/101/scores

Request body: {"score":80}

Response:
{
  "roll_no": 101,
  "scores": [
    80
  ]
}

HTTP Status: 200

## POST /students/101/scores

Request body: {"score":90}

Response:
{
  "roll_no": 101,
  "scores": [
    80,
    90
  ]
}

HTTP Status: 200

## GET /students/101/average

Request body: 

Response:
{
  "average": 85.0,
  "roll_no": 101
}

HTTP Status: 200

## GET /students

Request body: 

Response:
[
  {
    "average": 85.0,
    "name": "Ali",
    "roll_no": 101
  }
]

HTTP Status: 200

## POST /students

Request body: {"roll_no":102}

Response:
{
  "error": "Name and roll_no are required"
}

HTTP Status: 400

## POST /students/101/scores

Request body: {"score":"abc"}

Response:
{
  "error": "Score must be between 0 and 100"
}

HTTP Status: 400
