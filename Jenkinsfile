node {
    def rc
    stage('Clone repository') {

            checkout scm
    }
    stage('Build image') {

            bat "docker-compose build"
    }
    stage ('Run '){
            bat "docker-compose up -d --force-recreate"
            bat "docker ps"
            /* Run some tests which require MySQL */
    }
    stage('test'){
            bat 'docker cp  ./scores.txt d10c56315c7d:/app/'
            bat 'python "C:/Users/Lenats/PycharmProjects/WorldOfGames/tests/e2e.py"'
    }

}