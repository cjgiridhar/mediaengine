# mediaengine

curl --dump-header - -H "Content-Type: application/json" -H "Authorization: ApiKey admin:<key>" -X POST --data '{"username":"deepti”, "email":"deepti@gmail.com","password":"ad2w", "first_name":"D", "last_name":"Giridhar"}' http://localhost:8000/api/v1/users/

curl --dump-header - -H "Content-Type: application/json" -H "Authorization: ApiKey admin:78fb77da661261a05f3e429108046ac16f032we3" -X POST --data '{"phone_number":"23423432", "title":"ENG", "company":"BJN", "user":{"username":"deepti.1"}}' http://localhost:8000/api/v1/user_profile/

curl --dump-header - -H "Content-Type: application/json" -H "Authorization: ApiKey admin:78fb77da661261a05f3e429108046ac16f032we3" -X POST --data '{"user":{"username":"deepti.1"}}' http://localhost:8000/api/v1/user_billing/

Chetans-MacBook-Pro-2:mediaengine cgiridhar$ curl --dump-header - -H "Content-Type: application/json" -H "Authorization: ApiKey admin:78fb77da661261a05f3e429108046ac16f032we3"  http://localhost:8000/api/v1/profiles/
HTTP/1.0 200 OK
Date: Tue, 28 Apr 2015 09:30:42 GMT
Server: WSGIServer/0.1 Python/2.7.5
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN
Content-Type: application/json
Cache-Control: no-cache

{"profiles": [{"audio": {"audio_bitrate": 128000, "audio_channels": 2, "audio_codec": "libfdk_aac", "audio_sample_rate": 44100, "id": 1}, "frame_rate": {"frame_rate": 30, "id": 1, "key_frame_interval": 180}, "id": 1, "resolution": {"aspect": "4:3", "height": 720, "id": 1, "width": 1280}, "video": {"id": 1, "video_bitrate": 512000, "video_codec": "libx264", "video_preset": "ultrafast", "video_profile": "baseline"}}]}
