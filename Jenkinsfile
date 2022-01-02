node {
    def rc
    stage('Clone repository') {

            checkout scm
    }
    stage('Build image') {

            bat "docker-compose build"
    }
    stage ('Run '){
            bat "docker-compose up -d"
            bat "docker ps"
            /* Run some tests which require MySQL */
    }
    stage('test'){
     bat 'python "C:/Users/Lenats/PycharmProjects/WorldOfGames/tests/e2e.py"'
    }

}