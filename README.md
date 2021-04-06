[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=4460163&assignment_repo_type=AssignmentRepo)
# Project 1 | **PhotoShare-api**

**PhotoShare-api** - An api for a simple PhotoSharing Application
Time spent: **~8** hours spent in total

## User Stories

The following **required** functionality is completed:
### PROFILES
- [x] An authenticated User can retrieve a list of profiles on the platform by sending a GET request to /api/profiles/. Each profile object contains the following fields (including a url to access that specific profile)
    ```json
    [
        {
            "id": 1,
            "user": "daniel",
            "image": "image/upload/v1613178112/r19z3ks9ugzcve8ql7ao.jpg",
            "bio": "This is the admin",
            "url": "http:/your-api-url.com/api/profiles/1/"
        },
        {
            "id": 3,
            "user": "jake",
            "image": "image/upload/v1613416955/profile_image/dyeclv8lf6mx6phkqm93.png",
            "bio": "this is jake from state farm",
            "url": "http:/your-api-url.com/api/profiles/3/"
        },
    ]
    ```
- [x] An authenticated User can retrieve a profile object by sending a GET request to /api/profiles/\<int:profile_id> containing the following fields
    ```json
    {
        "id": 1,
        "user": "daniel",
        "image": "image/upload/v1613178112/r19z3ks9ugzcve8ql7ao.jpg",
        "bio": "This is the admin",
        "url": "http:/your-api-url.com/api/profiles/1/"
    }
    ```
- [x] An authenticated User can edit her bio (PUT/PATCH) at /api/profile/\<int:profile_id> but **NOT** the bio of others. The request should return the following fields
    ```json
    {
        "id": 2,
        "user": "second_user",
        "image": "image/upload/v1614207821/profile_image/kwmahwsxktokwbondrkk.jpg",
        "bio": "Hello, I am second user9",
        "url": "https://belashare.herokuapp.com/api/profiles/2/"
    }
    ```

### POSTS
- [x] An authenticated User can retrieve a list of posts by sending a GET request to /api/posts/. Each post object contains the following fields (including a url to access that specific post)
    ```json
    [
        {
            "id": 1,
            "user": {
                "id": 1,
                "user": "daniel",
                "url": "https://belashare.herokuapp.com/api/profiles/1/"
            },
            "picture": "image/upload/v1613178173/post_images/ejf8mx4f87gp3ihyk1ni.jpg",
            "date_posted": "2021-02-13T01:02:53.355320Z",
            "comments": [
                {
                    "user": "second_user",
                    "comment": "this is a nice post daniel",
                    "comment_date": "2021-02-13T01:04:23.154675Z"
                },
                {
                    "user": "second_user",
                    "comment": "this is a nice post daniel",
                    "comment_date": "2021-02-13T03:09:35.228267Z"
                }
            ],
            "description": "First post",
            "url": "https://belashare.herokuapp.com/api/posts/1/"
        },
        {
            "id": 2,
            "user": {
                "id": 2,
                "user": "second_user",
                "url": "https://belashare.herokuapp.com/api/profiles/2/"
            },
            "picture": "image/upload/v1613178252/post_images/q5mnwmomfeq6pat43x7d.jpg",
            "date_posted": "2021-02-13T01:04:12.027039Z",
            "comments": [
                {
                    "user": "daniel",
                    "comment": "right back at you second user",
                    "comment_date": "2021-02-13T01:04:42.829548Z"
                },
                {
                    "user": "second_user",
                    "comment": "I am adding a sample comment",
                    "comment_date": "2021-02-13T03:08:50.256931Z"
                }
            ],
            "description": "my own post",
            "url": "https://belashare.herokuapp.com/api/posts/2/"
        }
    ]
    ```
- [x] An authenticated User can add a new post by sending a POST request to /api/posts. Only a description is required, the imageField should be set to blank. The added post should automatically be associated with the user who submitted the request. The request should return the following fields
    ```json
    {
        "id": 7,
        "user": {
            "id": 2,
            "user": "second_user",
            "url": "https://belashare.herokuapp.com/api/profiles/2/"
        },
        "picture": "",
        "date_posted": "2021-02-25T01:31:59.403438Z",
        "comments": [],
        "description": "new post I added",
        "url": "https://belashare.herokuapp.com/api/posts/7/"
    }
    ```
- [x] An authenticated User can change any of her posts' description by sending a PUT/PATCH request to /api/posts/\<int:post_id> but **NOT** the posts of others.
    ```json
    {
        "id": 7,
        "user": {
            "id": 2,
            "user": "second_user",
            "url": "https://belashare.herokuapp.com/api/profiles/2/"
        },
        "picture": "",
        "date_posted": "2021-02-25T01:31:59.403438Z",
        "comments": [],
        "description": "new post I added and changed description",
        "url": "https://belashare.herokuapp.com/api/posts/7/"
    }
    ```
- [x] An authenticated User can delete any of her posts by sending a DELETE request to /api/posts/\<int:post_id> but **NOT** the posts of others. the request should return an HTTP 204 No Content

### COMMENTS
- [x] An authenticated User can retrieve a list of comments on a post by sending a GET request to /api/posts/\<int:post_id>/comments/. Each post object contains the following fields
    ```json
    [
        {
            "user": "second_user",
            "comment": "this is a nice post daniel",
            "comment_date": "2021-02-13T01:04:23.154675Z"
        },
        {
            "user": "second_user",
            "comment": "this is a nice post daniel",
            "comment_date": "2021-02-13T03:09:35.228267Z"
        }
    ]
    ```
- [x] An authenticated User can add a new comment to a post by sending a POST request to /api/posts/\<int:post_id>/comments/. The added comment should automatically be
associated with the user who submitted the request. The request should return the new list of comments OR the specific comment that was added

### MISC
- [x] All endpoints require some form of authentication (i.e unathenticated clients cannot access endpoints)
- [ ] Integration tests and unit tests (where necessary) have been written for all the endpoints


The following **optional** features are implemented:
- [x] A user should able to access a Browsable version (with login) of the API in Browser
- [ ] An authenticated User can edit any of her comments on a post by sending a POST request to /api/posts/\<int:post_id>/comments/\<int:comment_id> but **NOT** the comments of others.
- [ ] An authenticated User can delete any of her comments on a post by sending a DELETE request to /api/posts/\<int:post_id>/comments/\<int:comment_id>/ but **NOT** the comments of others.


## TESTING
Code Coverage: 38%

A coverage report is included at: [insert coverage report path]

## Video Walkthrough

Here's a walkthrough of implemented user stories:

<img src='[insert_gif_source_here]' title='Video Walkthrough' alt='Video Walkthrough' />

GIF created with [LiceCap](http://www.cockos.com/licecap/).

## Notes

Describe any challenges encountered while building the app.

The challenges when building the app was mainly trying to understand how the model relationships work alongside their respective serializers.
One of the biggest problems I had to face was understanding how the models interacted with each other, and other than that, most of the API was done by Django, so not much was needed
when it came to implementing the API views. Some of the time was used to just understanding how the serializers worked in the rest framework, which the tutorial covered really well for me
to understand and grasp the idea.

## License

    Copyright [Year] [Name]

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
