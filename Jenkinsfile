node {
    def rc
    stage('Clone repository') {

            checkout scm
    }
    stage('Build image') {

            bat "docker-compose build"
    }
    stage ('Run '){
            bat "docker-compose --project-name wog_score_for_test up -d  --force-recreate"
            bat "docker ps"
            /* Run some tests which require MySQL */
    }
    stage('test'){
            bat 'docker cp  ./scores.txt wog_score_for_test_web_1:/app/'
            bat 'C:/Users/Lenats/AppData/Local/Programs/Python/Python38/python.exe "C:/Users/Lenats/PycharmProjects/WorldOfGames/tests/e2e.py"'
    }
    stage ('kill'){
            bat "docker kill wog_score_for_test_web_1"
    }
    stage push{
            bat "docker push lenats/wog:$build_id"
    }

}