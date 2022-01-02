node {
    def rc
    def image_c
    stage('Clone repository') {

            checkout scm
    }
    stage('Build image') {

            image_c = docker.build("wog:${env.BUILD_ID}")
    }
    stage ('Run and test'){
            cmd 'docker run --rm wog:${env.BUILD_ID} '
            docker.ps(){}
            /* Run some tests which require MySQL */
            rc = cmd 'python "C:/Users/Lenats/PycharmProjects/WorldOfGames/tests/e2e.py"'
        }
    }
}