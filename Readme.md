Main files:
==============


MainGame.py: lets you choose the game &play
MainScores: manages and saves score  on web. TODO:  implement for different users
e2e.py selenium test for scores on web
Jenkinsfile:
1. Checkout - checkout the repository.
2. Build - Build our docker image.
3. Run - will run our dockerized application. The application will expose the port 8777 on
localhost, and a dummy Scores.txt will be mounted to it in order to server the results for
the tests.
4. Test - With our e2e.py file it will selenium test our scores web service and fail the
pipeline if the tests failed.
5. Finalize - Will terminate our tested container and push to DockerHub the new image we
created.