import json

qa_1 = json.dumps({

    "tests": [
       
        {
            "testKey": "QA-1",
            "start": "2014-08-30T11:51:00+01:00",
            "finish": "2014-08-30T11:52:30+01:00",
            "comment": "Execution failed. Example #5 FAIL.",
            "status": "FAILED",
            "evidence": [
                {
                    "data": "iVBORw0KGgoAAAANSUhEUgAABkIAAAO9CAYAAADezXv6AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAEn(...base64 file enconding)",
                    "filename": "image21.jpg",
                    "contentType": "image/jpeg"
                }
            ],
            "examples": [
                "PASSED",
                "PASSED",
                "PASSED",
                "PASSED",
                "FAILED"
            ]
        }
    ]
})


qa_2 = json.dumps({
    "tests" : [
    
        {
            "testKey" : "QA-1",
            "start" : "2013-05-03T12:19:23+01:00",
            "finish" : "2013-05-03T12:20:01+01:00",
            "comment" : "Error decreasing space shuttle speed.",
            "status" : "FAILED",
            "examples" : [
                "PASSED",
                "PASSED",
                "PASSED",
                "PASSED",
                "PASSED",
                "FAILED"
            ]
        }
    ]
})

qa_3 = json.dumps