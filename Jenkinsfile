node {
    def rc
    stage('Clone repository') {

            checkout scm
    }
    stage('Build image') {

            bat "docker-compose build"
    }
    stage ('Run '){
            bat "docker-compose up -d -p wog_score_for_test --force-recreate"
            bat "docker ps"
            /* Run some tests which require MySQL */
    }
    stage('test'){
            bat 'docker cp  ./scores.txt wog_score_for_test:/app/'
            bat 'C:/Users/Lenats/AppData/Local/Programs/Python/Python38/python.exe "C:/Users/Lenats/PycharmProjects/WorldOfGames/tests/e2e.py"'
    }
    stage ('kill'){
    bat "docker kill wog_score_for_test"
    }
    stage push{
    }

}